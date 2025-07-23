import cv2
import pytesseract
from PIL import Image
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

img_path = 'C:/Users/PC/Desktop/sh_hackathon/image/receipt_nh.jpg'

img1 = Image.open(img_path)
fixed_dpi_path = "C:/Users/PC/Desktop/sh_hackathon/image/receipt_hd_300dpi.jpg"
img1.save(fixed_dpi_path, dpi=(300, 300))

img = cv2.imread(fixed_dpi_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]


custom_config = (
    r'--oem 3 --psm 6 -c load_system_dawg=0 -c load_freq_dawg=0'
    r'-c tessedit_load_sublangs=1 '
    r'-c user_words=./word_list.txt'
    r'-c tessedit_char_whitelist=가나다라마바사0123456789₩'
)

text = pytesseract.image_to_string(thresh, lang='kor+eng', config=custom_config)



for i, line in enumerate(text.splitlines()):
    print(f"{i+1:02d}: {line.strip()}")
