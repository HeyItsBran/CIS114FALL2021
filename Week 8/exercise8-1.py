alist = [1,2,3,4]
blist = [1,2,3,4]

def chop(x):
	del x[0]
	del x[-1]
	return None

def middle(x)
	nlist = x[1:]
	del nlist[-1]
	return nlist

clist = chop(alist)
print(clist)

mlist = middle(blist)
print(mlist)