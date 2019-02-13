from cryptography.fernet import Fernet
file = open('key.key', 'rb')
key = file.read()
file.close()

message = "my deep dark secret"
encoded = message.encode()

f = Fernet(key)
encrypted = f.encrypt(encoded)
print(encrypted)


f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)
print(decrypted)

original_message = decrypted.decode()
print(original_message)


##encrypt files
with open('myfile.txt', 'rb') as f:
    data = f.read()

f3 = Fernet(key)
enc2 = f3.encrypt(data)
with open('myfile.txt.encrypted', 'wb') as f:
    f.write(encrypted)

f4 = Fernet(key)
enc3 = f4.decrypt(enc2)
##decrypt files
with open('myfile.txt.decrypted', 'wb') as f:
    f.write(enc3)





print(enc2)
