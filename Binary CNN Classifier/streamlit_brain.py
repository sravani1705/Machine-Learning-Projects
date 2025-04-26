import streamlit as st
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image

# --- Define your model ---
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.conv3 = nn.Conv2d(16, 32, 5)
        self.fc1 = nn.Linear(32 * 24 * 24, 2048)
        self.fc2 = nn.Linear(2048, 512)
        self.fc3 = nn.Linear(512, 2)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        #print("conv1:", x.shape)
        x = self.pool(F.relu(self.conv2(x)))
        #print("conv2:", x.shape)
        x = self.pool(F.relu(self.conv3(x)))
        #print("conv3:", x.shape)
        x = torch.flatten(x, 1) # flatten all dimensions except batch
        x = F.relu(self.fc1(x))
        #print("fc1:", x.shape)
        x = F.relu(self.fc2(x))
        #print("fc2:", x.shape)
        x = self.fc3(x)
        #print("fc3:", x.shape)
        return x

# --- Load model and weights ---
model = Net()
model.load_state_dict(torch.load('/home/sravani/Documents/datasets/model_weigths.pt', map_location=torch.device('cpu')))
model.eval()

# --- Image transform ---
transform = transforms.Compose([
    transforms.Lambda(lambda img: img.convert("RGB")),  # force 3 channels
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# --- Streamlit App ---
st.title(" Brain Tumor Detection")
st.write("Upload a MRI image to predict the class (0 or 1)")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    img_tensor = transform(image).unsqueeze(0)  # add batch dim

    with torch.no_grad():
        output = model(img_tensor)
        _, prediction = torch.max(output,1)
    if int(prediction) == 1:
        st.write("### Result: Patient has brain tumor")
    else:
        st.write("### Result: Patient does not have brain tumor")
