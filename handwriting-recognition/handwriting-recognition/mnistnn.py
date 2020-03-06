import mnist_loader as ml
import readf as rd
import network as nt
import numpy as np

n=nt.Network([784,30,10])
a,b,c=ml.load_data_wrapper()
print "Training\n"
n.SGD(a,20,20,3.0,c)

def main(testfile=None):
	if testfile:
		tr=rd.read(testfile)
		ti=np.array(tr)
		tir=[np.reshape(x,(784,1)) for x in ti]
		return(n.evaluate(tir))
	else:
		n.SGD(a,20,20,3,0,c)

if __name__=="__main__":
	main()
