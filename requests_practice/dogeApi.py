import requests
from PIL import Image
from io import BytesIO
import time




url = "https://dog.ceo/api/breeds/image/random"
headers = {'user-agent':'test-app/0.0.1'}
r = requests.get(url=url, headers=headers)
print(r.status_code)
output = r.json()

urlImage = output['message']


imageRequest = requests.get(url=urlImage)

i = Image.open(BytesIO(imageRequest.content))
i.show()