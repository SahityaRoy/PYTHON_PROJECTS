import pyttsx3
import PyPDF2
book = open('syllabus.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
page = pdfReader.getPage(num)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()