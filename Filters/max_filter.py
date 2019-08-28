from PIL import Image, ImageFilter


def max_filter(img: Image.Image, size=3):
    return img.filter(ImageFilter.MaxFilter(size))
