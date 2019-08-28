from PIL import Image, ImageFilter


def gaussian_blur(img: Image.Image, n=2.) -> Image.Image:
    return img.filter(ImageFilter.GaussianBlur(n))
