from PIL import Image, ImageFilter


def runk_filter(img: Image.Image, size=5, rank=10):
    return img.filter(ImageFilter.RankFilter(size, rank))