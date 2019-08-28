from PIL import Image
import itertools


def test_filter(img: Image.Image, factor=2.0) -> Image.Image:
    pixels = img.load()
    x, y = img.size
    for i, j in itertools.product(range(x), range(y)):
        r, g, b = pixels[i, j]
        pixels[i, j] = (
            min(int(factor * r), 255),
            min(int(factor * g), 255),
            min(int(factor * b), 255))
    return img
