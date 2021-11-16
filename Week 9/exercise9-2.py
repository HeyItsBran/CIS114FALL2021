#Exercise  9.2
#Write a program that categorizes each mail message by which day
#of the week the commit was done. To do this, look for lines that start with
#"From", then look for the third word and keep a running count of each of the
#days of the week. At the end of the program, print out the contents of your
#dictionary (order does not matter).



days = dict()
fname = input('Enter a file name: ')
if len(fname) < 1 :
    fname = "mbox-short.txt"
fhand = open(fname)

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in days:
            days[words[2]] = 1
        else:
            days[words[2]] += 1

print(days)