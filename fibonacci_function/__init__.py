import azure.functions as func
import logging

from .api_client import call_apim_function
from .cache_utils import get_cached_fibonacci, cache_fibonacci
from .storage_utils import save_to_blob
from mpmath import mp

mp.dps = 50  # Set precision for large Fibonacci numbers

def fast_doubling(n):
    if n == 0:
        return 0
    def _fib(k):
        if k == 0:
            return (0, 1)
        a, b = _fib(k >> 1)
        c = a * (2 * b - a)
        d = a * a + b * b
        if k & 1:
            return (d, c + d)
        else:
            return (c, d)
    return _fib(n)[0]

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        n = int(req.params.get('n'))
        if n < 0:
            raise ValueError("n must be non-negative")

        # 1. Check the cache
        cached = get_cached_fibonacci(n)
        if cached is not None:
            logging.info(f"Cache hit for n={n}")
            return func.HttpResponse(str(cached))

        # 2. Call external API (if needed)
        # api_result = call_apim_function()
        # logging.info(f"API call result: {api_result}")

        # 3. Compute Fibonacci number
        result = fast_doubling(n)

        # 4. Save to cache
        cache_fibonacci(n, result)

        # 5. Save result to Azure Blob
        blob_name = f"fib_{n}.txt"
        save_to_blob(blob_name, str(result))

        return func.HttpResponse(str(result))

    except Exception as e:
        logging.exception("An error occurred in the Fibonacci Function.")
        return func.HttpResponse(f"Error: {str(e)}", status_code=400)
