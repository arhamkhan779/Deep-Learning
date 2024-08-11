import tensorflow  as tf
from tensorflow import keras
from PIL import Image 
import numpy as np
import cv2

__model=None

face_cascade=cv2.CascadeClassifier(".\opencv\harcascade\haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier(".\opencv\harcascade\haarcascade_eye.xml")

def Load_Saved_Artifects():
    
    global __model
    print("Loading Saved Artifects ---- Start")
    if __model is None:
        __model=keras.models.load_model("saved_model.keras")
    print("Loading Saved Artifects ---- Done")

def get_cropped_image(image):
    # image=cv2.imread(image)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        face_image=cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_color=face_image[y:y+h,w:w+x]
    return roi_color



def classify(image):

    global __model
    classes=['Male','Female']
    cropped=get_cropped_image(image)
    resize_img = cv2.resize(cropped,(224, 224))
    scale=resize_img/255
    Final=scale.reshape(1,224,224,3)

    pred=__model.predict(Final)
    threshold=0.5
    prediction=[1 if pred > threshold else 0]

    return classes[prediction[0]],pred



if __name__ == "__main__":
    # Load_Saved_Artifects()
    pass
    