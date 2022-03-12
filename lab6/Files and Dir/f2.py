import os

path = "C:\ZNBURG\courses\PP2\lab6\Files and Dir"
if os.path.exists(path):
    print("The path and directory exist")
    f = open("f2.txt", "w")
    f.write("It's writable")
    f.close()

    f = open("f2.txt", "r")
    print(f.readline(), "It's readable", sep="\n")
    f.close()
else:
    print("Doesn't exist")
