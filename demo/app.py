from flask import Flask, render_template, request
from scipy.misc import imread, imresize
import re
import base64

import tensorflow as tf
import numpy as np
from tensorflow import keras

import json

## Define our output classes
out_classes = ['axe', 'boomerang', 'candle', 'donut', 'envelope', 'fish', 'frying pan', 'golf club', 'headphones', 'hourglass', 'ice cream', 'jail', 'knife', 'ladder', 'mountain', 'mushroom', 'octagon', 'pliers', 'rain', 'star', 'see saw', 'syringe', 'triangle', 'traffic light', 'umbrella', 'vase', 'wine glass', 'zigzag']

## Initalize our flask app
app = Flask(__name__)

## Load the model trained on colab
model = keras.models.load_model ("my_model.h5", custom_objects = {'GlorotUniform': tf.keras.initializers.glorot_uniform()})
model._make_predict_function()

## Decoding an image from base64 into raw representation
def convertImage(imgData1):
	imgstr = re.search(r'base64,(.*)',imgData1).group(1).encode()
	with open('output.png','wb') as output:
		output.write(base64.b64decode(imgstr))

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/predict/',methods=['GET','POST'])
def predict():
	imgData = request.get_data()
	convertImage(imgData.decode())
	
	## Read the image into memory
	x = imread('output.png', mode = 'L')
	## Compute a bit-wise inversion so black becomes white and vice versa
	x = np.invert(x)
	## Make it the right size
	x = imresize(x, (28, 28))
	## Convert to a 4D tensor to feed into our model
	x = x.reshape(1,28,28,1)
	## Normalize
	x = x / 255
	## Make the top 4 predictions.
	pred = model.predict(x)
	ind = (-pred).argsort()
	ind = np.ndarray.flatten(ind)
	ind = ind[0:4]
	## Create and return the response
	response = {}
	for i in range(4):
	    response[str(i)] = out_classes[ind[i]]
	return json.dumps(response)


if __name__ == "__main__":
	port = 5000
	app.run(host='0.0.0.0', port=port)
