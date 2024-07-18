import requests
from bs4 import BeautifulSoup
import os
import io
from PIL import Image
url="https://www.google.com/search?sca_esv=d925498cb48557f7&sca_upv=1&sxsrf=ADLYWIKk7zpmlr5-eCLvHo6wISkmCvqFZQ:1720968231634&q=polar+bear+cubs&uds=ADvngMgryM7dRxzrsE7kfc2eLe79yUyU83sNJ0npS5frZ5kvRoKsIOOxdgvevKSC6aHebhlcrWcXCbBIIfVEqf96_OvSPpgRwM4bGJvze_wPLBLjLrDrudaAG9G-h7bhpZFlNCTjxg6r&udm=2&sa=X&ved=2ahUKEwjn1vag4qaHAxUZTaQEHRvfDN8QxKsJegUIowEQAQ&ictx=0&biw=1366&bih=641&dpr=1"

r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')

images=soup.find_all('img')

links=[]
for img in images:
    links.append(img['src'])
new_l=links[1:] 

def download_image(download_path,url_list,file_name):
    count=81
    for url in url_list:
        image_content=requests.get(url).content
        image_file=io.BytesIO(image_content)
        image=Image.open(image_file)

        file_path=download_path+file_name +str(count)+".jpg"

        with open(file_path,"wb") as f:
            image.save(f,"JPEG")
        count+=1
download_image("./bear",new_l,"/bear")

# im_url=new_l[4]
# image_content=requests.get(im_url).content
# image_file=io.BytesIO(image_content)
# image=Image.open(image_file)
# file_path="./cat"+"/p.jpg"

# with open(file_path,"wb") as f:
#     image.save(f,'JPEG')
