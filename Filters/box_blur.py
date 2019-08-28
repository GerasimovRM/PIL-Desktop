from PIL import Image, ImageFilter


def box_blur(img: Image.Image, radius=1.0) -> Image.Image:
    return img.filter(ImageFilter.BoxBlur(radius))
