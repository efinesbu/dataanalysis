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

def save(dict):
    dd.io.save('C:/Users/efine/PycharmProjects/dataanalysis/Data/test2.h5', dict)

def load():
    return dd.io.load('./Data/test2.h5')

##################################################################################

imgPath = './Data/emilfine2.jpg'
img_gray = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE) # Load Image in Grayscale
# ex = np.expand_dims(img_gray, axis=2)
# Create data structure
dict = {'IDs': [1],
        'ImgData': [img_gray],
        'MetaData': {
                'Recommendations': ["Say Hi"],
                'Users': ["User Name"]
          }}

# Save data in H5f format
save(dict)
dictload = load()


# Add New Recommendation
addRec(dictload)

# Parse data
# cv2.imshow("Image", dictload['ImgData'])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
