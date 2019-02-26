# ImageClassificationCNN
The purpose of this repo is to give readers a clear idea of how to build and optimise a CNN model for their own image classification applications.
The image classifier I used here is to classify dog vs cat images.

## Prerequisities
I recommend to install [Anaconda python 3.7 version](https://www.anaconda.com/distribution/) in your computer because it supports porting for all the popular python libraries in data science and it comes with Jupyter Notebook which is an open-source web application  we will use later. There are some other python libraries we also need to install to complete setting up our working environment. 
You can install them by opening one Terminal (Mac/Linux) or Command Prompt (Windows) and run these command lines:
  - [Tensorflow](https://anaconda.org/conda-forge/tensorflow)
  - [Opencv](https://anaconda.org/conda-forge/opencv)
  

## Gather dataset
Before we start, the dogs-cats dataset which contains around 25,000 images of dogs and cats could be downloaded from [kaggle-dataset](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data). In the file *1_GatherLocalData.ipynb*, you can change the DATADIR path to match with your kaggle folder name.
You can open file *.ipynb* by typing in Command: 

`jupyter notebook` 

## Build a CNN model
The explanation for each step or substep could be found in the code. If you are new to CNN, please have a look [here](http://cs231n.github.io/)

**1. Gather and prepare data**
  - Convert image examples to numpy arrays
  - Resize the shape of arrays
  - Create training_dataset
  - Shuffle the dataset
  - Pack to variables 
  - Save data to feed neural network
  
**2. Build and train a CNN model**
  - Load the prepared data
  - Set up CNN model
  - Train the model

  
**3. Implement the trained model**

After training the model, you can play around with test-images that I downloaded from Google or use your own images to check if the trained image classifier actually works.

<img src="https://github.com/Khai8388/ImageClassificationCNN/blob/master/images/example_result.png" height="256" width="324">


## Optimization algorithm
While training models for the project, to ensure that you get the best model architecture, use Tensorboard
  
  `tensorboard --logdir=path/to/log-directory`
  
  
  or
  
  `tensorboard --logdir=path/to/log-directory --host localhosty`
  
  <img src="https://github.com/Khai8388/ImageClassificationCNN/blob/master/images/Tensorboard.PNG"  height="512" width="612">
  
This part should be done before you carry out the step 2, to choose the best architecture for your CNN model. It is also higly recommended to have look at [Deep Leaning course 2 and 3](https://www.coursera.org/learn/deep-neural-network/home/welcome) to understand how to get deep learning to work well and successfully build a project.

## Available CNN architectures
There are famous CNN architectures that you can try besides building your own, such as AlexNet, VGGNet, GoogLeNet or ResNet depending on the size of your dataset and the desired speed/precision of your application.

## Reference
Deep learning basics - sentdex : https://www.youtube.com/watch?v=wQ8BIBpya2k&list=PLQVvvaa0QuDfhTox0AjmQ6tvTgMBZBEXN&pbjreload=10
