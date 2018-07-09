#-*- encoding:UTF-8 -*-

from PIL import Image


# 获取图片宽高
def get_w_h(path):
    im = Image.open(path)
    img_size = im.size
    w = img_size[0]
    h = img_size[1]
    return w, h


# 图片截取, 横坐标从x开始，截取长度为w，纵坐标从y开始，截取长度为y
def pic_cut(pic, x, y, w, h):
    new_pic = pic.crop((x, y, x + w, y + h))
    return new_pic


# 图片旋转，逆时针旋转270度
def route_angle_270(pic):
    new_pic = pic.transpose(Image.ROTATE_270)
    return new_pic


# 图片旋转，逆时针旋转90度
def route_angle_90(pic):
    new_pic = pic.transpose(Image.ROTATE_90)
    return new_pic


# 图片旋转，逆时针旋转180度
def route_angle_180(pic):
    new_pic = pic.transpose(Image.ROTATE_180)
    return new_pic


# 获取图片的格式，例如：‘JPEG’
def get_format(pic):
    img = Image.open(pic)
    return img.format


# 将图片缩放成宽为w，高为h的图片
def resize_pic(pic, w, h):
    img = Image.open(pic)
    new_pic = img.resize((w, h))
    return new_pic


# 将图片进行等比例缩放
def thumbnail_pic(pic, w, h):
    img = Image.open(pic)
    img.thumbnail((w, h))
    return img


# 将图片转换为灰阶图片
def get_pic_grey(pic):
    img = Image.open(pic)
    return img.convert('L')


# 获取图片中某一点的RGB值
def get_RGB(pic, x, y):
    img = Image.open(pic)
    pix = img.load()
    r, g, b = pix[x, y]
    return (r, g, b)