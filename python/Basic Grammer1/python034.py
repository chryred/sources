import time

for i in range(100):
	msg = "\r진행률 %d%%" %(i+1)
	print('' * len(msg), end='')
	print(msg, end='')
	time.sleep(0.1)
