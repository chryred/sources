'''
    Numpy
    - Numerical Python
    - 파이썬의 고성능 과학 계산용 기초 패키지
    - Matrix와 Vector와 같은 Array연산의 사실상의 표준(Standard de facto)
    - 한글로 넘파이로 주로 통칭, 넘피/늄파이라고 부르는 사람도 있음.
    특징
    - 일반 List에 비해 빠르고, 메모리 효율적
    - 반복문이 없이 데이터 배열에 대한 처리를 지원함.
    - 선행대수와 관련된 다양한 기능을 제공함
    - C, C++, 포트란등의 언어와 통합가능
      From 파이썬 라이브러리를 활용한 데이터 분석
    References
    - cs231 - http://cs231n.github.io/python-numpy-tutorial/#Numpy
    - https://docs.scipy.org/doc/Numpy-dev/user/quickstart.html
    - 데이터 사이언스 스쿨(파이썬 버전) - https://goo.gl/3hsjbS
    - Numpy - https://goo.gl/7Nwjw
    - 파이썬 라이브러리를 활용한 데이터 분석
    Numpy example - import
    import numpy as np
    - numpy의 호출방법
    - 일반적으로 numpy는 np라는 alias(별칭)를 이용해서 호출함
    - 특별한 이유는 없음 세계적인 약속 같은 것
    - numpy는 np.array함수를 활용하여 배열을 생성함
    - numpy는 하나의 데이터 type만 배열에 넣을 수 있음
    - List와 가장 큰 차이점, Dynamic typing not supported
    - C의 Array를 사용하여 배열을 생성함.
    - dtype속성 : numpy array의 데이터 type을 반환함
      https://docs.scipy.org/doc/numpy/reference/arrays.scalars.html#arrays-scalars-built-in
'''
import numpy as np
test_array = np.array([1, 3, 4, 5], float)
print(test_array)
print(type(test_array[3]))
print("*" * 20)
test_array = np.array([1, 2, 3, "8"], np.float32)  # 문자열을 넣어도 자동으로 형변환 처리됨
print(test_array)
print(type(test_array[3]))
print(test_array.dtype)
print("*" * 20)
'''
    Numpy example - 값 할당
    - List와 달리 이차원 배열에서 [0, 0]과 같은 표기법을 제공함
    - Matrix관점에서는 앞은 row 뒤는 column을 의미함.
'''
a = np.array([[1,2,3], [4.5, 5, 6]], int)
print(a)
print(a[0, 0])
print(a[0][0])

a[0,0] = 12
print(a)
a[0][0] = 5
print(a)
print("*" * 20)
'''
    Numpy exaple - Slicing
'''
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], int)
print(a[:,2:])  # 전체 Row의 2열 이상
print(a[1,1:3]) # 1Row의 1열 ~ 2열
print(a[1:3]) # 1row ~ 2Row의 전체
print("*" * 20)
'''
    Numpy exaple - function #1, 2
'''
print("#1", np.arange(30)) # range: List의 range와 같은 효과 , integer 0~29까지 배열 추출
print("#2", np.arange(30).dtype) # dtype: 배열의 data type을 표시함
print("#3", np.arange(30).reshape(5, 6)) # reshape(x, y): 기존 배열을 row x, column y의 two dimensional array로 변경(three도 가능)
print("#3", np.arange(30).reshape(5, 6)) # reshape(x, y): 기존 배열을 row x, column y의 two dimensional array로 변경(three도 가능)
print("#4", np.zeros(10)) # 10 - zero vector 생성
print("#5", np.zeros((2, 5))) # 2 by 5 -zero matrix 생성
print("#6", np.zeros((2, 5), int)) # 2 by 5 -zero matrix를 integer type으로 생성
print("#7", np.zeros((2, 5)).ndim) # 2 by 5의 matrix의 차원의 크기 (row 기준)
print("#8", np.zeros((2, 5)).shape) # 2 by 5의 matrix의 전체 크기 (tuple형태로 리턴)
print("*" * 20)
'''
    Numpy exaple - function #3
'''
print("#1", np.ones((5, 5), float)) # 초기값을 1로 설정하여 matrix생성
print("#2", np.empty((5, 5), float)) # 초기값이 할당되지 않는 matrix생성
#print(np.ones((5, 5), float)[0, 0] == np.empty((5, 5), float)[0, 0])
print("#3", np.eye(5, 5)) # x by y의 matrix를 생성 후 대각행렬에 1을 할당
print("#4", np.identity(5)) # x by y의 matrix를 생성 후 대각 행렬에 1을 할당
