import speech_recognition as sr 
import pyttsx3 as tts

listener = sr.Recognizer()
engine = tts.init()

try:
    print("Listening......")
    with sr.Microphone() as source:
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        if 'jarvis' in command:
            engine.say(command)
            engine.runAndWait()
            print(command)
except:
    pass 




