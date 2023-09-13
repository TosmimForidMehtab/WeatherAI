import speech_recognition as sr

# TODO: Support voice input in Gujrati
def speechToText():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1.1)
        print("Listening...")
        audio = recognizer.listen(source)
        print("Processing...")

        try:
            text = recognizer.recognize_google(audio)
            if text is not None:
                text = text.lower()
                return text
        except sr.UnknownValueError:
            print('Sorry I could not understand the audio')
        except sr.RequestError:
            print("API unavailable or unresponsive")

if __name__ == "__main__":
    result = speechToText()
    print(result)