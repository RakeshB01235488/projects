import knn
import readtr as rt
import readf as rd
import cnvrt_value as cnv

def main(i=0,j=62,testfile=None):
	tr,ts=rt.read2(i,j)
	k=3
	if testfile:
		tst=rd.read2(testfile)
		predictions=[]
		for x in range(len(tst)):
			neighbors = knn.getNeighbors(tr, tst[x], k)
			result = knn.getResponse(neighbors)
			predictions.append(cnv.convert(int(result)))
			print predictions
		return(predictions)
	else:
		knn.main(tr,ts)


if __name__=="__main__":
	main(0,62,"fed1small.txt")
