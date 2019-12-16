import pandas as pd
import cv2
import deepdish as dd
import numpy as np

##################################################################################
#INCREASE DEFAULT COLUMN VISIBILITY
desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 25)
pd.set_option('display.max_rows', 40)

##################################################################################
#FUNCTIONS

#Add New Recommendation
def addRec(dict):
    rec = input("Add new recommendation: ")
    dict['MetaData']['Recommendations'].append(rec)
    print(dict['MetaData']['Recommendations'])

# SAVE in H5F Format
def save(dict):
    dd.io.save('./Data/test2.h5', dict)

# LOAD
def load():
    return dd.io.load('./Data/test2.h5')

# ADD IMAGE
def addImg(dict):

    # imgPath = './Data/emilfine2.jpg'
    imgPath = input("Enter Path: ")
    img_gray = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE) # Load Image in Grayscale
    id = len(dict['IDs'])+1
    dict['IDs'].append(id)
    dict['ImgData'].append(img_gray)
    dict['MetaData']['Recommendations'] = []
    dict['MetaData']['Users'] = []
    dict['MetaData']['Label'].append(imgPath)
    save(dict)
    return dict


##################################################################################
# MAIN

dict = load()

if input("Add image? Yes/No: ") == 'Yes':
    imgData = addImg(dict)


# # Reset original dataset
# imgPath = './Data/emilfine2.jpg'
# img_gray = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE) # Load Image in Grayscale
#
# dict = {'IDs': [1],
#         'ImgData': [img_gray],
#         'MetaData': {
#                 'Recommendations': ["Say Hi"],
#                 'Users': ["User Name"],
#                 'Label': []
#           }}
# save(dict)


# dictload = load()
#
# # Add New Recommendation
# addRec(dictload)

# Parse data
# cv2.imshow("Image", dictload['ImgData'])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
