from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
im = Image.open('images/dog.jpg')


def get_dominant_color(pil_img, palette_size=16):
    img = pil_img.copy()
    img.thumbnail((100, 100))
    paletted = img.convert('P', palette=Image.ADAPTIVE, colors=palette_size)
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    palette_index = color_counts[0][1]
    dominant_color = palette[palette_index*3:palette_index*3+3]
    return dominant_color

image_rgb = get_dominant_color(im)
print(image_rgb)
image_rgb[0] = image_rgb[0] / 1000
image_rgb[1] = image_rgb[1] / 1000
image_rgb[2] = image_rgb[2] / 1000


plt.plot()
ax = plt.axes()
ax.set_facecolor(image_rgb)
plt.show()