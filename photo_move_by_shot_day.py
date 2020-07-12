import os
import exifread
import shutil


def move_file(src_file, dst_dir):
    if not os.path.isdir(dst_dir):
        os.makedirs(dst_dir)
    shutil.move(src_file, dst_dir)


def get_photo_path(old_dir, new_dir):
    global count
    photos = os.listdir(old_dir)

    for photo in photos:
        old_pic_path = os.path.join(old_dir, photo)
        # print(old_pic_path)
        try:
            photo_read = open(old_pic_path, 'rb')
            photo_info = exifread.process_file(photo_read)

            # 查看照片信息里关于照片时间的key名称
            # print(photo_info.keys())
            # for i in photo_info.keys():
            #     print(i)
            photo_date = str(photo_info['EXIF DateTimeOriginal'])
            # photo_date = str(photo_info['Image DateTime'])

            # print(photo_date)
            year = photo_date[0:4]
            month = photo_date[5:7]
            day = photo_date[8:10]
            dir_name = '{}年{}月{}日'.format(year, month, day)
            new_pic_path = new_dir + '/' + dir_name
            # print(new_pic_path)
            move_file(old_pic_path, new_pic_path)
        except Exception as e:
            count += 1
            print(e)
            print(old_pic_path)


def main():
    global count
    old_dir = r'/Users/jiangzhiyi/Downloads/iPhoneX'
    new_dir = r'/Users/jiangzhiyi/Downloads/temp'
    try:
        photos = os.listdir(old_dir)
        for file in photos:
            if file == '.DS_Store':
                pass
            else:
                child_dir = os.path.join(old_dir, file)
                print(child_dir)
                get_photo_path(child_dir, new_dir)
    except Exception as s:
        get_photo_path(old_dir, new_dir)


if __name__ == '__main__':
    count = 0
    main()
    print(count)
