'''[산술/논리 연산에 관련된 함수]
   hex(n)						정수 n의 16진수 값을 구해서 '문자열'로 반환한다.
   oct(n)						정수 n의 8진수 값을 구해서 '문자열'로 반환한다.
   bin(x)						정수 n의 2진수 값을 구해서 '문자열'로 반환한다.
   abs(n)						절대값을 구한다. 복수수의 경우 크기를 구한다.
   pow(x,y[,z])				거듭제곱을 구한다. pow(x,y)은 x**y와 같다.
   divmod(a,b)				a를 b로 나눈(몫, 나머지)를 구한다. 튜플 반환
   all(iterable)				iterable의 모든 요소가 True일 경우 True를 반환
   any(iterable)			iterable의 하나 이상의 요소가 True일 경우 True를 반환
   max(iterable)			최대값을 구한다.
   max(arg1, arg2, ...)
   min(iterable)			최소값을 구한다.
   min(arg1, arg2, ...)
   round()					반올림을 한다.
'''

def dynamicFunc(x, *y):
	print(x)
	print(type(y))
	print(y[0])

dynamicFunc(1, [1, 2, 3])

print(abs(1+2j))