# Guess_the_doodle
In this project, I have explored the power of **Convolutional Neural Networks (CNNs)** and have used it for the task of **Object  Classification.** My CNN can look at the picture of a doodle you drew and by extracting and processing all sorts of **'features'**, present on those doodle images, guess what you have drawn with ~92% accuracy.

I have used the **Quick Draw** dataset from the [Google Quick Draw game](https://quickdraw.withgoogle.com/#) for the purposes 
of training and testing the CNN model. Actually, this project more or less recreates what happens in the Quick Draw game, however, there are minor differences in the gameplay and the approach using which the predictions are made is different.

Before I proceed however, here's a shoutout to [@darkHarry](https://github.com/darkHarry), [@saranshbarua](https://github.com/saranshbarua), and [@sxnaprkhr](https://github.com/sxnaprkhr) for helping with the design of the demo website.

## Running this code
If you would like to train the CNN model, then it can be done on [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb). Simply import the Jupyter Notebook from this repo to Colab and fire it up.

After training the model, you'll get a file that is similar to the file **demo/my_model.h5**. This file contains the information related to our model, and will be used by our web app at the back end to actually classify the user made doodles.

To run the web app, make sure you have the followig dependencies installed, within brackets are the specific versions I had:

- TensorFlow (v.1.11.0)
- Flask (v1.0.2)

Other essential dependencies are stated below, but these should automatically get installed along with TensorFlow:
- Keras (2.1.6-tf)
- SciPy (1.1.0)
- NumPy (v1.15.4)

Finally, to run the web app, open your terminal, cd to the directory called **demo**, and type:
```
>> python3 app.py
```
Then open up your web browser (I had used Mozilla Firefox) and go to the following address:
```
http://localhost:5000
```
Enjoy playing. :)

## An overview of Computer Vision and CNNs.
If you are a beginner, and want to learn more about Deep Learning, Computer Vision, or CNNs in particular, I recommend you to 
look up various blog posts that talk about these topics. Plenty of MOOCs and open courses from prestigious institutions are 
available as well. However, here is an introduction to get you started:

Humans use their eyes to capture the visual information around them, the optic nerves, send this information to the brain, and 
the brain processes this information to create a sense of vision for them.

**Computer Vision** is the science that aims to give a similar, if not better, capability to a machine or a computer. It is 
concerned with the automatic extraction, analysis, and understanding of useful information from a single image or sequence of
images.

A typical machine must be **hard coded** to perform a given task. *“If this is equal to this then execute these set of statements”.*
With this classic approach, if a machine has to be given the sense of vision, it must be hard coded to understand visual data.

However, this hard engineering approach is not suitable for a task like computer vision because, it is not easy to hard code the
features that describe visual data. Features, refer to the most basic individual properties or patterns that make up something.

On the other hand, we humans are able to visually perceive the world that surrounds us because our brains have, through some 
unknown process, **trained themselves** to understand these underlying properties or features of visual data.

Talking about how the animal brain processes visual data, in terms of a typical mathematical equation, y = f(x), we can 
consider **x** to be the features (the relevant information extracted from data), **f** to be the computations that the brain
performs, and **y** to be the interpretations that the brain makes after all the processing is done. Also, please ignore this
paragraph if it made things more confusing for you.

An Artificial Neural Network (ANN) or simply, a Neural Network is a kind of [directed, weighted graph](https://en.wikipedia.org/wiki/Graph_theory) 
that tries to mimic the connectivity pattern of the neurons inside the animal brain. Trust me, I would not have used the graphs
to describe Neural Networks if they weren't making things simpler. Now, individual nodes of this graph are called **Neurons of the
Artificial Neural Network.** An input can be fed to this network, and an output can be obtained from it, this output can be compared
with the expected output and the weights can be adjusted if the expectations are not met. Looping over this step multiple times 
would give us a set of weights that give us the minimum error between the output obtained and the expected output. This process
of looping over is called training the Neural Network.

A modified architecture of the ANN which is prominently used for computer vision is called the **Convolutional Neural Network (CNN).**
They were inspired by the biological visual cortex, the part of the brain that interprets the signals from the optic nerves and 
creates the sensation of vision. Basically, the connectivity pattern between the neurons of the CNN, resembles the organization
of the animal visual cortex.

In animals, individual cortical neurons respond to stimuli only in a restricted region of the visual field, known as the 
receptive field. The receptive fields of different neurons partially overlap such that they cover the entire visual field.

Convolutional Neural Networks recreate this process by convolving different parts of the image (receptive field), having partial 
overlap, with the same **filter.** The operation is called the convolution operation but mathematically, it is the **cross 
correlation operation.** Note that an image is expressed as a matrix of numbers and a filter is also just a (smaller) matrix of 
numbers and acts like the weights of the CNN. 

When a filter matrix is composed of the right set of numbers, it becomes a relevant **feature detector,** detecting simple 
features such as vertical or horizontal edges, or even complex features such as eyes or ear. These “right set of numbers” are 
obtained by training of the CNN. This allows the CNN to automatically extract features from Image data and excludes the need for
us to hard code these features.

Cross correlation, allows a filter to detect 'how much' of a given pattern is prevalent on the area of the image to which the 
filter is applied. So, a vertical edge detecting filter, when convolved with a part of the image, will output a number that will
denote ‘how much vertical edge is present in this area of the image’.

Thus, by using CNNs, we exclude the need for us to hard code the visual features and we can quantify them as well. This allows
our machines to effectively understand, process, and derive conclusions from images, thus, allowing them to ‘perceive’ vision.
