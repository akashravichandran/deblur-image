# # # from scipy import ndimage
# # import cv2 
# # image = cv2.imread('deblur.jpg')
# # # print(image)

# def TowerOfHanoi(n , from_rod, to_rod, aux_rod): 
#     if n == 1: 
#         print("Move disk 1 from rod",from_rod,"to rod",to_rod) 
#         return
#     TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
#     print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
#     TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 
          
# # Driver code 
# n = 3
# TowerOfHanoi(n, 'A', 'B', 'C')  
# # A, C, B are the name of rods 

# def  countSetBits(n): 
#     count = 0
#     while (n): 
#         count += n & 1
#         n >>= 1
#     return count 
  
  
# Program to test function countSetBits */ 
# i = 9
# print(countSetBits(i)) 

# import numpy as np
# import matplotlib.pyplot as plt
# import cv2
# from skimage import color, data, restoration

# astro = cv2.imread('deblur.jpg')
# from scipy.signal import convolve2d as conv2
# psf = np.ones((5, 5)) / 25
# astro = conv2(astro, psf, 'same')
# astro += 0.1 * astro.std() * np.random.standard_normal(astro.shape)

# deconvolved, _ = restoration.unsupervised_wiener(astro, psf)

# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 5),
#                        sharex=True, sharey=True)

# plt.gray()

# ax[0].imshow(astro, vmin=deconvolved.min(), vmax=deconvolved.max())
# ax[0].axis('off')
# ax[0].set_title('Data')

# ax[1].imshow(deconvolved)
# ax[1].axis('off')
# ax[1].set_title('Self tuned restoration')

# fig.tight_layout()

# plt.show()




import numpy as np
import matplotlib.pyplot as plt
# from scipy.misc import imread
import cv2
import imageio
from skimage import color, data, restoration
from scipy.signal import convolve2d as conv2

def main():
    image = cv2.imread("deblur.jpg")
    psf = np.ones((5, 5)) / 25


    #plt.imshow(arr, cmap='gray')
    #plt.show()
    #blurred_arr = imfilter(arr, "blur")
    # psf = np.ones((5, 5)) / 25
    # image = conv2(image, psf, 'same')
    # image += 0.1 * image.std() * np.random.standard_normal(image.shape)

    # deconvolved = restoration.wiener(image, psf, 1, clip=False)
    #print deconvolved
    #print image

if __name__ == "__main__":
    main()