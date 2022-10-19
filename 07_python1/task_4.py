# Написать скрипт, который:
#
# 1. принимает на входе два аргумента. Первый - режим преобразования, второй - строка;
# 2. если первый параметр равен `crypt` - преобразует второй параметр в строку Base64;
# 3. если первый параметр равен `decrypt` - преобразует второй параметр в текст;
# 4. если первый параметр равен любой другой строке - выйти из скрипта с ненулевым кодом возврата и сообщить об этом пользователю;
# 5. если количество параметров скрипта не равно двум - выйти из скрипта с ненулевым кодом возврата выдать сообщение пользователю и завершить работу.
#
# Пример работы:
#
# ```
# $ ./script.py crypt test
# Encrypting...
# dGVzdAo=
# $ ./script.py decrypt dGVzdAo=
# Decrypting...
# test
# ```
import base64
import sys

args = sys.argv
if len(args) < 3:
    print('Incorrect input')
    exit(1)

if args[1] == 'crypt':
    print('Encrypting...')

    text_bytes = args[2].encode('ascii')
    enc = base64.b64encode(text_bytes)
    print(enc.decode('ascii'))

    exit(0)
elif args[1] == 'decrypt':
    print('Decrypting...')

    text_bytes = args[2].encode('ascii')
    dec = base64.b64decode(text_bytes)
    print(dec.decode('ascii'))

    exit(0)
else:
    print('Incorrect input')
    exit(1)
