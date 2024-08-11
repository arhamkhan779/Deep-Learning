import streamlit as st
from PIL import Image
from util import classify
from util import Load_Saved_Artifects
import tensorflow  as tf
from tensorflow import keras
import numpy as np
import base64
import cv2



Load_Saved_Artifects()
st.markdown("# AI Based Gender Recognition System")

img=Image.open("man.png")
img2=Image.open("woman.png")
st.image([img,img2,img],width=200,) 
st.markdown("### Please Upload A Image")


file=st.file_uploader(' ',type=['jpg','png','jpeg'])

if file is not None:
    image=Image.open(file).convert("RGB")
    img_array = np.array(image)
    img=image.resize((224,224))
    st.image(img,width=500)
    name,score=classify(img_array)
    
    st.markdown(f"## Gender: {name}")
    st.markdown(f"## Prediction Score: {score}")