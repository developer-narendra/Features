import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get input text from user
text = input("Enter the text you want to convert to speech: ")

# Set speech rate and volume
engine.setProperty('rate', 150) # Speed of speech
engine.setProperty('volume', 0.8) # Volume (0.0 to 1.0)

# Convert text to speech
engine.say(text)
engine.runAndWait()