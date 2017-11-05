fp = open("test_2.txt", "r")
line_num = 1
line = fp.readline()
while line:
	print("%d %s" %(line_num, line), end='')
	line = fp.readline()
	line_num = line_num + 1
fp.close()
print("-" * 10)
fp = open("test_2.txt", "r")
lines = fp.readlines()
for line_num, line in enumerate(lines):
	print("%d %s" %(line_num + 15, line), end='')
fp.close()