from PIL import Image, ImageFilter


def unsharp_mask(img: Image.Image, radius=2., percent=150, threshold=3):
    return img.filter(ImageFilter.UnsharpMask(radius=radius, percent=percent, threshold=threshold))