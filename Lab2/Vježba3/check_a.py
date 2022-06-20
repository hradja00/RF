import hashlib
import os
import glob

filenames = glob.glob("test*")

for filename in filenames:
    with open(filename, 'rb') as inputFile:
        readFile = inputFile.read()

        md5hash = hashlib.md5(readFile)
        md5hashed = md5hash.hexdigest()

        sh1hash = hashlib.sha1(readFile)
        sh1hashed = sh1hash.hexdigest()

        sha256hash = hashlib.sha256(readFile)
        sha256hashed = sha256hash.hexdigest()

        print(f"{filename} is hashed as:\n md5: {md5hashed}\n sha1: {sh1hashed}\n sha256: {sha256hashed}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")