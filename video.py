import cv2


# 将视频分解成帧，只支持python27
def get_pic(video, pic_path):
    vc = cv2.VideoCapture(video)  # 读入视频文件 c=1

    if vc.isOpened():  # 判  是否正常打开
        rval , fame = vc.read()
    else:
        rval = False

    timeF = 2  # 视频帧计数间隔频率

    while rval:  #  读取视频帧
        rval, frame = vc.read()
        if(c%timeF == 0):  # 每  timeF帧进行存储操作
            cv2.imwrite(pic_path + '\\'+str ( c) + '.jpg',frame)  # 存储为图像
        c = c + 1
        cv2.waitKey(1)