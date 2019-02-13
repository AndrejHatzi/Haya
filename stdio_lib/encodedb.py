import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = 'password';
password = password_provided.encode()
salt = b'\x18p\xbf\xe7\x8c\\\xdf\x99\x0c\x15\xa3D\xc1K\xc3X';
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
key = base64.urlsafe_b64encode(kdf.derive(password))
with open('key.key', 'wb') as f:
    f.write(key)
