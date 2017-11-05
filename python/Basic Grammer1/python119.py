from random import shuffle

listdata = list(range(1, 11))
for i in range(3):
	shuffle(listdata)
	print(listdata)

solarsys = ["태양", "수성", "금성", "지구", "화성", "목성", "토성", "천왕성", "해왕성"]
ret = list(enumerate(solarsys))
print(ret)

for index, content in ret:
	print(index, " : ", content)

print(sum(listdata))