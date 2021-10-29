#importing pyqrcode module to generate qr code and save as png
import pyqrcode   

#variable for creating the qr code
anyt = "I am Letters Dropped and this project is the part of my Python learning journey."

#creating qr code
url = pyqrcode.create(anyt)

#saving as png
url.png('anytqr.png', scale=6)

#terminal message
print("Success!")


