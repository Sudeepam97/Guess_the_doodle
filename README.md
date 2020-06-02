# Guess_the_doodle
This project uses **Convolutional Neural Networks (CNNs)** for the task of **Image  Classification.** The model looks at the picture of a doodle you drew and by extracting and processing all sorts of 'features', guesss the correct label with ~87% accuracy. The **Quick Draw** dataset from the [Google Quick Draw game](https://quickdraw.withgoogle.com/#) has been used for the purpose of training. This implementation classifies a doodle to one of the 60 output classes.

# Demo
A video demonstration of this project can be found [here](https://youtu.be/CuCKVue0Lt8)

## Running this code
You can run this application on your `localhost`. To do that, clone the repo and `cd` to the `demo` directory. Then...
```sh
# Setup a virtual environment of python
# and activate the virtual environment.
--

# Install the required dependencies.
# The `env_setup.sh` script takes care of this task.
chmod +x env_setup.sh
./env_setup.sh

# Start the Flask server.
python3 app.py
```
* After this, open your browser and visit `http://localhost:5000` to enjoy playing. :)

## Training your own model
* There is a Jupyter Notebook called `doodle_classifier.ipynb` in this repository. If you would like to train this model from scratch, simply open that notebook in [Colab](https://colab.research.google.com/notebooks/welcome.ipynb) and start your work.

* Training would yield a `.h5` file (called `doodle_model.h5` by default). This file contains the information about the architecture and weights of the model. This is the file that is used by our demo web application to classify the user made doodles. To deploy your own model, just replace the `doodle_model.h5` file in our `demo` directory with your own.
