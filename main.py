import pyttsx3 
import PyPDF2

book = open('pdfNameGoesHere.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
for totalNum in range(1, pages):
    page = pdfReader.getPage(totalNum)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()