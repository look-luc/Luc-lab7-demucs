import os
import sys

import redis

# Hardcode the host to "redis" to bypass any env variable issues
redisClient = redis.StrictRedis(host="redis", port=6379, db=0)

while True:
    try:
        work = redisClient.blpop("logging", timeout=0)
        print(work[1].decode('utf-8'))
    except Exception as exp:
        print(f"Exception raised in log loop: {str(exp)}")
    sys.stdout.flush()
    sys.stderr.flush()
