add = lambda x, y: x + y
ret = add(1, 3)
print(ret)

funcs= [lambda x: x + ".pptx", lambda x: x + ".docx"]
ret1 = funcs[0]("Intro")
ret2 = funcs[1]("Report")

print(ret1)
print(ret2)

names = {"Marry":10999, "Sams":211}
ret3 = sorted(names.items(), key=lambda x: x[1])
print(ret3)