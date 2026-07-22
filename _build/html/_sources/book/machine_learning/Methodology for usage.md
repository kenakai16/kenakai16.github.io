# Methodology for usage

This chapter will give a recipe on how to tackle Machine learning problems
## 3 Step process

 1. Define what you need to do and how to measure(metrics) how well/bad you are going.
 2. Start with a very simple model (Few layers)
 3. Add more complexity when needed.

## Define goals
Normally by being slightly better than human performance(in terms of accuracy or prediction time), is already enough for a good product.

## Metrics
Accuracy: % of correct examples
Coverage: Number of processed examples per unit of time
Precision: Number of detections that are correct
Error: Amount of error

## Start with simplest model
Look if available for the state-of-the-art method for solving that problem. If not available use the following recipe.
 1. 
Lots of noise and now much structure(ex: House price from features like number of rooms,kitchen size, etc...): Don't use deep learning
 2. 
Few noise but lot's of structure (ex: Images, video, text): Use deep learning

## Examples for Non-deep methods:
Logistic Regression
SVM
Boosted decision trees (Previous favorite "default" algorithm), used a lot in robotics

## What kind of deep
Few structure: Use only Fully-Connected layers 2-3 layers (Relu, Dropout, SGD+Momentum). Need at least few thousand examples per class.
Spatial structure: Use CONV layers (Inception/Residual, Relu, Droput, Batch-Norm, SGD+Momentum).
Sequencial structure (text, market movement): Use Recurrent networks (LSTM, SGD, Gradient clipping).
When using Residual/Inception networks start with the shallowest example possible.

## Solving High train errors
Do the following actions on this order:
 1. 
Inspect for defects on the data. (Need human intervention)
 2. 
Check for software bugs on your library. (Use gradient check, it's probably a backprop error)
 3. 
Tune learning rate (Make it smaller)
 4. 
Make network deeper. (You should start with a shallow network on the beginning)

## Solving High test errors
Do the following actions on this order:
 1. 
Do more data augmentation (Also try generative models to create more data)
 2. 
Add dropout and batch-norm
 3. 
Get more data (More data has more influence on Accuracy then anything else)

## Some trends
Following the late 2016 Andrew Ng lecture these are the topics that we need to pay attention.
1. Scalability
Have a computing system that scale well for more data and more model complexity.
2. Team
Have on your team divided with with AI people and HPC (Cuda, OpenCl, etc...).
3. Data first
Data is more important than your model, always try to get more quality data before trying to change your model.
4. Data Augmentation
Use normal data augmentation techniques plus Generative models(Unsupervised).
5. Make sure that Validation Set and Test set come from same distribution
This will avoid having a test or validation set that does not tell the reality. Also helps to check if your training is valid.
6. Have Human level performance metric
Have a team of experts to compare with your current system performance. Also it drives decisions between getting more data, or making model more complex.
7. Data server
Have a unified data-warehouse. All team must have access to data, with SSD quality access speed.
8. Using Games
Using games are cool to help augment datasets, but attention because games does not have the same variants of the same class as real life. For example GTA does not have enough car models compared to real life.
9. Ensembles always help
Training separately different networks and averaging their end results always gives some extra 2% accuracy. (Imagenet 2016 best results were simple ensambles)
10. What to do if you have more than 1000 classes
Use hierarchical Softmax to increase performance.
11. How many samples per class do we need to have good result
If training from scratch, use the same number of parameters. For example Model has 1000 parameters, so use 1000 samples per class.
If doing transfer learning is much less (Much is not defined yet, more is better).