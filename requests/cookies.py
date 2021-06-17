import requests

url = "https://httpbin.org/cookies"

cookies = {'location': 'New York'}

r = requests.get(url, cookies=cookies)
print(r.text)

r2 = requests.get('https://google.com')
print(r2.cookies)