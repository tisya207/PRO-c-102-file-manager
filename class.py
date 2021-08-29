import os
import shutil
#print(os.system('date'))
#os.mkdir('C:/tisyawhj/test')
print(os.getcwd())
path= 'C:/tisyawhj/test/abc.docx'
path1= 'C:/tisyawhj/c 99/test/abc.docx'
shutil.move(path1, path)
print(os.path.exists(path))
print(os.path.exists(path1))
root_ext= os.path.splitext(path)
print(root_ext)
print(os.listdir())