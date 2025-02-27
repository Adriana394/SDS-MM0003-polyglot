import pyttsx3
import sys

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 125)

    def  speak(self,response):
        self.engine.say(response)
        self.engine.runAndWait()

txt2speech = TextToSpeech()
txt2speech.speak(str((sys.argv[1])))