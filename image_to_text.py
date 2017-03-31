#from PIL import Image
#from pytesseract import image_to_string

#print image_to_string(Image.open('test.png'))
#print image_to_string(Image.open('test.png'), lang='eng')
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("test.png") # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.png')
text = pytesseract.image_to_string(Image.open('temp2.png'))
print(text)
