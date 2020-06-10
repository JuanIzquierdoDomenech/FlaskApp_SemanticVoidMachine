import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

labelsFile = "labels.txt"
labels = []

with open(labelsFile, 'r') as File:
	infoFile = File.readlines()
	for line in infoFile:
		words = line.split()
		labels.append(words[1])

print(labels)

np.set_printoptions(suppress = True)# Load the model
model = tensorflow.keras.models.load_model('model.h5', compile=False)

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 64, 64, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open('test/test_photo_on_1.jpg')

#resize the image to a 64x64 with the same strategy as in the model:
#resizing the image to be at least 64x64 and then cropping from the center
size = (64, 64)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)

# display the resized image
image.show()

# Normalize the image
normalized_image_array = (image_array.astype(np.float32))/255.0

# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
print(prediction)
print(prediction.shape)
print(prediction[0][0])
print(prediction[0][1])

label_index = np.argmax(prediction[0])
print("Predicted class: " + labels[label_index])