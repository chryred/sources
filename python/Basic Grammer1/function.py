''' 함수(function) : 재사용 가능한 프로그램, 명령 덩어리
	우리가 접했던 함수 range(1,5)함수는 이미 만들어져 있는(내장되어 있는)
	내장함수였다. 앞ㅍ에서 우리는 range()함수를 호출해서 사용했다.

	함수는 프로그램을 작성할 때 필요한 중요한 단위이다.

	함수에는 내장함수, 사용자 정의 함수가 있다.

	[[문자열 함수]]
	문자열 포멧팅 함수 format()
'''
# {n}는 자리 표시자를 의미한다. 여기서 n은 숫자를 말한다. format()에 지정된 위치(인덱스)를 표시한다.
aa = "you've {0} a friend".format("got")
print(aa)

str = "{2} {0} {1}".format("a", 100, 200)
print(str)

number = 100
day = "sunday"

print("오늘은 우리가 사귄지 {0}째 되는날!! 요일은 {1}!!".format(number, day))

# 인덱스와 이름을 혼용해서 사용하기
print("오늘은 우리가 사귄지 {0}일째 되는날!! 요일은{day}".format(300,day=	"sunday"))

# 좌측 정렬
name = "김말똥"
print("{0:<10}".format(name))
# 우측 정렬
print("{0:>10}".format(name))
# 가운데 정렬
print("{0:^10}".format(name))
print("{0:-^20}".format(name))

# 소문자를 대문자로 바꾸는 함수
aa = "hello"
aa1 = aa.upper()
print(aa)
# 대문자를 소문자로 바꾸는 함수
print(aa1.lower())

# 문자갯수를 리턴하는 함수
aa = "abcde"
cnt = aa.count("e")
print(cnt)

# 문자열의 길이 구하는 함수
cnt = len(aa) # len(문자열)
print(cnt)

# 문자 위치 찾기 함수 : 문자열에서 찾고자하는 문자의 첫번째 위치를 리턴하는 함수
bb = "cefdegfff"
loc = bb.find("h") # 찾고자 하는 문자가 없는 경우에는 -1을 반환한다.
print(loc)

#loc = bb.index("h") # 찾고자 하는 문자가 없을 경우는 에러를 발생한다.
print(loc)

# 공백지우기 함수(lstrip, strip, rstrip)
aa = "   good   "
print(aa.lstrip() + " morning")
print(aa.rstrip() + " morning")
print(aa.strip() + " morning")

# 문자열 대체 함수(replace) : 문자열 내에 함수(replace
aa = "good morning Jane!!"
bb = aa.replace("morning", "night") # 바꿀 대상(문자열), 바꿀 문자열
print(bb)

# 문자열 나누기(split)
str = "good morning Jane"
str_split = "김말똥,서울/38"
print(str.split("/"))