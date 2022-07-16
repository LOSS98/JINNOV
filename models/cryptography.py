import hashlib
import random

from datetime import datetime

def hash(plain_text: str, salt: str) -> str:
  """
  It takes a plain text password and a salt, and returns a hashed password
  
  :param plain_text: The password to be hashed
  :type plain_text: str
  :param salt: A random string of characters that is used to make the hash more secure
  :type salt: str
  :return: A string of the hashed password.
  """
  return hashlib.pbkdf2_hmac('sha512', plain_text.encode('utf-8'), salt.encode('utf-8'), 100000).hex()

def generate_salt() -> str:
  """
  Generate a random salt with a random number between 10e4 and 10e5, and the current UTC time 
  according to the SHA-256 algorithm.

  :return: The 16 first characters of the new generated salt as a string
  """
  a = str(random.randint(10000,100000))
  b = str(datetime.utcnow())
  return hashlib.sha256((a+b).encode('utf8')).hexdigest()[:16]
