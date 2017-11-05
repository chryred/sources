''' 딕셔너리
	리스트와 비슷하지만 좀 더 일반적입니다. 리스트에서, 지수는 정수만 가능합니다. 
	딕셔너리에서는 (거의) 모든 형이 가능합니다.
	딕셔너리를 지수(키(key)라고 불립니다.)와 값 간의 사상을 볼 수 있습니다. 각 키
	는 값과 대응합니다. 키와 값을 결합을 키-값(key-value pair)이나 때로 항목(item)
	이라고 부릅니다.

	다음은 기본적인 딕셔너리의 모습이다.
	{key1:value1, key2:value2, key3:value3....}
	즉, key와 value쌍들이 여러개가 '{'과 '}'으로 둘러싸이고 각각의 요소는 key value
	형태로 이루어져 있고 쉼표(',')로 구분되어져 있음을 볼 수 있다.

	다음의 딕셔너리 예를 보도록 하자
	>>> dic = {'name':'홍길동', 'phone':'01011111111', 'birth':'118'}

	위에서 key는 각각 'name'... key이고 '홍길동'... 이 value가 된다.
'''
a = {1:"Hello!!"}
print(a)
a = {'first':['a', 'b', 'c']}
print(a)
print(a['first'][0])

sports = {"축구":"박지성", "야구":"강정호", "체조":"손연제"}
print(sports["축구"])

aa = {1:"안녕"}
aa[2] = "하이"
aa["key"] = "이렇게도 되나?"
aa["age"] = 123

del aa["age"]
# del aa[0] key값이 없을 경우 에러발생
aa[(2,3)] = "1111"
print(aa)

'''
	딕셔너리 주의사항
	1. key값(지수)은 고유한 값이므로 중복되는 값을 설정해 놓으면 안된다.
	   만약 중복이 된다면 하나만 적용되고 나머지는 제외된다.
	2. 키값으로 리스트는 쓸 수 없다. 튜플은 키 값으로 사용 가능하다.
	    키값은값이 변할 없다는 전제하에 타입을 설정하면 된다.
	dict() 함수
'''

aa = dict() # 항목(key:value)이 없는 딕셔너리를 만든다.
print(aa)

aa["one"] = "첫번째"
print(aa)

# key 리스트를 만드는 함수
bb = {"name":"홍길동", "hp":"010-2222-2223", "age":24}
print(bb.keys())

for key in bb.keys():
	print("key : {0}, value : {1}".format(key, bb[key]), end="\t")
print()
# valueList를 만드는 함수 (values())
print(bb.values()) # 리턴값은 dic_values객체이다.

# key와 value 한쌍(항목)을 얻기(items())
print(bb.items()) # 리턴값은 dic_items객체이다. 이 객체의 요소는 튜플형태이다.
cc = bb.items()
for key, value in bb.items():
	print(key, ":", value)

# key:value쌍을 모두 삭제하기 (clear())
# bb.clear()
print(bb)

# key값을 이용해서 value를 얻어오기 (get)
# get()함수는 키값이 존재하지 않을 경우에는 None값을 리턴한다.
print(bb.get("age"))
print(bb.get("1")) # 오류 미발생 리턴값 None
print(bb["age"])
# print(bb["1"]) 오류 발생

# 딕셔너리내에 키값이 없을 경우 디폴트 값을 주는 방법
gender = bb.get("gender", "디폴트 값")
print(gender)

# 딕셔너리내에 해당 키값이 존재하는지 알아보기
confirm_bb = 'gender' in bb
print(confirm_bb)
confirm_bb = 'age' in bb
print(confirm_bb)

# pop()함수를 이용해서 value값을 가져오기 : 딕셔너리 항목을 제거한다.
m = bb.pop("name")
# m = bb.pop() # key값을 설정해야 함.
print(m)
print(bb)

bb["name"] = "홍길동"
print(bb)

m = bb.pop("gender", None) # 디폴트 값을 표시하면 에러 발생하지 않음.
print(m)

lens = len(bb)
print(lens) # 딕셔너리의 항목 개수를 구함.

