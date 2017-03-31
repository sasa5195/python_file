Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
====================== RESTART: C:/Python27/project.py ======================
1280
>>> 
====================== RESTART: C:/Python27/project.py ======================
1280
>>> 
====================== RESTART: C:/Python27/project.py ======================

Traceback (most recent call last):
  File "C:/Python27/project.py", line 11, in <module>
    st= bytes(s, 'utf-8')
TypeError: str() takes at most 1 argument (2 given)
>>> 
====================== RESTART: C:/Python27/project.py ======================
>>> hash("sahil")
1833260178
>>> 
================= RESTART: C:/Python27/bytearray_to_image.py =================

Traceback (most recent call last):
  File "C:/Python27/bytearray_to_image.py", line 3, in <module>
    import Image
ImportError: No module named Image
>>> import Image

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import Image
ImportError: No module named Image
>>> import image
>>> 
================= RESTART: C:/Python27/bytearray_to_image.py =================

Traceback (most recent call last):
  File "C:/Python27/bytearray_to_image.py", line 12, in <module>
    image = image.open(io.BytesIO(bytes))
AttributeError: 'module' object has no attribute 'open'
>>> import PIL
>>> 
================= RESTART: C:/Python27/bytearray_to_image.py =================
>>> import pypdf2

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    import pypdf2
ImportError: No module named pypdf2
>>> import PyPDF2
>>> dir(PyPDF2)
['PageRange', 'PdfFileMerger', 'PdfFileReader', 'PdfFileWriter', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', '__version__', '_version', 'filters', 'generic', 'merger', 'pagerange', 'parse_filename_page_ranges', 'pdf', 'utils']
>>> 
================= RESTART: C:/Python27/bytearray_to_image.py =================
>>> 
================= RESTART: C:/Python27/bytearray_to_image.py =================
>>> hash("sahil",16)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    hash("sahil",16)
TypeError: hash() takes exactly one argument (2 given)
>>> a=12978845872201336276964580418345643041114028253719021902337103292577461706126680445144232843607674268433441931714851076719184927709687699853632058857408691371481511956735910336732863085268235343149976708400670299905348401027334026593414622578897502492586208579736934803708520119924748719059352578778678371076170532277340661521081342890116847167695847642917699307797513161461051883857268848440548958478903382638889348968603578973148297562370625693709140269595798028867146965588410703489828461488715915971749494462269109920744644573648427839453141396788512463465613983826994274658164530882912429708652449059947795274621,156822987366672858512560809136094409244411982585224615979927833247226672539266758044031431453120237683744751063674157295402429589662791219200012191987619096783498213366010572290493991606163256970411008105592533908050219896958686300640144697744309758612879094632612068130513694941727888033575862517271904248779
>>> c=bin(a)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c=bin(a)
TypeError: 'tuple' object cannot be interpreted as an index
>>> bin(a)

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    bin(a)
TypeError: 'tuple' object cannot be interpreted as an index
>>> a='''12978845872201336276964580418345643041114028253719021902337103292577461706126680445144232843607674268433441931714851076719184927709687699853632058857408691371481511956735910336732863085268235343149976708400670299905348401027334026593414622578897502492586208579736934803708520119924748719059352578778678371076170532277340661521081342890116847167695847642917699307797513161461051883857268848440548958478903382638889348968603578973148297562370625693709140269595798028867146965588410703489828461488715915971749494462269109920744644573648427839453141396788512463465613983826994274658164530882912429708652449059947795274621,156822987366672858512560809136094409244411982585224615979927833247226672539266758044031431453120237683744751063674157295402429589662791219200012191987619096783498213366010572290493991606163256970411008105592533908050219896958686300640144697744309758612879094632612068130513694941727888033575862517271904248779'''
>>> a=int(a)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a=int(a)
ValueError: invalid literal for int() with base 10: '12978845872201336276964580418345643041114028253719021902337103292577461706126680445144232843607674268433441931714851076719184927709687699853632058857408691371481511956735910336732863085268235343149976'
>>> 
