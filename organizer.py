import os
import shutil

path = input('Insira o caminho para organizar: ')
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
    print('Arquivos organizados com sucesso!')
    if existing_files != 0:
        print(f'{existing_files} arquivos já existentes não foram movidos.')
except Exception as e:
    print('Erro ao organizar arquivos: ', e)