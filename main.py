import cv2
import glob
import numpy as np

# Load an colorr image in colour
img = cv2.imread('data/0001.jpg', cv2.IMREAD_COLOR)

# Write colour image
cv2.imwrite('media/figure1.png',img)

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
imgs = [cv2.imread("data/{:04}.jpg".format(i), cv2.IMREAD_COLOR) for i in range(1, len(glob.glob("data/*.jpg")))]
imgs_stack = np.stack(imgs, axis=0)
print(imgs_stack.shape)

# Calculate misty image
misty_img = np.mean(imgs_stack, axis=0)

# Save misty image
cv2.imwrite('media/figure2.png', misty_img.astype(np.uint8))


print(misty_img.shape, misty_img.max())
cv2.imshow('image', misty_img.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
