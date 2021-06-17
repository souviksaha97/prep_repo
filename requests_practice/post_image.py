import requests

url = 'https://httpbin.org/post'

## Single file
# files = {'file': open('sample1.jpeg','rb')}

files = [
{'image1', ('sample1.jpeg', open('sample1.jpeg', 'rb'), 'jpeg')},
{'image2', ('sample2.jpg', open('sample2.jpg', 'rb'), 'jpg')},
]

r =  requests.post(url, files=files)
print(r.status_code)
print(r.text)