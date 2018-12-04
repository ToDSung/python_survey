import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'E://Program Files (x86)/Tesseract-OCR/tesseract.exe'

image = Image.open(r".\HelloWorld.png")
text = pytesseract.image_to_string(image)
print(text)