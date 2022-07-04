import hashlib
import random

from datetime import datetime

def hash(plain_text: str, salt: str) -> str:
  return hashlib.pbkdf2_hmac('sha512', plain_text.encode('utf-8'), salt.encode('utf-8'), 100000).hex()

def generate_salt() -> str:
  a = str(random.randint(10000,100000))
  b = str(datetime.utcnow())
  return hashlib.sha256((a+b).encode('utf8')).hexdigest()[:16]
