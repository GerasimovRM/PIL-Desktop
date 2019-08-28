from PIL import Image, ImageFilter


def mode_filter(img: Image.Image, size=3):
    return img.filter(ImageFilter.ModeFilter(size))
