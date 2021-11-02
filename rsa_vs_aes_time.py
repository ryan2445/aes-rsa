from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
import binascii, time

#   Data to be encrypted
data = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

#----------------RSA PART----------------#

#   RSA Public / Private Keys
rsa_private_key = RSA.generate(2048)
rsa_public_key = rsa_private_key.publickey()

#   RSA encrypt / decrypt ciphers
rsa_cipher_encrypt = PKCS1_OAEP.new(rsa_public_key)
rsa_cipher_decrypt = PKCS1_OAEP.new(rsa_private_key)

#   Start timer for RSA encryption
rsa_start = time.perf_counter()

#   RSA Encryption
rsa_ciphertext = rsa_cipher_encrypt.encrypt(data)

#   RSA Decryption
rsa_decrypted = rsa_cipher_decrypt.decrypt(rsa_ciphertext)

#   End timer for RSA Decryption
rsa_end = time.perf_counter()

#   Print RSA Results
print(f"RSA Encrypted and Decrypted in {rsa_end - rsa_start:0.8f} seconds")
print("RSA Encrypted Data:\n", binascii.hexlify(rsa_ciphertext))
print("RSA Decrypted Data:\n", rsa_decrypted)

print("\n")

#----------------AES PART----------------#

#   AES Key
key = b"Ryans AES Key..."

#   AES CVC cipher use for encryption
cbc_cipher_encrypt = AES.new(key, AES.MODE_CBC)

#   AES CBC cipher used for decryption
cbc_cipher_decrypt = AES.new(key, AES.MODE_CBC, cbc_cipher_encrypt.iv)

#   Start AES timer
aes_start = time.perf_counter()

#   AES Encrypt
cbc_ciphertext = cbc_cipher_encrypt.encrypt(pad(data, AES.block_size))

#   AES Decrypt
cbc_decrypted = unpad(cbc_cipher_decrypt.decrypt(cbc_ciphertext), AES.block_size)

#   End AES timer
aes_end = time.perf_counter()

#   Print AES results
print(f"AES Encrypted and Decrypted in {aes_end - aes_start:0.8f} seconds")
print("AES CBC Encrypted Data:\n", binascii.hexlify(cbc_ciphertext))
print("AES CBC Decrypted Data:\n", cbc_decrypted)