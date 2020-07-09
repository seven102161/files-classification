import os
import json

# 遍历文件夹及其子文件夹中的文件，并存储在一个列表中
# 输入文件夹路径、空文件列表[]
# 返回 文件列表file_list,包含文件名（完整路径）


def get_file_list(_dir, _file_list):
    new_dir = _dir
    if os.path.isfile(_dir):
        _file_list.append(_dir)
        # # 若只是要返回文件文，使用这个
        # file_list.append(os.path.basename(dir))
    elif os.path.isdir(_dir):
        for s in os.listdir(_dir):
            # 如果需要忽略某些文件夹，使用以下代码
            # if s == "xxx":
            # continue
            new_dir = os.path.join(_dir, s)
            get_file_list(new_dir, _file_list)
    return _file_list


if __name__ == '__main__':
    file_path = r'/Users/jiangzhiyi/synologydrive/python3'
    file_keys = os.listdir(file_path)
    file_dict = dict()
    for key in file_keys:
        new_path = os.path.join(file_path, key)
        file_list = get_file_list(new_path, [])
        file_dict[key] = file_list
    with open('file_list.json', 'w', encoding='utf-8') as fp:
        json.dump(file_dict, fp)
    print('写入成功')






