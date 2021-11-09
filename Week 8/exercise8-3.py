fhand = open('mbox-short.txt')
count = 0
for line in fhand:
	line = line.rstrip()
	words = line.split()

	if len(words) < 3 or if words[0] != 'From':
		continue
	print(words[2])