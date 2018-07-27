# UCI-HAR-python
Using logistic regression model to classify Human Activity based on sensor values

## Requirements
### Here is a list of all the python libraries I used:
numpy

sklearn

time

## Dataset
I have made some changes to the original dataset found here https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones

Download the dataset and unpack it in the same directory as the HAR_Logistic.py file.
Delete the '_MACOSX' folder as it is not required.

For the X_train and X_test replace '  '(2 spaces) with ' '(1 space) at all places using a text editor

Let there be a new line after the last entry in X_train.txt and X_test.txt

delete the new line in y_train and y_test datasets at the end.


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
