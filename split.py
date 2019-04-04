import sys      #Enable system functionality
import PyPDF2   #Enable PDF functionality
import datetime #Enable date and time functionality

gendate = (datetime.datetime.now()).strftime('%Y%m%d-%H%M%S') #set the date and time the files are generated

file1 = str(sys.argv[1]) #get the file name from the first argument

pdf1 = open(file1, 'rb') #set the open file as pdf1

pdf1Reader = PyPDF2.PdfFileReader(pdf1)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    singlepage = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(singlepage)
    pdfOutputFile = open(str(int(pageNum+1)) + '-' + gendate + '.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdfWriter = PyPDF2.PdfFileWriter() #Clear var so you get only 1 page each time