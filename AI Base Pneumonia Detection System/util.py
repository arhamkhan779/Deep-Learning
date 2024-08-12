import cv2
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np

##Define a global variable to save the model
__model=None

#Define a function to load saved model
def load_saved_artifects():

    global __model
    
    if __model is None:
        print("Loading Saved Artifects ---- Start")
        __model=keras.models.load_model("saved_model.keras")
        print("Loading Saved Artifects ---- Done")

#Define a function to Detect Pneumonia
def classify(image):
    global __model
    classes=['Pneumonia','Normal']
    # img_arr=np.array(image)
    resize=cv2.resize(image,(224,224))
    scale=resize/255
    final=scale.reshape(1,224,224,3)

    prediction=__model.predict(final)
    threshold=0.5
    prediction1=[1 if prediction > 0.5 else 0]
    name=classes[prediction1[0]]

    return [prediction,name]

if __name__ == "__main__":
    pass




