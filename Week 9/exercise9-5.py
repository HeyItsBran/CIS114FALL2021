#Exercise  9.5
#This program records the domain name (instead of the address)
#where the message was sent from instead of who the mail came from (i.e., the
#whole email address). At the end of the program, print out the contents of
#your dictionary.

domains = dict()

name = input('Enter file name: ')
if len(name) < 1 :
	name = "mbox-short.txt"
fname = open(name)

for line in fname:
	words = line.split()
	if len(words) < 2 or words[0] != "From:" :
		continue
	else:
		atsign = words[1].find("@")
		dname = words[1][atsign + 1:]
		if dname not in domains :
			domains[dname] = 1
		else:
			domains[dname] += 1

print(domains)