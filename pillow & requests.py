# requests
import requests

r = requests.get('https://urban-university.ru/members/')
if r.status_code == 200:
    print(r.text)
else:
    print(f'Ошибка {r.status_code}: {r.reason}')

#pillow
from PIL import Image

image_path = 'img_1.jpg'
image = Image.open(image_path)

new_size = (1200,800)
res_img = image.resize(new_size)

new_image = 'img_1.png'
res_img.save(new_image, format='PNG')

