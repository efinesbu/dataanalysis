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

# if input("Add new image? y/n: ").lower() == 'y'.strip():
#     imgData = addImg(dict)

if input("See image options? y/n: ").lower() == 'y'.strip():
    print(dict['MetaData']['Label'])
    imagechoice = input("Which image would you like to see?: [enter index, from 0] ")
    cv2.imshow("image", dict['ImgData'][int(imagechoice)])
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    # addRec(dict)

##################################################################################
# # # RESET ORIGINAL DATASET
#
# imgPath = './Data/emilfine2.jpg'
# img_gray = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE) # Load Image in Grayscale
#
# dict = {'IDs': [1],
#         'ImgData': [img_gray],
#         'MetaData': {
#                 'Recommendations': ["Say Hi"],
#                 'Users': ["Advisor"],
#                 'Label': ["Emil Fine Image"]
#           }}
# save(dict)
##################################################################################

# dictload = load()
#
# # Add New Recommendation
# addRec(dictload)

# Parse data
# cv2.imshow("Image", dictload['ImgData'])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
