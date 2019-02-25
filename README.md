# ImageClassificationCNN
The purpose of this repo is to give readers a clear idea of how to build and optimise a CNN model for their own image classification applications.

# Gather dataset
Before we start, the dogs-cats dataset could be downloaded from https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data 

# Build a CNN model
The reasons behind each step or substep could be found in the code. For futher understanding of how a CNN model works, please have a look at https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148
  1. Gather and prepare data
  - Convert image examples to numpy arrays
  - Resize the shape of arrays
  - Create training_dataset
  - Shuffle the dataset
  - Pack to variables 
  - Save data to feed neural network
  2. Build and train a CNN model
  - Load data built in step 1
  - Set up CNN model
  - Train the model
  3. Implement the trained model
