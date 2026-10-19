import json
import os
import platform
import sys
import time

import requests

import minio
import redis

REDIS_HOST  = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
MINIO_ENDPOINT = os.environ.get("MINIO_ENDPOINT", "localhost:9000")

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
minio_client = minio.Minio(
    MINIO_ENDPOINT,
    access_key="rootuser",
    secret_key="rootpass123",
    secure=False
)

BUCKET_NAME = "demucs-bucket"

def log_info(message):
    print("INFO:", message)
    redis_client.lpush('logging', f"{platform.node()}.worker.info:{message}")

def log_debug(message):
    print("DEBUG:", message)
    redis_client.lpush('logging', f"{platform.node()}.worker.debug:{message}")

def main_worker_loop():
    log_info("Worker started and waiting for work on 'toWorker' queue...")

    while True:
        try:
            work_item = redis_client.blpop("toWorker", timeout=0)
            payload_json = work_item[1].decode('utf-8')
            task = json.loads(payload_json)

            songhash = task.get("songhash")
            callback_url = task.get("callback")

            log_info(f"Processing task for songhash: {songhash}")

            local_input_path = f"/tmp/{songhash}.mp3"
            minio_client.fget_object(BUCKET_NAME, f"{songhash}.mp3", local_input_path)

            demucs_command = f"python3 -m demucs.separate --mp3 --out /tmp/output {local_input_path}"
            log_debug(f"Executing command: {demucs_command}")

            exit_code = os.system(demucs_command)

            if exit_code != 0:
                raise Exception(f"DEMUCS processing failed with exit code {exit_code}")

            stems = ["bass", "drums", "vocals", "other"]
            for stem in stems:
                local_stem_path = f"/tmp/output/mdx_extra_q/{songhash}/{stem}.mp3"
                remote_object_name = f"{songhash}-{stem}.mp3"

                minio_client.fput_object(BUCKET_NAME, remote_object_name, local_stem_path)
                log_debug(f"Uploaded {remote_object_name} to Min.io")
            if callback_url is not None:
                try:
                    log_info(f"Sending webhook callback to {callback_url}")
                    requests.post(callback_url, json=task, timeout=10)
                except Exception as webhook_err:
                    log_debug(f"Webhook callback failed: {str(webhook_err)}")

            log_info(f"Successfully completed processing for {songhash}")
        except Exception as e:
            log_info(f"Error in worker loop: {str(e)}")

if __name__ == "__main__":
    main_worker_loop()
