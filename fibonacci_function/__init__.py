import azure.functions as func
import logging
from cache_utils import get_cached_fibonacci, cache_fibonacci
from storage_utils import save_to_blob

from mpmath import mp
mp.dps = 50  # Set sufficient precision

def fast_doubling(n: int):
    if n == 0:
        return mp.mpf(0)
    a, b = mp.mpf(0), mp.mpf(1)
    for bit in bin(n)[3:]:
        x = a * (2 * b - a)
        y = a * a + b * b
        a, b = (x, y) if bit == '0' else (y, x + y)
    return int(a)  # Convert back to integer

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        n = int(req.params.get('n'))
        
        # Check cache first
        cached = get_cached_fibonacci(n)
        if cached:
            return func.HttpResponse(str(cached))
            
        # Compute and store
        result = fast_doubling(n)
        cache_fibonacci(n, result)
        save_to_blob(n, result)
        
        return func.HttpResponse(str(result))
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=400)