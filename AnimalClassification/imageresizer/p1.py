from PIL import Image
import os,shutil

def resize(im):
    resize_image=im.resize((140,140))
    return resize_image

files=os.listdir("./dataset/lion")
path="./dataset/lion"
new_path=f"{path}/cropped_lion"

count=1
for file in files:
    im=Image.open(f"{path}/{file}")

    im_resize=resize(im)
    if  os.path.exists(new_path):
        file_path=f"{path}/cropped_lion/lion{count}.jpg"

        im_resize.save(file_path)

        count+=1
    else:
        os.mkdir(new_path)
        