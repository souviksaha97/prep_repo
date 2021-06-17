import requests

s = requests.Session()

username = {'userName': 'John99'}
location = {'location': 'New York'}

setCookieUrl = 'https://httpbin.org/cookies/set'
getCookiesUrl = 'https://httpbin.org/cookies'


s.get(setCookieUrl, params=username)
s.get(setCookieUrl, params=location)

r = s.get(getCookiesUrl)
print(r.text)
print(r.url)