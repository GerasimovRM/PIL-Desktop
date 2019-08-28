from PIL import Image


def anaglyph(img: Image.Image, delta=3.) -> Image.Image:
    x, y = img.size
    res = Image.new('RGB', (x, y), (0, 0, 0))
    pixels2 = res.load()
    pixels = img.load()
    for i in range(x):
        for j in range(y):
            if i < delta:
                r, g, b = pixels[i, j]
                pixels2[i, j] = 0, g, b
            else:
                g, b = pixels[i, j][1:]
                r = pixels[i - delta, j][0]
                pixels2[i, j] = r, g, b
    return res
