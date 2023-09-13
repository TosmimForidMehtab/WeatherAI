import pyttsx3 as tts
import audioToText as at
import sys
import random

greeting = ['Hey, how can I help you?', 'What can I do for you?', 'What can I help you with?', 'What can I do for you?', 'How can I help you?']

questions1 = ['For which city do you want to know the weather?', 'Provide the city name to know weather info', 'City name please', 'What can I help you with?', 'Please say the name of the city for which you want to know the weather']

# Generate random number in the range of 0 to 4
index = random.randint(0, len(greeting)-1)

engine = tts.init()
engine.setProperty("rate", 150)
wake = at.speechToText()

# Convert text to lowercase
if wake is not None:
    wake = wake.lower()
else:
    # exit the program
    sys.exit()


if 'vortex' in wake:
    engine.say(greeting[index])
    engine.runAndWait()
    reply1 = at.speechToText()
    print(reply1)
else:
    engine.say('Sorry, I did not understand')
        