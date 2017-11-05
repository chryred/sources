''' [열거형의 정보를 얻는 함수]
	len(seq)					시퀀스형을 받아서 그 길이를 반환한다.
	iter(obj[,sentinel])	객체의 이터레이터(iterator)를 반환한다.
	next(iterator)			이터레이터의 현재요소를 반환하고 포인터를 하나 넘긴다.
	enumerate(iterable, start=0)		이터러블에서 enumerate형을 반환하나.
	sorted(iterable[,key][,reverse])	정렬된 리스트를 반환
	reverse(seq)							역순으로 된 iterator를 반환한다.
	filter(func, iterable)					iterable의 각 요소 중 func()의 반환 값이 참인 것만 묶어서 이터레이터로 반환하는 함수
	map(func, iterable)					iterable의 각 요소를 fun()의 반환 값으로 매핑해서 이터레이터로 반환
	* iterable : 반복가능한 자료형(문자열, 리스트, 튜플, 딕셔너리, 집합)
'''

lists = [1, 2, 3, 4]
iters = iter(lists)

print(next(iters))

print(list(map(lambda x : x * 2, lists)))

li = [lambda x, y: x-y, lambda x,y: x/y]
print(li)
print(li[0](1,2))