import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import subprocess


print('Loading your AI Health Assistant - Amante')

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI Health Assistant Amante")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how you feel")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Amante is shutting down,Good bye')
            print('your personal assistant Amante is shutting down,Good bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "Good" or 'fine' or 'well' in statement:
            speak('Okay, please tell me whenever you feel sick, I am here to help you stay healthy.')
            print('Okay, please tell me whenever you feel sick, I am here to help you stay healthy.')

        elif "not well" or "sick" or "ill" or "not good" or "bad" in statement:
            print('What kind of sickness do you have?')
            speak('What kind of problems are you having?')

        elif "fever" in statement:
            speak('I am very sorry to hear that')
            print('I am very sorry to hear that')
            print('Do you only have only fever?')
            speak('Do you only have only fever?')
            if "no" in statement:
                speak("If you have a fever that lasts for more than 3 days, consult a doctor. A paracetamol may help.")
            else:
                speak('what other problem do you have?')
                print('what other problem do you have?')
                if "cold" or "cough" or "congestion" or "sore throat" in statement:
                    speak('You have symptoms of common cold')
                    print('Maybe you have common cold')
                    speak("Generally a common cold or flu recovers on its own within a short period of time. However, home remedies like ginger, garlic and honey helps")
                    print("Generally a common cold or flu recovers on its own within a short period of time. However, home remedies like ginger, garlic and honey helps")
                    speak('If you have severe cough, try having some cough syrup')
                    print('In case of extreme cough, some cough syrup might help')
                    print('If you problem persists for long, consult a doctor')
                    speak('If you problem persists for long, consult a doctor')



