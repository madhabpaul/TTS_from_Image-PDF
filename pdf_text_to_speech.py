from gtts import gTTS
import os, PyPDF2

alert ='''****************************************************************
       File must be saved in your present directory
                Support PDF File only             
****************************************************************'''
print(alert) 
file_name = input("Enter File Name (with extension) :-")
# creating a pdf file object
pdf_file = open(file_name, "rb")
# creating a pdf reader object 
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# calculating number of pages in pdf file 
total_page = pdf_reader.numPages 
text = ""
for i in range(total_page):
    pageObj = pdf_reader.getPage(i)
    text = text + pageObj.extractText()
print(text)

# closing the pdf file object 
pdf_file.close()

print("Converting Text to Audio........")
voice_output=str(text) 
tts = gTTS(text=voice_output, lang='en')
#text is converted into mp3 file
tts.save("voice.mp3")   
os.system("mpg321 voice.mp3") 