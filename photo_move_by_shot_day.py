import os
import sys
from shutil import Error
from shutil import copystat
from shutil import copy2
import exifread
import shutil


# print('1:os.name', os.name)
# print('2:os.getcwd', os.getcwd())
# print('3:os.sep', os.sep)
# print('4:os.linesep', os.linesep)
# print('5:os.pathsep', os.pathsep)
# print(os.path.isdir(r'/Users/jiangzhiyi/desktop/test_photo_lib'))
# print(os.listdir(r'/Users/jiangzhiyi/desktop/test_photo_lib'))


def move_file(src_file, dst_dir):
    if not os.path.isdir(dst_dir):
        os.makedirs(dst_dir)
    shutil.move(src_file, dst_dir)


def main():
    global count
    old_dir = r'/Users/jiangzhiyi/downloads/yan_old'
    new_dir = r'/Users/jiangzhiyi/downloads/yan_new'
    photos = os.listdir(old_dir)
    # print(photos)
    for photo in photos:
        old_pic_path = os.path.join(old_dir, photo)
        print(old_pic_path)
        try:
            photo_read = open(old_pic_path, 'rb')
            photo_info = exifread.process_file(photo_read)

            # 查看照片信息里关于照片时间的key名称
            # print(photo_info.keys())
            # for i in photo_info.keys():
            #     print(i)
            photo_date = str(photo_info['EXIF DateTimeOriginal'])
            # print(photo_date)
            year = photo_date[0:4]
            month = photo_date[5:7]
            day = photo_date[8:10]
            dir_name = '{}年{}月{}日'.format(year, month, day)
            new_pic_path = new_dir + '/' + dir_name
            print(new_pic_path)
            move_file(old_pic_path, new_pic_path)
        except Exception as e:
            count += 1
            print(e)


if __name__ == '__main__':
    count = 0
    main()
    print(count)
