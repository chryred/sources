class MyClass:
	var = "안녕하세요"
	def sayHello(self):
		print(self.var)

if __name__ == "__main__":
	obj = MyClass()
#	MyClass.var = "바보"
	obj.sayHello()
	print(obj.var)
	print(MyClass.var)
