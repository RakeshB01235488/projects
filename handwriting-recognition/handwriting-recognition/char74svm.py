import readtr as rt
from sklearn import svm
import readf as rd
import numpy as np
import cnvrt_value as cnv
clf=svm.SVC()
a,b=rt.read()
res=[]
res_converted=[]
def init(i=0,j=62):
	global clf
	global a
	global b
	clf=svm.SVC()
	a,b=rt.read(i,j)
	clf.fit(a[0],a[1])

def main(testfile=None):
	global clf
	global a
	global b
	if testfile:
		tf=rd.read(testfile)
		ts=np.array(tf)
		res=clf.predict(ts)
		for i in res:
			res_converted.append(cnv.convert(int(i)))
		print (res_converted)
	else:
		pred=[int(a+.1) for a in clf.predict(b[0])]
		nc=sum(int(x==y) for x,y in zip(pred,b[1]))
		print "{0} of {1} correct = {2}%".format(nc,len(b[1]),(100.0*float(nc)/len(b[1])))
		

if __name__=="__main__":
	init()
	main("fed1num.txt")
