import os
import re
import PyPDF2

# "writetofile" function for writting extracted data to 'extracted_data.txt'
def writetofile(extracted_data, ext_date,i):
    outputFileDir = fileDirectory + '/Output_Folder/'
    if i == 1:
        open_txt_file = open(outputFileDir + 'extracted_data.txt','w')
        #first page: earse all the datas and overwrite them.
    else:
        open_txt_file = open(outputFileDir + 'extracted_data.txt','a')
        #second or after pages: append the text
    c = 0
    for c in range(len(extracted_data)):
        open_txt_file.write(ext_date[c] + ' ' + extracted_data[c] + '\n')
        c = c + 1
    open_txt_file.close()
    return True

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
if not os.path.exists(fileDirectory + '/Output_Folder'):
    os.makedirs(fileDirectory + '/Output_Folder')
    #create output folder if it doesn't exist;
i = 1
pdf_lists = []
for i in range(Page_number):
    pageObj = pdfReader.getPage(i)
    pdf_lists.append(pageObj.extractText())
    #get the according page text to the pdf_lists list.
    if not pdf_lists:
        print('pdf_lists list is empty') #check if the list is empty.
    else:
        spent_part_data = re.findall(r'DateAmountDescription(.*?)Banking/Check',pdf_lists[i-1])
        dateRegex = re.compile(r'(\d\d\/\d\d)')
        ext_date = dateRegex.findall(str(spent_part_data))
        dateNumRegex = re.compile(r'(?<=\d\d\/\d\d).*?(?=\d\d\/\d\d)')
        extracted_data = dateNumRegex.findall(str(spent_part_data))
        if writetofile(extracted_data, ext_date, i):
            print('Page ' + str(i) + ' Successfully Outputted.')
        else:
            print('Page ' + str(i) + ' Failed.')
    i = i + 1
