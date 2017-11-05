''' 사용자 정의 함수
	def 함수명():
		<실행할 명령1>
		<실행할 명령2>
		...
	인수(매개변수, 파라미터)
'''

def show_list_max(list):
	aa = -1
	for i in list:
		if(aa < i):
			aa = i
		
	return aa

def show_max(a, b):
	if a > b:
		print(a, "는 최대값이다")
	elif a == b:
		print(a, "와", b, "는 같다")
	else:
		print(b, "는 최대값이다.")

print(show_list_max([1,2,10,11]))
show_max(3, 3)

def sum(a, b):
	return a + b

print(sum(11, 12))

def sum(a, b, c):
	return a + b + c

c = sum(10,20,30)
print(c)

''' 일반적인 함수의 구조
	def 함수명(인수,...)
		<실행할 명령
		.....
		return 결과값
	[[ 인수가 없는 함수(입력값이 없는 함수) ]]
'''
def show():
	return "Hello"

print(show())

# 인수도 없고 리턴값도 없는 함수

def show():
	print("안녕하세요")

show()

''' 예상할 수 없는 인수를 갖는 함수
	def 함수명(*인수)
'''

def sum(*a):
	tot = 0
	for i in a:
		tot += i
	return tot

res = sum(10, 20, 30)
print("{0:->10}".format(res))
print("-" * 20)

def calc(aa, *a):
	tot = 0
	if aa == "sum":
		for i in a:
			tot += i
	elif aa == "mul":
		tot = 1
		for i in a:
			tot *= i
	elif aa == "min":
		for i in a:
			tot -= a
	return tot

res = calc("mul", 2, 12)
print(calc("sum", 1,2,3,4,5,6))

# 리턴값의 유형
def return_value(a,b):
	return a+b, a-b

a = return_value(3, 2)
print(a)

# return만 단독으로 사용할 경우에는 함수를 바로 빠져 나간다.
def show(aa):
	if aa == 0:
		return
	print("{0}이 아니다".format(0))
show(1)

# 인수에 초기값을 설정하기 : 초기화 하고자 하는 인수는 마지막에 설정하자.
def show(name, age, gender="M"):
	print("이름은 %s, 나이는 %d" %(name,age))

	if gender == "M":
		print("남자")
	else:
		print("여자")

show("홍길동", 12, "C")

def show(name, gender="M", age):
	print("이름은 %s, 나이는 %d" %(name,age))

	if gender == "M":
		print("남자")
	else:
		print("여자")

show("홍길동", "M" , 12) # default값 때문에 에러 발생