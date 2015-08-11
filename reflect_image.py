import numpy as np

#takes image as numpy array of pixel data
#reflect images horizontally (around a vertical line)
def reflect_horizontally(image):
	num_cols = image.shape[1]
	#only iterate over the left half (will be swapped with right half)
	for col in range(num_cols/2):
		#swap values with mirror image column
		#in all color channels and all rows
		temp_val = np.copy(image[:,col,:]) #make a deep copy of this column's values
		image[:,col,:] = image[:,num_cols - (col + 1),:]
		image[:,num_cols - (col + 1),:] = temp_val
	return image

def reflect_vertically(image):
	num_rows = image.shape[0]
	#only iterate over the left half (will be swapped with right half)
	for row in range(num_rows/2):
		#swap values with mirror image column
		#in all color channels and all rows
		temp_val = np.copy(image[row,:,:]) #make a deep copy of this column's values
		image[row,:,:] = image[num_rows - (row + 1),:,:]
		image[num_rows - (row + 1),:,:] = temp_val
	return image

#generic reflection (horizontal or vertical, 2D or 3D)
def reflect(image, dimension):
	num_dimensions = len(image.shape)
	dimension_size = image.shape[dimension]
	#only iterate over the left half (will be swapped with right half)
	for entry in range(dimension_size/2):
		#swap values with mirror image column
		#in all color channels and all rows
		temp_val = image.take(entry,axis=dimension) #make a deep copy of this column's values
		image.take(entry,axis=dimension) = image.take(dimension_size - (entry+1),axis=dimension)
		image.take(dimension_size - (entry+1),axis=dimension) = temp_val
	return image

#take slice (vector) of this array (of given number of dimensions) in given dimensions
def index_arr(arr, dimension, num_dimensions):
	 pass #think np.take() will do this

if __name__ == "__main__":
	import matplotlib.pyplot as plt
	img_file = "imgres.jpg"
	img = plt.imread(img_file)
	#plt.imshow(img)
	#plt.figure()
	#reflected_image = reflect_horizontally(img)
	reflected_image = reflect_vertically(img)
	plt.imshow(reflected_image)
	#plt.figure()
	plt.show()
	
