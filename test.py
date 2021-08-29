import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('c812598eb7689b0817c7b798957ae01c.jpg')

text = pytesseract.image_to_string(img, lang='fas')
print(text)
