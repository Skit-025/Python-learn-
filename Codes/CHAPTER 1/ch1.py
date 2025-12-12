A="hello world"
print(A)
import pyjokes
joke=pyjokes.get_joke()
print(joke)
import pyttsx3
ref=pyttsx3.init()
ref.say(joke)
ref.runAndWait()
ref.say(A)
ref.runAndWait()
'''import os
directory_path="/"
content = os.listdir(directory_path)
for items in content:print(items)
'''