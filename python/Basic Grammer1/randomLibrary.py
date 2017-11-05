'''[random 모듈 : 난수 발생 모듈]
   난수 : 0.0 ~ 1.0사이의 실수 값
'''

import random
print(random.random())
print(int(random.random()  * 10))
print(random.randint(1, 10))


def pop_list(data):
	n = random.randint(0, len(data) - 1)
	return data.pop(n)

if __name__ == "__main__":
	data = [1, 2, 3, 4, 5]
	while data:
		print("data :", pop_list(data))
