from PIL import Image
from PIL import ImageFilter



with Image.open('img.png') as pic_img:
    pic_Blured = pic_img.filter(ImageFilter.GaussianBlur(4))
    pic_Blured.save('Blured.jpg')
    pic_Blured.show()