import os
path = "C:\ZNBURG\courses\PP2\lab6\Files and Dir"
if os.path.isdir(path):
    f = open("f8.txt", "w")
    f.write("nothing change")
    f.close()
    if os.path.isfile("f8.txt"):
        os.remove("f8.txt")
else:
    print("The path doesn't exist")
