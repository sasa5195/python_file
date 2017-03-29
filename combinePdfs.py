import PyPDF2, os

pdfFiles = []
for filename in os.listdir('C:/Users/sbaid/Documents/Books'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()
f=open("C:/Users/sbaid/Documents/Books/manifest_all_in_one.txt","w")
tbl_hdr="FileName".center(100)+" "+"Page".center(100)
f.write(tbl_hdr+"\n")
r=1
for filename in pdfFiles:
    pdfFileObj = open('C:/Users/sbaid/Documents/Books/'+filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    f.write(filename.center(100)+" "+str(r).center(100)+"\n")
    r=r+pdfReader.numPages
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
f.close()
pdfOutput = open('C:/Users/sbaid/Documents/Books/all_in_one.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
