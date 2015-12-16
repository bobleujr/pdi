import numpy as np
import cv2
import time

hist = {}
it = 1

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
		for i in xrange(0, hist[imagem][canal].size):
			if (hist[imagem][canal][i] / multiplo) >= contador_multiplo:
				contador_multiplo += 1
				print str(hist[imagem][canal][i])




# cv2.imshow('image1',slices[0])
# cv2.imshow('image2',slices[1])
# cv2.imshow('image3',slices[2])
# cv2.imshow('image4',slices[3])

# k = cv2.waitKey(0)
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()


