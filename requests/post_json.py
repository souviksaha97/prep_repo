import requests

data = {'firstName': 'John', 'phoneNumber': 9819970347}

r = requests.post('https://httpbin.org/post', json=data)
print(r.text)