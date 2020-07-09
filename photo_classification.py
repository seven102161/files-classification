import os
import sys
from shutil import Error
from shutil import copystat
from shutil import copy2
import exifread
import shutil


# 图片所处的绝对路径，其中r表示去掉python的内部转义
PhotoPath = r'D:/photo'
NewPath = r'D:/pushiji/图片/生命时间轴P/'


# 根据传参判断复制的目标地址是否存在如果不存在进行创建，并且执行复制操作
def copy_file(src_file, dst_dir):
    if not os.path.isdir(dst_dir):
        os.makedirs(dst_dir)
    copy2(src_file, dst_dir)


#根据传参判断复制的目标地址是否存在如果不存在进行创建，并且执行移动操作
def move_file(src_file, dst_dir):
    if not os.path.isdir(dst_dir):
        os.makedirs(dst_dir)
    shutil.move(src_file, dst_dir)


#遍历整个图片路径底下的所有文件并获取其拍摄时间，根据拍摄时间进行操作
def walk_file(file_path):
    for root,dirs,files in os.walk(file_path,topdown=False):
		for name in files:
			photo = os.path.join(root,name)
			try:
				with open(photo, 'rb') as img:
					dateStr = str(exifread.process_file(img)['Image DateTime'])
				year = dateStr[0:4]
				month = dateStr[5:7]
				new_path = NewPath+year+'年/'+year+'年'+month+'月/'
				move_file(photo,new_path)
				print("moved '{}' to '{}'".format(photo,new_path))
			except:
				print("Movement failed. {}".format(photo))
		for name in dirs:
			walk_file(name)


if __name__ == '__main__':
    walk_file(PhotoPath)

