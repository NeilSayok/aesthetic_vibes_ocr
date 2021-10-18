import cv2 
import pytesseract
import os
import re

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

pattern = re.compile("AESTHETIC VIBES", re.IGNORECASE)

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
custom_config = r'--oem 3 --psm 6'

with open("readme.md","w") as fh:

    fh.write("|Serial No.|Text|Image|File Name\n")
    fh.write("|:----------:|:----------------------:|:-------------------:|:-------------------:|\n")

    c = 1
    for f in sorted_alphanumeric(os.listdir("aesthetic_o_vibes")):

        img = cv2.imread(f'F:\\FFOutput\\aesthetic_o_vibes\\{f}')
        img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
        s = pytesseract.image_to_string(img, config=custom_config).replace("\n","<br>")
        s = pattern.sub("", s)
        s = s.replace("|","I")

        print(f"Writing details of image {f}")
        fh.write(f'|{c}|<p>{s}</p>|<img src="aesthetic_o_vibes\\{f}" width="50%" height="auto">|{f}\n')
        c += 1
        # if c == 5:
        #     break
