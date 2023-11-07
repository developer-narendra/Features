import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Use the default microphone as the source
with sr.Microphone() as source:
print("Listening...")
audio = r.listen(source)

try:
# Recognize speech using Google Speech Recognition
text = r.recognize_google(audio)
print("You said: " + text)
except sr.UnknownValueError:
print("Sorry, I could not understand audio")
except sr.RequestError as e:
print("Sorry, could not request results from Google Speech Recognition service; {0}".format(e))
