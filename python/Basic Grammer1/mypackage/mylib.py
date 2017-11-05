# 전체(절대:absolute)경로를 이용해서 지정하는 경우
# from AAA.BBB.bbb import test_bbb
# 상대(relative)경로를 이용해서 지정하는 경우(".."(이전폴더), "."(현재폴더)를 사용한다.)
# from ..bbb import test_bbb
# 이러한 relative접근자는 모듈에서만 사용 가능하다.
# 파이썬 셸(인터프리터)에서는 사용할 수 없다.
 
def add_txt(t1, t2):
	return t1 + ":" + t2

def reverse1(x, y, z):
	return z, y, x