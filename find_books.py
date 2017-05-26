# import of necessary package

import sys

import numpy as np
import cv2

image = cv2.imread("1-3,jpg")
gray_im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_im = cv2.GaussianBlur(gray_im, (3, 3), 0)
cv2.imwrite('gray.jpg', gray_im);

edged = cv2.Canny(gray_im, 10, 250)
cv2.imwrite("edged.jpg", edged)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = (cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel));
cv2.imwrite("closed.jpg", closed);

cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
total = 0

for c in cnts:
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)

	if len(approx) == 4:
		cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
		total += 1

output = cv2.imwrite("output.jpg", image)
print("I found {0} books").format(total)
