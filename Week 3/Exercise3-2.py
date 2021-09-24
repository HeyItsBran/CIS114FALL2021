hrs = input("Enter Hours:")
wage = input("Enter Rate:")
try:
	w = float(wage)
	h = float(hrs)
except:
	print("Error! Use '.' and numbers only!")
	quit()
otWage = float(w * 1.5)
otHrs = float(h - 40)
pay = h * w
if h > 40:
	pay = w * 40 + otHrs * otWage
print(pay)