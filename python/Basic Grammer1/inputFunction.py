''' [사용자 입력]
	input() 함수를 이용하여 사용자로 부터 다양한 입력을 받을 수 있다.
	aa = input() : 사용자로 부터 입력받은 내용을 aa에 할당한다.

	사용자 프롬프트 만들기 : input("숫자를 입력하세요 >>>")
	input(문자열 type)

	[출력(print)]
	print함수는 모든 자료형을 출력해 주는 함수
'''

# aa = input()
# print(aa)

# aa = input("숫자를 입력하세요 >>> ")

print("안녕하세요!!!" "반갑습니다")
print("안녕하세요!!!" + "반갑습니다.")
print("안녕하세요!!!", "반갑습니다.") # 콤마(,)를 사용하면 문자열간의 띄어쓰기가 된다.

for i in range(5): # for i in range(0, 5): 동일 range의 인수가 한개인 경우 0이 생략됨
	print(i, end='') # end파라미터는 마지막 문자를 지정하는 인수이다.



