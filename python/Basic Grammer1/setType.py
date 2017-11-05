'''
	# -*- coding:utf-8 -*-
	# -*- coding:euc-kr -*-
	집합(Sets) : 버전 2.3부터 지원되기 시작함
	집합에 관련된 것들을 쉽게 처리하기 위한 자료형 "set" 키워드를 이용하여	 만들 수 있다.

	ss = set(['a', 'b', 'c'])

'''
ss = set(['a', 'b', 'c'])
print(ss)

ss = set([1, 2, 3])
print(ss)

ss = set("Goodd Morning")
print(ss)

'''
# 집합의 특징 : 1. 중복을 허용하지 않는다. 중복을 제거하기 위한 필터로 활용되기도 한다.
					 2. 순서가 없다. unordered
   리스트 튜플은 순서가 있다. 따라서, 인덱싱을 이용하여 값을 얻어올 수 있다.
   집합은 순서가 없기 때문에 인덱싱으로 값을 얻어올 수 없다. 딕셔너리 역시 순서가 없는 자료형이다.
   집합과 딕셔너리는 인덱싱을 지원하지 않는다.
   집합에 지정된 값을 인덱싱으로 접근하기 위해서는 리스트나 튜플로 변환해야 한다.
'''
ss1 = set([1,2,3])
li = list(ss1)
li.sort()
print(li)

# 교집합, 합집합, 차집합을 이용하자
s1 = set([1,2,3,4,5,6,7])
s2 = set([3,5,6,8,9])
# 교집합은 '&'기호를 이용하여 구한다. 또는 intersection함수를 이용한다.
print(s1 & s2)  
print(s1.intersection(s2))
# 합집합은 '|'기호를 이용한다. 또는 union함수를 이용한다.
print(s1 | s2)
print(s1.union(s2))
# 차집합은 '-'기호을 이용한다. 또는 difference함수를 이용한다.
print(s1 - s2)
print(s1.difference(s2))

# 집합에 값을 추가하기
s1 = set([1,2,3])
s1.add(100) # 하나의 값을 추가할때 사용
print(s1)

s1.update([10,100,1000])
print(s1)

# 집합에서 값을 삭제하기
s1 = set([1,2,3,4,5])
s1.remove(1)  # 값이 미존재시 에러 발생
print(s1)
print(3 in s1)

# 대칭 차집합(^) : 두개의 집합이 있을 때 둘 중 한 집합에만 있는 요소(항목)들
s = set("Good Morning")
t = set("Good Night")
print(s ^ t)

s.remove("g")
# s.remove("s")
print(s.discard("h"))  # 집합에서 항목을 제거하는 함수. 집합내에 없는 항목을 제거 할 때는 에러를 미발생
lens = len(s)
print(lens)
# 집합에서 모든 항목을 제거
s.clear()
print(s)