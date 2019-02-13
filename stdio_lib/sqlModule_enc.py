# some_file.py
#import sys
#sys.path.insert(0, '/path/to/application/app/folder')
#
#import file
#-----------------------------------------------------
'''
import sqlite3
connection = sqlite3.connect('sqlite3_db')
cursor = connection.cursor()
# cursor.execute('CREATE TABLE names(id INTEGER PRIMARY KEY, name TEXT)')
#cursor.execute('INSERT INTO names VALUES(?, ?)', (1, 'Donald'))
#cursor.execute('INSERT INTO names(name) VALUES(?)', ('Richard', ))

cursor.execute('SELECT * FROM names')
row = cursor.fetchall()
for rows in row:
    #print('id:', str(rows[0]), str(rows[1]))
    print(rows)
connection.commit()
'''

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

message = "Adamo"

encoded = message.encode()
f = Fernet(key)

encrypted = f.encrypt(encoded)


connection = sqlite3.connect('teste1_db')
cursor = connection.cursor()
try:
    cursor.execute('CREATE TABLE names(id INTEGER PRIMARY KEY, name TEXT)')
except:
    pass

cursor.execute('INSERT INTO names VALUES(?, ?)', (2, encrypted))
cursor.execute('SELECT * FROM NAMES')
data = cursor.fetchall()
#=> colocar esta treta toda num ficheiro e abri-lo simples!
for rows in data:
    print(rows[1])
    x = rows[1].decode()
    decrypted = f.decrypt(x)
    print(decrypted)

    
connection.commit()
