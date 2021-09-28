def computePay(hours, rate) :
	if hours > 40:
		pay = hours * rate
		otPay = (hours - 40) * (rate * 0.5)
		gross = pay + otPay
	else:
		gross = hours * rate
	return gross

hrs = input("Enter Hours:")
wage = input("Enter Rate:")
w = float(wage)
h = float(hrs)
computePay(h, w)
gross = computePay(h, w)
print("Pay:",gross)