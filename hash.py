from cryptography.hazmat.backends import default_backend
import base64
from cryptography.hazmat.primitives import hashes

print("HASHING \n")

#The MD5 hash function is not advisable to use as its not that secure
digestMD5 = hashes.Hash(hashes.MD5(), backend = default_backend()) #This calls the MD5 hash function
digestMD5.update(b"I love you and that's all that matters")
digestMD5.update(b"I know I'm weird but it's beyond my control")
textDigestMD5 = digestMD5.finalize() #This signals that we are done updating the hash function

#The SHAKE256 hash function allows you to determine the size of your hash code
digestSHAKE256 = hashes.Hash(hashes.SHAKE256(200), backend = default_backend()) #This calls the MD5 hash function
digestSHAKE256.update(b"I love you and that's all that matters")
digestSHAKE256.update(b"I know I'm weird but it's beyond my control")
textDigestSHAKE256 = digestSHAKE256.finalize() #This signals that we are done updating the hash function

#This is the SHA256 hash function
digestSHA256 = hashes.Hash(hashes.SHA256(), backend = default_backend()) #This calls the SHA256 hash function
digestSHA256.update(b"I love you and that's all that matters")
digestSHA256.update(b"I know I'm weird but it's beyond my control")
textDigestSHA256 = digestSHA256.finalize() #This signals that we are done updating the hash function

#This is the SHA512 hash function
digestSHA512 = hashes.Hash(hashes.SHA512(), backend = default_backend()) #This calls the SHA256 hash function
digestSHA512.update(b"I love you and that's all that matters")
digestSHA512.update(b"I know I'm weird but it's beyond my control")
textDigestSHA512 = digestSHA512.finalize() #This signals that we are done updating the hash function

print(f"MD5 Hash code: {base64.b64encode(textDigestMD5)}") #This converts the gibberish to base 64 encoding
print(f"SHA256 Hash code: {base64.b64encode(textDigestSHA256)}") #This converts the gibberish to base 64 encoding
print(f"SHA512 Hash code: {base64.b64encode(textDigestSHA512)}") #This converts the gibberish to base 64 encoding
print(f"SHAKE256 Hash code: {base64.b64encode(textDigestSHAKE256)}") #This converts the gibberish to base 64 encoding

print("\n")