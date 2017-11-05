txt1 = "A"
txt2 = "안녕"
txt3 = "warcraft Three"
txt4 = "3PO"

print(txt1.isalpha())
print(txt2.isalpha())
print(txt3.isalpha())
print(txt4.isalpha())

txt1 = "010-222-2222"
txt2 = "R2D2"
txt3 = "1232"

print(txt1.isdigit())
print(txt2.isdigit())
print(txt3.isdigit())

print(txt1.isalnum())
print(txt2.isalnum())
print(txt3.isalnum())

txt = "A lot of Things occur each day"
ret1 = txt.upper()
ret2 = txt.lower()
print(ret1)
print(ret2)

txt = " 양쪽에 공백이 있는 문자열 입니다. "
print("<" + txt.lstrip() + ">")
print("<" + txt.rstrip() + ">")
print("<" + txt.strip() + ">")