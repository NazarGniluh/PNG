import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
files = os.listdir("photo")
for photo in files:
    with Image.open("photo/"+photo) as image:


        draw =ImageDraw.Draw(image)


        font = ImageFont.truetype("beer money.ttf", 30)

        draw.text((10, 10), "КВАЧІКВАЛЬКУЛЯ", font=font, fill="Black")

        image.save("resuits/"+photo)