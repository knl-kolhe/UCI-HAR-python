# UCI Human Activity Recognition python
The Autobiography of this DataSet:
I could be gathered from your phone, your smartwatch, or even in a chip embedded in your body. But I reckon it's going to be a few years before that happens. Using me, a smart device can automatically classify what you are doing and help keep track of your actions. Using a model which I have helped train, can be used to classofy your actions locally on the device. then this classification can be stored on a cloud☁️ for long term tracking and that can help you regulate your actions. This can be in the form of changing behaviours to include more activity in your day to day life or even getting more rest at proper intervals so that you can be fresh for a new challenge every day. 
wThank you for listening to my story and my purpose, now Kunal will explain how he used me to build a machine learning model which classifies human actions.

Kunal: Thank you data, now lets continue...

Using logistic regression model to classify Human Activity based on sensor values

## Requirements
### Here is a list of all the python libraries I used:
numpy

sklearn

time

## Dataset
I have made some changes to the original dataset found here https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones
Download the dataset and unpack it in the same directory as the HAR_Logistic.py file.

For the X_train and X_test replace '  '(2 spaces) with ' '(1 space) at all places using a text editor

Let there be a new line after the last entry in X_train.txt and X_test.txt

delete the new line in y_train and y_test datasets at the end. (Will modify code so that these changes are not required)

## Program
The code is classifying all the sensor values into 6 classes.

WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING


## Results:

Time Required to train: 4.20775032043457

Time Required to test: 0.0059566497802734375

Exact number of accurate predictions in test set: 2836/2947

            
             precision    recall  f1-score   support

          1       0.94      1.00      0.97       496
          2       0.97      0.95      0.96       471
          3       1.00      0.97      0.98       420
          4       0.98      0.88      0.93       491
          5       0.90      0.98      0.94       532
          6       1.00      1.00      1.00       537
    avg / total   0.96      0.96      0.96      2947

I ran it on an i7 7700. 
Program runs on only 1 core.
