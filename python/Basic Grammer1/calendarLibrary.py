'''[calendar(달력) 모듈] : 파이썬에서 달력을 표시해주는 모듈이다.
   calendar.calendar(해당 년도) : 해당 년도의 달력을 출력한다. 
		또는 calendar.prcal도 사용가능
   calendar.prmonth(년도, 월) : 해당 월에 대한 달력만 출력한다.
   calendar.weekday(년도, 월, 일) : 입력 받은 날자의 요일을 반환한다.
   calendar.monthrange(년도, 월) : 입력 받은 달의 1일이 무슨 요일인지 
											   그달의 마지막 일자를 반환해 주는 함수(튜플형태)
'''
import calendar
#print(calendar.calendar(2017))
help(calendar.prcal)
#print(calendar.prcal(2017))
#calendar.prcal(2017)
calendar.prmonth(2017,5)
print()
print(calendar.weekday(2017, 5, 13))
print(calendar.monthrange(2017, 5))