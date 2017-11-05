'''	[객체지향 프로그래밍]
	- C++, JAVA, Python
	구조적 프로그래밍과 다르게 큰 문제를 작게 쪼개는 것이 아니라,
	먼저 작은 문제들을 해결할 수 있는 객체를 만든 뒤,
	이 객체들을 조합해서 큰 문제를 해결하는 상향식(Bottom-up)해결을 도입

	이 객체라는 것을 일단 한번 독립성/신뢰성이 높게 만들어 놓기만 하면
	그 이후에 그 객체를 수정 없이 사용할 수 있으므로 개발 기간과 비용이 대폭 줄어 들게 된다.
'''

# 절차(구조적)지향 프로그래밍의 예

showInfo = ""
w_showInfo = ""

def person(name, age):
	global showInfo
	showInfo = "이름: " + name + ". 나이: " + str(age)
	return showInfo

def w_person(name, age):
	global w_showInfo
	w_showInfo = "이름: " + name + ". 나이: " + str(age)

print(person("홍길동", 12))
print(showInfo)

print(w_person("홍길순", 12))
print(w_showInfo)

# 객체지향 프로그래밍 예
class Person:
	def __init__(self):
		self.info = ""

	def showInfo(self, name, age):
		self.info += "이름: " + name + "나이: " + str(age)
		print(self.info)

man = Person()
man.showInfo("홍길동", 23)

woman = Person()
woman.showInfo("홍길순", 22)