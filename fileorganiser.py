import os
import shutil
path=input('enter the name of the folder ')
listoffiles= os.listdir(path)
for file in listoffiles:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file, path+'/'+ext + '/'+ file)
    else:
        os.mkdir(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext + '/'+ file)

print('folder sorted')