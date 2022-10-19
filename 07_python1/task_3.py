# Напишите скрипт, который принимает один параметр и определяет,
# какой объект передан этим параметром (файл, каталог или не существующий).
# **Например:**
# **./test.py \windows**
# **c:\windows - dir**
# **./test.py c:\pagefile.sys**
# **c:\pagefile.sys - file**
# **user@user:~$ c:\windows1**
# **c:\windows1 - not exist**
import os
import sys

args = sys.argv
if len(args) >= 2 and os.path.exists(args[1]):
    path = args[1]
    if os.path.isdir(path):
        print("{0} - dir".format(path))
    elif os.path.isfile(args[1]):
        print("{0} - file".format(path))
    else:
        print("{0} - not exist".format(path))
else:
    print("{0} - not exist".format(args[1]))
