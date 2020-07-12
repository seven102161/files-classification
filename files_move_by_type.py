import os
import shutil


def file_move(old_path, new_path, t):
    global count
    files = os.listdir(old_path)
    for file in files:
        file_path = os.path.join(old_path, file)
        if os.path.isfile(file_path):
            if file.endswith(t):
                new_file_path = os.path.join(new_path, file)
                shutil.move(file_path, new_file_path)
                count += 1
            else:
                pass
        elif os.path.isdir(file_path):
            file_move(file_path, new_path, t)


def main():
    global video_type
    old_path = r'/Users/jiangzhiyi/Downloads/old_albums'
    new_path = r'/Users/jiangzhiyi/Downloads/other'
    for t in video_type:
        file_move(old_path, new_path, t)


if __name__ == '__main__':
    count = 0
    video_type = ['mp4', 'MOV', 'mov']
    print('done')
    print(count)
    main()

