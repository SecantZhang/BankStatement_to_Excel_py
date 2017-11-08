import os
import re
import PyPDF2

fileDirectory = 'C:\Users\Wilson Zhang\Google Drive\Projects\Python\Manipulating with pdf'
fileName = 'Sep-Oct PNC Statement.pdf'
#get directory path and file names.
date = {'Start_month': 9, 'start_day': 14, 'end_month': 10, 'end_day': 12}
os.chdir(fileDirectory)
pdfFileObj = open(fileDirectory + '\' + fileName, 'rb')
#embed the file directory into the pdf PyPDF2 function
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
Page_number = pdfReader.numPages
#get page number in Page_number variable.
if not os.path.exists(fileDirectory + '/Output_Folder'):
    os.makedirs(fileDirectory + '/Output_Folder')
    #create output folder if it doesn't exist;
i = 1
pdf_lists = []
spent_part_data = []
for i in range(Page_number):
    pageObj = pdfReader.getPage(i)
    pdf_lists.append(pageObj.extractText())
    #get the according page text to the pdf_lists list.
    spent_part_data.append(re.search('DateAmountDiscription (.*?) Banking/Check'))
    if not pdf_lists:
        print('pdf_lists list is empty') #check if the list is empty.
    else:
        dateNumRegex = re.compile(r'(?<=\d\d\/\d\d).*?(?=\d\d\/\d\d)')
        extracted_data = dateNumRegex.findall(spent_part_data[i-1])
        print(mo)
    i = i + 1
