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
def addRec(imgList):
    imagechoice = int(input("Which image would you like to add a recommendation to?: [enter image ID #] ").strip())-1
    imgList[imagechoice]['MetaData']['Recommendations'].append(input("Enter your recommendation: ").strip())
    imgList[imagechoice]['MetaData']['Users'].append(input("Enter your ID: ").strip())
    save(imgList)
    return imgList

# SAVE in H5F Format
def save(imgList):
    dd.io.save('./Data/test3.h5', imgList)

# LOAD
def load():
    return dd.io.load('./Data/test3.h5')

# ADD IMAGE
def addImg(imgList):

    #  ./Data/emilfine2.jpg
    #  ./Data/test.jpg

    imgPath = input("Enter Path: ")
    img_gray = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE) # Load Image in Grayscale
    id = len(imgList)+1
    imgList.append({
        'ID': id,
        'Label': imgPath,
        'ImgData': img_gray,
        'MetaData': {
            'Recommendations': [],
            'Users': []
         }
    })
    save(imgList)
    return imgList

def showImg(imgData):
    cv2.imshow("Image", imgData)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

##################################################################################
# MAIN


imgList = load()

if input("Add new image? y/n: ").lower() == 'y'.strip():
    imgData = addImg(imgList)
print()

if input("See image options? y/n: ").lower() == 'y'.strip():
    for x in imgList:
        print(x['Label'], x['ID'])
    print()
    imagechoice = int(input("Which image would you like to see?: [enter ID #] ").strip())-1
    showImg(imgList[imagechoice]['ImgData'])
print()

if input("Would you like to add recommendation? y/n: ").lower() == 'y'.strip():
    imgList = addRec(imgList)
print()

##################################################################################
# # RESET ORIGINAL DATASET STRUCTURE

# imgPath = './Data/emilfine2.jpg'
# img_gray = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE) # Load Image in Grayscale
#
# imgList = [{'ID': 1,
#             'Label': "Emil Fine Image",
#             'ImgData': img_gray,
#             'MetaData': {
#                 'Recommendations': [],
#                 'Users': []
#                         }}
#                 ]
#
# save(imgList)
##################################################################################

# TO DO
# Confirm link works
# Resize if necessary