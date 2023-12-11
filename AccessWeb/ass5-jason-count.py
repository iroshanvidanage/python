import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter :')
# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url = 'http://py4e-data.dr-chuck.net/comments_1167420.json'

print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved Data', len(data), 'Characters')

try:
    js = json.loads(data)
except:
    js = None

num_list = list()
for u in js["comments"]:
    num_list.append(int(u["count"]))

print('Sum:', sum(num_list))