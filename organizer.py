import os
import shutil

path = input('Insert path to organize: ')

files = os.listdir(path)
try:
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(path+'/'+extension):
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    print('Files organized.')
except Exception as e:
    print(e)