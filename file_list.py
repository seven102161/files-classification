import os
import json

# 遍历文件夹及其子文件夹中的文件，并存储在一个列表中
# 输入文件夹路径、空文件列表[]
# 返回 文件列表file_list,包含文件名（完整路径）


def get_file_list(_dir, _file_list):
    new_dir = _dir
    if os.path.isfile(_dir):
        _file_list.append(_dir)
        # # 若只是要返回文件名，使用这个
        # _file_list.append(os.path.basename(dir))
    elif os.path.isdir(_dir):
        for s in os.listdir(_dir):
            # 如果需要忽略某些文件夹，使用以下代码
            # if s == "xxx":
            # continue
            new_dir = os.path.join(_dir, s)
            get_file_list(new_dir, _file_list)
    return _file_list


def write_to_txt(name, dic):
    name = name + '.txt'
    with open(name, 'w') as f:
        for k, v in dic.items():
            f.write(f'{k}\n')
            for i in v:
                f.write(f'{i}\n')
    print('File: {} saved!'.format(name))


def write_to_json(name, dic):
    name = name + '.json'
    with open(name, 'w', encoding='utf-8') as fp:
        json.dump(dic, fp)
    print('File: {} saved!'.format(name))


if __name__ == '__main__':
    file_path = r'E:\二级党委'  # 写入要扫描的文件夹
    # 将扫描文件夹里的第一层目录做为KEY，并以此创建字典。
    file_keys = os.listdir(file_path)
    file_dict = dict()
    for key in file_keys:
        new_path = os.path.join(file_path, key)
        file_list = get_file_list(new_path, [])
        # 去掉windows目录的盘符标识,Linux不需要。
        file_list = [i.replace('D:', '') for i in file_list]  # C:,D:,E:,F:
        file_dict[key] = file_list

    # 将结果保存为txt文件
    write_to_txt(r'E:\file_list', file_dict)

    # 将结果保存存为json文件
    write_to_json(r'E:\file_list', file_dict)






