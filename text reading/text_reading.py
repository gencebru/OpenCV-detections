from PIL import Image
import pytesseract

im = Image.open("text.png")
text = pytesseract.image_to_string(im,lang="tur")
print(text)
