# try ~ finally문

import sys
import time

fp = None

try:
	fp = open("test_2.txt", "r")

	while True:
		line = fp.readline()
		if(len(line) == 0):
			break
		print(line)
		sys.stdout.flush()  # print문 뒤에 사용해서 발로바로 화면에 출력하라...
		time.sleep(2)
except IOError:
	print("파일이 존재하지 않습니다.")
except KeyboardInterrupt:
	print("사용자가 취소를 하였습니다....")
finally:
	if fp:
		fp.close()
	print("파일을 close처리 하였습니다.")