from tkinter.filedialog import *
import PyPDF2


from gtts import gTTS
import os
book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages

for num in range(0,pages):
    page = pdfreader.getPage(num)
    mytext = page.extractText()

    audio = gTTS(text=mytext,lang='en',slow=False)
    audio.save('try.mp3')
os.system('try.mp3')

