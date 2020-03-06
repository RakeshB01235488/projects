import mnist_loader as ml
from sklearn import svm
import readf as rd
import numpy as np

clf=svm.SVC()
a,b,c=ml.load_data()
clf.fit(a[0],a[1])

def main(testfile=None):
	if testfile:
		tf=rd.read(testfile)
		ts=np.array(tf)
		return(clf.predict(ts))
	else:
		pred=[int(a) for a in clf.predict(c[0])]
		nc=sum(int(x==y) for x,y in zip(pred,c[1]))
		print "{0} of {1} correct = {2}%".format(nc,len(c[1]),(100.0*float(nc)/len(c[1])))
		

if __name__=="__main__":
	main("fe1.txt")
