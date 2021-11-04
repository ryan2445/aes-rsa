from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

key = b"Ryans AES Key..."
data = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
#                               Error here vvvv, 'tema' used to be 'amet'
data_with_errors = b"Lorem ipsum dolor sit tema, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print("#--------- AES Encryption Using Different Modes ---------#")
print("Using AES Key:", key)
print("USing AES Plaintext:", data)
print("\n")

#   Encrypting and decrypting with AES ECB
ecb_cipher = AES.new(key, AES.MODE_ECB)
ecb_ciphertext = ecb_cipher.encrypt(pad(data, AES.block_size))
print("AES ECB Ciphertext:\n", binascii.hexlify(ecb_ciphertext))
print("\nAES ECB Plaintext:\n", unpad(ecb_cipher.decrypt(ecb_ciphertext), AES.block_size))

print("\n")

#   Encrypting and decrypting with Errors in AES ECB
ecb_cipher = AES.new(key, AES.MODE_ECB)
ecb_ciphertext = ecb_cipher.encrypt(pad(data_with_errors, AES.block_size))
print("AES ECB Ciphertext with Errors:\n", binascii.hexlify(ecb_ciphertext))
print("\nAES ECB Plaintext with Errors:\n", unpad(ecb_cipher.decrypt(ecb_ciphertext), AES.block_size))

print("\n")

#   Encrypting and decrypting with AES CBC
cbc_cipher1 = AES.new(key, AES.MODE_CBC)
cbc_ciphertext = cbc_cipher1.encrypt(pad(data, AES.block_size))
print("AES CBC Ciphertext:\n", binascii.hexlify(cbc_ciphertext))
cbc_cipher2 = AES.new(key, AES.MODE_CBC, cbc_cipher1.iv)
print("\nAES CBC Plaintext:\n", unpad(cbc_cipher2.decrypt(cbc_ciphertext), AES.block_size))

print("\n")

#   Encrypting and decrypting with Errors in AES CBC
cbc_cipher1 = AES.new(key, AES.MODE_CBC, cbc_cipher1.iv)
cbc_ciphertext = cbc_cipher1.encrypt(pad(data_with_errors, AES.block_size))
print("AES CBC Ciphertext with Errors:\n", binascii.hexlify(cbc_ciphertext))
cbc_cipher2 = AES.new(key, AES.MODE_CBC, cbc_cipher1.iv)
print("\nAES CBC Plaintext with Errors:\n", unpad(cbc_cipher2.decrypt(cbc_ciphertext), AES.block_size))

print("\n")

#   Encrypting and decrypting with AES CFB
cfb_cipher1 = AES.new(key, AES.MODE_CFB)
cfb_ciphertext = cfb_cipher1.encrypt(data)
print("AES CFB Ciphertext:\n", binascii.hexlify(cfb_ciphertext))
cfb_cipher2 = AES.new(key, AES.MODE_CFB, cfb_cipher1.iv)
print("\nAES CFB Plaintext:\n", cfb_cipher2.decrypt(cfb_ciphertext))

print("\n")

#   Encrypting and decrypting with Errors in AES CFB
cfb_cipher1 = AES.new(key, AES.MODE_CFB, cfb_cipher1.iv)
cfb_ciphertext = cfb_cipher1.encrypt(data_with_errors)
print("AES CFB Ciphertext with Errors:\n", binascii.hexlify(cfb_ciphertext))
cfb_cipher2 = AES.new(key, AES.MODE_CFB, cfb_cipher1.iv)
print("\nAES CFB Plaintext with Errors:\n", cfb_cipher2.decrypt(cfb_ciphertext))

print("\n")

#   Encrypting and decrypting using AES OFB
ofb_cipher1 = AES.new(key, AES.MODE_OFB)
ofb_ciphertext = ofb_cipher1.encrypt(data)
print("AES OFB Ciphertext:\n", binascii.hexlify(ofb_ciphertext))
ofb_cipher2 = AES.new(key, AES.MODE_OFB, ofb_cipher1.iv)
print("\nAES OFB Plaintext:\n", ofb_cipher2.decrypt(ofb_ciphertext))

print("\n")

#   Encrypting and decrypting with Errors using AES OFB
ofb_cipher1 = AES.new(key, AES.MODE_OFB, ofb_cipher1.iv)
ofb_ciphertext = ofb_cipher1.encrypt(data_with_errors)
print("AES OFB Ciphertext with Errors:\n", binascii.hexlify(ofb_ciphertext))
ofb_cipher2 = AES.new(key, AES.MODE_OFB, ofb_cipher1.iv)
print("\nAES OFB Plaintext with Errors:\n", ofb_cipher2.decrypt(ofb_ciphertext))

print("\n")

#   Encrypting and decrypting using AES CTR mode
ctr_cipher1 = AES.new(key, AES.MODE_CTR)
ctr_ciphertext = ctr_cipher1.encrypt(data)
print("AES CTR Ciphertext:\n", binascii.hexlify(ctr_ciphertext))
ctr_cipher2 = AES.new(key, AES.MODE_CTR, nonce = ctr_cipher1.nonce)
print("\nAES CTR Plaintext:\n", ctr_cipher2.decrypt(ctr_ciphertext))

print("\n")

#   Encrypting and decrypting with Errors using AES CTR mode
ctr_cipher1 = AES.new(key, AES.MODE_CTR, nonce = ctr_cipher1.nonce)
ctr_ciphertext = ctr_cipher1.encrypt(data_with_errors)
print("AES CTR Ciphertext with Errors:\n", binascii.hexlify(ctr_ciphertext))
ctr_cipher2 = AES.new(key, AES.MODE_CTR, nonce = ctr_cipher1.nonce)
print("\nAES CTR Plaintext with Errors:\n", ctr_cipher2.decrypt(ctr_ciphertext))
