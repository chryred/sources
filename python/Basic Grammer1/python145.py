spos = 105 # 파일을 읽는 위치 지정
size = 500

f = open("test_2.txt", "r")
h = open("test_2_copy.txt", "w")

f.seek(spos)
data = f.read(size)
h.write(data)

f.close()
h.close()