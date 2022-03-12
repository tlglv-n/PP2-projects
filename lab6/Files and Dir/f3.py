import os
path = "C:\ZNBURG\courses\PP2\lab6\Files and Dir"
if os.path.isdir(path):
    print("The path exists")
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print("Doesn't exist")
