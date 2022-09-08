import cv2
import glob
import numpy as np

COLOUR = cv2.IMREAD_GRAYSCALE
#COLOUR = cv2.IMREAD_COLOR

# Load an colorr image in colour
img = cv2.imread('data/0001.jpg', COLOUR)

# Write colour image
cv2.imwrite('media/figure3.png',img)

# show image
"""
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print(type(img), img.shape)

# Read in all images
for i in range(1, 15):
    print("data/{:04}.jpg".format(i))
imgs = [cv2.imread("data/{:04}.jpg".format(i), COLOUR) for i in range(1, len(glob.glob("data/*.jpg")))]
imgs_stack = np.stack(imgs, axis=0)
print(imgs_stack.shape)

# Calculate misty image
misty_img = np.mean(imgs_stack, axis=0)

# Save misty image
cv2.imwrite('media/figure4.png', misty_img.astype(np.uint8))
