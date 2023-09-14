import pyttsx3 as tts
import audioToText as at
import sys
import random
import checkinWeather as ciw
import time 

engine = tts.init()
engine.setProperty("rate", 150)
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
def processor():
    greeting = ['Hey, how can I help you?', 'hello, What can I do for you?', 'Hi, What can I help you with?', 'Hey What can I do for you?', 'Hello mate, How can I help you?']

    questions1 = ['For which city do you want to know the weather?', 'Provide the city name to know weather info', 'City name please', 'for which city can I help you with?', 'Please say the name of the city for which you want to know the weather']

    #========================Constants End============================================

    # Generate random number in the range of 0 to 4
    index = random.randint(0, len(greeting)-1)
    wake = at.speechToText()

    # Convert text to lowercase
    # if wake is not None:
    #     wake = wake.lower()
    # else:
    #     # exit the program
    #     sys.exit()
    while(wake is None):
        speak("Sorry, i did not understand, please say it again!")
        wake = at.speechToText()
        if(checkExit(wake)):
            speak("Thank you for using Vortex! Hope to meet you soon!,Bye!")
            sys.exit()


    while('vortex' not in wake):
        speak("Sorry, i did not understand, please say it again!")
        wake = at.speechToText()
        if(checkExit(wake)):
            speak("Thank you for using Vortex! Hope to meet you soon!,Bye!")
            sys.exit()
    
    else:
        speak(greeting[index])
        
        reply1 = at.speechToText()
        
        while('weather' not in reply1):
            speak("Sorry, i did not understand, please say it again!")
            reply1 = at.speechToText()
            if(checkExit(reply1)):
                speak("Thank you for using Vortex! Hope to meet you soon!,Bye!")
                sys.exit()

        else:
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
                    time.sleep(1.2) 
                    
                    # Asking the user to say "exit" or "stop" to exit or the city name of another city to get weather
                    
                    speak("Say 'exit' or 'stop' or 'quit' to exit the program or say the city name of another city to get the weather")
            
