# 예외 발생시키기 : raise명령어를 이용해서 강제로 발생시키는 방법

class Fleight:
	def fly(self):
		raise NotImplementedError # 파이썬의 내장 에러로 구현되지 않았을 때 발생시키는 에러

class Plane(Fleight):
	# pass
	def fly(self):
		print("날아라")

plane = Plane()
plane.fly()