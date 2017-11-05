'''
# time 모듈 : 시간과 관련된 것들(유용한 시간 함수들을 많이 가지고 있다.)

   time.time() : 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초단위로 돌려주는 함수
					  UTC(Universal Time Coordinated 세계 협정 표준시)를 이용해서 실수 형태로 반환한다.
   time.localtime() : time.time()를 통해서 얻어온 실수값을 이용해서 년도 월 일 시 분 초형태로 표시된다.
   struct_time 객체 속성
		tm_year : 년도
		tm_mon : 월(1~12)
		tm_mday : 일
		tm_hour : 시간(0~23)
		tm_min : 분
		tm_sec : 초
		tm_wday : 요일을 숫자로 표현(월요일 : 0 ~ 일요일 : 6)
		tm_yday : 1월 1일부터 누적된 날짜를 나타냄(1~366)
		tm_isdst : 서머타임(일광절약 시간제 0,1,-1)
	
	time.gmtime() : UTC기준의 현재 시간
	time.asctime() : 알아보기 쉬운 날짜와 시간을 반환해 주는 함수
	time.ctime() : time.asctime을 더 간단하게 표현해 주는 함수
	time.strftime() : 시간을 나타내는 포맷을 지정해서 세밀하게 표현할 수 있는 함수
		형식지정자(포맷코드)
		%y : 년도 축약, %Y : 2015
		%a : 요일 축약(Sun, Sat, Mon...), %A(Sunday, Saturday,...)
		%b : 월 축약(Jan), %B(January)
		%c : 날짜와 시간을 출력(15/01/01 13:21:10)
		%d : 날(day) --> 01 ~ 31
		%H : 시간을 24시간 형태로 출력 --> 0~23
		%I : 시간을 12시간 단위로 표현 --> 01~`12
		%j : 누적날짜 표현 --> 001 ~ 366
		%m : 달 --> 1~12
		%M : 분 --> 01~59
		%p : 오전/오후 --> AM, PM
		%S : 초 --> 00~60
		%U : 누적주 --> 일요일 시작 00~53주
		%w : 요일 --> 0~6
		%W : 
		%x :  날짜 출력 --> 15/01/01
		%X : 시간 출력 --> 13:12:34
		%Z : 시간대 출력 --> 대한민국 표준시

	time.sleep : 루프문 안에서 많이 사용된다. 일정한 시간 간격을 주기 위해 사용하는 함수이다.
'''

import time
print(time.time())
print(time.localtime()[0], time.localtime().tm_year)
print(time.gmtime())
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime("%y %Y%m%d %H%m%S/%c", time.localtime()))
print(time.strftime("%x", time.localtime()))
print(time.strftime("%c", time.localtime(time.time())))

help(time.sleep)