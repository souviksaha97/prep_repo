import requests

payload = {"firstName": "John", "lastName":"Smith"}
headers = {'user-agent':'test-app/0.0.1'}

r = requests.get("https://httpbin.org/get", params=payload, headers=headers)

print(r.url)
print(r.status_code)
print(r.text)
print(r.content)
