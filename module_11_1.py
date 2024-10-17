import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

imgage = requests.get('http://learn.python.ru/media/projects/sl1_Cj4bKxp.png')
with open('logo.png', 'wb') as f:
    f.write(imgage.content)


tf = pd.read_csv('text_file_11_1', delimiter=':')
print(tf)


a = np.array ([365, 888, 1009, 56, 493, 2554, 10, 25, 999])
print(a)
print(a + 10)
print(a > 10)
print(a / 2)





phi = np.linspace(0, 2. * np.pi, 100)
plt.plot (phi, np.sin(phi))
plt.plot (phi, np.cos(phi))

plt.show()



file_name = 'logo.png'
with Image.open(file_name) as img:
    img.load()

print(type(img))
print(img.size)


convert_image = img.transpose(Image.FLIP_TOP_BOTTOM)
convert_image.save('logo.png')
rotate_image = img.rotate(45)
rotate_image.save('logo.png')