import os
import shutil
from datetime import datetime
import time


def move_file(src_file, dst_dir):
    if not os.path.isdir(dst_dir):
        os.makedirs(dst_dir)
    shutil.move(src_file, dst_dir)


def main():
    global count
    old_dir = r'/Users/jiangzhiyi/downloads/yan_old'
    new_dir = r'/Users/jiangzhiyi/downloads/yan_new'
    photos = os.listdir(old_dir)[0:1]
    # print(photos)
    for photo in photos:
        old_pic_path = os.path.join(old_dir, photo)
        pic_time = os.path.getmtime(old_pic_path)
        dt = datetime.fromtimestamp(pic_time)
        print(dt.strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    count = 0
    main()
    # print(count)
