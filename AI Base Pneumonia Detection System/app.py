import streamlit as st
from PIL import Image
import cv2
import tensorflow as tf
from tensorflow import keras
import numpy as np
import util as ut
from util import classify

ut.load_saved_artifects()
page_bg_img='''
<style>
[data-testid="stAppViewContainer"] {
background-image: url(https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg?cs=srgb&dl=pexels-jplenio-1103970.jpg&fm=jpg);
background-size: cover;
);
}

</style>
'''
st.markdown(page_bg_img,unsafe_allow_html=True)
st.markdown("# AI Automated Pneumonia Detection System")

file=st.file_uploader(label='Upload a Picture',type=['png','jpg','jpeg'])

if file is not None:
    image=Image.open(file).convert('RGB')
    img_array=np.array(image)
    st.image(image,width=300)

    pred_list=classify(img_array)

    score=pred_list[0]
    label=pred_list[1]

    st.markdown(f"## Results : {label}")
    st.markdown(f"## Results Score : {score}")