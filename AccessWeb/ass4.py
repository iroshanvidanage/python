import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter :')
# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = 'http://py4e-data.dr-chuck.net/comments_1167419.xml'

data = urllib.request.urlopen(url, context=ctx).read()
data_2 = ET.fromstring(data)

lst = data_2.findall('comments/comment')
num_lst = list()

print('User Count:', len(lst))
for item in lst:
    print('Name:', item.find('name').text)
    _ = int(item.find('count').text)
    num_lst.append(_)
    print('Count:', _)

print(sum(num_lst))
