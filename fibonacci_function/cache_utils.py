import redis
import pickle

# Connect to Azure Redis Cache
redis_client = redis.StrictRedis(
    host='<YOUR_REDIS_HOST>.redis.cache.windows.net',
    port=6380,
    ssl=True,
    password='<YOUR_REDIS_KEY>'
)

def cache_fibonacci(n: int, value):
    """Cache Fibonacci(n) in Redis."""
    redis_client.set(f"fib:{n}", pickle.dumps(value))

def get_cached_fibonacci(n: int):
    """Retrieve Fibonacci(n) from Redis."""
    cached = redis_client.get(f"fib:{n}")
    return pickle.loads(cached) if cached else None