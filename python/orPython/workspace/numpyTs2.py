import numpy as np
test_a = np.array([[1, 2, 3], [4, 5, 6]], float)

a = test_a + test_a
print(a)
a = test_a - test_a
print(a)
a = test_a.transpose()
print("transpose : ", a)
a = test_a * test_a
print(a)
a = test_a.T.dot(test_a)
print(a)
print("*" * 20)
test_matrix = np.array([[1, 2, 3], [4, 5, 6]], float)
scalar = 5
print(test_matrix + scalar)
print(test_matrix - scalar)
print(test_matrix * scalar)
print(test_matrix / scalar)
print(test_matrix // 0.2)
print(test_matrix ** 2)
print(1 // 0.2  )
print(1 / 0.2  )
print("*" * 20)
'''
    - 일반적으로 속도는 아래 순
      for loop < list comprehension < Numpy
    - 100,000,000번의 loop가 돌 때 약 4배 이상의 성능 차이를 보임
    - Numpy는 C로 구현되어 있어, 성능을 확보하는 대신 파이썬의 가장 큰
      특징인 dynamic typing을 포기함
    - 대용량 계산에서는 가장 흔히 사용됨
    - Concatenate처럼 계산이 아닌, 할당에서는 연산 속도가의 이점이 없음
'''

# Numpy comparison operation #1
test_a = np.array([1, 3, 0], float)
test_b = np.array([5, 2, 1], float)
print(test_a > test_b)
print(test_a == test_b)
# Numpy는 배열의 크기가 동일 할 때, element간의 비교의 결과를 boolean type으로
# 반환하여 돌려줌
print("*" * 20)
# Numpy comparison operation #2
a = np.array([1, 3, 0], float)
print(np.logical_and(a > 0, a < 3))
b = np.array([True, False, True], bool)
print(np.logical_not(b))
c = np.array([False, True, False], bool)
print(np.logical_or(b, c))
print(np.where(a > 0, 3, 2))
print("*" * 20)
# Numpy comparison operation #3
a = np.array([1, np.NaN, np.Inf], float)
print(np.isnan(a)) # Not a number인 것을 찾아라
print(np.isfinite(a)) # 한정된 값을 찾아라
print("*" * 20)
# Numpy boolean index
test_array = np.array([1, 4, 0, 2, 3, 8, 9, 7], float)
print(test_array > 3)
print(test_array[test_array > 3])
condition = test_array < 3
print(test_array[condition])
print("*" * 20)
# Numpy fancy index
a = np.array([2, 4, 6, 8], float)
b = np.array([0, 0, 1, 3, 2, 1], int) # 반드시 Integer로 선언
print(a[b]) # bracket index, b배열의 값을 index로 하여 a의 값들을 추출함
print(a.take(b)) # 위와 동일
a = np.array([[1, 4], [9, 16]], float)
b = np.array([0, 0, 1, 1, 0], int)
c = np.array([0, 1, 1, 1, 1], int)
print(a[b, c]) # b를 row index, c를 column index로 변환하여 표시함
print("*" * 20)
# Solve the system of equations 3 * x0 + x1 = 9 and x0 + 2 * x1 = 8
a = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(a, b)
print(x)
print(a.dot(x.T))
