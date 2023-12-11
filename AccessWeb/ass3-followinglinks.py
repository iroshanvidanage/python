import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter :')
# url1 = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url1 = 'http://py4e-data.dr-chuck.net/known_by_Ayat.html'

link_pos = 18
itr_time = 7

for _ in range(itr_time + 1):
    if _ == 0:
        url = url1
    else:
        url = tags[link_pos - 1].get('href', None)
    print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
