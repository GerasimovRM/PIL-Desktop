from PIL import Image, ImageFilter


def min_filter(img: Image.Image, size=3):
    return img.filter(ImageFilter.MinFilter(size))
