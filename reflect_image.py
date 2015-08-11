import numpy as np

#Reflect arrays of any dimension horizontally or vertically
#dimension = 0: reflect vertically (around x-axis)
#dimension = 1: reflect horizontally (around y-axis)
def reflect(image, dimension):
	dimension_size = image.shape[dimension] #get size of this dimension
	#changes VIEW ONLY: want dimension to slice along to be first for easy indexing
	image = image.swapaxes(dimension, 0)
	#only iterate over the left half (will be swapped with right half)
	for entry in range(dimension_size/2):
		#swap values with mirror image column
		#in all color channels and all rows
		temp_val = np.copy(image[entry])
		image[entry] = image[dimension_size - (entry+1)]
		image[dimension_size - (entry+1)] = temp_val
	image = image.swapaxes(dimension, 0) #swap dimensions back
	return image

if __name__ == "__main__":
	import matplotlib.pyplot as plt
	img_file = "imgres.jpg"
	img = plt.imread(img_file)

	vertically_reflected_image = reflect(np.copy(img), 0)
	horizontally_reflected_image = reflect(np.copy(img), 1)

	#make plots	
	plt.imshow(img)
	plt.title("original image: ")
	plt.figure()

	plt.imshow(vertically_reflected_image)
	plt.title("specifying dimension reflected around x axis: ")
	plt.figure()

	plt.imshow(horizontally_reflected_image)
	plt.title("specifying dimension reflected around y axis: ")
	#don't need to specify last figure

	#show plot
	plt.show()
	
