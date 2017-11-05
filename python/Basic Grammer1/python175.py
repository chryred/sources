BUFSIZE = 1024 * 256
merge_filename = "ret.exe"
filelist = ["python-3.5.2.exe_" + str(x) for x in range(10)]

with open(merge_filename, "wb") as h:
	for file in filelist:
		print("[%s] 파일 합치는 중..." %file)
		with open(file, "rb") as f:
			buf = f.read(BUFSIZE)
			while buf:
				h.write(buf)
				buf = f.read(BUFSIZE)

print("파일 합치기가 완료되었습니다.")