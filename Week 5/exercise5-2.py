maximum = None
minimum = None
number = None

while True:
    try:
        number = input("Enter a number: ")
        if number == "done":
            break
        number = int(number)
        if maximum is None or maximum < number:
            maximum = number
        elif minimum is None or minimum > number:
             minimum = number
    except ValueError:
        print("Invalid input")
 
print ("Maximum is", maximum)
print ("Minimum is", minimum)