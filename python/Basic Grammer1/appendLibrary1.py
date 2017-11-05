# 임시파일(tempfile) 모듈 : 임시적으로 파일을 만들어 사용할때 유용하게 쓰이는 모듈이다.
'''
	tempfile.mktemp() : 임시로 파일을 만들어서 돌려주는 함수(중복되지 않도록 만들어 준다.)
	tempfile.TemporaryFile() : 임시적인 저장공간으로 사용될 파일 객체를 돌려주는 함수, w + b모드를 갖는다.

	mode
	w : 쓰기모드로 파일 열기
	r : 읽기모드로 파일 열기
	a : 추가모드로 파일 열기
	b : 바이너리 모드로 파일 열기

	w+, r+, a+ 파일을 업데이트할 용도로 사용
	b는 w, r, a뒤에 붙여서 사용한다.

	r : 단지 읽기 위해서 사용하는 모드(스트림은 제일 처음 위치)
	r+ : 읽기와 쓰기 모드로 파일을 연다.
	w : 파일을 쓰기모드로 열고, 파일이 없는 경우에는 새로 생성(스트림의 위치는 파일 처음 위치)
	w+ : 읽기와 쓰기 모드로 열고, 파일이 없을 경우에는 새로 생성
	a : 쓰기모드로 파일을 열고, 파일이 없는 경우는 새로 생성(파일이 있는 경우에는 스트림의 위치가 파일 끝에 위치0
	a+ : 읽기와 쓰기 모드로 파일을 연다. 파일이 없을 경우 파일을 새로 생성. 포인터의 위치는 파일 끝에 위치한다.

	모드 활용 예)
		파일을 읽을려면 : r, r+, w+, a+
		파일을 쓰려면 : r+, w, w+, a, a+
		없는 파일을 생성하려면 : w, w+, a, a+
		파일을 덮어쓸려면 : w, w+
		파일을 덧붙이려면 : 1. 앞쪽에 붙이려면 : r+
		                           2. 뒷쪽에 붙이려면 : a, a+
'''
import tempfile

#fp = tempfile.mktemp()
#print(fp)

from tempfile import TemporaryFile
f = tempfile.TemporaryFile("w+t")
f.write("하이 파이썬 \n")
f.seek(0)
data = f.read()

#with TemporaryFile("w+t") as f:
#	f.write("하이 파이썬 \n")
#	f.seek(0)
f.close()

print(data)
