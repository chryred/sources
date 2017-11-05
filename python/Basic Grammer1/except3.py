# 에러 피하기(pass활용): 특정 에러가 발생할 경우 통과시키는 방법

try:
	fp = open("nofile.txt", "r")
except FileNotFoundError:
	pass