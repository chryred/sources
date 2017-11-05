'''
3) 리스트(list)
: 다른 언어의 배열과 같은 형을 의미한다.
리스트의 예) aa = [10, 20, 30]
		  movie = ["트랜스포머", "국제시장", "명량"]
		  bb = [10, 20, "명량", "국제시장"]
		  cc = [10, 20, ["명량", "국제시장"]]
		  dd = []
       ** 리스트내에는 어떠한 자료형도 포함시킬 수 있다.
[리스트의 인덱싱화 슬라이싱]
'''
aa = [1, 2, 3]
print(aa[0])
print(aa[0] + aa[1])
print(aa[-1]) # 인덱스 값이 -인 경우에는 뒤에서부터 요소를 가리킨다.

bb = [10, 20, 30, ["ab", "cd", "ef"]]
print(bb[0])
print(bb[-1])
print(bb[-1][2])

cc = [10, 20, ['aa', 'bb', 'cc', ["국제시장", "명량"]]] # 삼중 리스트 구조
print(cc[2][3][0])

# [리스트의 슬라이싱]
ab = [1, 10, 100, 1000, 10000]
print(ab[:3])

ab = "11010010001000"
print(ab[:3])

# 리스트 연산 (+, *:반복)
aa = [10, 20, 30]
bb = [100, 200, 300]
cc = aa + bb
cc[0] = 111
print(cc)
print(aa*2)

# 리스트의 값을 변경하기
aa[1] = 100 # 문자열, 튜플은 변경이 안되지만 리스트의 경우는 변경이 가능함.
print(aa)
print(aa[2:])
aa[2:] = ["국제시장", "명량"]
print(aa)
print(aa[1:3])
aa[1:3] = ["백", "천", "만"]
print(aa)
aa[4] = ["십만", "백만", "천만"]
print(aa)

# del aa[4][0]
# print(aa)

aa[1:4] = [] # 요소 삭제 인덱스 1에서 4까지 지우는 방법
print(aa)

del aa[0] # del함수를 이용한 삭제 방법 del(파이썬 내장함수) del객체(모든 자료형)

''' 4) 튜플(tuple) : 리스트와 비슷한 자료형이다.
-  리스트와 튜플의 차이점
 . 리스트는 [], 튜플은 ()를 사용한다.
 . 리스트는 요소의 변경(수정, 삭제, 생성)이 가능하지만, 튜플은 요소의 값을 변경할 수 없다.
 사용 예)
 tu = () --> 빈값이 들어있는 형태
 tu2 = (1,)
 tu3 = (10, 20, 30, 40)
 tu4 = 10, 20, 30
 tu5 = ("국제시장", "명량", ("ab", "cd"))
 튜플의 인덱싱, 슬라이싱, 연산
'''
tu = ()
print(tu)
tu2 = (1,)
print(tu2)

tu5 = ("국제시장", "명량", ("ab", "cd"))
print(tu5[2])
print(tu5[1:2])

tu2 = 'd', 'e', 'f'
print(tu2 + tu2)
print(tu2 * 3)

# del tu2[2]

''' 불린형(참과 거짓)
문자열 : "aaa" --> 참(True), ""거짓(False)
리스트 : [1,22,33] 참, [] 거짓
튜플 : (1, 2, 3) 참, () 거짓
딕셔너리 : {}(거짓)
숫자 : 1(참), 0(거짓)
None (거짓)
'''

if []:
	print("참")
else:
	print("거짓")

if [1, 2]:
	print("참")
else:
	print("거짓")
aa = None
if aa == None:
	print("거짓")