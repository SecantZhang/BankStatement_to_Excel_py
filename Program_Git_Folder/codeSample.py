import os
import re
import PyPDF2

fileDirectory = '/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf'
fileName = 'Sep-Oct PNC Statement.pdf'
#get directory path and file names.
date = {'Start_month': 9, 'start_day': 14, 'end_month': 10, 'end_day': 12}
os.chdir(fileDirectory)
pdfFileObj = open(fileDirectory + '/' + fileName, 'rb')
#embed the file directory into the pdf PyPDF2 function
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
Page_number = pdfReader.numPages
#get page number in Page_number variable.
i = 1
pageObj = pdfReader.getPage(i)
pdf_lists = pageObj.extractText()
    #get the according page text to the pdf_lists list.
if not pdf_lists:
    print('pdf_lists list is empty') #check if the list is empty.
else:
    #create the output folder
    dateNumRegex = re.compile(r'(?<=\d\d\/\d\d).*?(?=\d\d\/\d\d)')
    mo = dateNumRegex.findall(pdf_lists)
    i = i + 1
    print(mo[10])
