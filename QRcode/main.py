import pyqrcode

url = input("Enter URL to generate QR Code..:")

qr_code = pyqrcode.create(url)
qr_code.svg('qrcode.svg', scale=5)