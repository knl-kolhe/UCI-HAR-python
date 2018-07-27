# UCI-HAR-python
Using logistic regression model to classify Human Activity based on sensor values

I have made some changes to the original dataset found here https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones

Download the dataset and unpack it in the same directory as the HAR_logistic.py file.
Delete the '_MACOSX' folder as it is not required.

For the X_train and X_test replace "  " with " " at all places in notepad
let there be a new line after the last entry in X_train.txt and X_test.txt

delete the new line in y_train and y_test datasets at the end.

Results:

Time Required to train: 4.20775032043457
Time Required to test: 0.0059566497802734375
Exact number of accurate predictions in test set: 2836
             
            
             precision    recall  f1-score   support

          1       0.94      1.00      0.97       496
          2       0.97      0.95      0.96       471
          3       1.00      0.97      0.98       420
          4       0.98      0.88      0.93       491
          5       0.90      0.98      0.94       532
          6       1.00      1.00      1.00       537
    avg / total   0.96      0.96      0.96      2947

