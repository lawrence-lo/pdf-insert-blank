import io, os, re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from PyPDF2 import PdfFileReader, PdfFileWriter

# Settings
input_path = os.path.dirname(os.path.realpath(__file__)) + '/sample.pdf' # PDF file path
output_path = input_path[:-4] + '_blank.pdf' # Output file suffix
search_str = r'email@company' # Search string
blank_width = 612 # Letter size
blank_height = 792 # Letter size

# pdfminer setup
fp = open(input_path, 'rb')
rsrcmgr = PDFResourceManager()
retstr = io.StringIO()
codec = 'utf-8'
laparams = LAParams()
device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

# Read file with PyPDF2
file1 = PdfFileReader(open(input_path, 'rb'))
output = PdfFileWriter()

# Page index of output file
page_index = 0

# Blank page counter
blank_added = 0

for page_num, page in enumerate(PDFPage.get_pages(fp)):
    print('Page in progress: ' + str(page_num), end="\r") # Check progress
    interpreter.process_page(page)
    data = retstr.getvalue()

    # Move page to output with PyPDF2
    output.addPage(file1.getPage(page_num))

    is_found = re.search(search_str, data) is not None
    if is_found:
        # Add a blank page before found page if page index is odd
        if page_index % 2 != 0:
            output.insertBlankPage(width=blank_width, height=blank_height, index=page_index)
            blank_added += 1
            page_index += 1
        # Add a blank page after found page
        output.addBlankPage(width=blank_width, height=blank_height)
        blank_added += 1
        page_index += 1

    data = ''
    retstr.truncate(0)
    retstr.seek(0)

    page_index += 1

# Write to output file
outputStream = open(output_path, 'wb')
output.write(outputStream)
outputStream.close()

fp.close()
device.close()
retstr.close()

print('\nBlank pages added: ' + str(blank_added))