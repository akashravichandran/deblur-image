# deblur-image

In this post we will try to understand how does deblurring system works.

Due to my sub-par photography skills, I ended up with this picture. 
We will proceed with a step by step process on how to deblur my photo.

I would like to split this post into three sections 

- Doing it using a Deblur Weiner Filter
- By using a Pretrained deblur model

Wiener-Filter

Wiener Filter is used to denoise and deblur noisy images corrupted by Gaussian noise and motion blurring. The implemented filter was tested on the Lena image with the resolutions of 1960x1960 and 512x512 attached in the repo.