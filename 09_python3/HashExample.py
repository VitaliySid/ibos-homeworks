import hashlib

from Crypto import Random
from Crypto.Cipher import AES

text = 'test12345'
salt = 'salt'
print("MD5:")
for i in text.split():
    md5 = hashlib.md5(i.encode())

    print(i, ':', md5.hexdigest())

print(hashlib.md5(text.encode()).hexdigest())

print("SHA256:")
sha_str = hashlib.pbkdf2_hmac('sha256', bytes(text.encode()), bytes(salt.encode()), 100000)
print(sha_str.hex())

print("AES:")
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
plain_text = '''Secret
Information
'''
key = hashlib.sha256(b'111').digest()
print('KEY: ', key)

plain_text_pad = pad(plain_text)
iv = Random.new().read(BS)
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher_text = (iv + cipher.encrypt(plain_text_pad.encode()))
print("\nCiphered text:", cipher_text.hex())

unpad = lambda s: s[:-ord(s[len(s) - 1:])]
cipher_text = cipher_text
iv = cipher_text[:BS]
cipher = AES.new(key, AES.MODE_CBC, iv)
plain_text_unpad = unpad(cipher.decrypt(cipher_text[BS:]))
print("\nPlain text:", plain_text_unpad)