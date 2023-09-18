import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass


def WishME():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning SIR!")
    elif hour >= 12 and hour < 18:
        speak("Good After Noon SIR")
    else:
        speak("Good Evening SIR")
    speak("hello Sir !, i am JARVAS . YOUR Ai ASSISTANT how i can help you? ")
    


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f" you Say:{query}\n")
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "none"
    return query


if __name__ == "__main__":
    WishME()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            print(wikipedia)
            speak("Sir!! just give me a minute  i am searching for this ")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Sir!! just give me a second  i am opening youtube ")
            webbrowser.open('https://www.youtube.com')
        elif 'open google' in query:
            speak("Sir!! just give me a second  i am opening Google ")
            webbrowser.open('https://www.google.com')
        elif 'open chat gpt' in query:

            speak("Sir!! just give me a second  i am opening vscode ")
            webbrowser.open('https://chat.openai.com')
        elif 'open stack overflow' in query:
            speak("Sir!! just give me a second  i am opening Stackoverflow ")
            webbrowser.open('https://stackoverflow.com')
        elif 'play music' in query:
            music_dir = 'F:\\\My mobile data\\zapya.music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir! the time is {strtime}")
            print(strtime)
        elif 'the code' in query:
            codepath = '"C:\\Users\\SoNiC\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codepath)
        # elif ' send email to Aqib' in query:
        #     try:
        #         speak("what should I say?")
        #         content=takeCommand()
        #         to='kfueit2742@gmail.com'

        # else:
        #     speak("Sorry Sir!!this not in my wikipedia")
