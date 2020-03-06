import mnist_loader as ml
import knn
import readf as rd
import numpy as np

a,b,c=ml.load_data()
train=[]
for i in xrange(5000):
	train.append([])
	train[i].append(a[1][i])
	for j in xrange(784):
		train[i].append(a[0][i][j])
tests=[]
for i in xrange(1000):
	tests.append([])
	tests[i].append(c[1][i])
	for j in xrange(784):
		tests[i].append(c[0][i][j])

def main(testfile=None):
	if testfile:
		a=rd.read(testfile)
		k=3
		predictions=[]
		for x in range(len(a)):
			neighbors = knn.getNeighbors(train, a[x], k)
			result = knn.getResponse(neighbors)
			predictions.append(result)
			print predictions
		return(predictions)
	else:
		knn.main(train,tests)

if __name__=="__main__":
	main("fed1small.txt")