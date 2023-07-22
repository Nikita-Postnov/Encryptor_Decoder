import tkinter as tk
from tkinter import filedialog
import os

# Функция для шифрования файла с помощью XOR
def xor_encrypt(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    encrypted_data = bytes([byte ^ key for byte in data])
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Функция для дешифрования файла с помощью XOR
def xor_decrypt(file_path, key):
    xor_encrypt(file_path, key)  # Дешифрование - это тоже самое, что и шифрование с тем же ключом

# Функция для выбора файла
def select_file():
    file_path = filedialog.askopenfilename()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

# Функция для шифрования или дешифрования файла
def process_file():
    file_path = entry_path.get()
    key = int(entry_key.get())

    if encrypt_var.get():
        xor_encrypt(file_path, key)
        label_status.config(text="Файл успешно зашифрован!", fg="green")
    else:
        xor_decrypt(file_path, key)
        label_status.config(text="Файл успешно дешифрован!", fg="green")

# Создаем окно
root = tk.Tk()
root.title("Шифратор и дешифратор файлов")

# Добавляем элементы интерфейса
label_path = tk.Label(root, text="Выберите файл:")
label_path.pack()

entry_path = tk.Entry(root, width=50)
entry_path.pack()

button_select = tk.Button(root, text="Обзор", command=select_file)
button_select.pack()

label_key = tk.Label(root, text="Введите ключ (целое число):")
label_key.pack()

entry_key = tk.Entry(root, width=20)
entry_key.pack()

encrypt_var = tk.BooleanVar()
checkbox_encrypt = tk.Checkbutton(root, text="Зашифровать", variable=encrypt_var)
checkbox_encrypt.pack()

button_process = tk.Button(root, text="Обработать", command=process_file)
button_process.pack()

label_status = tk.Label(root, text="")
label_status.pack()

root.mainloop()
