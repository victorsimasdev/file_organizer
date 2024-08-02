import os
import shutil
import filecmp
import tkinter as tk
from tkinter import filedialog, messagebox

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
            
            if not os.path.exists(extension_dir) and extension != 'exe':
                os.makedirs(extension_dir)

            new_file_path = os.path.join(extension_dir, file)
            if not extension == 'exe':
                if not os.path.exists(new_file_path):
                    shutil.move(file_path, new_file_path)
                else:
                    if not filecmp.cmp(file_path, new_file_path, shallow=False):
                        new_file_path = os.path.join(extension_dir, f"copy_{file}")
                        shutil.move(file_path, new_file_path)
                    else:
                        existing_files += 1

        if existing_files != 0:
            messagebox.showinfo("Organização de Arquivos", f'Arquivos organizados com sucesso! {existing_files} arquivos já existentes não foram movidos.')
        else:
            messagebox.showinfo("Organização de Arquivos", 'Arquivos organizados com sucesso!')
    except Exception as e:
        messagebox.showerror("Erro", f'Erro ao organizar arquivos: {e}')

def select_organize():
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        organize_files(folder_selected)
if __name__ == "__main__":
    select_organize()