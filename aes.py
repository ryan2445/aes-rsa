from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode

key = b"Ryans AES Key..."
data = b"Ryans AES Data"

ecb_cipher = AES.new(key, AES.MODE_ECB)
ecb_ciphertext = ecb_cipher.encrypt(pad(data, AES.block_size))
ecb_ciphertext_b64 = b64encode(ecb_ciphertext).decode('utf-8')
print("ECB Ciphertext Base64:", ecb_ciphertext_b64)
print("ECB Plaintext:", unpad(ecb_cipher.decrypt(ecb_ciphertext), AES.block_size))

print("\n")

cbc_cipher1 = AES.new(key, AES.MODE_CBC)
cbc_ciphertext = cbc_cipher1.encrypt(pad(data, AES.block_size))
cbc_ciphertext_b64 = b64encode(cbc_ciphertext).decode('utf-8')
print("CBC Ciphertext:", cbc_ciphertext_b64)
cbc_cipher2 = AES.new(key, AES.MODE_CBC, cbc_cipher1.iv)
print("CBC Plaintext:", unpad(cbc_cipher2.decrypt(cbc_ciphertext), AES.block_size))

print("\n")

cfb_cipher1 = AES.new(key, AES.MODE_CFB)
cfb_ciphertext = cfb_cipher1.encrypt(data)
cfb_ciphertext_b64 = b64encode(cfb_ciphertext).decode('utf-8')
print("CFB Ciphertext:", cfb_ciphertext_b64)
cfb_cipher2 = AES.new(key, AES.MODE_CFB, cfb_cipher1.iv)
print("CFB Plaintext:", cfb_cipher2.decrypt(cfb_ciphertext))

print("\n")

ofb_cipher1 = AES.new(key, AES.MODE_OFB)
ofb_ciphertext = ofb_cipher1.encrypt(data)
ofb_ciphertext_b64 = b64encode(ofb_ciphertext).decode('utf-8')
print("OFB Ciphertext:", ofb_ciphertext_b64)
ofb_cipher2 = AES.new(key, AES.MODE_OFB, ofb_cipher1.iv)
print("OFB Plaintext:", ofb_cipher2.decrypt(ofb_ciphertext))


print("\n")

ctr_cipher1 = AES.new(key, AES.MODE_CTR)
ctr_ciphertext = ctr_cipher1.encrypt(data)
ctr_ciphertext_b64 = b64encode(ctr_ciphertext).decode('utf-8')
print("CTR Ciphertext:", ctr_ciphertext_b64)
ctr_cipher2 = AES.new(key, AES.MODE_CTR, nonce = ctr_cipher1.nonce)
print("CTR Plaintext:", ctr_cipher2.decrypt(ctr_ciphertext))