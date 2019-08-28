from PIL import Image, ImageFilter


def median_filter(img: Image.Image, size=3):
    return img.filter(ImageFilter.MedianFilter(size))

