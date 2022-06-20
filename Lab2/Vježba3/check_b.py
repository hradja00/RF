import hashlib
import glob
import magic

filenames = glob.glob("Secret*")

HASH_TO_TEST = "c15e32d27635f248c1c8b66bb012850e5b342119"

for filename in filenames:
    with open(filename, 'rb') as inputFile:
        readFile = inputFile.read()

        md5hash = hashlib.md5(readFile)
        md5hashed = md5hash.hexdigest()

        sh1hash = hashlib.sha1(readFile)
        sh1hashed = sh1hash.hexdigest()

        sha256hash = hashlib.sha256(readFile)
        sha256hashed = sha256hash.hexdigest()

        if(md5hashed == HASH_TO_TEST or sh1hashed == HASH_TO_TEST or sha256hashed == HASH_TO_TEST):
            print("File you are looking for is: " + filename)
            print("File type is: " + magic.from_buffer(open(filename, "rb").read(2048)))       