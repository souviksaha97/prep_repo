import requests

r = requests.get('https://api.github.com/events')
events =  r.json()
print(events[0])