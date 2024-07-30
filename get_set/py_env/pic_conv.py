
import qrcode
import requests
from PIL import Image
from auth import *

def conv():
    im = Image.open("image.webp").convert("RGB")
    im.save("imadd.png","png")

login = input("get the login : ")
url = get_pic(login)
response = requests.get(url)
# print(response)
# im = Image.open("re")
with open("image.webp","wb") as f:
    f.write(response.content)
conv()
image = Image.open('imadd.png')
new_image = image.resize((250,250))
new_image.save('pro.png')

