import speech_recognition as sr

def speech_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say a word:")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: ", text)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")

speech_recognition()
