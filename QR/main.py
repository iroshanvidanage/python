import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image


qr = pyqrcode.create("https://www.youtube.com/watch?v=R3n6coWdsEE")
qr.png("genQR.png", scale = 10)

d = decode(Image.open("genQR.png"))
print(d)
print(d[0].data.decode("ascii"))