import os
import redis


# heroku config | grep REDIS
#export REDIS_URL=redis://h:p13aec89cb487040bd9f19d0f8841e8b96acc74110d01ea6dc80ad6bfac3dc670@ec2-184-73-117-128.compute-1.amazonaws.com:17359

URL = os.environ.get("REDIS_URL")
redisConnection = None
print('os.environ.get("REDIS_URL")', URL)
if URL:
    redisConnection = redis.from_url(URL)
