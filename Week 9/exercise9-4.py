name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
fname = open(name)
emails = dict()
emailstotal = None
emailaddress = None

for line in fname:
    if not line.startswith("From:"):
        continue
    line = line.split()
    line = line[1]
    emails[line] = emails.get(line, 0) + 1

for word,count in emails.items():
    if emailstotal == None or count > emailstotal:
        emailstotal = count
        emailaddress = word

print(emailaddress, emailstotal)
