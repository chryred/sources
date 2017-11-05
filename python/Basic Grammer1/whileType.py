''' while문
 ** while문의 구조
 while<조건문>:
	 <실행할 명령문1>
	 <실행할 명령문2>
	 <실행할 명령문3>
'''
aa = 0
while aa < 10:
	aa = aa + 1
	print ("aa 값은 %d입니다" %aa)

	if aa == 9:
		print("종료합니다")
		break
# 무한 루프
bb = 0
while 1:
	bb += 1
	print("무한반복 됩니다")

	if bb > 10:
		break

# 1에서 부터 10까지의 정수 중 홀수를 출력하는 코드
i = 0
while i < 10:
	i += 1
	if i % 2 == 0: continue # continue문은 while문의 맨처음(i<10)으로 돌아가게 하는 명령어
	print(i)