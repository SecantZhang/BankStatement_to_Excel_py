Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
import PyPDF2
>>> pdfFileObj = open('/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf', 'rb')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    pdfFileObj = open('/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf', 'rb')
IsADirectoryError: [Errno 21] Is a directory: '/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf'
>>> pdfFileObj = open('/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf', 'rb')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    pdfFileObj = open('/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf', 'rb')
IsADirectoryError: [Errno 21] Is a directory: '/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf'
>>> import os
>>> os.chdir('/Users/Michavillson/Google Drive/Projects/Python/')
>>> pdfFileObj = open('Manipulating with pdf/meetingminutes.pdf')
>>> pdfReader = pyPDF2.PdfFileReader(pdfFileObj)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    pdfReader = pyPDF2.PdfFileReader(pdfFileObj)
NameError: name 'pyPDF2' is not defined
>>> pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
PdfReadWarning: PdfFileReader stream/file object is not in binary mode. It may not be read correctly. [pdf.py:1079]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/PyPDF2/pdf.py", line 1084, in __init__
    self.read(stream)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/PyPDF2/pdf.py", line 1689, in read
    stream.seek(-1, 2)
io.UnsupportedOperation: can't do nonzero end-relative seeks
>>> pdfFileObj = open('Manipulating with pdf/meetingminutes.pdf', 'rb')
>>> pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
>>> pdfReader.numPages
19
>>> pageObj = pdfReader.getPage(0)
>>> pageObj.extractText()
'OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of \nMarch 7\n, 2014\n        \n     The Board of Elementary and Secondary Education shall provide leadership and \ncreate policies for education that expand opportunities for children, empower \nfamilies and communities, and advance Louisiana in an increasingly \ncompetitive glob\nal market.\n BOARD \n of ELEMENTARY\n and \n SECONDARY\n EDUCATION\n  '
>>> pageObj = pdfReader.getPage(1)
>>> pageObj.extractText()
' LOUISIANA STATE BOARD OF ELEMENTARY AND SECONDARY EDUCATION\n   MARCH 7, 2014\n  \n The Louisiana Purchase Room\n  Baton Rouge, LA\n   \n \n \nThe Louisiana State Board of Elementary and Secondary Education met in \nregular\n session on\n March 7, 2014\n, in the Louisiana Purcha\nse Room, located in the Claiborne \nBuilding in Baton Rouge, Louisiana.  The meeting was called to order at \n9:17 a.m.\n by \nBoard President \nChas Roemer\n and opened with a prayer by\n Ms. Terry Johnson, Bossier \nParish School System\n.  \nBoard members present were \nDr. Lottie Beebe, Ms. Holly Boffy, Mr. Jim Garvey, Mr.\n Jay \nGuillot, Ms.\n Carolyn Hill, Mr. Walter Lee, \nDr. Judith Miranti, \nMr. Chas Roemer\n, and \nMs. Jane Smith\n.  Ms. Connie Bradford\n and Ms. Kira Orange Jones were\n absent.\n  \nDr. Charlie Michel, Lafourche Parish Sch\nool System,\n led the Pledge of Allegiance.\n  Agenda\n Item 2.\n On motion of Mr. Garvey, seconded by Ms. Boffy, the Board approved the \nagenda, as printed and disseminated.\n (Schedule 1)\n  Agenda\n Item 3.\n On motion of Ms. Smith, seconded by Ms. Boffy, the Board app\nroved the \nminutes of January 15, 2014.\n  Agenda\n Item 4.\n Report by the State Superintendent of Education\n  State Superintendent of Education John White provided an update on the \nintense and increased support that the LDE is providing to teachers to \nassist wi\nth \nnew academic expectations.  The LDE has established the \nfollowing support structures:  \n(1) \nnetwork teams are working directly with \nsuperintendents; \n(2) \ndistrict planning teams and district planning guides \nhave been established in every district; and \n(3) teacher leader team\ns are\n doubling to 4,000 next year.  Sample test items are being released.  The \ncurriculum package for next year is being released.\n  Next year™s \nassessment guides will be produced in the following weeks.\n  '
>>> pdfFileObj = PyPDF2.pdfFileReader(open('Manipulating with pdf/
				       
SyntaxError: EOL while scanning string literal
>>> pdfFileObj = PyPDF2.pdfFileReader(open('Manipulating with pdf/encrypted.pdf','rb'))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    pdfFileObj = PyPDF2.pdfFileReader(open('Manipulating with pdf/encrypted.pdf','rb'))
AttributeError: module 'PyPDF2' has no attribute 'pdfFileReader'
>>> pdfReader = PyPDF2.PdfFileReader(open('Manipulated with pdf/encrypted.pdf','rb'))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    pdfReader = PyPDF2.PdfFileReader(open('Manipulated with pdf/encrypted.pdf','rb'))
FileNotFoundError: [Errno 2] No such file or directory: 'Manipulated with pdf/encrypted.pdf'
>>> os.chdir('/Users/Michavillson/Google Drive/Projects/Python/')
>>> pdfReader = PyPDF2.PdfFileReader(open('Manipulating with pdf/encrypted.pdf','rb'))
>>> pdfReader.isEncrypted
True
>>> pdfReader.decrypt('rosebud')
1
>>> pageObj = pdfReader.getPage(0)
>>> pageObj.extractText()
'OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of \nMarch 7\n, 2014\n        \n     The Board of Elementary and Secondary Education shall provide leadership and \ncreate policies for education that expand opportunities for children, empower \nfamilies and communities, and advance Louisiana in an increasingly \ncompetitive glob\nal market.\n BOARD \n of ELEMENTARY\n and \n SECONDARY\n EDUCATION\n  '
>>> pdfFileObj = open('Manipulating with pdf/Sep-Oct PNC Statement.pdf/','rb')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    pdfFileObj = open('Manipulating with pdf/Sep-Oct PNC Statement.pdf/','rb')
NotADirectoryError: [Errno 20] Not a directory: 'Manipulating with pdf/Sep-Oct PNC Statement.pdf/'
>>> pdfFileObj = open('Manipulating with pdf/Sep-Oct PNC Statement.pdf','rb')
>>> pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
>>> pdfReader.numPages
4
>>> pageObj = pdfReader.getPage(0)
>>> pageObj.extractText()
'Virtual Wallet Spend StatementPNC BankPrimary account number:60-1722-7081For the period09/14/2017to10/12/2017Number of enclosures:0ZHENG ZHANGFor 24-hour banking, and transaction or4701 COLLEGE DR MB 1097interest rate information, sign-on toERIE PA 16563-0001PNC Bank Online Banking at pnc.comFor customer service call 1-888-PNC-BANKMonday - Friday: 7 AM - 10 PM ETSaturday & Sunday: 8 AM - 5 PM ETPara servicio en espanol, 1-866-HOLA-PNCMoving?Please contact us at 1-888-PNC-BANKWrite to:  Customer ServicePO Box 609Pittsburgh, PA  15230-9738Visit us at pnc.comTDD terminal: 1-800-531-1648For hearing impaired clients onlyADDITIONAL DOCUMENTS ARE AVAILABLE FOR DIGITAL DELIVERYAdditional documents are eligible for digital delivery and will no longer be sent by US Mail for accountsthat have selected to have digital delivery of account servicing communications. The additional documentseligible for digital delivery are listed below. A complete list of all documents delivered online isavailable in the Online Documents tab within Online Banking. This list will be updated as additionaldocuments are made available. When a document is available to view we will notify you by sending an email tothe email address on file.> Inactive Status Notice (as of 6/17/17)> Automatic Check Renewal Notice (as of 10/21/17)Virtual Wallet Spend Account SummaryAccount number:60-1722-7081Overdraft ProtectionProvided By:   XXXXXX7102XXXXXX7129Overdraft Coverage- Your account is currentlyOpted-Out.ZHENG ZHANGBalance SummaryBeginningbalanceDeposits andother additionsChecks and otherdeductionsEndingbalance3,411.451,252.844,622.9641.33Average monthlybalanceChargesand fees603.391.53Transaction SummaryCheckspaid/withdrawalsCheck Card POSsigned transactionsCheck Card/BankcardPOS PIN transactions0539Total ATMtransactionsPNC Bank ATMtransactionsOther Bank ATMtransactions000Page 1 of '
>>> pageObj = pdfReader.getPage(1)
>>> pageObj.extractText()
"Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedActivity DetailDeposits and Other AdditionsThere were 7 Deposits and OtherAdditions totaling $1,252.84.DateAmountDescription09/2251.94Debit Card Credit Amazonprime Membershipamzn.com/pr WA10/02705.73Funds Transfer From Acct 601722710210/031.19Funds Transfer From Acct 601722710210/04134.02Funds Transfer From Acct 601722710210/0639.82Funds Transfer From Acct 601722710210/10182.80Funds Transfer From Acct 601722710210/12137.34Funds Transfer From Acct 6017227102Banking/Check Card Withdrawals and PurchasesThere were 9 Check Card/Bank cardPIN POS purchases totaling$339.95.There were 54 other BankingMachine/Check Card deductionstotaling $1,549.23.DateAmountDescription09/1439.689979 Debit Card Purchase Amazon MktplacePmts09/155.309979 Debit Card Purchase Kfc J625156  EriePA09/1857.199979 Debit Card Purchase Paypal *SephoraUSA09/1819.959979 Debit Card Purchase Paypal *CheggTxtbk09/187.309979 Debit Card Purchase McDonald'sF12018  Eri09/1863.599979 Recurring Debit Card Ea *Origin.Com09/1840.859979 Debit Card Purchase Sato RamenBuffalo NY09/186.47POS Purchase Maid Of The Mi Niagara FallNY09/186.009979 Debit Card Purchase NiagaraReservation Sp09/18136.969979 Debit Card Purchase CheesecakeBuffalo09/1838.70POS Purchase Sunoco 0573575 Angola NY09/193.359979 Debit Card Purchase Niagara Res StatePark09/196.589979 Debit Card Purchase Prospect Pointe09/1968.679979 Debit Card Purchase Ni HoowaSupermarket09/1916.009979 Debit Card Purchase Ni HoowaSupermarket09/1950.009979 Debit Card Purchase Psu Id+ Office09/1952.66POS Purchase Wal-Mart Super Erie PA09/2144.999979 Recurring Debit Card Twc*Time WrnrCable09/219.009979 Debit Card Purchase Laser Wash/ErieErie09/2151.949979 Recurring Debit Card AmazonprimeMembershi09/2219.009979 Debit Card Purchase Codeschool.Com09/2252.439979 Debit Card Purchase Peking ChineseRestaurBanking/Check Card Withdrawals and Purchases continued on next pagePage 2 of "
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py 
PdfReadWarning: PdfFileReader stream/file object is not in binary mode. It may not be read correctly. [pdf.py:1079]
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py", line 12, in <module>
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/PyPDF2/pdf.py", line 1084, in __init__
    self.read(stream)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/PyPDF2/pdf.py", line 1689, in read
    stream.seek(-1, 2)
io.UnsupportedOperation: can't do nonzero end-relative seeks
>>> import os
>>> import re
>>> import PyPDF2
>>> fileDirectory = '/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf'
>>> fileName = 'Sep-Oct PNC Statement.pdf'
>>> date = {'Start_month': 9, 'start_day': 14, 'end_month': 10, 'end_day': 12}
>>> os.chdir(fileDirectory)
>>> pdfFileObj = open(fileDirectory + '/' + fileName, 'rb')
>>> pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
>>> Page_number = pdfReader.numPages
>>> Page_number
4
>>> i = 0
>>> pdf_lists = None
>>> dateNumRegex = None
>>> for i in range(Page_number):
	pageObj = pdfReader.getPage(i)
	pdf_lists[i] = pageObj.extractText()
	if not pdf_lists:
		print('pdf_lists list is empty')
	else:
		os.makedirs(fileDirectory + '/Output_Folder')
		dateNumRegex = re.compile(r'\d\d/\d\d (.*) \d\d/\d\d')
		print('1')
		mo = dateNumRegex.findall(pdf_lists[i])
		print(mo.group())

		
Traceback (most recent call last):
  File "<pyshell#59>", line 3, in <module>
    pdf_lists[i] = pageObj.extractText()
TypeError: 'NoneType' object does not support item assignment
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py", line 18, in <module>
    pdf_lists[i] = pageObj.extractText()
NameError: name 'pdf_lists' is not defined
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py", line 19, in <module>
    pdf_lists[i] = pageObj.extractText()
IndexError: list assignment index out of range
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py", line 19, in <module>
    pdf_lists[i] = pageObj.extractText()
IndexError: list assignment index out of range
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py", line 18, in <module>
    pdf_lists[i] = pageObj.extractText()
IndexError: list assignment index out of range
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py", line 27, in <module>
    print(mo.group())
AttributeError: 'list' object has no attribute 'group'
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py", line 22, in <module>
    os.makedirs(fileDirectory + '/Output_Folder')
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/os.py", line 220, in makedirs
    mkdir(name, mode)
FileExistsError: [Errno 17] File exists: '/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Output_Folder'
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
Virtual Wallet Spend StatementPNC BankPrimary account number:60-1722-7081For the period09/14/2017to10/12/2017Number of enclosures:0ZHENG ZHANGFor 24-hour banking, and transaction or4701 COLLEGE DR MB 1097interest rate information, sign-on toERIE PA 16563-0001PNC Bank Online Banking at pnc.comFor customer service call 1-888-PNC-BANKMonday - Friday: 7 AM - 10 PM ETSaturday & Sunday: 8 AM - 5 PM ETPara servicio en espanol, 1-866-HOLA-PNCMoving?Please contact us at 1-888-PNC-BANKWrite to:  Customer ServicePO Box 609Pittsburgh, PA  15230-9738Visit us at pnc.comTDD terminal: 1-800-531-1648For hearing impaired clients onlyADDITIONAL DOCUMENTS ARE AVAILABLE FOR DIGITAL DELIVERYAdditional documents are eligible for digital delivery and will no longer be sent by US Mail for accountsthat have selected to have digital delivery of account servicing communications. The additional documentseligible for digital delivery are listed below. A complete list of all documents delivered online isavailable in the Online Documents tab within Online Banking. This list will be updated as additionaldocuments are made available. When a document is available to view we will notify you by sending an email tothe email address on file.> Inactive Status Notice (as of 6/17/17)> Automatic Check Renewal Notice (as of 10/21/17)Virtual Wallet Spend Account SummaryAccount number:60-1722-7081Overdraft ProtectionProvided By:   XXXXXX7102XXXXXX7129Overdraft Coverage- Your account is currentlyOpted-Out.ZHENG ZHANGBalance SummaryBeginningbalanceDeposits andother additionsChecks and otherdeductionsEndingbalance3,411.451,252.844,622.9641.33Average monthlybalanceChargesand fees603.391.53Transaction SummaryCheckspaid/withdrawalsCheck Card POSsigned transactionsCheck Card/BankcardPOS PIN transactions0539Total ATMtransactionsPNC Bank ATMtransactionsOther Bank ATMtransactions000Page 1 of 
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
[]
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py", line 26, in <module>
    print(mo.group())
AttributeError: 'list' object has no attribute 'group'
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py", line 26, in <module>
    print(mo.group())
AttributeError: 'NoneType' object has no attribute 'group'
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py", line 26, in <module>
    print(mo.group())
AttributeError: 'list' object has no attribute 'group'
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py", line 26, in <module>
    print(mo.group())
AttributeError: 'list' object has no attribute 'group'
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py", line 26, in <module>
    print(mo.group())
AttributeError: 'list' object has no attribute 'group'
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py", line 26, in <module>
    print(mo.group())
AttributeError: 'list' object has no attribute 'group'
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py", line 26, in <module>
    print(mo.group())
AttributeError: 'list' object has no attribute 'group'
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
['60', '17', '22', '70', '81', '09', '14', '20', '17', '10', '12', '20', '17', '24', '47', '01', '10', '97', '16', '56', '00', '01', '88', '10', '86', '88', '60', '15', '23', '97', '38', '80', '53', '16', '48', '17', '17', '10', '21', '17', '60', '17', '22', '70', '81', '71', '02', '71', '29', '41', '45', '25', '84', '62', '96', '41', '33', '60', '39', '53', '05', '39', '00']
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
['09/14', '10/12', '17/17', '10/21']
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
[]
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
[]
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
['09/14', '10/12', '09/22', '10/02', '10/03', '10/04', '10/06', '10/10', '10/12', '09/14', '09/15', '09/18', '09/18', '09/18', '09/18', '09/18', '09/18', '09/18', '09/18', '09/18', '09/19', '09/19', '09/19', '09/19', '09/19', '09/19', '09/21', '09/21', '09/21', '09/22', '09/22']
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py", line 23, in <module>
    dateNumRegex = re.compile(r'(?<=\d\d\/\d\d).*?(?=\d\d\/\d\d')
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/re.py", line 233, in compile
    return _compile(pattern, flags)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/re.py", line 301, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/sre_compile.py", line 562, in compile
    p = sre_parse.parse(p, flags)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/sre_parse.py", line 856, in parse
    p = _parse_sub(source, pattern, flags & SRE_FLAG_VERBOSE, False)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/sre_parse.py", line 415, in _parse_sub
    itemsappend(_parse(source, state, verbose))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/sre_parse.py", line 701, in _parse
    source.tell() - start)
sre_constants.error: missing ), unterminated subpattern at position 18
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
['/2017to', '/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedActivity DetailDeposits and Other AdditionsThere were 7 Deposits and OtherAdditions totaling $1,252.84.DateAmountDescription', '51.94Debit Card Credit Amazonprime Membershipamzn.com/pr WA', '705.73Funds Transfer From Acct 6017227102', '1.19Funds Transfer From Acct 6017227102', '134.02Funds Transfer From Acct 6017227102', '39.82Funds Transfer From Acct 6017227102', '182.80Funds Transfer From Acct 6017227102', '137.34Funds Transfer From Acct 6017227102Banking/Check Card Withdrawals and PurchasesThere were 9 Check Card/Bank cardPIN POS purchases totaling$339.95.There were 54 other BankingMachine/Check Card deductionstotaling $1,549.23.DateAmountDescription', '39.689979 Debit Card Purchase Amazon MktplacePmts', '5.309979 Debit Card Purchase Kfc J625156  EriePA', '57.199979 Debit Card Purchase Paypal *SephoraUSA', '19.959979 Debit Card Purchase Paypal *CheggTxtbk', "7.309979 Debit Card Purchase McDonald'sF12018  Eri", '63.599979 Recurring Debit Card Ea *Origin.Com', '40.859979 Debit Card Purchase Sato RamenBuffalo NY', '6.47POS Purchase Maid Of The Mi Niagara FallNY', '6.009979 Debit Card Purchase NiagaraReservation Sp', '136.969979 Debit Card Purchase CheesecakeBuffalo', '38.70POS Purchase Sunoco 0573575 Angola NY', '3.359979 Debit Card Purchase Niagara Res StatePark', '6.589979 Debit Card Purchase Prospect Pointe', '68.679979 Debit Card Purchase Ni HoowaSupermarket', '16.009979 Debit Card Purchase Ni HoowaSupermarket', '50.009979 Debit Card Purchase Psu Id+ Office', '52.66POS Purchase Wal-Mart Super Erie PA', '44.999979 Recurring Debit Card Twc*Time WrnrCable', '9.009979 Debit Card Purchase Laser Wash/ErieErie', '51.949979 Recurring Debit Card AmazonprimeMembershi', '19.009979 Debit Card Purchase Codeschool.Com']
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py", line 26, in <module>
    print(mo.group(1))
AttributeError: 'list' object has no attribute 'group'
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedActivity DetailDeposits and Other AdditionsThere were 7 Deposits and OtherAdditions totaling $1,252.84.DateAmountDescription
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/codeSample.py 
5.309979 Debit Card Purchase Kfc J625156  EriePA
>>> pageObj = pdfReader.getPage(1)
>>> print(pageObj.extractText())
Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedActivity DetailDeposits and Other AdditionsThere were 7 Deposits and OtherAdditions totaling $1,252.84.DateAmountDescription09/2251.94Debit Card Credit Amazonprime Membershipamzn.com/pr WA10/02705.73Funds Transfer From Acct 601722710210/031.19Funds Transfer From Acct 601722710210/04134.02Funds Transfer From Acct 601722710210/0639.82Funds Transfer From Acct 601722710210/10182.80Funds Transfer From Acct 601722710210/12137.34Funds Transfer From Acct 6017227102Banking/Check Card Withdrawals and PurchasesThere were 9 Check Card/Bank cardPIN POS purchases totaling$339.95.There were 54 other BankingMachine/Check Card deductionstotaling $1,549.23.DateAmountDescription09/1439.689979 Debit Card Purchase Amazon MktplacePmts09/155.309979 Debit Card Purchase Kfc J625156  EriePA09/1857.199979 Debit Card Purchase Paypal *SephoraUSA09/1819.959979 Debit Card Purchase Paypal *CheggTxtbk09/187.309979 Debit Card Purchase McDonald'sF12018  Eri09/1863.599979 Recurring Debit Card Ea *Origin.Com09/1840.859979 Debit Card Purchase Sato RamenBuffalo NY09/186.47POS Purchase Maid Of The Mi Niagara FallNY09/186.009979 Debit Card Purchase NiagaraReservation Sp09/18136.969979 Debit Card Purchase CheesecakeBuffalo09/1838.70POS Purchase Sunoco 0573575 Angola NY09/193.359979 Debit Card Purchase Niagara Res StatePark09/196.589979 Debit Card Purchase Prospect Pointe09/1968.679979 Debit Card Purchase Ni HoowaSupermarket09/1916.009979 Debit Card Purchase Ni HoowaSupermarket09/1950.009979 Debit Card Purchase Psu Id+ Office09/1952.66POS Purchase Wal-Mart Super Erie PA09/2144.999979 Recurring Debit Card Twc*Time WrnrCable09/219.009979 Debit Card Purchase Laser Wash/ErieErie09/2151.949979 Recurring Debit Card AmazonprimeMembershi09/2219.009979 Debit Card Purchase Codeschool.Com09/2252.439979 Debit Card Purchase Peking ChineseRestaurBanking/Check Card Withdrawals and Purchases continued on next pagePage 2 of 
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py", line 23, in <module>
    pdf_lists[i] = pageObj.extractText()
IndexError: list assignment index out of range
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py", line 21, in <module>
    pdf_lists[i] = pageObj.extractText()
NameError: name 'pdf_lists' is not defined
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py", line 25, in <module>
    spent_part_data.append(re.search('DateAmountDiscription (.*?) Banking/Check'))
TypeError: search() missing 1 required positional argument: 'string'
>>> 
=============================== RESTART: Shell ===============================
>>> import os
>>> import re
>>> import PyPDF2
>>> fileDirectory = '/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf'
>>> fileName = 'Sep-Oct PNC Statement.pdf'
>>> date = {'Start_month':9, 'Start_day':14, 'End_month':10, 'End_day':12}
>>> os.chdir(fileDirectory_)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    os.chdir(fileDirectory_)
NameError: name 'fileDirectory_' is not defined
>>> os.chdir(fileDirectory)
>>> pdfFileObj = open(fileDirectory + '\' + fileName, 'rb')
		  
SyntaxError: EOL while scanning string literal
>>> pdfFileObj = open(fileDirectory + '"\"' + fileName, 'rb')
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    pdfFileObj = open(fileDirectory + '"\"' + fileName, 'rb')
FileNotFoundError: [Errno 2] No such file or directory: '/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf""Sep-Oct PNC Statement.pdf'
>>> pdfFileObj - open(fileDirectory + '/' + fileName, 'rb')
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    pdfFileObj - open(fileDirectory + '/' + fileName, 'rb')
NameError: name 'pdfFileObj' is not defined
>>> pdfFileObj = open(fileDirectory + '/' + fileName, 'rb')
>>> pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
>>> page_number = pdfReader.numPages
>>> if not os.path.exists(fileDirectory + '/Output_Folder'):
	os.makedirs(fileDirectory + '/Output_Folder')

	
>>> i = 1
>>> pdf_lists = []
>>> spent_part_data = []
>>> pageObj = pdfReader.getPage(i)
>>> pdf_lists.append(pageObj.extractText())
>>> pdf_lists
["Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedActivity DetailDeposits and Other AdditionsThere were 7 Deposits and OtherAdditions totaling $1,252.84.DateAmountDescription09/2251.94Debit Card Credit Amazonprime Membershipamzn.com/pr WA10/02705.73Funds Transfer From Acct 601722710210/031.19Funds Transfer From Acct 601722710210/04134.02Funds Transfer From Acct 601722710210/0639.82Funds Transfer From Acct 601722710210/10182.80Funds Transfer From Acct 601722710210/12137.34Funds Transfer From Acct 6017227102Banking/Check Card Withdrawals and PurchasesThere were 9 Check Card/Bank cardPIN POS purchases totaling$339.95.There were 54 other BankingMachine/Check Card deductionstotaling $1,549.23.DateAmountDescription09/1439.689979 Debit Card Purchase Amazon MktplacePmts09/155.309979 Debit Card Purchase Kfc J625156  EriePA09/1857.199979 Debit Card Purchase Paypal *SephoraUSA09/1819.959979 Debit Card Purchase Paypal *CheggTxtbk09/187.309979 Debit Card Purchase McDonald'sF12018  Eri09/1863.599979 Recurring Debit Card Ea *Origin.Com09/1840.859979 Debit Card Purchase Sato RamenBuffalo NY09/186.47POS Purchase Maid Of The Mi Niagara FallNY09/186.009979 Debit Card Purchase NiagaraReservation Sp09/18136.969979 Debit Card Purchase CheesecakeBuffalo09/1838.70POS Purchase Sunoco 0573575 Angola NY09/193.359979 Debit Card Purchase Niagara Res StatePark09/196.589979 Debit Card Purchase Prospect Pointe09/1968.679979 Debit Card Purchase Ni HoowaSupermarket09/1916.009979 Debit Card Purchase Ni HoowaSupermarket09/1950.009979 Debit Card Purchase Psu Id+ Office09/1952.66POS Purchase Wal-Mart Super Erie PA09/2144.999979 Recurring Debit Card Twc*Time WrnrCable09/219.009979 Debit Card Purchase Laser Wash/ErieErie09/2151.949979 Recurring Debit Card AmazonprimeMembershi09/2219.009979 Debit Card Purchase Codeschool.Com09/2252.439979 Debit Card Purchase Peking ChineseRestaurBanking/Check Card Withdrawals and Purchases continued on next pagePage 2 of "]
>>> spent_part_data.append(re.search('DateAmountDiscription (.*?) Banking/Check'))
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    spent_part_data.append(re.search('DateAmountDiscription (.*?) Banking/Check'))
TypeError: search() missing 1 required positional argument: 'string'
>>> spent_part_data = re.compile(r'DateAmountDiscription (.*?) Banking/Check')
>>> mo = spent_part_data.findall(pdf_lists[0])
>>> mo
[]
>>> spent_part_data = re.compile(r'(?<=DateAmountDiscription).*?(?=Banking/Check)')
>>> mo = spent_part_data.findall(pdf_lists[0])
>>> mo
[]
>>> spent_part_data[0].append(re.compile(r'(?<=DateAmountDiscription).*?(?=Banking/Check)'))
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    spent_part_data[0].append(re.compile(r'(?<=DateAmountDiscription).*?(?=Banking/Check)'))
TypeError: '_sre.SRE_Pattern' object is not subscriptable
>>> pdf_lists
["Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedActivity DetailDeposits and Other AdditionsThere were 7 Deposits and OtherAdditions totaling $1,252.84.DateAmountDescription09/2251.94Debit Card Credit Amazonprime Membershipamzn.com/pr WA10/02705.73Funds Transfer From Acct 601722710210/031.19Funds Transfer From Acct 601722710210/04134.02Funds Transfer From Acct 601722710210/0639.82Funds Transfer From Acct 601722710210/10182.80Funds Transfer From Acct 601722710210/12137.34Funds Transfer From Acct 6017227102Banking/Check Card Withdrawals and PurchasesThere were 9 Check Card/Bank cardPIN POS purchases totaling$339.95.There were 54 other BankingMachine/Check Card deductionstotaling $1,549.23.DateAmountDescription09/1439.689979 Debit Card Purchase Amazon MktplacePmts09/155.309979 Debit Card Purchase Kfc J625156  EriePA09/1857.199979 Debit Card Purchase Paypal *SephoraUSA09/1819.959979 Debit Card Purchase Paypal *CheggTxtbk09/187.309979 Debit Card Purchase McDonald'sF12018  Eri09/1863.599979 Recurring Debit Card Ea *Origin.Com09/1840.859979 Debit Card Purchase Sato RamenBuffalo NY09/186.47POS Purchase Maid Of The Mi Niagara FallNY09/186.009979 Debit Card Purchase NiagaraReservation Sp09/18136.969979 Debit Card Purchase CheesecakeBuffalo09/1838.70POS Purchase Sunoco 0573575 Angola NY09/193.359979 Debit Card Purchase Niagara Res StatePark09/196.589979 Debit Card Purchase Prospect Pointe09/1968.679979 Debit Card Purchase Ni HoowaSupermarket09/1916.009979 Debit Card Purchase Ni HoowaSupermarket09/1950.009979 Debit Card Purchase Psu Id+ Office09/1952.66POS Purchase Wal-Mart Super Erie PA09/2144.999979 Recurring Debit Card Twc*Time WrnrCable09/219.009979 Debit Card Purchase Laser Wash/ErieErie09/2151.949979 Recurring Debit Card AmazonprimeMembershi09/2219.009979 Debit Card Purchase Codeschool.Com09/2252.439979 Debit Card Purchase Peking ChineseRestaurBanking/Check Card Withdrawals and Purchases continued on next pagePage 2 of "]
>>> pdf_lists[0]
"Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedActivity DetailDeposits and Other AdditionsThere were 7 Deposits and OtherAdditions totaling $1,252.84.DateAmountDescription09/2251.94Debit Card Credit Amazonprime Membershipamzn.com/pr WA10/02705.73Funds Transfer From Acct 601722710210/031.19Funds Transfer From Acct 601722710210/04134.02Funds Transfer From Acct 601722710210/0639.82Funds Transfer From Acct 601722710210/10182.80Funds Transfer From Acct 601722710210/12137.34Funds Transfer From Acct 6017227102Banking/Check Card Withdrawals and PurchasesThere were 9 Check Card/Bank cardPIN POS purchases totaling$339.95.There were 54 other BankingMachine/Check Card deductionstotaling $1,549.23.DateAmountDescription09/1439.689979 Debit Card Purchase Amazon MktplacePmts09/155.309979 Debit Card Purchase Kfc J625156  EriePA09/1857.199979 Debit Card Purchase Paypal *SephoraUSA09/1819.959979 Debit Card Purchase Paypal *CheggTxtbk09/187.309979 Debit Card Purchase McDonald'sF12018  Eri09/1863.599979 Recurring Debit Card Ea *Origin.Com09/1840.859979 Debit Card Purchase Sato RamenBuffalo NY09/186.47POS Purchase Maid Of The Mi Niagara FallNY09/186.009979 Debit Card Purchase NiagaraReservation Sp09/18136.969979 Debit Card Purchase CheesecakeBuffalo09/1838.70POS Purchase Sunoco 0573575 Angola NY09/193.359979 Debit Card Purchase Niagara Res StatePark09/196.589979 Debit Card Purchase Prospect Pointe09/1968.679979 Debit Card Purchase Ni HoowaSupermarket09/1916.009979 Debit Card Purchase Ni HoowaSupermarket09/1950.009979 Debit Card Purchase Psu Id+ Office09/1952.66POS Purchase Wal-Mart Super Erie PA09/2144.999979 Recurring Debit Card Twc*Time WrnrCable09/219.009979 Debit Card Purchase Laser Wash/ErieErie09/2151.949979 Recurring Debit Card AmazonprimeMembershi09/2219.009979 Debit Card Purchase Codeschool.Com09/2252.439979 Debit Card Purchase Peking ChineseRestaurBanking/Check Card Withdrawals and Purchases continued on next pagePage 2 of "
>>> spent_part_data.append(re.findall(r'DateAmountDescription(.*?)Banking/Check', pdf_lists[0]))
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    spent_part_data.append(re.findall(r'DateAmountDescription(.*?)Banking/Check', pdf_lists[0]))
AttributeError: '_sre.SRE_Pattern' object has no attribute 'append'
>>> spent_part_data = re.findall(r'DateAmountDescription(.*?)Banking/Check', pdf_lists[0])
>>> spent_part_data
['09/2251.94Debit Card Credit Amazonprime Membershipamzn.com/pr WA10/02705.73Funds Transfer From Acct 601722710210/031.19Funds Transfer From Acct 601722710210/04134.02Funds Transfer From Acct 601722710210/0639.82Funds Transfer From Acct 601722710210/10182.80Funds Transfer From Acct 601722710210/12137.34Funds Transfer From Acct 6017227102', "09/1439.689979 Debit Card Purchase Amazon MktplacePmts09/155.309979 Debit Card Purchase Kfc J625156  EriePA09/1857.199979 Debit Card Purchase Paypal *SephoraUSA09/1819.959979 Debit Card Purchase Paypal *CheggTxtbk09/187.309979 Debit Card Purchase McDonald'sF12018  Eri09/1863.599979 Recurring Debit Card Ea *Origin.Com09/1840.859979 Debit Card Purchase Sato RamenBuffalo NY09/186.47POS Purchase Maid Of The Mi Niagara FallNY09/186.009979 Debit Card Purchase NiagaraReservation Sp09/18136.969979 Debit Card Purchase CheesecakeBuffalo09/1838.70POS Purchase Sunoco 0573575 Angola NY09/193.359979 Debit Card Purchase Niagara Res StatePark09/196.589979 Debit Card Purchase Prospect Pointe09/1968.679979 Debit Card Purchase Ni HoowaSupermarket09/1916.009979 Debit Card Purchase Ni HoowaSupermarket09/1950.009979 Debit Card Purchase Psu Id+ Office09/1952.66POS Purchase Wal-Mart Super Erie PA09/2144.999979 Recurring Debit Card Twc*Time WrnrCable09/219.009979 Debit Card Purchase Laser Wash/ErieErie09/2151.949979 Recurring Debit Card AmazonprimeMembershi09/2219.009979 Debit Card Purchase Codeschool.Com09/2252.439979 Debit Card Purchase Peking ChineseRestaur"]
>>> spent_part_data.group(1)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    spent_part_data.group(1)
AttributeError: 'list' object has no attribute 'group'
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py", line 44, in <module>
    extracted_data = dateNumRegex.findall(spent_part_data)
TypeError: expected string or bytes-like object
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py", line 45, in <module>
    extracted_data = dateNumRegex.findall(spent_part_data)
TypeError: expected string or bytes-like object
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py", line 45, in <module>
    extracted_data.append(dateNumRegex.findall(spent_part_data))
TypeError: expected string or bytes-like object
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py", line 46, in <module>
    print(i + ' Page successfully wrote')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
0 Page successfully wrote
1 Page successfully wrote
2 Page successfully wrote
3 Page successfully wrote
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
[]
0 Page successfully wrote
[]
1 Page successfully wrote
[]
2 Page successfully wrote
[]
3 Page successfully wrote
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
[]
[]
0 Page successfully wrote
[]
[]
1 Page successfully wrote
[]
[]
2 Page successfully wrote
[]
[]
3 Page successfully wrote
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
Virtual Wallet Spend StatementPNC BankPrimary account number:60-1722-7081For the period09/14/2017to10/12/2017Number of enclosures:0ZHENG ZHANGFor 24-hour banking, and transaction or4701 COLLEGE DR MB 1097interest rate information, sign-on toERIE PA 16563-0001PNC Bank Online Banking at pnc.comFor customer service call 1-888-PNC-BANKMonday - Friday: 7 AM - 10 PM ETSaturday & Sunday: 8 AM - 5 PM ETPara servicio en espanol, 1-866-HOLA-PNCMoving?Please contact us at 1-888-PNC-BANKWrite to:  Customer ServicePO Box 609Pittsburgh, PA  15230-9738Visit us at pnc.comTDD terminal: 1-800-531-1648For hearing impaired clients onlyADDITIONAL DOCUMENTS ARE AVAILABLE FOR DIGITAL DELIVERYAdditional documents are eligible for digital delivery and will no longer be sent by US Mail for accountsthat have selected to have digital delivery of account servicing communications. The additional documentseligible for digital delivery are listed below. A complete list of all documents delivered online isavailable in the Online Documents tab within Online Banking. This list will be updated as additionaldocuments are made available. When a document is available to view we will notify you by sending an email tothe email address on file.> Inactive Status Notice (as of 6/17/17)> Automatic Check Renewal Notice (as of 10/21/17)Virtual Wallet Spend Account SummaryAccount number:60-1722-7081Overdraft ProtectionProvided By:   XXXXXX7102XXXXXX7129Overdraft Coverage- Your account is currentlyOpted-Out.ZHENG ZHANGBalance SummaryBeginningbalanceDeposits andother additionsChecks and otherdeductionsEndingbalance3,411.451,252.844,622.9641.33Average monthlybalanceChargesand fees603.391.53Transaction SummaryCheckspaid/withdrawalsCheck Card POSsigned transactionsCheck Card/BankcardPOS PIN transactions0539Total ATMtransactionsPNC Bank ATMtransactionsOther Bank ATMtransactions000Page 1 of 
[]
[]
0 Page successfully wrote
Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedActivity DetailDeposits and Other AdditionsThere were 7 Deposits and OtherAdditions totaling $1,252.84.DateAmountDescription09/2251.94Debit Card Credit Amazonprime Membershipamzn.com/pr WA10/02705.73Funds Transfer From Acct 601722710210/031.19Funds Transfer From Acct 601722710210/04134.02Funds Transfer From Acct 601722710210/0639.82Funds Transfer From Acct 601722710210/10182.80Funds Transfer From Acct 601722710210/12137.34Funds Transfer From Acct 6017227102Banking/Check Card Withdrawals and PurchasesThere were 9 Check Card/Bank cardPIN POS purchases totaling$339.95.There were 54 other BankingMachine/Check Card deductionstotaling $1,549.23.DateAmountDescription09/1439.689979 Debit Card Purchase Amazon MktplacePmts09/155.309979 Debit Card Purchase Kfc J625156  EriePA09/1857.199979 Debit Card Purchase Paypal *SephoraUSA09/1819.959979 Debit Card Purchase Paypal *CheggTxtbk09/187.309979 Debit Card Purchase McDonald'sF12018  Eri09/1863.599979 Recurring Debit Card Ea *Origin.Com09/1840.859979 Debit Card Purchase Sato RamenBuffalo NY09/186.47POS Purchase Maid Of The Mi Niagara FallNY09/186.009979 Debit Card Purchase NiagaraReservation Sp09/18136.969979 Debit Card Purchase CheesecakeBuffalo09/1838.70POS Purchase Sunoco 0573575 Angola NY09/193.359979 Debit Card Purchase Niagara Res StatePark09/196.589979 Debit Card Purchase Prospect Pointe09/1968.679979 Debit Card Purchase Ni HoowaSupermarket09/1916.009979 Debit Card Purchase Ni HoowaSupermarket09/1950.009979 Debit Card Purchase Psu Id+ Office09/1952.66POS Purchase Wal-Mart Super Erie PA09/2144.999979 Recurring Debit Card Twc*Time WrnrCable09/219.009979 Debit Card Purchase Laser Wash/ErieErie09/2151.949979 Recurring Debit Card AmazonprimeMembershi09/2219.009979 Debit Card Purchase Codeschool.Com09/2252.439979 Debit Card Purchase Peking ChineseRestaurBanking/Check Card Withdrawals and Purchases continued on next pagePage 2 of 
[]
[]
1 Page successfully wrote
Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedBanking/Check Card Withdrawals and PurchasesDateAmountDescription09/2580.469979 Debit Card Purchase Erie 10 Minute OilCha09/255.939979 Debit Card Purchase McDonald'sF1237509/2525.969979 Recurring Debit Card Inet-Cash.De*Durip09/2521.969979 Debit Card Purchase Sq *Yummy Cafe09/2521.009979 Debit Card Purchase Kimchi KoreanRestaura09/2528.93POS Purchase Snappys 501 State Colleg PA09/2537.849979 Debit Card Purchase Country Fair #4609/25.78International POS Fee  Vis 0923              Df09/266.149979 Debit Card Purchase Tim Horton's#91633209/2651.949979 Recurring Debit Card AmazonprimeMembershi09/2614.719979 Debit Card Purchase Amazon.ComAmzn.Com/Bi09/277.289979 Debit Card Purchase Psu Housing andFoods09/27.999979 Debit Card Purchase Apl*Itunes.Com/Bill09/288.269979 Debit Card Purchase Psu Housing andFoods09/2810.599979 Debit Card Purchase Apl*Itunes.Com/Bill09/288.999979 Debit Card Purchase Paypal*Guangdong1109/2953.959979 Debit Card Purchase Amazon MktplacePmts09/294.989979 Debit Card Purchase Psu Housing andFoods09/293.599979 Debit Card Purchase Psu Housing andFoods09/2926.499979 Recurring Debit Card Sling.Com  888-39363110/02149.059979 Debit Card Purchase Amazon.ComAmzn.Com/Bi10/026.039979 Debit Card Purchase Tim Horton's#91633210/0243.61POS Purchase Get Go #3290 Erie PA10/039.999979 Debit Card Purchase Sunprod  727-4986514 P10/034.999979 Debit Card Purchase Sunprod  727-4986514 P10/044.299979 Debit Card Purchase Psu Housing andFoods10/051.199979 Debit Card Purchase Psu Housing andFoods10/0550.009979 Debit Card Purchase Psu Id+ OfficeBanking/Check Card Withdrawals and Purchases continued on next pagePage 3 of 
[]
[]
2 Page successfully wrote
Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedBanking/Check Card Withdrawals and PurchasesDateAmountDescription10/0546.75POS Purchase Wegmans 6143 P Erie PA10/0624.999979 Debit Card PurchaseCcbilleu.Com*Durip Bv10/0612.289979 Debit Card Purchase Amazon MktplacePmts10/0639.07POS Purchase Get Go #3290 Erie PA10/06.75International POS Fee  Vis 1004              Gb10/1019.989979 Debit Card Purchase Amazon.comAmzn.Com/B10/1012.009979 Debit Card Purchase Paypal *Fastspring10/1016.939979 Debit Card Purchase Kfc J625156  EriePA10/1010.009979 Debit Card Purchase Amazon MktplacePmts10/1036.88POS Purchase Wm Supercenter Erie PA10/1046.88POS Purchase Wm Supercenter Erie PA10/1039.139979 Debit Card Purchase Paynow*FirstEnergy10/1297.019979 Debit Card Purchase Expedia7302347701530Online and Electronic Banking DeductionsThere were 3 Online or ElectronicBanking Deductions totaling$2,733.78.DateAmountDescription09/141,725.58Online Transfer To        000000601722710209/1847.45Web Pmt Single - Payment Venmo 67545537210/02960.75Web Pmt Single - E-Payment Discover 6269Daily Balance DetailDateBalanceDateBalanceDateBalanceDateBalance09/141,646.1909/151,640.8909/181,216.4309/191,019.1709/21913.2409/22893.7509/25670.8909/26598.1009/27589.8309/28561.9909/29472.9810/0219.2710/035.4810/04135.2110/0537.2710/06.0010/101.0010/1241.33Member FDICEqual Housing LenderPage 4 of 
[]
[]
3 Page successfully wrote
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
Virtual Wallet Spend StatementPNC BankPrimary account number:60-1722-7081For the period09/14/2017to10/12/2017Number of enclosures:0ZHENG ZHANGFor 24-hour banking, and transaction or4701 COLLEGE DR MB 1097interest rate information, sign-on toERIE PA 16563-0001PNC Bank Online Banking at pnc.comFor customer service call 1-888-PNC-BANKMonday - Friday: 7 AM - 10 PM ETSaturday & Sunday: 8 AM - 5 PM ETPara servicio en espanol, 1-866-HOLA-PNCMoving?Please contact us at 1-888-PNC-BANKWrite to:  Customer ServicePO Box 609Pittsburgh, PA  15230-9738Visit us at pnc.comTDD terminal: 1-800-531-1648For hearing impaired clients onlyADDITIONAL DOCUMENTS ARE AVAILABLE FOR DIGITAL DELIVERYAdditional documents are eligible for digital delivery and will no longer be sent by US Mail for accountsthat have selected to have digital delivery of account servicing communications. The additional documentseligible for digital delivery are listed below. A complete list of all documents delivered online isavailable in the Online Documents tab within Online Banking. This list will be updated as additionaldocuments are made available. When a document is available to view we will notify you by sending an email tothe email address on file.> Inactive Status Notice (as of 6/17/17)> Automatic Check Renewal Notice (as of 10/21/17)Virtual Wallet Spend Account SummaryAccount number:60-1722-7081Overdraft ProtectionProvided By:   XXXXXX7102XXXXXX7129Overdraft Coverage- Your account is currentlyOpted-Out.ZHENG ZHANGBalance SummaryBeginningbalanceDeposits andother additionsChecks and otherdeductionsEndingbalance3,411.451,252.844,622.9641.33Average monthlybalanceChargesand fees603.391.53Transaction SummaryCheckspaid/withdrawalsCheck Card POSsigned transactionsCheck Card/BankcardPOS PIN transactions0539Total ATMtransactionsPNC Bank ATMtransactionsOther Bank ATMtransactions000Page 1 of 
[]
[]
0 Page successfully wrote
Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedActivity DetailDeposits and Other AdditionsThere were 7 Deposits and OtherAdditions totaling $1,252.84.DateAmountDescription09/2251.94Debit Card Credit Amazonprime Membershipamzn.com/pr WA10/02705.73Funds Transfer From Acct 601722710210/031.19Funds Transfer From Acct 601722710210/04134.02Funds Transfer From Acct 601722710210/0639.82Funds Transfer From Acct 601722710210/10182.80Funds Transfer From Acct 601722710210/12137.34Funds Transfer From Acct 6017227102Banking/Check Card Withdrawals and PurchasesThere were 9 Check Card/Bank cardPIN POS purchases totaling$339.95.There were 54 other BankingMachine/Check Card deductionstotaling $1,549.23.DateAmountDescription09/1439.689979 Debit Card Purchase Amazon MktplacePmts09/155.309979 Debit Card Purchase Kfc J625156  EriePA09/1857.199979 Debit Card Purchase Paypal *SephoraUSA09/1819.959979 Debit Card Purchase Paypal *CheggTxtbk09/187.309979 Debit Card Purchase McDonald'sF12018  Eri09/1863.599979 Recurring Debit Card Ea *Origin.Com09/1840.859979 Debit Card Purchase Sato RamenBuffalo NY09/186.47POS Purchase Maid Of The Mi Niagara FallNY09/186.009979 Debit Card Purchase NiagaraReservation Sp09/18136.969979 Debit Card Purchase CheesecakeBuffalo09/1838.70POS Purchase Sunoco 0573575 Angola NY09/193.359979 Debit Card Purchase Niagara Res StatePark09/196.589979 Debit Card Purchase Prospect Pointe09/1968.679979 Debit Card Purchase Ni HoowaSupermarket09/1916.009979 Debit Card Purchase Ni HoowaSupermarket09/1950.009979 Debit Card Purchase Psu Id+ Office09/1952.66POS Purchase Wal-Mart Super Erie PA09/2144.999979 Recurring Debit Card Twc*Time WrnrCable09/219.009979 Debit Card Purchase Laser Wash/ErieErie09/2151.949979 Recurring Debit Card AmazonprimeMembershi09/2219.009979 Debit Card Purchase Codeschool.Com09/2252.439979 Debit Card Purchase Peking ChineseRestaurBanking/Check Card Withdrawals and Purchases continued on next pagePage 2 of 
[]
[]
1 Page successfully wrote
Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedBanking/Check Card Withdrawals and PurchasesDateAmountDescription09/2580.469979 Debit Card Purchase Erie 10 Minute OilCha09/255.939979 Debit Card Purchase McDonald'sF1237509/2525.969979 Recurring Debit Card Inet-Cash.De*Durip09/2521.969979 Debit Card Purchase Sq *Yummy Cafe09/2521.009979 Debit Card Purchase Kimchi KoreanRestaura09/2528.93POS Purchase Snappys 501 State Colleg PA09/2537.849979 Debit Card Purchase Country Fair #4609/25.78International POS Fee  Vis 0923              Df09/266.149979 Debit Card Purchase Tim Horton's#91633209/2651.949979 Recurring Debit Card AmazonprimeMembershi09/2614.719979 Debit Card Purchase Amazon.ComAmzn.Com/Bi09/277.289979 Debit Card Purchase Psu Housing andFoods09/27.999979 Debit Card Purchase Apl*Itunes.Com/Bill09/288.269979 Debit Card Purchase Psu Housing andFoods09/2810.599979 Debit Card Purchase Apl*Itunes.Com/Bill09/288.999979 Debit Card Purchase Paypal*Guangdong1109/2953.959979 Debit Card Purchase Amazon MktplacePmts09/294.989979 Debit Card Purchase Psu Housing andFoods09/293.599979 Debit Card Purchase Psu Housing andFoods09/2926.499979 Recurring Debit Card Sling.Com  888-39363110/02149.059979 Debit Card Purchase Amazon.ComAmzn.Com/Bi10/026.039979 Debit Card Purchase Tim Horton's#91633210/0243.61POS Purchase Get Go #3290 Erie PA10/039.999979 Debit Card Purchase Sunprod  727-4986514 P10/034.999979 Debit Card Purchase Sunprod  727-4986514 P10/044.299979 Debit Card Purchase Psu Housing andFoods10/051.199979 Debit Card Purchase Psu Housing andFoods10/0550.009979 Debit Card Purchase Psu Id+ OfficeBanking/Check Card Withdrawals and Purchases continued on next pagePage 3 of 
[]
[]
2 Page successfully wrote
Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedBanking/Check Card Withdrawals and PurchasesDateAmountDescription10/0546.75POS Purchase Wegmans 6143 P Erie PA10/0624.999979 Debit Card PurchaseCcbilleu.Com*Durip Bv10/0612.289979 Debit Card Purchase Amazon MktplacePmts10/0639.07POS Purchase Get Go #3290 Erie PA10/06.75International POS Fee  Vis 1004              Gb10/1019.989979 Debit Card Purchase Amazon.comAmzn.Com/B10/1012.009979 Debit Card Purchase Paypal *Fastspring10/1016.939979 Debit Card Purchase Kfc J625156  EriePA10/1010.009979 Debit Card Purchase Amazon MktplacePmts10/1036.88POS Purchase Wm Supercenter Erie PA10/1046.88POS Purchase Wm Supercenter Erie PA10/1039.139979 Debit Card Purchase Paynow*FirstEnergy10/1297.019979 Debit Card Purchase Expedia7302347701530Online and Electronic Banking DeductionsThere were 3 Online or ElectronicBanking Deductions totaling$2,733.78.DateAmountDescription09/141,725.58Online Transfer To        000000601722710209/1847.45Web Pmt Single - Payment Venmo 67545537210/02960.75Web Pmt Single - E-Payment Discover 6269Daily Balance DetailDateBalanceDateBalanceDateBalanceDateBalance09/141,646.1909/151,640.8909/181,216.4309/191,019.1709/21913.2409/22893.7509/25670.8909/26598.1009/27589.8309/28561.9909/29472.9810/0219.2710/035.4810/04135.2110/0537.2710/06.0010/101.0010/1241.33Member FDICEqual Housing LenderPage 4 of 
[]
[]
3 Page successfully wrote
>>> pdf_lists
'Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedBanking/Check Card Withdrawals and PurchasesDateAmountDescription10/0546.75POS Purchase Wegmans 6143 P Erie PA10/0624.999979 Debit Card PurchaseCcbilleu.Com*Durip Bv10/0612.289979 Debit Card Purchase Amazon MktplacePmts10/0639.07POS Purchase Get Go #3290 Erie PA10/06.75International POS Fee  Vis 1004              Gb10/1019.989979 Debit Card Purchase Amazon.comAmzn.Com/B10/1012.009979 Debit Card Purchase Paypal *Fastspring10/1016.939979 Debit Card Purchase Kfc J625156  EriePA10/1010.009979 Debit Card Purchase Amazon MktplacePmts10/1036.88POS Purchase Wm Supercenter Erie PA10/1046.88POS Purchase Wm Supercenter Erie PA10/1039.139979 Debit Card Purchase Paynow*FirstEnergy10/1297.019979 Debit Card Purchase Expedia7302347701530Online and Electronic Banking DeductionsThere were 3 Online or ElectronicBanking Deductions totaling$2,733.78.DateAmountDescription09/141,725.58Online Transfer To        000000601722710209/1847.45Web Pmt Single - Payment Venmo 67545537210/02960.75Web Pmt Single - E-Payment Discover 6269Daily Balance DetailDateBalanceDateBalanceDateBalanceDateBalance09/141,646.1909/151,640.8909/181,216.4309/191,019.1709/21913.2409/22893.7509/25670.8909/26598.1009/27589.8309/28561.9909/29472.9810/0219.2710/035.4810/04135.2110/0537.2710/06.0010/101.0010/1241.33Member FDICEqual Housing LenderPage 4 of '
>>> spent_part_data = re.findall(r'DataAmountDiscription(.*?)Banking/Check',pdf_lists)
>>> spent_part_data
[]
>>> spent_part_data = re.findall(r'DateAmountDescription(.*?)Banking/Check', pdf_lists[0])
>>> spent_part_data
[]
>>> pdf_lists[0]
'V'
>>> pdf_lists2 = []
>>> pageObj = pdfReader.getPage(i)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    pageObj = pdfReader.getPage(i)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/PyPDF2/pdf.py", line 1177, in getPage
    return self.flattenedPages[pageNumber]
IndexError: list index out of range
>>> pageObj = pdfReader.getPage(2)
>>> pdf_lists.append(pageObj.extractText())
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    pdf_lists.append(pageObj.extractText())
AttributeError: 'str' object has no attribute 'append'
>>> pdf_lists2.append(pageObj.extractText())
>>> pdf_lists2
["Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedBanking/Check Card Withdrawals and PurchasesDateAmountDescription09/2580.469979 Debit Card Purchase Erie 10 Minute OilCha09/255.939979 Debit Card Purchase McDonald'sF1237509/2525.969979 Recurring Debit Card Inet-Cash.De*Durip09/2521.969979 Debit Card Purchase Sq *Yummy Cafe09/2521.009979 Debit Card Purchase Kimchi KoreanRestaura09/2528.93POS Purchase Snappys 501 State Colleg PA09/2537.849979 Debit Card Purchase Country Fair #4609/25.78International POS Fee  Vis 0923              Df09/266.149979 Debit Card Purchase Tim Horton's#91633209/2651.949979 Recurring Debit Card AmazonprimeMembershi09/2614.719979 Debit Card Purchase Amazon.ComAmzn.Com/Bi09/277.289979 Debit Card Purchase Psu Housing andFoods09/27.999979 Debit Card Purchase Apl*Itunes.Com/Bill09/288.269979 Debit Card Purchase Psu Housing andFoods09/2810.599979 Debit Card Purchase Apl*Itunes.Com/Bill09/288.999979 Debit Card Purchase Paypal*Guangdong1109/2953.959979 Debit Card Purchase Amazon MktplacePmts09/294.989979 Debit Card Purchase Psu Housing andFoods09/293.599979 Debit Card Purchase Psu Housing andFoods09/2926.499979 Recurring Debit Card Sling.Com  888-39363110/02149.059979 Debit Card Purchase Amazon.ComAmzn.Com/Bi10/026.039979 Debit Card Purchase Tim Horton's#91633210/0243.61POS Purchase Get Go #3290 Erie PA10/039.999979 Debit Card Purchase Sunprod  727-4986514 P10/034.999979 Debit Card Purchase Sunprod  727-4986514 P10/044.299979 Debit Card Purchase Psu Housing andFoods10/051.199979 Debit Card Purchase Psu Housing andFoods10/0550.009979 Debit Card Purchase Psu Id+ OfficeBanking/Check Card Withdrawals and Purchases continued on next pagePage 3 of "]
>>> pdf_lists2[0]
"Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedBanking/Check Card Withdrawals and PurchasesDateAmountDescription09/2580.469979 Debit Card Purchase Erie 10 Minute OilCha09/255.939979 Debit Card Purchase McDonald'sF1237509/2525.969979 Recurring Debit Card Inet-Cash.De*Durip09/2521.969979 Debit Card Purchase Sq *Yummy Cafe09/2521.009979 Debit Card Purchase Kimchi KoreanRestaura09/2528.93POS Purchase Snappys 501 State Colleg PA09/2537.849979 Debit Card Purchase Country Fair #4609/25.78International POS Fee  Vis 0923              Df09/266.149979 Debit Card Purchase Tim Horton's#91633209/2651.949979 Recurring Debit Card AmazonprimeMembershi09/2614.719979 Debit Card Purchase Amazon.ComAmzn.Com/Bi09/277.289979 Debit Card Purchase Psu Housing andFoods09/27.999979 Debit Card Purchase Apl*Itunes.Com/Bill09/288.269979 Debit Card Purchase Psu Housing andFoods09/2810.599979 Debit Card Purchase Apl*Itunes.Com/Bill09/288.999979 Debit Card Purchase Paypal*Guangdong1109/2953.959979 Debit Card Purchase Amazon MktplacePmts09/294.989979 Debit Card Purchase Psu Housing andFoods09/293.599979 Debit Card Purchase Psu Housing andFoods09/2926.499979 Recurring Debit Card Sling.Com  888-39363110/02149.059979 Debit Card Purchase Amazon.ComAmzn.Com/Bi10/026.039979 Debit Card Purchase Tim Horton's#91633210/0243.61POS Purchase Get Go #3290 Erie PA10/039.999979 Debit Card Purchase Sunprod  727-4986514 P10/034.999979 Debit Card Purchase Sunprod  727-4986514 P10/044.299979 Debit Card Purchase Psu Housing andFoods10/051.199979 Debit Card Purchase Psu Housing andFoods10/0550.009979 Debit Card Purchase Psu Id+ OfficeBanking/Check Card Withdrawals and Purchases continued on next pagePage 3 of "
>>> spent_part_data = re.findall(r'DateAmountDescription(.*?)Banking/Check', pdf_lists2[0])
>>> spent_part_data
["09/2580.469979 Debit Card Purchase Erie 10 Minute OilCha09/255.939979 Debit Card Purchase McDonald'sF1237509/2525.969979 Recurring Debit Card Inet-Cash.De*Durip09/2521.969979 Debit Card Purchase Sq *Yummy Cafe09/2521.009979 Debit Card Purchase Kimchi KoreanRestaura09/2528.93POS Purchase Snappys 501 State Colleg PA09/2537.849979 Debit Card Purchase Country Fair #4609/25.78International POS Fee  Vis 0923              Df09/266.149979 Debit Card Purchase Tim Horton's#91633209/2651.949979 Recurring Debit Card AmazonprimeMembershi09/2614.719979 Debit Card Purchase Amazon.ComAmzn.Com/Bi09/277.289979 Debit Card Purchase Psu Housing andFoods09/27.999979 Debit Card Purchase Apl*Itunes.Com/Bill09/288.269979 Debit Card Purchase Psu Housing andFoods09/2810.599979 Debit Card Purchase Apl*Itunes.Com/Bill09/288.999979 Debit Card Purchase Paypal*Guangdong1109/2953.959979 Debit Card Purchase Amazon MktplacePmts09/294.989979 Debit Card Purchase Psu Housing andFoods09/293.599979 Debit Card Purchase Psu Housing andFoods09/2926.499979 Recurring Debit Card Sling.Com  888-39363110/02149.059979 Debit Card Purchase Amazon.ComAmzn.Com/Bi10/026.039979 Debit Card Purchase Tim Horton's#91633210/0243.61POS Purchase Get Go #3290 Erie PA10/039.999979 Debit Card Purchase Sunprod  727-4986514 P10/034.999979 Debit Card Purchase Sunprod  727-4986514 P10/044.299979 Debit Card Purchase Psu Housing andFoods10/051.199979 Debit Card Purchase Psu Housing andFoods10/0550.009979 Debit Card Purchase Psu Id+ Office"]
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
Virtual Wallet Spend StatementPNC BankPrimary account number:60-1722-7081For the period09/14/2017to10/12/2017Number of enclosures:0ZHENG ZHANGFor 24-hour banking, and transaction or4701 COLLEGE DR MB 1097interest rate information, sign-on toERIE PA 16563-0001PNC Bank Online Banking at pnc.comFor customer service call 1-888-PNC-BANKMonday - Friday: 7 AM - 10 PM ETSaturday & Sunday: 8 AM - 5 PM ETPara servicio en espanol, 1-866-HOLA-PNCMoving?Please contact us at 1-888-PNC-BANKWrite to:  Customer ServicePO Box 609Pittsburgh, PA  15230-9738Visit us at pnc.comTDD terminal: 1-800-531-1648For hearing impaired clients onlyADDITIONAL DOCUMENTS ARE AVAILABLE FOR DIGITAL DELIVERYAdditional documents are eligible for digital delivery and will no longer be sent by US Mail for accountsthat have selected to have digital delivery of account servicing communications. The additional documentseligible for digital delivery are listed below. A complete list of all documents delivered online isavailable in the Online Documents tab within Online Banking. This list will be updated as additionaldocuments are made available. When a document is available to view we will notify you by sending an email tothe email address on file.> Inactive Status Notice (as of 6/17/17)> Automatic Check Renewal Notice (as of 10/21/17)Virtual Wallet Spend Account SummaryAccount number:60-1722-7081Overdraft ProtectionProvided By:   XXXXXX7102XXXXXX7129Overdraft Coverage- Your account is currentlyOpted-Out.ZHENG ZHANGBalance SummaryBeginningbalanceDeposits andother additionsChecks and otherdeductionsEndingbalance3,411.451,252.844,622.9641.33Average monthlybalanceChargesand fees603.391.53Transaction SummaryCheckspaid/withdrawalsCheck Card POSsigned transactionsCheck Card/BankcardPOS PIN transactions0539Total ATMtransactionsPNC Bank ATMtransactionsOther Bank ATMtransactions000Page 1 of 
[]
[]
0 Page successfully wrote
Virtual Wallet Spend StatementPNC BankPrimary account number:60-1722-7081For the period09/14/2017to10/12/2017Number of enclosures:0ZHENG ZHANGFor 24-hour banking, and transaction or4701 COLLEGE DR MB 1097interest rate information, sign-on toERIE PA 16563-0001PNC Bank Online Banking at pnc.comFor customer service call 1-888-PNC-BANKMonday - Friday: 7 AM - 10 PM ETSaturday & Sunday: 8 AM - 5 PM ETPara servicio en espanol, 1-866-HOLA-PNCMoving?Please contact us at 1-888-PNC-BANKWrite to:  Customer ServicePO Box 609Pittsburgh, PA  15230-9738Visit us at pnc.comTDD terminal: 1-800-531-1648For hearing impaired clients onlyADDITIONAL DOCUMENTS ARE AVAILABLE FOR DIGITAL DELIVERYAdditional documents are eligible for digital delivery and will no longer be sent by US Mail for accountsthat have selected to have digital delivery of account servicing communications. The additional documentseligible for digital delivery are listed below. A complete list of all documents delivered online isavailable in the Online Documents tab within Online Banking. This list will be updated as additionaldocuments are made available. When a document is available to view we will notify you by sending an email tothe email address on file.> Inactive Status Notice (as of 6/17/17)> Automatic Check Renewal Notice (as of 10/21/17)Virtual Wallet Spend Account SummaryAccount number:60-1722-7081Overdraft ProtectionProvided By:   XXXXXX7102XXXXXX7129Overdraft Coverage- Your account is currentlyOpted-Out.ZHENG ZHANGBalance SummaryBeginningbalanceDeposits andother additionsChecks and otherdeductionsEndingbalance3,411.451,252.844,622.9641.33Average monthlybalanceChargesand fees603.391.53Transaction SummaryCheckspaid/withdrawalsCheck Card POSsigned transactionsCheck Card/BankcardPOS PIN transactions0539Total ATMtransactionsPNC Bank ATMtransactionsOther Bank ATMtransactions000Page 1 of 
[]
[]
1 Page successfully wrote
Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedActivity DetailDeposits and Other AdditionsThere were 7 Deposits and OtherAdditions totaling $1,252.84.DateAmountDescription09/2251.94Debit Card Credit Amazonprime Membershipamzn.com/pr WA10/02705.73Funds Transfer From Acct 601722710210/031.19Funds Transfer From Acct 601722710210/04134.02Funds Transfer From Acct 601722710210/0639.82Funds Transfer From Acct 601722710210/10182.80Funds Transfer From Acct 601722710210/12137.34Funds Transfer From Acct 6017227102Banking/Check Card Withdrawals and PurchasesThere were 9 Check Card/Bank cardPIN POS purchases totaling$339.95.There were 54 other BankingMachine/Check Card deductionstotaling $1,549.23.DateAmountDescription09/1439.689979 Debit Card Purchase Amazon MktplacePmts09/155.309979 Debit Card Purchase Kfc J625156  EriePA09/1857.199979 Debit Card Purchase Paypal *SephoraUSA09/1819.959979 Debit Card Purchase Paypal *CheggTxtbk09/187.309979 Debit Card Purchase McDonald'sF12018  Eri09/1863.599979 Recurring Debit Card Ea *Origin.Com09/1840.859979 Debit Card Purchase Sato RamenBuffalo NY09/186.47POS Purchase Maid Of The Mi Niagara FallNY09/186.009979 Debit Card Purchase NiagaraReservation Sp09/18136.969979 Debit Card Purchase CheesecakeBuffalo09/1838.70POS Purchase Sunoco 0573575 Angola NY09/193.359979 Debit Card Purchase Niagara Res StatePark09/196.589979 Debit Card Purchase Prospect Pointe09/1968.679979 Debit Card Purchase Ni HoowaSupermarket09/1916.009979 Debit Card Purchase Ni HoowaSupermarket09/1950.009979 Debit Card Purchase Psu Id+ Office09/1952.66POS Purchase Wal-Mart Super Erie PA09/2144.999979 Recurring Debit Card Twc*Time WrnrCable09/219.009979 Debit Card Purchase Laser Wash/ErieErie09/2151.949979 Recurring Debit Card AmazonprimeMembershi09/2219.009979 Debit Card Purchase Codeschool.Com09/2252.439979 Debit Card Purchase Peking ChineseRestaurBanking/Check Card Withdrawals and Purchases continued on next pagePage 2 of 
[]
[]
2 Page successfully wrote
Virtual Wallet Spend StatementFor the period09/14/2017to10/12/2017For 24-hour information,sign on to PNC Bank Online BankingZHENG ZHANGon pnc.comPrimary account number:60-1722-7081Account Number:60-1722-7081- continuedBanking/Check Card Withdrawals and PurchasesDateAmountDescription09/2580.469979 Debit Card Purchase Erie 10 Minute OilCha09/255.939979 Debit Card Purchase McDonald'sF1237509/2525.969979 Recurring Debit Card Inet-Cash.De*Durip09/2521.969979 Debit Card Purchase Sq *Yummy Cafe09/2521.009979 Debit Card Purchase Kimchi KoreanRestaura09/2528.93POS Purchase Snappys 501 State Colleg PA09/2537.849979 Debit Card Purchase Country Fair #4609/25.78International POS Fee  Vis 0923              Df09/266.149979 Debit Card Purchase Tim Horton's#91633209/2651.949979 Recurring Debit Card AmazonprimeMembershi09/2614.719979 Debit Card Purchase Amazon.ComAmzn.Com/Bi09/277.289979 Debit Card Purchase Psu Housing andFoods09/27.999979 Debit Card Purchase Apl*Itunes.Com/Bill09/288.269979 Debit Card Purchase Psu Housing andFoods09/2810.599979 Debit Card Purchase Apl*Itunes.Com/Bill09/288.999979 Debit Card Purchase Paypal*Guangdong1109/2953.959979 Debit Card Purchase Amazon MktplacePmts09/294.989979 Debit Card Purchase Psu Housing andFoods09/293.599979 Debit Card Purchase Psu Housing andFoods09/2926.499979 Recurring Debit Card Sling.Com  888-39363110/02149.059979 Debit Card Purchase Amazon.ComAmzn.Com/Bi10/026.039979 Debit Card Purchase Tim Horton's#91633210/0243.61POS Purchase Get Go #3290 Erie PA10/039.999979 Debit Card Purchase Sunprod  727-4986514 P10/034.999979 Debit Card Purchase Sunprod  727-4986514 P10/044.299979 Debit Card Purchase Psu Housing andFoods10/051.199979 Debit Card Purchase Psu Housing andFoods10/0550.009979 Debit Card Purchase Psu Id+ OfficeBanking/Check Card Withdrawals and Purchases continued on next pagePage 3 of 
[]
[]
3 Page successfully wrote
>>> pdb myscript.py
SyntaxError: invalid syntax
>>> pdb code_mac.py
SyntaxError: invalid syntax
>>> pythin -m pdb /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py
SyntaxError: invalid syntax
>>> python -m pdb /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py
SyntaxError: invalid syntax
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py", line 4, in <module>
    import pdb
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/pdb.py", line 76, in <module>
    import code
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py", line 10
    pdfFileObj = open(fileDirectory + '\' + fileName, 'rb')
                                                          ^
SyntaxError: EOL while scanning string literal
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py", line 4, in <module>
    import pdb
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/pdb.py", line 76, in <module>
    import code
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py", line 10
    pdfFileObj = open(fileDirectory + '\' + fileName, 'rb')
                                                          ^
SyntaxError: EOL while scanning string literal
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py", line 4, in <module>
    import pdb
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/pdb.py", line 76, in <module>
    import code
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py", line 10
    pdfFileObj = open(fileDirectory + '\' + fileName, 'rb')
                                                          ^
SyntaxError: EOL while scanning string literal
>>> 
=============================== RESTART: Shell ===============================
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py", line 4, in <module>
    import pdb
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/pdb.py", line 76, in <module>
    import code
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py", line 10
    pdfFileObj = open(fileDirectory + '\' + fileName, 'rb')
                                                          ^
SyntaxError: EOL while scanning string literal
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py", line 4, in <module>
    import pdb
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/pdb.py", line 76, in <module>
    import code
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code.py", line 10
    pdfFileObj = open(fileDirectory + '\' + fileName, 'rb')
                                                          ^
SyntaxError: EOL while scanning string literal
>>> c
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> 
 RESTART: /Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py 
[]
Traceback (most recent call last):
  File "/Users/Michavillson/Google Drive/Projects/Python/Manipulating with pdf/Program_Git_Folder/code_mac.py", line 46, in <module>
    extracted_data = dateNumRegex.findall(spent_part_data)
TypeError: expected string or bytes-like object
>>> 