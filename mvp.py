import pandas as pd
import cv2
import deepdish as dd

##################################################################################
#INCREASE DEFAULT COLUMN VISIBILITY
desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 25)
pd.set_option('display.max_rows', 40)

##################################################################################

imgPath = './Data/emilfine2.jpg'
img_gray = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE) # Load Image in Grayscale

# Create data structure
dict = {'ID': 1,
        'ImgData': img_gray,
        'MetaData': {
                'Recommendation': "Say Hi",
                'User': "User Name"
          }}

# Save data in H5f foromat
dd.io.save('C:/Users/efine/PycharmProjects/dataanalysis/Data/test2.h5', dict)

# Load data
dictload = dd.io.load('./Data/test2.h5')

a = dictload
print(a)

# Parse data
# cv2.imshow("Image", dictload['ImgData'])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
