#  ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
#     ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     digits = '0123456789'
#     hexdigits = '0123456789abcdefABCDEF'
#     octdigits = '01234567'
#     printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
#     punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#     whitespace = ' \t\n\r\x0b\x0c'
aphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ абвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890='
encode_str = 'Секрет 294'
global_key = 11


def CipherTsesarEncode(plain_text, key):
    ciphertext = ''
    for symbol in plain_text:
        if symbol in aphabet:
            num = aphabet.find(symbol)
            num = num + key

            if num >= len(aphabet):
                num = num - len(aphabet)

            ciphertext = ciphertext + aphabet[num]
        else:
            ciphertext = ciphertext + symbol
            print(ciphertext)

    return ciphertext


def CipherTsesarDecode(ciphertext, key):
    decode_text = ''
    for symbol in ciphertext:
        if symbol in aphabet:
            num = aphabet.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(aphabet)

            decode_text += aphabet[num]
        else:
            decode_text += symbol

    return decode_text


cipher_text = CipherTsesarEncode(encode_str, global_key)
print('Encoded text: ' + cipher_text)
print('Original text: ' + CipherTsesarDecode(cipher_text, global_key))
