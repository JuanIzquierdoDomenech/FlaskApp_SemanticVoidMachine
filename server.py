from flask import Flask, request, Response
import tensorflow.keras
from tensorflow.keras.layers import LeakyReLU
import jsonpickle
from PIL import Image, ImageOps
import numpy as np
import os

all_models = {}
all_labels = {}

# Fills all_models and all_labels
def load_models():
	##### 				Classification model: Engine button on/off 				#####

	all_models['class:engine_button'] = tensorflow.keras.models.load_model('models/classification/engine_button/model.h5', compile=False)
	labelsFile = "models/classification/engine_button/labels.txt"
	labels = []

	with open(labelsFile, 'r') as File:
		infoFile = File.readlines()
		for line in infoFile:
			words = line.split()
			labels.append(words[1])
	all_labels['class:engine_button'] = labels

	##### 				Regression model: Void needle [0,25] 					#####

	all_models['reg:void_needle'] = tensorflow.keras.models.load_model('models/regression/void_needle/model.h5', compile=False, custom_objects={'LeakyReLU': LeakyReLU})


##############################

load_models()

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello world!"

@app.route('/predict/classification/engine_button', methods=['POST'])
def predict_class_eng_btn():
	# Get the file from the POST request
	imagefile = request.files.get('imagefile', '')
	image = Image.open(imagefile)

	np.set_printoptions(suppress = True)

	# Resize and normalize, as expected by the model
	data = np.ndarray(shape=(1, 64, 64, 3), dtype=np.float32)

	size = (64, 64)
	image = ImageOps.fit(image, size, Image.ANTIALIAS)
	image_array = np.asarray(image)

	normalized_image_array = (image_array.astype(np.float32))/255.0

	data[0] = normalized_image_array

	# Run the inference
	prediction = all_models['class:engine_button'].predict(data)

	# Get the max probability
	label_index = np.argmax(prediction[0])

	# Return the label
	return all_labels['class:engine_button'][label_index]

@app.route('/predict/regression/void_needle', methods=['POST'])
def predict_reg_void_needle():
	# Get the file from the POST request
	imagefile = request.files.get('imagefile', '')
	image = Image.open(imagefile).convert('L')

	np.set_printoptions(suppress = True)

	# Resize and normalize, as expected by the model
	image = image.resize((100, 100), Image.ANTIALIAS)
	image = np.array(image)

	image = image/255.0
	image = image.reshape((1, 100, 100, 1))

	# Run the inference
	prediction = all_models['reg:void_needle'].predict(image)

	# Return the label
	return str(int(prediction*25))

if __name__ == '__main__':
	# app.run(port=5000)			# Localhost on 127.0.0.1
	app.run(host='192.168.1.53')	# Localhost for local network access (same public IP)








