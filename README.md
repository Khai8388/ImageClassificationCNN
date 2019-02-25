# ImageClassificationCNN
The purpose of this repo is to give readers a clear idea of how to build and optimise a CNN model for their own image classification applications.
The image classifier I used here is to classify dog vs cat images.

## Gather dataset
Before we start, the dogs-cats dataset could be downloaded from [kaggle-dataset](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data).

## Build a CNN model
The explanation for each step or substep could be found in the code. If you are curious about CNN, please have a look [here](http://cs231n.github.io/)

**1. Gather and prepare data**
  - Convert image examples to numpy arrays
  - Resize the shape of arrays
  - Create training_dataset
  - Shuffle the dataset
  - Pack to variables 
  - Save data to feed neural network
  
**2. Build and train a CNN model**
  - Load data built in step 1
  - Set up CNN model
  - Train the model
  
**3. Implement the trained model**

## Optimization algorithm
This part should be done before you carry out the step 2, to choose the best architecture for the project. It is also higly recommended to have look at [Deep Leaning course 2 and 3](https://www.coursera.org/learn/deep-neural-network/home/welcome) to understand how to get deep learning to work well and successfully build a project.

## Available CNN architectures
There are famous CNN architectures that you can try besides building your own, such as AlexNet, VGGNet, GoogLeNet or ResNet depending on the size of your dataset and the desired speed/precision of your application.
