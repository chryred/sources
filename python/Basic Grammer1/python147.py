import os

target_file = "test_2_copy.txt"
k = input("[%s]파일을 삭제하겠습니까? (y/n)" %target_file)
if k == "y":
	os.remove(target_file)
	print("[%s]를 삭제하였습니다." %target_file)
