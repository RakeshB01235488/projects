import readtr as rt
import readf as rd
import network as nt
import numpy as np
import cnvrt_value as cnv
n=nt.Network([2500,30,30,10])
a,b=rt.readnn(0,62)
res=[]
res_converted=[]
def init(i=0,j=62):
	global n
	global a
	global b
	a,b=rt.readnn(i,j)
	len=j-i
	n=nt.Network([2500,30,30,len])
	print "Training\n"
	n.SGD(a,10,5,3.0,b)

def main(testfile=None):
	global n
	global a
	global b
	if testfile:
		tr=rd.read(testfile)
		ti=np.array(tr)
		tir=[np.reshape(x,(2500,1)) for x in ti]
		res=n.evaluate(tir)
		for i in res:
			res_converted.append(cnv.convert(int(i)))
		print (res_converted)
	else:
		n.SGD(a,20,20,3.0,b)

if __name__=="__main__":
	init()
	main("fed1small.txt")
