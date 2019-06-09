from commands1 import commander
from pygame.mixer import *
import speech_recognition as sr
# speech recognizer
r=sr.Recognizer()
init()
running=True

cmd=commander()
def initSpeech():
    print("Listening...")
    music.load('coins.mp3')
    
    with sr.Microphone() as source:
        print("Please wait calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=1)
        music.play()
        print("Say Something")
        audio=r.listen(source)
    music.load('to-the-point.mp3')
    music.play()
    try:
        command=r.recognize_google(audio)
    except:
        print("Couldn't understand you")

    print("Your command: ",end="")
    print(command)
    cmd.discover(command)
    if command in ["quit","bye","goodbye","exit","see you"]:
            global running
            running=False
    print("\n")
    
while running==True:
    initSpeech()    
