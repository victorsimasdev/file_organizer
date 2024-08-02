import os
import shutil
import filecmp

def organize_files(path):
    existing_files = 0
    files = os.listdir(path)
    try:
        for file in files:
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                continue

            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            extension_dir = os.path.join(path, extension)
            
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)

            new_file_path = os.path.join(extension_dir, file)
            if not os.path.exists(new_file_path):
                shutil.move(file_path, new_file_path)
            else:
                if not filecmp.cmp(file_path, new_file_path, shallow=False):
                    new_file_path = os.path.join(extension_dir, f"copy_{file}")
                    shutil.move(file_path, new_file_path)
                else:
                    existing_files += 1

        print('Arquivos organizados com sucesso!')
        if existing_files != 0:
            print(f'{existing_files} arquivos já existentes não foram movidos.')
    except Exception as e:
        print('Erro ao organizar arquivos: ', e)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    organize_files(path)