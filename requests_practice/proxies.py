import requests

proxies = {'https': 'https://46.237.255.2:8080'}


r = requests.get('https://httpbin.org/ip', proxies=proxies)
print(r.text)