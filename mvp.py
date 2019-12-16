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

# ADD NEW RECOMMENDATION
def addRec(dict):
    dict['MetaData'][int(imagechoice)-1]['Recommendations'].append(input("Enter your recommendation: "))
    dict['MetaData'][int(imagechoice) - 1]['Recommendations'].append(input("Enter your ID: "))
    save(dict)

# SAVE in H5F Format
def save(dict):
    dd.io.save('./Data/test2.h5', dict)

# LOAD
def load():
    return dd.io.load('./Data/test2.h5')

# ADD IMAGE
def addImg(dict):

    #  ./Data/emilfine2.jpg
    #  ./Data/test.jpg

    imgPath = input("Enter Path: ")
    img_gray = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE) # Load Image in Grayscale
    id = len(dict['IDs'])+1
    dict['IDs'].append(id)
    dict['ImgData'].append(img_gray)
    # dict['MetaData']['Recommendations'] = []
    # dict['MetaData']['Users'] = []
    dict['Label'].append(imgPath)
    save(dict)
    return dict

def showImg(imgData):
    cv2.imshow("Image", imgData)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

##################################################################################
# MAIN

dict = load()

# print(dict['IDs'])
# print(dict['MetaData'])
# print(dict['Label'])
# print(dict['MetaData'][0])

# if input("Add new image? y/n: ").lower() == 'y'.strip():
#     imgData = addImg(dict)

# if input("See image options? y/n: ").lower() == 'y'.strip():
#     print(dict['Label'], '\n', dict['IDs'])
#     imagechoice = input("Which image would you like to see?: [enter ID #] ")
#     showImg(dict['ImgData'][int(imagechoice)-1])

if input("Would you like to add recommendation? y/n: ").lower() == 'y'.strip():
    imagechoice = input("Which image would you like to add a recommendation to?: [enter image ID #] ")
    addRec(dict)



##################################################################################
# # RESET ORIGINAL DATASET

# imgPath = './Data/emilfine2.jpg'
# img_gray = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE) # Load Image in Grayscale
#
# dict = {'IDs': [1],
#         'Label': ["Emil Fine Image"],
#         'ImgData': [img_gray],
#         'MetaData': [{
#                 'Recommendations': ["Some Text"],
#                 'Users': ["Advisor ID"]
#
#           }]}
# save(dict)
##################################################################################
