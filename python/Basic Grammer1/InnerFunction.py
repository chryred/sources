''' [내장함수]
	print(x)				객체를 문자열로 표시한다.
	input([prompt])	사용자 입력을 문자열로 반환한다.
	help([x])				x에 대한 도움말을 출력한다.
	globals()			전역 변수의 리스트를 반환한다.
	locals() 혹은 vars()	지역 변수의 리스트를 반환한다.
	vars(obj)				__dict__어트리뷰트를 반환한다.(객체의 내부 변수가 저장된 딕셔너리)
	del(x) 혹은 del x		객체를 변수 공간에서 삭제한다.
	eval(expr)				파이썬 명령을 실행시킨다.
	open(filename[,mode]))	파일을 연다.
	str(obj)							문자열로 반환해 준다.
	list(obj)							데이터를 받아서 순서열 리스트로 반환함.
	
	[기본 자료형의 생성과 변환 함수]
	object()				새로운 object(모든 객체의 base)를 생성한다.
	bool(obj)			객체의 진리값을 반환한다.
	int(obj)				문자열 형태의 숫자나 실수를 정수로 변환한다.
	float(obj)			문자열 형태의 숫자나 정수를 실수로 변환한다.
	complex(re[, img])	문자열이나 주어진 숫자로 복소수를 생성한다.

	[기본 자료형의 정보를 얻어 함수]
	type(obj)			객체의 형을 반환한다.
	dir(obj)				객체가 가진 함수나 변수들을 리스트 형태로 반환한다.
	repr(obj)			eval()함수로 다시 객체를 복원할 수 잇는 문자열 생성
							repr()과 유사하나 non-ascii문자는 escape한다.
	id(obj)				객체의 고유번호(int형)을 반환한다.
	hash(obj)			객체의 해시값(int형)을 반환. (같은 값이면 해시도 같다.)
	chr(num)			ASCII값을 문자로 반환
	ord(str)				한문자의 ASCII값을 반환
	isinstance(obj, className)	객체가 클래스의 인스턴스인지를 판단한다.
	issubclass(class, classinfo)	class가 classinfo의 서브클래스일때 True반환

'''

help(locals)
x = complex(1, 2)
print(eval("x * 10"))