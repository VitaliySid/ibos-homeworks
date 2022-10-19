# Напишите два скрипта, каждый из которых принимает один параметр и:
# - первый - прибавляет к параметру единицу как строку.
# **Например:**
# **./python3 test_1.py 5**
# **51**
import sys

args = sys.argv
if len(args) >= 2:
    print(args[1] + '1')
else:
    print('Incorrect input')
