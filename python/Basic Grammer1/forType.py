''' for문
for문의 기본구조
for 변수 i 리스트, 튜플, 문자열
	<실행할 문장1>
	<실행할 문장2>
'''

list1 = ["a", "b", "c"]

for i in list1:
	print(i)

jumsu = [90, 50, 60, 70, 80]

aa = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for (i, j) in aa:
	print("%s : %s" %(i, j))

# for문과 range함수
# - range함수는 두개의 숫자를 이용하는 함수이다.
# 사용 예) range(1, 5) --> 리스트[1,2,3,4]반환한다.
# 숫자가 두개인 경우는 1씩 증가하는 숫자의 리스트를 반환핟나.
# 숫자가 세개인 경우는 세번째 숫자는 증가
for i in range(2, 10):
	for j in range(1, 10):
		print (i * j, end='\t')
	print('')

for i in range(1,5):
	print(i)
#	break
else: # 반복문에서 else절은 루프를 다 돌고 난 뒤에 항상 수행한다. break문을 사용햇을 경우는 수행되지 않느다.
	print("반복문 종료")

''' c언어에 for문과 파이썬의 for문은 근본적으로 다르다.
	파이썬의 for문은 c#과 foreach루프하고 비슷하고, java의 for(int k : intArray)와 비슷하다.
	c언어에서는 for(int i =0; i < 5; i++)과 같이 파이썬에서 표현을 한다면
	for i in range(0, 5)와 같이 표기할 수 있다.
'''
# [range 함수를 이용해서 구구단 출력하기]

for i in range(2, 10):
	for j in range(1, 10):
		print("%d * %d= %d" %(i, j, i*j), end="\t")
	print('')

# 리스트안에 for문을 이용하여 프로그램 해보기
aa = [1,2,3,4,5,6,7,8,9]

gugudan_2 = []

for i in aa:
	gugudan_2.append(i*2)
print(gugudan_2)

gugudan_2 = [i*2 for i in aa]
print(gugudan_2)

# 5단의 결과값 중에서 짝수만 리스트에 추가하는 예
gugudan_5 = [i*5 for i in aa if i%2 == 0]
print(gugudan_5)

''' 리스트 내포(List comprehension)의 일반적인 구조
1) [표현식 for항목 in 반복 가능한 객체 if조건]
   위에서 if조건은 생략이 가능하다.
2) [표현식 for 항목1 in 반복가능한 객체 if조건1
          for 항목2 in 반복가능한 객체2 if조건2
		  ...
		  for 항목n in 반복가능한 객체n if조건n
'''

# 구구단의 결과를 저장하는 리스트
gugudan = [i*j for i in range(2,10) for j in range(1,10)]
print (gugudan)