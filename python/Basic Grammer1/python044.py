#from mypackage import mylib
import mypackage.mylib

# __init__.py : 3.3 이전 버전에서는 init파일이 없으면, 패키지로 인식이 안됨.
# 3.3버전부터는 init파일이 없어도 패키지로 인식됨.
# 하위버전과 호환을 위해서는 __init__.py파일을 생성하는 것이 올바른 방법이다.
test = 12
del test
print(dir(mypackage))
print(dir())
ret1 = mypackage.mylib.add_txt("대한민국", "1등")
ret2 = mypackage.mylib.reverse1(1, 2, 3)
print(ret1)
print(ret2)