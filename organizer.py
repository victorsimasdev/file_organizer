import os
import shutil

path = input('Insert path to organize: ')
existing_files = 0
files = os.listdir(path)
try:
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(path+'/'+extension):
            if not os.path.exists(path+'/'+extension+'/'+file):
                shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
            else:
                existing_files += 1
        else:
            os.makedirs(path+'/'+extension)
            if not os.path.exists(path+'/'+extension+'/'+file):
                shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
            else:
                existing_files += 1
    if existing_files != 0:
        print(f'Arquivos organizados com sucesso! {existing_files} arquivos já existentes não foram movidos.')
    print('Arquivos organizados com sucesso!')
except Exception as e:
    print('Erro ao organizar arquivos: ', e)