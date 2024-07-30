import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import cv2
import pathlib
import tensorflow as tf
from tensorflow import keras
import tensorflow_hub as hub
import PIL
from PIL import Image


__model=None

def load_save_artifects():
    global __model
    print("Loading Save Artifects ---- Start")
    if __model == None:
      __model=keras.models.load_model("my_model.keras")
    print("Loading Save Artifects ---- Done")

def clasify(path):
   global __model
   pathli=pathlib.Path(path)
   img=cv2.imread(str(pathli))
   img_res=cv2.resize(img,(224,224,))
   img_sc=img_res/255
   image=img_sc.reshape(1,224,224,3)
   pred=np.argmax(__model.predict(image))
   return pred

if __name__ == "__main__":
   pass