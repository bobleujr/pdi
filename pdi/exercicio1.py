import numpy as np
import cv2


run = False
lbp_array = {}
slices = {}
hist = {}


    #LOOP STARTS


for it in xrange(1,1000):
	print "Processing image "+str(it)

	img = cv2.imread('/Users/paulotabarro/Downloads/image.orig/'+str(it)+'.jpg',0)

	rows = img.shape[0]
	cols = img.shape[1]

	slices[0] = img[0:rows/2, 0:cols/2]
	slices[1] = img[0:rows/2, cols/2:cols]
	slices[2] = img[rows/2:rows, 0:cols/2]
	slices[3] = img[rows/2:rows, cols/2:cols]

	# cv2.imshow('image1',slices[0])
	# cv2.imshow('image2',slices[1])
	# cv2.imshow('image3',slices[2])
	# cv2.imshow('image4',slices[3])

	#
	# lbp_array[0] = img[0:rows/2,0:cols/2]
	# lbp_array[1] = img[0:rows/2,0:cols/2]
	# lbp_array[2] = img[0:rows/2,0:cols/2]
	# lbp_array[3] = img[0:rows/2,0:cols/2]
	lbp_array[0] = np.zeros((rows/2,cols/2), dtype=np.int)
	lbp_array[1] = np.zeros((rows/2,cols/2), dtype=np.int)
	lbp_array[2] = np.zeros((rows/2,cols/2), dtype=np.int)
	lbp_array[3] = np.zeros((rows/2,cols/2), dtype=np.int)


	for slic in slices:
		for i in xrange(1, slices[slic].shape[0]-2):
			for j in xrange(1, slices[slic].shape[1]-2):
				lbp_array_temporary = ""
				lbp_array_temporary += '0' if slices[slic][i,j] >= slices[slic][i-1,j-1] else '1'
				lbp_array_temporary += '0' if slices[slic][i,j] >= slices[slic][i,j-1] else '1'
				lbp_array_temporary += '0' if slices[slic][i,j] >= slices[slic][i+1,j-1] else '1'
				lbp_array_temporary += '0' if slices[slic][i,j] >= slices[slic][i+1,j] else '1'
				lbp_array_temporary += '0' if slices[slic][i,j] >= slices[slic][i+1,j+1] else '1'
				lbp_array_temporary += '0' if slices[slic][i,j] >= slices[slic][i,j+1] else '1'
				lbp_array_temporary += '0' if slices[slic][i,j] >= slices[slic][i-1,j+1] else '1'
				lbp_array_temporary += '0' if slices[slic][i,j] >= slices[slic][i-1,j] else '1'

				lbp_array[slic][i,j] = int(lbp_array_temporary,2)
		# print lbp_array[slic]

	for i in lbp_array:
		# hist[i] = cv2.calcHist([lbp_array[i]], [0], None, [256], [0,256])
		hist[i] = np.histogram(lbp_array[i].ravel(),256,[0,256])[0]

	
	# soma = 0
	# for i in xrange(0,256):
	# 	soma += hist[i]	

	# DOESNT NEED TO RUN TWICE

	if not run:
		target = open('database.arff', 'a')
		target.truncate()
		target.write("@RELATION textura")
		target.write("\n")

		#attributes

		for i in xrange(1,1025):
			target.write("@ATTRIBUTE atr"+str(i)+" NUMERIC")
			target.write("\n")
		target.write("@ATTRIBUTE class {0,1,2,3,4,5,6,7,8,9}")
		target.write("\n")
		target.write("\n")
		target.write("@DATA")
		target.write("\n")

		run = True



	for h in hist:
		for j in hist[h]:
			target.write(str(int(j))+",")
	target.write(str(int(it/100)))
	target.write("\n")
	target.write("\n")

	print "Finished image "+str(it)


target.close()
