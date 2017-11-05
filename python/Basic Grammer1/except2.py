'''[try~finally 문]
   finally절은 try문 수행 도중에 예외상황이 발생여부 관계없이 항상 수행된다.
'''

try:
	txt = input("입력 >>> ")
except EOFError as e:
	print("읽을 내용이 없습니다.")
else:
	print("당신이 입력한 내용은 {}입니다.".format(txt))
finally:
	print("명령을 수행하였습니다")