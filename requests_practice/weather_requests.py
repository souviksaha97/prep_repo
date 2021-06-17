import requests


payload = {
	'access_key' : '1b189d0184fa9a1b90bb17b03e28ef2a',
	'query' : 'Thane',
	'units' : 'm'
}


r = requests.get('http://api.weatherstack.com/current', params=payload)
print(r.status_code)
print(r.url)

json_output = r.json()

print(json_output['current'])