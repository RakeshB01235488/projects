import numpy as np
def read(name):
	f=open(name,"r")
	a=[]
	i=-1
	for lin in f:
		a.append(lin.strip().split(" "))
	b=[]
	for i in xrange(len(a)):
		b.append([])
		for j in xrange(len(a[i])):
			b[i].append(float(a[i][j])/255.0)
	f.close()
	return(b)
def read1(name):
	f=open(name,"r")
	a=[]
	for lin in f:
		a.append(lin.strip().split(" "))
	b=[]
	for i in xrange(len(a)):
		b.append([])
		for j in xrange(len(a[i])):
			b[i].append(float(a[i][j])/255.0)
	nb=[np.reshape(x, (len(b[i]), 1)) for x in b]
	f.close()
	return(nb)
def read2(name):
	f=open(name,"r")
	a=[]
	for lin in f:
		a.append(lin.strip().split(" "))
	b=[]
	for i in xrange(len(a)):
		b.append([])
		for j in xrange(len(a[i])):
			b[i].append(float(a[i][j]))
	f.close()
	return(b)
