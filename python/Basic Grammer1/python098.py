strings = "I love Java, Python, C, Javascript"
ret1 = sorted(strings)
ret2 = sorted(strings, reverse=True)

# ret1.reverse()
print(ret1)
ret1 = "".join(ret1)
ret2 = "".join(ret2)

print(ret1)
print(ret2)