import os
import shutil


old_path = r'/Users/jiangzhiyi/downloads/2015年/2015年6月12日'
new_path = r'/Users/jiangzhiyi/downloads/yan_new'

photos = os.listdir(old_path)
# print(photos)
count = 0
for i in photos:
    if i.endswith('cr2'):
        old_pic_path = old_path + '/' + i
        new_pic_path = new_path + '/' + i
        shutil.move(old_pic_path, new_pic_path)
        count += 1

print(count)



