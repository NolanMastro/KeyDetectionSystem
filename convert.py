import cv2
import pytesseract



def imageToText(path):
    #takes png or jpg * jpg could be 3x faster.
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # make greyscale
    image = cv2.GaussianBlur(image, (3,3), 0) # blur
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] #invert color

    return pytesseract.image_to_string(image, lang='eng', config='--psm 6')


    


    

