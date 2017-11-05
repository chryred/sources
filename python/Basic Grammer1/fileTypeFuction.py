# import를 이용한 모듈 입력방법(모듈: 함수들과 변수들을 모아놓은 것(sys, ...))

import sys # 파이썬에서 제공하는 모듈
			   # (도스 명령 중에 type이라는 기능을 구현하기 위해서 필요한 sys모듈을 가져온다)
args = sys.argv[1:]
# print(sys.argv)
print(args)

for filename in args:
	with open(filename, "r") as fp:
		lists = fp.readlines()
		print(lists)


