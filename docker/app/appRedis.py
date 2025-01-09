from redis import Redis, RedisError

# Connect to Redis
redis = Redis(host="redis-manager", db=0, socket_connect_timeout=2, socket_timeout=2, decode_responses=True)
redis.config_set('maxmemory-policy', 'allkeys-lru')

def cache(short):
    try:
        return redis.get(short)
    except:
        return None

def update(short, long):
    try:
        redis.setex(short, 30, long)
    except:
        pass
