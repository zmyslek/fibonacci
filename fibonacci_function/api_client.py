import requests

APIM_URL = "https://fibonacciapimanagement.azure-api.net/fibonacciapimanagement/fibonacci-final"
APIM_SUBSCRIPTION_KEY = "d23b1cc6b2994c40b7cf48163efdb51b"

def call_apim_function():
    headers = {
        "Ocp-Apim-Subscription-Key": APIM_SUBSCRIPTION_KEY
    }
    response = requests.get(APIM_URL, headers=headers)
    response.raise_for_status()  # Optional: raise error if bad status
    return response.json()
