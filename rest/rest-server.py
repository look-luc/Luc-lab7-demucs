import base64
import hashlib
import io
import json
import os
import platform
import sys

from flask import Flask, jsonify, request, send_file

import minio
import redis

app = Flask(__name__)
redis_client = redis.Redis(host="redis", port=6379, db=0)
QUEUE_NAME = "Song enqueued for separation"

MINIO_ENDPOINT = os.environ.get('MINIO_ENDPOINT', 'localhost:9000')
minio_client = minio.Minio(
    MINIO_ENDPOINT,
    access_key="rootuser",
    secret_key="rootpass123",
    secure=False
)

BUCKET_NAME = "demucs-bucket"

redisHost = os.getenv("REDIS_HOST") or "localhost"
redisPort = os.getenv("REDIS_PORT") or 6379

infoKey = "{}.rest.info".format(platform.node())
debugKey = "{}.rest.debug".format(platform.node())

def log_debug(message, key=debugKey):
    print("DEBUG:", message, file=sys.stdout)
    redisClient = redis.StrictRedis(host=redisHost, port=redisPort, db=0)
    redisClient.lpush('logging', f"{debugKey}:{message}")

def log_info(message, key=infoKey):
    print("INFO:", message, file=sys.stdout)
    redisClient = redis.StrictRedis(host=redisHost, port=redisPort, db=0)
    redisClient.lpush('logging', f"{infoKey}:{message}")

@app.route("/", methods=["GET"])
def hello_world():
    return '<h1> Music Separation Server</h1><p> Use a valid endpoint </p>'

def generate_song_hash(audio_bytes: bytes) -> str:
    """
    Generates a unique, deterministic SHA-256 hex string for a given byte array.
    """
    sha256_hash = hashlib.sha256()
    # Update the hash in chunks if dealing with large memory loads
    sha256_hash.update(audio_bytes)
    return sha256_hash.hexdigest()

@app.route('/apiv1/route_separate', methods=['POST'])
def route_separate():
    r = request.get_json()
    if not r:
        return jsonify({"error": "Invalid or missing JSON payload"})

    model_name = r.get('model_name')
    audio_base64 = r.get('audio_data')

    if not model_name or not audio_base64:
        return jsonify({"error": f"Missing 'model_name' or 'audio_data' in request, got {model_name} and {audio_base64}"})

    try:
        if "," in audio_base64:
            audio_base64 = audio_base64.split(",")[-1]

        audio_bytes = base64.b64decode(audio_base64)
    except Exception as e:
        return jsonify({"error": f"Failed to decode base64: {str(e)}"})

    song_hash = generate_song_hash(audio_bytes)
    object_name = f"{song_hash}.mp3"

    try:
        if not minio_client.bucket_exists(BUCKET_NAME):
            minio_client.make_bucket(BUCKET_NAME)

        audio_stream = io.BytesIO(audio_bytes)
        minio_client.put_object(
            bucket_name=BUCKET_NAME,
            object_name=object_name,
            data=audio_stream,
            length=len(audio_bytes),
            content_type="audio/mpeg"
        )
    except Exception as e:
        return jsonify({"error": f"MinIO storage failed: {str(e)}"}), 500

    try:
        job_data = {
            "song_hash": song_hash,
            "model_name": model_name,
            "object_name": object_name
        }

        redis_client.lpush(QUEUE_NAME, json.dumps(job_data))
    except Exception as e:
        return jsonify({"error": f"Failed to push message to Redis queue: {str(e)}"}), 500

    return jsonify({
        "status": "hash",
        "song_hash": song_hash,
        "reason": QUEUE_NAME
    }), 200

@app.route('/apiv1/queue', methods=["GET"])
def get_queue():
    # Fetch all elements from index 0 to -1 in the 'toWorker' list
    raw_queue = redis_client.lrange('toWorker', 0, -1)

    # Decode bytes to strings so JSON serialization works smoothly
    queue_items = [item.decode('utf-8') if isinstance(item, bytes) else item for item in raw_queue]

    return {"queue": queue_items}, 200

@app.route('/apiv1/track/<songhash>/track', methods=["GET"])
def get_track(songhash, track_name):
    object_name = f"{songhash}"
    bucket_name = "demucs-bucket"

    try:
        # Fetch the object stream from Min.io
        response = minio_client.get_object(bucket_name, object_name)

        # Read the response data into memory or stream it directly using send_file
        file_data = io.BytesIO(response.read())
        response.close()
        response.release_conn()

        return send_file(
            file_data,
            mimetype='audio/mpeg',
            as_attachment=True,
            download_name=track_name
        )
    except Exception as e:
        return {"error": str(e)}, 404

@app.route('/apiv1/remove/<songhash>/track', methods=['GET', 'DELETE'])
def remove_track(songhash, track_name):
    object_name = f"{songhash}-{track_name}"
    bucket_name = "demucs-bucket"

    try:
        minio_client.remove_object(bucket_name, object_name)
        return {"status": "success", "message": f"Successfully removed {track_name} for {songhash}"}, 200
    except Exception as e:
        return {"error": str(e)}, 404
