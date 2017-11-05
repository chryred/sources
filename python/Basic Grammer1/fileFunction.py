''' [파일 입출력]
	.파일 생성
	파일 객체 = open(파일이름, 파일 열기모드)

	----- 파일 열기 모드 ------
	- r모드: 읽기모드(파일을 읽기 용도로 사용할때)
	- w모드: 쓰기모드(파일에 내용을 쓸 때
					-> 파일이 존재하는 경우에는 본래있던 내용이 모두 지워지면서 열린다.
					-> 파일이 존재하지 않는 경우에는 새로운 파일이 생성된다.)
	- a모드: 추가모드(파일에 새로운 내용을 추가할 때)

'''
# fp = open("D:\Lecture\\Python\\Basic Grammer\\test_new.txt")

# fp = open("test_new.txt", "w")

'''
for i in range(1, 5):
	content = "%d 번째 줄...\n" %i
	fp.write(content)
'''

# close()는 생략해도 무방하다. 파이썬에서는 프로그램 종료시 열린 파일 객체들을 자동으로 닫아준다.
# 그렇지만 될수 있으면 직접 닫아주는 것이 올바른 방법이다.
# 쓰기모드로 열었던 파일을 닫지 않고 재상용하는 경우에는 에러가 발생하기 때문에
# 닫아주는 습관을 갖자!!
#fp.close()

'''
for i in range(1, 10):
	content = "%d 번째 줄... " %i
	print(content)
'''
''' 파일을 읽어오는 방법
	파일객체에서 사용할 수 있는 readline() 이용하기
'''
fp = open("test_new.txt", "r")
data = fp.readline() # 읽어온 라인을 리턴한다.
print(data)
fp.close()

fp = open("test_new.txt", "r")

while(True): # 참과 거짓 : True, False
	data = fp.readline() # 더이상 파일에서 읽어올 라인이 없는 경우에는 
	if not data: break
	print(data)

fp.close()
'''
while 1:
	userData = input() # 사용자가 입력한(키보드로 입력한) 데이터를 콘솔에 출력하는 예
	if not userData: break
	print(userData)
'''
'''
	readlines()
'''
fp = open("test_new.txt", "r")
datas = fp.readlines() # 리턴값이 list형태이다.
print(datas)
for data in datas:
	print(data)
fp.close()

# .read()함수를 이용한 파일 읽기
fp = open("test_new.txt", "r")
data = fp.read() # read()함수는 파일 전체를 문자열로 리턴함.
print("=" * 20)
print(data)
fp.close()

'''
fp = open("test_new.txt", "a")
for i in range(5, 8):
	content = "%d번째 라인...\n" %i
	fp.write(content)
fp.close()
'''

# with문을 이용해서 파일 객체 다루기 : with문을 이용하면 파일을	닫을 필요가 없다. 자동으로 파일을 닫아준다.
fp = open("test_2.txt", "w")
fp.write("파일 입출력 테스트 2번째")
fp.close()

with open("test_2.txt", "w") as fp:
	fp.write("with문을 이용하여 파일 입출력 테스트")
