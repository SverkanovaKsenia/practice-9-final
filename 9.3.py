import os
from PIL import Image, ImageFilter

os.makedirs("filtered", exist_ok=True)

for i in range(1, 6):
    image = Image.open(f"{i}.jpg")
    # Фильтр EMBOSS (стр.22 - тиснение)
    filtered = image.filter(ImageFilter.EMBOSS)
    filtered.save(f"filtered/filtered_{i}.jpg")