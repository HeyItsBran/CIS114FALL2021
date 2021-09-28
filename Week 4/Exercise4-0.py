def big(a, b, c):
	x = max(a, b, c)
	return x


try:
	a = int(input("Enter a number: "))
except ValueError:
	print("Numbers only, please! Start again.")
	exit()
try:
	b = int(input("Enter a second number: "))
except ValueError:
	print("Numbers only, please! Start again.")
	exit()
try:
	c = int(input("Enter a third number: "))
except ValueError:
	print("Numbers only, please! Start again.")
	exit()
big(a, b, c)
x = big(a, b, c)
print("The largest number you entered was",x)