number = 0
total = 0.0

while True :
	xvalue = input('Enter number: ')
	if xvalue == 'done' :
		break	
	try:
		fvalue = float(xvalue)
	except:
		print('Invalid input')
		continue
		
	number = number + 1
	total = total + fvalue

print(total,number,total/number)