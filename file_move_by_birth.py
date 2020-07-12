import os
from datetime import datetime
import shutil
from file_list import get_file_list

old_path = r'/Users/jiangzhiyi/Downloads/vedio'
new_path = r'/Users/jiangzhiyi/Downloads/temp'


def move_file(src_file, dst_dir):
    if not os.path.isdir(dst_dir):
        os.makedirs(dst_dir)
    shutil.move(src_file, dst_dir)


def get_new_path(file_list):
    global count
    for file_path in file_list:
        # print(file_path)
        try:
            stat = os.stat(file_path)
            # print(stat.st_birthtime)
            dt = datetime.fromtimestamp(stat.st_birthtime)
            dir_name = dt.strftime('%Y年%m月')
            # print(dir_name)
            des_path = os.path.join(new_path, dir_name)
            # print(des_path)
            move_file(file_path, des_path)
        except Exception as e:
            count += 1
            print(e)


def main():
    file_list = get_file_list(old_path, [])
    get_new_path(file_list)


if __name__ == '__main__':
    count = 0
    main()
