import numpy as np
import matplotlib.pyplot as plt
import PIL
import urllib
from sklearn.cluster import KMeans
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import json

def retrieve_image_from_url(url):
    urllib.request.urlretrieve(url, 'working_img1.jpeg')
    
    img = cv2.imread('working_img1.jpeg')
    plt.imshow(img)
    
    
    #Since by default the open CV readsm the color in order of BGR instead of RGB, so lets convert it out to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #return the numpy 3d numpy array
    return img

def resize_img(img):
    #just to cready 12d array of Kmeans to accept this as parameter
    image = cv2.resize(img, (600, 400), interpolation = cv2.INTER_AREA)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    return image

def hex_val_color(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def find_dominant_color(counts,center_colors):
    max_color_pixel=0
    for i in counts.keys():
        if counts[i]>max_color_pixel:
            max_color_pixel=counts[i]
            pos=i
    return hex_val_color(center_colors[pos])

def find_border_color(img):
    height, width, colors = img.shape
    color=img[0][height//2]
    return hex_val_color(color)

def find_colors_img(img, clusters_num):
    r_img=resize_img(img)
    
    kmeans=KMeans(n_clusters = clusters_num)
    
    labels = kmeans.fit_predict(r_img)
    
    counts = Counter(labels)
    # sort to ensure correct color percentage
    counts = dict(sorted(counts.items()))
    
    center_colors = kmeans.cluster_centers_
    
    #find dominant color in image
    max_color=find_dominant_color(counts,center_colors)
    
    #find border color in image
    border_color=find_border_color(img)
    
    return max_color, border_color

def get_json_val(url):
    
    img=retrieve_image_from_url(url)
    max_color, border_color=find_colors_img(img, clusters_num=8)
    dict={'logo_border': border_color,'dominant_color': max_color}
    return dict


