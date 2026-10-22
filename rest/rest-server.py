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

# Redis configuration
redisHost = os.getenv("REDIS_HOST") or "redis"
redisPort = int(os.getenv("REDIS_PORT") or 6379)
redis_client = redis.Redis(host=redisHost, port=redisPort, db=0)

# MinIO configuration
MINIO_ENDPOINT = os.environ.get('MINIO_ENDPOINT', 'minio:9000')
minio_client = minio.Minio(
    MINIO_ENDPOINT,
    access_key="rootuser",
    secret_key="rootpass123",
    secure=False
)

# Ensure required MinIO buckets exist on startup[cite: 5]
for bucket_name in ["queue", "output"]:
    try:
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)
    except Exception as e:
        print(f"Error ensuring bucket {bucket_name} exists: {e}", file=sys.stderr)

infoKey = "{}.rest.info".format(platform.node())
debugKey = "{}.rest.debug".format(platform.node())

def log_debug(message, key=debugKey):
    print("DEBUG:", message, file=sys.stdout)
    try:
        redis_client.lpush('logging', f"{debugKey}:{message}")
    except Exception:
        pass

def log_info(message, key=infoKey):
    print("INFO:", message, file=sys.stdout)
    try:
        redis_client.lpush('logging', f"{infoKey}:{message}")
    except Exception:
        pass

@app.route("/", methods=["GET"])
def hello_world():
    return '<h1>Music Separation Server</h1><p>Use a valid endpoint</p>'

@app.route('/apiv1/separate', methods=['POST'])
def separate():
    req_data = request.get_json()
    if not req_data or 'mp3' not in req_data:
        return jsonify({"error": "Missing 'mp3' field in JSON payload"}), 400

    mp3_b64 = req_data['mp3']
    try:
        if "," in mp3_b64:
            mp3_b64 = mp3_b64.split(",")[-1]
        audio_bytes = base64.b64decode(mp3_b64)
    except Exception as e:
        return jsonify({"error": f"Failed to decode base64 mp3 data: {str(e)}"}), 400

    # Generate unique song hash
    sha256_hash = hashlib.sha256()
    sha256_hash.update(audio_bytes)
    song_hash = sha256_hash.hexdigest()

    # Upload raw MP3 to MinIO 'queue' bucket[cite: 5]
    try:
        audio_stream = io.BytesIO(audio_bytes)
        minio_client.put_object(
            bucket_name="queue",
            object_name=song_hash,
            data=audio_stream,
            length=len(audio_bytes),
            content_type="audio/mpeg"
        )
    except Exception as e:
        log_debug(f"MinIO upload failed: {str(e)}")
        return jsonify({"error": f"MinIO storage failed: {str(e)}"}), 500

    # Push songhash to Redis worker queue ('toWorker')
    try:
        redis_client.lpush('toWorker', song_hash)
        log_info(f"Enqueued song {song_hash} for separation")
    except Exception as e:
        log_debug(f"Redis lpush failed: {str(e)}")
        return jsonify({"error": f"Failed to push message to Redis queue: {str(e)}"}), 500

    return jsonify({
        "hash": song_hash,
        "reason": "Song enqueued for separation"
    }), 200

@app.route('/apiv1/queue', methods=["GET"])
def get_queue():
    try:
        raw_queue = redis_client.lrange('toWorker', 0, -1)
        queue_items = [item.decode('utf-8') if isinstance(item, bytes) else item for item in raw_queue]
        return jsonify({"queue": queue_items}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/apiv1/track/<songhash>/<path:track_name>', methods=["GET"])
def get_track(songhash, track_name):
    # Output bucket objects are named <songhash>-<track>.mp3[cite: 5]
    object_name = f"{songhash}-{track_name}"
    try:
        response = minio_client.get_object("output", object_name)
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
        return jsonify({"error": str(e)}), 404

@app.route('/apiv1/remove/<songhash>/<path:track_name>', methods=["GET", "DELETE"])
def remove_track(songhash, track_name):
    object_name = f"{songhash}-{track_name}"
    try:
        minio_client.remove_object("output", object_name)
        return jsonify({"status": "success", "message": f"Successfully removed {track_name} for {songhash}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
