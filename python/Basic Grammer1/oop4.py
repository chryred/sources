# 클래스 변수와 객체변수의 예

class Man:
	# 클래스 변수
	cnt = 0
	def __init__(self, name):
		# 데이터 초기화 하기 
		self.name = name # self.name에서 name은 객체변수를 의미한다.
		print("초기화 중...{}".format(self.name))

		Man.cnt += 1 # 클래스 변수 접근하기 : 클래스명.클래스변수명
	
	def die(self):
		# Man객체가 소멸할 때
		print("객체가 소멸하였습니다. {0}".format(self.name))
		Man.cnt -= 1

		if Man.cnt == 0:
			print("{}는 최후의 생존자였다".format(self.name))
		else:
			print("아직 {:d}명의 생존자가 남아있다.".format(Man.cnt))
		
	def say(self):
		print("Hello, {0}".format(self.name))

	@classmethod # 장식자(decorator) : how_many = classmethod(how_many)의 다른표현
	def how_many(how):
		# 현재의 객체 수량을 체크한다
		print("현재 {}명이 남았습니다.".format(Man.cnt))

gameActor1 = Man("홍길동")
gameActor1 = Man("홍길동1")
gameActor1.say()
gameActor1.die()
Man.how_many()