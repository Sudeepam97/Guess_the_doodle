import re
import json
import base64
import keras
import numpy as np
from PIL import Image
from flask import Flask, render_template, request


## Define our output classes
out_classes = ['airplane', 'apple', 'axe', 'banana', 'baseball', 'baseball_bat', 'birthday_cake', 'book', 'bucket', 'bus', 'candle', 'camera', 'car', 'cell_phone', 'cloud', 'coffee_cup', 'crown', 'dolphin', 'donut', 'dumbbell', 'envelope', 'eye', 'eyeglasses', 'finger', 'fish', 'flashlight', 'flower', 'fork', 'golf_club', 'hammer', 'hand', 'headphones', 'hot_air_balloon', 'hourglass', 'ice_cream', 'key', 'knife', 'ladder', 'leaf', 'light_bulb', 'lightning', 'mountain', 'mushroom', 'octagon', 'pencil', 'pliers', 'screwdriver', 'see_saw', 'star', 'sword', 'syringe', 'tooth', 'toothbrush', 'traffic_light', 't-shirt', 'umbrella', 'vase', 'windmill', 'wine_glass', 'zigzag']

## Initalize our flask app
app = Flask(__name__)

## Load the model trained on colab
model = keras.models.load_model ("doodle_model.h5")
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

	# Read, Resize, Invert, Convert to 4D tensor, Normalize	
	pil_img = Image.open('output.png').convert('L')
	x = np.array(pil_img.resize((28, 28), resample=2))
	x = np.invert(x)
	x = x.reshape(1,28,28,1)
	x = x / 255

	## Make the top 3 predictions.
	pred = model.predict(x)
	ind = (-pred).argsort()
	ind = np.ndarray.flatten(ind)
	ind = ind[0:3]
	
	## Create and return the response
	response = {}
	for i in range(3):
	    response[str(i)] = out_classes[ind[i]]
	return json.dumps(response)


if __name__ == "__main__":
	port = 5000
	app.run(host='0.0.0.0', port=port, debug=True)
