import pandas as pd
import cv2
import deepdish as dd

##################################################################################
#INCREASE DEFAULT COLUMN VISIBILITY
desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 26)
pd.set_option('display.max_rows', 100)

##################################################################################

imgPath = './Data/emilfine2.jpg'
img_gray = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
# exp_img_gray = np.expand_dims(img_gray, axis=2)

dict = {'ID': "Img ID",
          'ImgData': img_gray,
          'MetaData': {
            'Text Options': "Say Hi"
          }}

dd.io.save('C:/Users/efine/PycharmProjects/dataanalysis/Data/test2.h5', dict)

dictload = dd.io.load('C:/Users/efine/PycharmProjects/dataanalysis/Data/test2.h5')


cv2.imshow("Image", dictload['ImgData'])
cv2.waitKey(0)
cv2.destroyAllWindows()