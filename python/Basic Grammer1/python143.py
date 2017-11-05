bufsize = 1024
f = open("투표포스터.jpg", "rb")
h = open("투표포스터_copy.jpg", "wb")

data = f.read(bufsize)

while data:
	h.write(data)
	data = f.read(bufsize)

f.close()
h.close()