import azure.functions as func
import logging
from .cache_utils import get_cached_fibonacci, cache_fibonacci
from .storage_utils import save_to_blob
from mpmath import mp
mp.dps = 50  # Set sufficient precision

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
        
        # Check cache first
        # cached = get_cached_fibonacci(n)
        # if cached:
        #     return func.HttpResponse(str(cached))
            
        # Compute and store
        result = fast_doubling(n)
        cache_fibonacci(n, result)
        save_to_blob(f"fib_{n}.txt", str(result))
        
        return func.HttpResponse(str(result))
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=400)