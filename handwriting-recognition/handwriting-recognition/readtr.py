import numpy as np
import random

s=0.98

def read(st=0,en=62):
	f=open("fetr1.txt","r")
	a=[]
	for lin in f:
		a.append(lin.strip().split(" "))
	b=[]
	c=[]
	for i in xrange(st*55,en*55):
		b.append([])
		for j in xrange(1,len(a[i])):
			b[i-st*55].append(float(a[i][j])/255.0)
		c.append(int(float(a[i][0]))-st)
	d=np.array(b,dtype=np.float32)
	e=np.array(c,dtype=int)
	fir=[]
	firl=[]
	fit=[]
	fitl=[]
	for i in xrange(len(e)):
		if(random.random()<s):
			fir.append(d[i])
			firl.append(e[i])
		else:
			fit.append(d[i])
			fitl.append(e[i])
	fi=[fir,firl]
	ti=[fit,fitl]
	f.close()
	return(fi,ti)
def readnn(st=0,en=62):
	a,b=read(st,en)
	ti=[np.reshape(x, (len(a[0][0]), 1)) for x in a[0]]
	tr=[vectorized_result(y,(en-st)) for y in a[1]]
	te=[np.reshape(x, (len(a[0][0]), 1)) for x in b[0]]
	trd= zip(ti,tr)
	tsd= zip(te,b[1])
	return(trd,tsd)
def vectorized_result(j,i):
	e = np.zeros((i, 1))
	e[j] = 1.0
	return e
def read2(st=0,en=62):
	f=open("fetr1.txt","r")
	a=[]
	for lin in f:
		a.append(lin.strip().split(" "))
	b=[]
	print type(st)
	for i in xrange(st*55,en*55):
		b.append([])
		for j in xrange(len(a[i])):
			b[i-st*55].append(float(a[i][j]))
	tr=[]
	ts=[]
	for i in xrange(len(b)):
		if(random.random()<s):
			tr.append(b[i])
		else:
			ts.append(b[i])
	f.close()
	return(tr,ts)