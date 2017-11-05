u_txt = "I love python"
b_txt = u_txt.encode()

print(u_txt)
print(b_txt)

print(u_txt[0] == "I")
print(b_txt[0] == ord("I"))
print(chr(b_txt[0]))

u_txt = b_txt.decode()
print(u_txt)