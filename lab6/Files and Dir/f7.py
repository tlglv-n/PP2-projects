import shutil
f = open("f7_1.txt", "w")
f.write("some facts about nothing")
f.close()

shutil.copy("f7_1.txt", "f7_2.txt")
f = open("f7_2.txt", "r")
print(*f.readlines())
