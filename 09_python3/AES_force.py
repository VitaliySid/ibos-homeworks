import hashlib

from Crypto import Random
from Crypto.Cipher import AES


def CryptAES(text, key):
    print('KEY: ', key)
    block_size = AES.block_size
    pad = lambda s: s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)
    text_pad = pad(text)
    iv = Random.new().read(block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = (iv + cipher.encrypt(text_pad.encode()))
    print("\nCiphered text:", cipher_text.hex())
    return cipher_text


def DecryptAES(cipher_text, key):
    print('KEY: ', key)
    block_size = AES.block_size
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]
    iv = cipher_text[:block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    text_unpad = unpad(cipher.decrypt(cipher_text[block_size:]))
    print("\nPlain text:", text_unpad)
    return text_unpad


def ForceDecrypt(cipher_text, original_text, keys):
    for key in keys:
        decrypt_text = DecryptAES(cipher_text, hashlib.sha256(key).digest())
        if original_text == decrypt_text.decode():
            print("Success key:", key.decode())
            return


plain_text = '''Secret
Information
'''
key = hashlib.sha256(b'111').digest()
cipher_text = CryptAES(plain_text, key)

keys = [bytes(str(k).encode()) for k in range(110, 115)]

ForceDecrypt(cipher_text, plain_text, keys)
