import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

img_path = 'C:/Users/PC/Desktop/sh_hackathon/image/receipt_nh.jpg'
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# lang='kor' 설정 추가
text = pytesseract.image_to_string(thresh, lang='kor+eng')

for i, line in enumerate(text.splitlines()):
    print(f"{i+1:02d}: {line.strip()}")
