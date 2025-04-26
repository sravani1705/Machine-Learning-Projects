# Brain Tumor Detection
# Dataset
1.Download the dataset from kaggle "https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection"
2. Extract the zip file and sort the files to train and test folders

# CNN Classifier
1. In this project, a CNN classifier is built from scratch with series of conv and fc layers
2. Loss function and Optimiser are initialised. Hyperparmeters like epoch, learning rate, momentum, batch size are fixed
3. Save the model weights for future evaluation
4. Load the saved weights and evaluate the built model with a test image

# Deploy
The model is deployed using streamlit and to run the app, execute streamlit run streamlit_brain.py
The output of the above command :
![alt_text](https://github.com/sravani1705/Machine-Learning-Projects/Binary CNN Classifier/brain_tumor1.png)
Upload any test image and get the result as shown in figure
![alt_text](https://github.com/sravani1705/Machine-Learning-Projects/Binary CNN Classifier/brain_tumor2.png)
 
