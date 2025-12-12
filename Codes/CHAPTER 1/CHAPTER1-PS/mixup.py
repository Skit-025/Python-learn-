import os
directory_path="/"
content=os.listdir(directory_path)
for item in content:
    print(item)
    import pyjokes
    joke=pyjokes.get_joke()
    print(joke)
    import pyttsx3
    ref=pyttsx3.init()
    ref.say("hello")
    ref.runAndWait()