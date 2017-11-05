# 라이브러리(library) : 전세계의 파이썬 개발자(사용자)들에 의해서 이미 만들어진 프로그램들을 모아 놓은 것을 만한다.

'''
	파이썬 라이브러리는 파이썬 설치시 자동으로 컴퓨터에 설치가 된다.
	sys모듈, pickle모듈, io모듈, glob모듈, time모듈, calendar모듈,
	random모듈, 쓰레드(thread)모듈, ...

	sys.argv : 명령행에서 인수를 전달한다.
	sys.exit() : ctrl+z(윈도우 환경), ctrl+D(유닉스환경)를 눌러서 대화형 인터프리터(쉘)을 종료하는 기능
	sys.path : 자신이 만든 모듈을 불러서 사용하기 위해 위치를 지정하는 명령
	
	pickle모듈 : 객체 형태를 그대로 유지해서 파일에 저장 시키고, 불러 올 수 있게 하는 모듈이다.
					 바이너리 형태로 저장한다.
	pickle.dump(obj, file) : 객체를 저장시
	pickle.load(file명) : 저장된 객체를 불러올 경우
	pickle.dumps(obj) : 
	pickle.loads(String) : 
'''

import pickle
# listA = [1, 2, 3, 4]
listA = {"dict":1, "key":12, "value":"pickle"}
fp = open("dump.txt", "wb")
pickle.dump(listA, fp)
fp.close()

fp = open("dump.txt", "rb")
listB = pickle.load(fp)
print(listB)
fp.close()

class Foo:
	var = "Foo 클래스"

fooString = pickle.dumps(Foo)
print(fooString)
fooClass = pickle.loads(fooString)
print(fooClass)
foo = fooClass()
print(foo.var)