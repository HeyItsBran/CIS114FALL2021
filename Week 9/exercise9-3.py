#Exercise  9.3
#Write a program to read through a mail log, build a histogram
#using a dictionary to count how many messages have come from each email
#address, and print the dictionary.

addresses = dict()
name = input('Enter file name: ')
if len(name) < 1 :
	name = "mbox-short.txt"
fname = open(name)

for line in fname:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in addresses:
            addresses[words[1]] = 1
        else:
            addresses[words[1]] += 1

print(addresses)