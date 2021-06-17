import requests

r =  requests.get("https://httpbin.org/status/500", timeout=1)
r.raise_for_status()