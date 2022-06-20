import magic
import os
for filename in os.listdir():
    # result = magic.from_file(filename)
    result = magic.from_buffer(open(filename, "rb").read(2048))
    print(f"{filename} je tipa {result}")