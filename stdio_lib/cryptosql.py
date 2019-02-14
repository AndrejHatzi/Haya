import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import sqlite3
file = open('key.key', 'rb')
key = file.read()
file.close()

message = "Hail the american night"
encoded = message.encode()
f = Fernet(key)

encrypted = f.encrypt(encoded)
#print(encrypted)
decrypted = f.decrypt(encrypted)
original_message = decrypted.decode()
#print(original_message)

connection = sqlite3.connect('encrypted_db')
cursor = connection.cursor()
try:
    cursor.execute('CREATE TABLE names(id INTEGER PRIMARY KEY, name TEXT)')
except:
    pass
cursor.execute('INSERT INTO names VALUES(?, ?)', (2, encrypted))
cursor.execute('SELECT * FROM NAMES')
data = cursor.fetchall()
for rows in data:
    ke = f.decrypt(rows[1])
    om = ke.decode()
    print(om)
    connection.commit()
