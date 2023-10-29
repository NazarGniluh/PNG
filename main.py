
from PIL import Image






with Image.open('img.png') as pic_img:
    print('Зображення відкрито\nРозмір:', pic_img.size)
    print('Формат:', pic_img.format)
    print('Тип:', pic_img.mode)
    pic_img.show()




