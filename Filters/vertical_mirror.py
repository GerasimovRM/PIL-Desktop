from PIL import Image


def vertical_mirror(img: Image.Image) -> Image.Image:
    pixels = img.load()
    x, y = img.size
    for i in range(x // 2):
        for j in range(y):
            pixels[i, j], pixels[x - i - 1, j] = pixels[x - i - 1, j], pixels[i, j]
    return img
