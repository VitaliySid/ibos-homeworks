# Напишите два скрипта, каждый из которых принимает один параметр и:
# - второй - прибавляет к параметру единицу как число.
# **Например:**
# **./python3 test_2.py 5**
# **6**
import sys

args = sys.argv
if len(args) >= 2 and args[1].isnumeric():
    print(int(args[1]) + 1)
else:
    print('Incorrect input')
