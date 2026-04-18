from PIL import Image

image = Image.open('meganfox.jpg')

res_img = image.reduce(3)
res_img.save('small_image.jpg')

horizontal = image.transpose(Image.FLIP_LEFT_RIGHT)
horizontal.save('horiz_mirror.jpg')

vertical = image.transpose(Image.FLIP_TOP_BOTTOM)
vertical.save('vert_mirror.jpg')