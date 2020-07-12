import os
import shutil


old_path = r'/Users/jiangzhiyi/Downloads/old_albums'
new_path = r'/Users/jiangzhiyi/Downloads/other'


def file_move(old_path, new_path):
    files = os.listdir(old_path)
    print(files)
    count = 0
    for file in files:
        child_path = os.path.join(old_path, file)
        print(child_path)
        if os.path.isfile(child_path):
            des_path = os.path.join(new_path, file)
            shutil.move(child_path, des_path)
            count += 1

        elif os.path.isdir(child_path):
            if file == '.DS_Store':
                pass
            else:
                file_move(child_path, new_path)
    print(count)


def main():
    file_move(old_path, new_path)


if __name__ == '__main__':
    main()
