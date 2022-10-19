# Напишите скрипт, который выводит содержимое каталога и подсчитывает в нём количество файлов.
# **Например:**
# **./test_dir.py**
# **admin_scripts**
# **...**
# **Videos**
# **Total: 22**
import os
import sys

path = '/' if len(sys.argv) < 2 else sys.argv[1]
dirs = os.listdir(path)
for pth in dirs:
    print(pth)

print("Total: {}".format(len(dirs)))
