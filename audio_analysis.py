# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
from playsound import playsound
import time
import pyaudio
import wave
import speech_recognition as sr
from sentiment_emotion import emotion
from sentiment_emotion import sentiment
from sentiment_emotion import final_report_dict
from sentiment_emotion import report
import sentiment_emotion

  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
mytext = mytext = ["Welcome to INTERVIEW BOT!","about how often did you feel worthless",
          "about how often did you feel nervous",
          "about how often did you feel so nervous that nothing could calm you down",
          "about how often did you feel hopeless",
          "about how often did you feel restless or fidgety",
          "about how often did you feel so restless you could not sit stil",
          "about how often did you feel depressed","about how often did you feel that everything was an effort",
          "about how often did you feel so sad that nothing could cheer you up",
          "about how often did you feel tired out for no good reason"]
  
# Language in which you want to convert 
language = 'en'


def audiototext(audio):
    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio = r.record(source)
        print ('Done!') 
    text = r.recognize_google(audio)
    
    return text
    

     
    
def recordaudio1(i):
    
    CHUNK = 1024 
    FORMAT = pyaudio.paInt16 #paInt8
    CHANNELS = 2 
    RATE = 44100 #sample rate
    RECORD_SECONDS = 10
    str="answered"+i+".wav"
    WAVE_OUTPUT_FILENAME =str

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK) #buffer

    print("* recording")
 
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data) # 2 bytes(16 bits) per channel

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    return str

  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
count=-1
for i in mytext:
    count+=1
    if(count>3):
        break
    myobj = gTTS(text=i, lang=language, slow=False) 
     # Saving the converted audio in a mp3 file named 
     # welcome 
    str="welcome"+i+".mp3"
    myobj.save(str) 
    # Playing the converted file 
    playsound(str)    
    # os.system("welcome.mp3")
    if(i!="Welcome to INTERVIEW BOT!"):
        s=recordaudio1(i)
        ans=audiototext(s)
        print(ans)
        emotion(ans)
        sentiment(ans)     

print("After break ")
dic_p={}
dic_p=final_report_dict()
print("Generating the final report....")
report(dic_p)
