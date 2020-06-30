import cv2
from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
#imageA = "./fingerprint_images/Vilas.png"
#imageB = "./login_FP_images/Vilas.png"

original = cv2.imread(r".\\fingerprint_images\\avi.png")
login_img = cv2.imread(r".\\login_FP_images\\avi.png")

original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
login_img = cv2.cvtColor(login_img, cv2.COLOR_BGR2GRAY)

s = measure.compare_ssim(original, login_img)

print(s)
if(s <= 1.00 and s > 0.20):
		print("Match")
else:
		print("Not Match")

'''

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
def compare_images(imageA, imageB):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = measure.compare_ssim(imageA, imageB)
	# setup the figure
	#fig = plt.figure(title)
	#plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
	# show first image
	#ax = fig.add_subplot(1, 2, 1)
	#plt.imshow(imageA, cmap = plt.cm.gray)
	#plt.axis("off")
	# show the second image
	#ax = fig.add_subplot(1, 2, 2)
	#plt.imshow(imageB, cmap = plt.cm.gray)
	#plt.axis("off")
	print(s)
	if(s <= 1.00 and s > 0.20):
    		print("Match")
	else:
    		print("Not Match")
	# show the images
	#plt.show()
	
    # load the images -- the original, the original + login_img,
# and the original + photoshop
original = cv2.imread(r".\\fingerprint_images\\AvinashM.png")
login_img = cv2.imread(r".\\login_FP_images\\AvinashM.png")
#shopped = cv2.imread(r"./fingerprint_images/Avinasha.png")
# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
login_img = cv2.cvtColor(login_img, cv2.COLOR_BGR2GRAY)
#shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)
# initialize the figure
fig = plt.figure("Images")
images = ("Original", original), ("login_img", login_img)
# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
# show the figure
plt.show()
# compare the images
#compare_images(original, original, "Original vs. Original")
compare_images(original, login_img)
#print(s)

#compare_images(original, shopped, "Original vs. Photoshopped")'''

