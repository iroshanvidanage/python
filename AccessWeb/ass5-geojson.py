import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 42
service_url = 'http://py4e-data.dr-chuck.net/json?'
address = 'South Federal University'
address_target = 'Old Dominion University'
param = {"address": address_target, "key": api_key}

url = service_url + urllib.parse.urlencode(param)

print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved', len(data), 'Characters')

js = json.loads(data)

print(json.dumps(js, indent=4))
print('PLACE ID:', js["results"][0]["place_id"])

