from PIL import Image
import pytesseract
from gtts import gTTS
import os

path = os.getcwd()
alert ='''****************************************************************
       File must be saved in your present directory
                Support Image File only             
****************************************************************'''
print(alert) 
file_name = input("Enter File Name (with extension) :-")
img = Image.open(path+'/'+file_name)

text = pytesseract.image_to_string(img, lang = 'eng')

print(text)
print("Converting Text to Audio........")
voice_output=str(text) 
tts = gTTS(text=voice_output, lang='en')
tts.save("voice.mp3")   #text is converted into mp3 file
os.system("mpg321 voice.mp3") 