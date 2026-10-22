import json
import os
import platform
import sys
import time

import requests

import minio
import redis

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
MINIO_ENDPOINT = os.environ.get("MINIO_ENDPOINT", "minio:9000")

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
minio_client = minio.Minio(
    MINIO_ENDPOINT,
    access_key="rootuser",
    secret_key="rootpass123",
    secure=False
)

QUEUE_BUCKET = "queue"
OUTPUT_BUCKET = "output"

def log_info(message):
    print("INFO:", message)
    try:
        redis_client.lpush('logging', f"{platform.node()}.worker.info:{message}")
    except Exception:
        pass

def log_debug(message):
    print("DEBUG:", message)
    try:
        redis_client.lpush('logging', f"{platform.node()}.worker.debug:{message}")
    except Exception:
        pass

def main_worker_loop():
    log_info("Worker started and waiting for work on 'toWorker' queue...")

    while True:
        try:
            work_item = redis_client.blpop("toWorker", timeout=0)
            payload = work_item[1].decode('utf-8')

            # Robustly handle both JSON payloads and raw string songhashes
            callback = None
            try:
                task = json.loads(payload)
                if isinstance(task, dict):
                    songhash = task.get("songhash") or task.get("hash")
                    callback = task.get("callback")
                else:
                    songhash = payload
            except json.JSONDecodeError:
                songhash = payload

            if not songhash:
                log_info("Received empty songhash from queue.")
                continue

            log_info(f"Processing task for songhash: {songhash}")

            local_input_path = f"/tmp/{songhash}.mp3"

            # 1. Fetch raw MP3 from the 'queue' bucket using the exact object name (songhash)
            minio_client.fget_object(QUEUE_BUCKET, songhash, local_input_path)

            demucs_command = f"python3 -m demucs.separate --mp3 --out /tmp/output {local_input_path}"
            log_debug(f"Executing command: {demucs_command}")

            exit_code = os.system(demucs_command)

            if exit_code != 0:
                raise Exception(f"DEMUCS processing failed with exit code {exit_code}")

            stems = ["bass", "drums", "vocals", "other"]
            for stem in stems:
                local_stem_path = f"/tmp/output/mdx_extra_q/{songhash}/{stem}.mp3"
                remote_object_name = f"{songhash}-{stem}.mp3"

                # 2. Upload separated stems to the 'output' bucket[cite: 5]
                minio_client.fput_object(OUTPUT_BUCKET, remote_object_name, local_stem_path)
                log_debug(f"Uploaded {remote_object_name} to Min.io output bucket")

            # 3. Properly extract webhook URL and post payload data[cite: 6]
            if callback and isinstance(callback, dict):
                cb_url = callback.get("url")
                cb_data = callback.get("data")
                if cb_url:
                    try:
                        log_info(f"Sending webhook callback to {cb_url}")
                        requests.post(cb_url, json=cb_data, timeout=10)
                    except Exception as webhook_err:
                        log_debug(f"Webhook callback failed: {str(webhook_err)}")

            log_info(f"Successfully completed processing for {songhash}")
        except Exception as e:
            log_info(f"Error in worker loop: {str(e)}")

if __name__ == "__main__":
    main_worker_loop()
