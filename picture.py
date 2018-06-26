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