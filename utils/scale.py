import os 
import cv2 as cv 

currentDir = os.getcwd()
imagePath = os.path.join(currentDir, 'images')

def preprocess(imageArray):
    imageArray = cv.resize(imageArray, (250, 250))
    return imageArray


for i in os.listdir(imagePath):
    imageArray = cv.imread(os.path.join(imagePath, i))
    if 'scaleImages' not in os.listdir(currentDir):
        os.mkdir('scaleImages')
    scaledImage = preprocess(imageArray)
    cv.imwrite('scaleImages/{}'.format(str(i)), scaledImage)
    
