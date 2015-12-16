import numpy as np
import cv2


run = False
lbp_array = {}
slices = {}
hist = {}


    #LOOP STARTS


for it in xrange(1,999):
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

	
	lbp_array[0] = img[0:rows/2, 0:cols/2]
	lbp_array[1] = img[0:rows/2, 0:cols/2]
	lbp_array[2] = img[0:rows/2, 0:cols/2]
	lbp_array[3] = img[0:rows/2, 0:cols/2]


	for slic in slices:
		for i in xrange(1, slices[slic].shape[0]-2):
			for j in xrange(1, slices[slic].shape[1]-2):
				lbp_array_temporary = ""
				lbp_array_temporary += '0' if slices[slic][i][j] >= slices[slic][i-1][j-1] else '1'
				lbp_array_temporary += '0' if slices[slic][i][j] >= slices[slic][i][j-1] else '1'
				lbp_array_temporary += '0' if slices[slic][i][j] >= slices[slic][i+1][j-1] else '1'
				lbp_array_temporary += '0' if slices[slic][i][j] >= slices[slic][i+1][j] else '1'
				lbp_array_temporary += '0' if slices[slic][i][j] >= slices[slic][i+1][j+1] else '1'
				lbp_array_temporary += '0' if slices[slic][i][j] >= slices[slic][i][j+1] else '1'
				lbp_array_temporary += '0' if slices[slic][i][j] >= slices[slic][i-1][j+1] else '1'
				lbp_array_temporary += '0' if slices[slic][i][j] >= slices[slic][i-1][j] else '1'
				
				lbp_array[slic][i,j] = int(lbp_array_temporary,2)
	print "1"
	for i in lbp_array:
		hist[i] = cv2.calcHist([lbp_array[i]], [0], None, [256], [0,256])
		print "ok"
	print "2"
	
	# soma = 0
	# for i in xrange(0,256):
	# 	soma += hist[i]	

	target = open('database.txt', 'a')

	# target.truncate()

	#DOESNT NEED TO RUN TWICE
	print "3"
	
	if not run:
		target.write("@RELATION textura")
		target.write("\n")

		#attributes

		for i in xrange(1,1025):
			target.write("@ATTRIBUTE atr"+str(i)+" NUMERIC")
			target.write("\n")

		target.write("\n")
		target.write("\n")
		target.write("@DATA")
		target.write("\n")

		run = True
	print "4"
	

	for h in hist:
		for j in hist[h]:
			target.write(str(int(j))+",")
		target.write("\n")
		target.write("\n")
	target.write("\n")
	target.write("% new image")
	target.write("\n")


	target.close()

	print "Finished image "+str(it)
	gc.collect()
	#END OF LOOP
