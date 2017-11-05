''' [ 클래스와 객체]
	클래스는 객체의 틀이 되는 추상적인 개념이고, 객체는 클래스에 정의된 
	요소들의 실체입니다.

	붕어빵틀 = 클래스
	붕어빵 = 객체

	class Sample:
		pass

	위 클래스는 아무런 기능도 없는 클래스이다.
	껍질 뿐인 클래스도 인스턴스(instance)라는 것을 생성하는 기능을 갖는다.
	(클래스에 의해서 생성된 객체를 인스턴스라고 부른다.)
	인스턴스는 클래스에 의해서 만들어진 객체로 한개의 클래스는 무수히 많은 인스턴스를
	만들어 낼 수가 있다.
	Sample클래스의 인스턴스를 만드는 방법
		a = Sample()
	Sample()의 결과값을 돌려 받은 a가 인스턴스 마치 함수를 사용해서 그 결과값을 
	돌려 받는 모습과 비슷하다.

	[객체와 인스턴스의 차이]
	클래스에 의해서 만들어진 객체를 인스턴스라고도 한다.
	그렇다면 객체와 인스턴스의 차이는 무엇일까? 이렇게 생각해 보자.
	cat = Animal()이렇게 만들어진 cat은 객체이다. 그리고 cat이라는 객체는
	Animal의 인스턴스(instance)이다. 즉, 인스턴스라는 말은 특정 객체(cat)가
	어떤 클래스(Animal)의 객체인지를 관계위주로 설명할 때 사용된다. 즉, "cat은
	인스턴스" 보다는 "cat은 객체"표현이 "cat은 Animal의 객체"보다는 "cat은 
	Animal의 인스턴스"라는 표현이 훨씬 잘 어울린다.

	[클래스 기초]
	클래스 선언
'''
class Test: # 클래스명의 첫글자는 대문자로 사용한다. 붕어빵틀과 같다.
	str = "클래스 개념 잡기" # str은 Test클래스의 요소(attribute, field) 또는 Test클래스의 멤버라고도 한다.

test1 = Test() # test1객체는 Test클래스에 의해서 만들어진 인스턴스, test1은 Test클래스의 인스턴스
					# test1은 붕어빵과 같다.
print(test1.str)

'''  [클래스의 구성]
	class 클래스명:
		변수	# 클래스에 소속된 변수들을 필드(field)라고 부른다.

		함수 # 클래스(객체)내에 어떤 기능을 갖을 수 있도록 하는 함수
			   # 이러한 함수들을 클래스의 메소드(method)라고 한다.
결론적으로 클래스는 필드의 메소드로 구성된다.
변수나 함수와는 다르게 구별지어서 부르는 것은 클래스나 객체에
소속되어 있는 대상이라는 것을 나타내기 위함이다.

필드와 메소드들을 통틀어 클래스의 속성(attribute)라고 한다.

클래스내의 메소드와 일반 함수와의 차이점은 바로 'self'이다.

메소드의 경우 매개 변수의 목록에 항상 추가로 한개의 변수(self)를 맨앞에 추가해야 한다.
꼭 self를 사용해야 하는 것은 아니지만, 일반적으로 self를 사용한다.
(self를 표준으로 사용하고 있다.)

메소드를 호출 할 때 이 변수에는 직접 우리가 값을 넘겨 주지 않는다.
파이썬이 자동으로 self에 값을 할당한다.

self는 C++에서의 this포인터와 같은 것, java나 c#에서는 this와 같다.

'''
class Person:
	def say(self):
		print("Hello, Good Friend")

p1 = Person() # 객체화 환다. 즉 메모리에 인스턴스화한다.
p1.say()

print(p1)