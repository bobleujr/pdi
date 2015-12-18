import numpy as np
import cv2
import time

run = False
for it in xrange(1,1000):


	hist = {}

	# for it in xrange(1,999):
	print "Processing image "+str(it)

	img = cv2.imread('/Users/paulotabarro/Downloads/image.orig/'+str(it)+'.jpg',1)

	rows = img.shape[0]
	cols = img.shape[1]


	hist[0] = {}
	hist[1] = {}
	hist[2] = {}
	hist[3] = {}

	#channel 0 - blue
	#channel 1 - green
	#channel 2 - red
	for j in xrange(0, 3):
		hist[0][j] = cv2.calcHist(img[0:rows/2, 0:cols/2, j], [0], None, [256], [0,256])
		hist[1][j] = cv2.calcHist(img[0:rows/2, cols/2:cols, j], [0], None, [256], [0,256])
		hist[2][j] = cv2.calcHist(img[rows/2:rows, 0:cols/2, j], [0], None, [256], [0,256])
		hist[3][j] = cv2.calcHist(img[rows/2:rows, cols/2:cols, j], [0], None, [256], [0,256])


	for imagem in hist:
		for canal in hist[imagem]:
			for histograma in xrange(1,hist[imagem][canal].size):

				# print str(hist[imagem][canal][histograma]+hist[imagem][canal][histograma-1])+" = "+str(hist[imagem][canal][histograma])+" + "+str(hist[imagem][canal][histograma-1])
				hist[imagem][canal][histograma] = hist[imagem][canal][histograma]+hist[imagem][canal][histograma-1]
				
	percentis = {}
	percentis[0] = {}
	percentis[1] = {}
	percentis[2] = {}
	percentis[3] = {}
	contador_multiplo = 1

	for imagem in hist:
		percentis[imagem] = {}
		for canal in hist[imagem]:
			multiplo = int(hist[imagem][canal][-1] / 10)
			percentis[imagem][canal] = {}
			percentis[imagem][canal][0] = 0
			for i in xrange(0, hist[imagem][canal].size):
				if (hist[imagem][canal][i] / multiplo) >= contador_multiplo:
					percentis[imagem][canal][contador_multiplo] = i
					contador_multiplo = contador_multiplo + 1
			for i in xrange(0,len(percentis[imagem][canal])-1):
				percentis[imagem][canal][i] = percentis[imagem][canal][i+1] - percentis[imagem][canal][i]
			# print percentis[imagem][canal]

			contador_multiplo = 1

	if not run:
		target = open('database2.arff', 'w')
		target.truncate()
		target.write("@RELATION cor")
		target.write("\n")

		#attributes

		for i in xrange(1,120):
			target.write("@ATTRIBUTE atr"+str(i)+" NUMERIC")
			target.write("\n")
		target.write("@ATTRIBUTE class {0,1,2,3,4,5,6,7,8,9}")
		target.write("\n")
		target.write("\n")
		target.write("@DATA")
		target.write("\n")

		run = True



	for h in percentis:
		for j in percentis[h]:
			for f in xrange(0,len(percentis[h][j])-1):
				target.write(str(percentis[h][j][f])+",")
	target.write(str(int(it/100)))
	target.write("\n")
	target.write("\n")

	print "Finished image "+str(it)


target.close()

