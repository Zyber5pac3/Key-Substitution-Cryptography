Key-Substitution-Cryptography
=============================

Project in python 3.4 and Java 7 to encrypt/ decrypt Strings

PLEASE OPEN THE README FILE IN RAW MODE

Algorithm:

INDEX:
  x = current character in the String
  a = preceeding character in the String
  b = succeeding character in the String
  z = new , encrypted character , REPLACES x IN THE STRING.
  k = generator

ENCRYPTION:
      k.x + a + b + ( k - ( a + b ) mod k)
  z = ------------------------------------
                      k

DECRYPTION:
      k.z - a - b - ( k - ( a + b ) mod k)
  x = ------------------------------------
                      k
