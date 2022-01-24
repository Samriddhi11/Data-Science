from pdf2jpg import pdf2jpg
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import cv2
import re
inputpath = r"C:\\Users\\sschi\\Documents\\Data Science\\2-converted.pdf"
outputpath = r"C:\\Users\\sschi\\Documents\\Data Science"
result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, dpi=300, pages="ALL")
img=cv2.imread(r"C:\\Users\\sschi\\Documents\\Data Science\\2-converted.pdf_dir\\0_2-converted.pdf.jpg" )
text= pytesseract.image_to_string(img)
text= text.replace(',','')
pattern = re.findall(r"[-+]?\d*\.\d+|\d+",text)
float_nos =[]
bill=0
for i in pattern:
    if('.' in i):
        float_nos.append(float(i))
float_nos=sorted(float_nos)
bill= float_nos[len(float_nos)-1]
print(bill)
