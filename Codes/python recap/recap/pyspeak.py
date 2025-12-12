import pyttsx3
adi=pyttsx3.init()
voices = adi.getProperty('voices')
voices=adi.setProperty('voice',voices[4].id)
adi.say("I am Aditya Prasad Baarik")
adi.runAndWait()
