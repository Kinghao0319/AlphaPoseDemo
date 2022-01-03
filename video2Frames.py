# Kinghao 2022/1/3

import time,os

import cv2

# 运行顺序
# video2Frames.py
# demo.py 设置运行参数
# process_json.py

def video2frame(videos_path, frames_save_path, time_interval):
    '''
    :param videos_path: 视频的存放路径
    :param frames_save_path: 视频切分成帧之后图片的保存路径
    :param time_interval: 保存间隔
    :return:
    '''
    vidcap = cv2.VideoCapture(videos_path)
    success, image = vidcap.read()
    count = 0
    while success:
        success, image = vidcap.read()
        count += 1
        if count % time_interval == 0 and image is not None:
            cv2.imencode('.jpg', image)[1].tofile(frames_save_path + "/frame"+str(count).zfill(5)+".jpg")
        # if count == 20:
        #   break
    print(count)


if __name__ == '__main__':
    t0=time.time()
    videos_path = 'examples/video/001.mp4'
    frames_save_path = 'examples/frames'
    if not os.path.exists(frames_save_path):
        os.makedirs(frames_save_path)
    #time_interval = 2  # 隔一帧保存一次
    time_interval=5
    video2frame(videos_path, frames_save_path, time_interval)
    t1=time.time()
    print('耗时是 : %f' % (t1 - t0))