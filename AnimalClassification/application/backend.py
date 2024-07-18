# Importing Necessory Modules
import numpy as np
import cv2
import joblib

# Global Variable to store model
__model=None

# Define a function which wil load artifects
def load_saved_artifects():
    print("Loading Saved Artifects ..... Start")
    global __model
    if __model is None:
        with open("saved_model.pkl",'rb') as f:
            __model=joblib.load(f)
    print("Loading Saved Artifects....Done")

# Define a function for classification of images
def classify_image(path):
    img=cv2.imread(path)
    img_resize=cv2.resize(img,(140,140,))
    img_resize_sh=img_resize.reshape(1,140,140,3)
    img_scaled=img_resize_sh/255
    value=np.argmax(__model.predict(img_scaled))
    return value

if __name__ == "__main__":
    pass
    
