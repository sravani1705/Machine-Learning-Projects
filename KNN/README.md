**K Nearest Neighbour**

It is a supervised machine learning algorithm which predicts the instance based on the neighbours. This algorithm needs no training and predicts based on the distance from the neighbours.
1. Calculate the distance to each instance in train dataset. Examples of distance metric: Euclidean, Minkwoski, Manhattan etc.
2. Select K instances from train set which have minimal distance
3. For Classification : The label to the test instance is determined by majority of K instance's class labels.
   For Regression : The value of test instance is given by mean/median of the neighbours.

**Pros:**
1. Simple and Easily Implemented
2. Go to solution and can act as baseline
3. Interpretable

**Cons:**
1. Slow and Memory intensive
2. Depends on the distance metric
3. Cannot work well for large number of features
