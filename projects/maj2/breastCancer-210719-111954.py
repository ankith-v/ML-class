from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score



# Now we need to create new variables
data = load_breast_cancer()
label_names = data["target_names"]
labels = data["target"]
feature_names = data["feature_names"]
features = data["data"]




print(label_names)
print("Class label :", labels[0])
print(feature_names)
print(features[0], "\n")


# Splitting The Dataset
train, test, train_labels, test_labels = train_test_split(features, labels,
                                                          test_size=0.2,
                                                          random_state=42)


# Using Naive Bayes for Breast Cancer Detection
gnb = GaussianNB()
gnb.fit(train, train_labels)



# We can use the trained model to make predictions on our test set, which we use the predict() function.
preds = gnb.predict(test)
print(preds, "\n")



# We will use the accuracy_score () function provided by Scikit-Learn 
# to determine the accuracy rate of our machine learning classifier
print(accuracy_score(test_labels, preds))
