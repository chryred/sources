f = lambda x: x*x

def func(x):
	return x ** 3

args = [1, 2, 3, 4]
ret = map(func, args)
print(list(ret))

f = lambda x, y: x * x + y
x = [1, 2, 3, 4, 5]
y = [10, 9, 8, 7, 6]
ret = map(f, x, y)
print(list(ret))