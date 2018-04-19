#-*- encoding:UTF-8 -*-

from PIL import Image


# 获取图片长宽
def get_x_y(path):
    im = Image.open(path)
    img_size = im.size
    w = img_size[0]
    h = img_size[1]
    return w, h


# 图片截取, 横坐标从x开始，截取长度为w，纵坐标从y开始，截取长度为y
def pic_cut(pic, x, y, w, h):
    new_pic = pic.crop((x, y, x + w, y + h))
    return new_pic
