import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.police.lk/index.php/item/373-functional-division'


html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('p')
func_div = list()
for tag in tags:
    if str(tag.contents[0]).startswith('<') or str(tag.contents[0]).startswith('0'):
        continue
    func_div.append(tag.contents[0])

print(func_div)

with open('police-func.txt', 'w') as file:
    for _ in func_div:
        file.write(_ + '\n')