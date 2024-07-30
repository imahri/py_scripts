import qrcode
from PIL import Image 


qr = qrcode.QRCode(
    version= 1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size = 5,
    border = 1
)
img = qr.add_data("https://github.com/imahri")
img = qr.make_image()
img.save('image/qrcode.png')

# with open('maan/qrcode.png', 'wb') as image_file:
    # image_data = image_file.read()
