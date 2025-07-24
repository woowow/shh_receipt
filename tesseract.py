import cv2
import pytesseract
from PIL import Image
import numpy as np


# dpi check
def dpi_check(img):
    dpi = img.info.get('dpi', (72, 72))
    return dpi

# dpi modify
def dpi_modify(img_path, save_path):
    img = Image.open(img_path)
    exif = img.info.get('exif')
    img.save(save_path, dpi=(300, 300), exif=exif)


def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

#    img_path = 'C:/Users/PC/Desktop/sh_hackathon/image/receipt_nh.jpg'
    img_path = 'C:/Users/SSAFY/Desktop/shh_receipt/image/receipt_hd.jpg'

    save_path = 'C:/Users/SSAFY/Desktop/shh_receipt/image/receipt_hd_dpi_300.jpg'


    # 정확도 향상을 위한 grayscale 변환, 이진화 작업
    img = cv2.imread(img_path)
#    img = cv2.imread(save_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]



    custom_config = (
        r'--oem 3 --psm 6 -c load_system_dawg=0 -c load_freq_dawg=0'
        r'tessedit_load_sublangs=1 '
#        r'--oem 3 --psm 6 -c tessedit_load_sublangs=1 '
        r'-c user_words=./word_list.txt'
        r'tessedit_char_whitelist=가맹점상호명금액합계상품카드현금QWERTYUIOPASDFGHJKLZXCVBNM0123456789₩'
    )
#    text = pytesseract.image_to_string(img, lang='kor+eng', config=custom_config)
    text = pytesseract.image_to_string(thresh, lang='kor+eng', config=custom_config)



    for i, line in enumerate(text.splitlines()):
        print(f"{i+1:02d}: {line.strip()}")


if __name__ == "__main__":
    main()
