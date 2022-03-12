list1 = input().replace(' ', "*")
code = compile(list1, "<string>", "eval")
print(eval(code))
