fname = input("Enter file name: ")
fh = open(fname)
total = 0.0
count = 0

for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") :
                continue
        else:
                total = total + float(line[20:])
                count = count + 1

print("Average spam confidence:", total/count)