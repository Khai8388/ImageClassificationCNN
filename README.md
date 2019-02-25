# ImageClassificationCNN
The purpose of this repo is to give readers a clear idea of how to build and optimise a CNN model for their own image classification applications.
The image classifier I used here is to classify dog vs cat images.

## Gather dataset
Before we start, the dogs-cats dataset could be downloaded from [kaggle-dataset](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data). After that change the DATADIR in *1_GatherLocalData.ipynb* to match with your kaggle folder name.

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
  - Load the prepared data
  - Set up CNN model
  - Train the model

  
**3. Implement the trained model**

After training the model, you can play around with test-images that I downloaded from Google or use your own images to check if the trained image classifier actually works.

<img src="https://github.com/Khai8388/ImageClassificationCNN/blob/master/example_result.png" height="256" width="324">


## Optimization algorithm
While training models for the project, to ensure that you get the best model architecture, use Tensorboard
  
  `tensorboard --logdir=path/to/log-directory`
  
  or
  
  `python -m tensorboard.main --logdir=path/to/log-directory`
  
This part should be done before you carry out the step 2, to choose the best architecture for the project. It is also higly recommended to have look at [Deep Leaning course 2 and 3](https://www.coursera.org/learn/deep-neural-network/home/welcome) to understand how to get deep learning to work well and successfully build a project.

## Available CNN architectures
There are famous CNN architectures that you can try besides building your own, such as AlexNet, VGGNet, GoogLeNet or ResNet depending on the size of your dataset and the desired speed/precision of your application.

## Reference
Deep learning basics - sentdex : https://www.youtube.com/watch?v=wQ8BIBpya2k&list=PLQVvvaa0QuDfhTox0AjmQ6tvTgMBZBEXN&pbjreload=10
