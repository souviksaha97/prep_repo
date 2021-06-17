import requests

r = requests.get('http://github.com', allow_redirects=False)
print(r.url)
print(r.history)