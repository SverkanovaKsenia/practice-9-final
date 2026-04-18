import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs("watermarked", exist_ok=True)

for i in range(1, 6):
    image = Image.open(f"{i}.jpg")

    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()

    draw.text((image.width - 1000, image.height - 500), "Ksenia", fill="white", font=font)

    image.save(f"watermarked/watermarked_{i}.jpg")