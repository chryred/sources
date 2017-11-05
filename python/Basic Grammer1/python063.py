a = 1113
b = 23

ret1 = divmod(a, b)
print(ret1)


h1 = hex(97)
h2 = hex(98)
ret1 = h1 + h2
print(ret1)

a = int(h1, 16)
b = int(h2, 16)
c = int(133)

ret2 = a + b
print(ret2)
print(hex(ret2))