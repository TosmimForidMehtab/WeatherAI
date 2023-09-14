import pyttsx3 as tts
import audioToText as at
import sys
import random
import checkinWeather as ciw
import time 

#========================Utility Functions Start====================================
def speak(text):
    engine.say(text)
    engine.runAndWait()

def checkExit(word):
    if 'exit' in word or 'stop' in word or 'quit' in word:
        return True
    else:
        return False

#========================Utility Functions End====================================

#========================Constants Start==========================================
greeting = ['Hey, how can I help you?', 'hello, What can I do for you?', 'Hi, What can I help you with?', 'Hey What can I do for you?', 'Hello mate, How can I help you?']

questions1 = ['For which city do you want to know the weather?', 'Provide the city name to know weather info', 'City name please', 'for which city can I help you with?', 'Please say the name of the city for which you want to know the weather']

#========================Constants End============================================

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
    speak(greeting[index])
    
    reply1 = at.speechToText()
    
    if 'weather' in reply1:
            speak(questions1[index])

            while(True):
                reply2=at.speechToText() #asking for city. Here if the user says exit
                
                if(checkExit(reply2)):
                    speak("Thank you for using Vortex! Hope to meet you soon!,Bye!")
                    break
                
                
                reply2Array=reply2.split() #checking for last word in string array
                city=reply2Array[-1]

                # Telling the weather
                speak(ciw.getWeather(city))   
                
                #**should wait for 2 second here**#
                time.sleep(2) 
                
                # Asking the user to say "exit" or "stop" to exit or the city name of another city to get weather
                 
                speak("Say 'exit' or 'stop' or 'quit' to exit the program or say the city name of another city to get the weather")

    else:
            speak("Sorry, i am unable to understand you")
  
    
else:
    engine.say('Sorry, I did not understand')
        
