score = input("Enter Score: ")
s = float(score)
a = 0.9
b = 0.8
c = 0.7
d = 0.6

if s > 1 :
	print("Error!")
elif s < 0 :
	print("Error!")
elif s >= a :
	print("A")
elif s >= b :
	print("B")
elif s >= c :
	print("C")
elif s >= d :
	print("D")
elif s < d :
	print("F")