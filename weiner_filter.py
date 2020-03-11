import numpy as np
import cv2 as cv
from skimage.color import rgb2gray
from matplotlib import pyplot as plt
from scipy.fftpack import fft2, ifft2
from scipy.signal.windows import gaussian

def gaussian_kernel(kernel_size=3):
    h = gaussian(kernel_size, kernel_size/3).reshape(kernel_size, 1)
    h = np.dot(h, h.transpose())
    h /= np.sum(h)
    return h

def weiner_filter(img, kernel, size):
    kernel /= np.sum(kernel)
    dummy = np.copy(img)
    dummy = fft2(dummy)
    kernel = fft2(kernel, shape = img.shape)
    kernel = np.conj(kernel) / (np.abs(kernel) ** 2 + size)
    dummy = dummy * kernel
    dummy = np.abs(ifft2(dummy))
    return dummy

img = cv.imread('deblur.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('gray', img)
cv.waitKey(0)
kernel = gaussian_kernel(kernel_size=5)

filtered_img1 = weiner_filter(img, kernel, size=10)
