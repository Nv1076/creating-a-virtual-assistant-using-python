import pyttsx3

import datetime

import speech_recognition as sr

import wikipedia

import webbrowser

import os

import smtplib



engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

#print(voices[1].id) 

engine.setProperty('voice', voices[0].id)



def speak(audio):

    engine.say(audio)

    engine.runAndWait()



def wishMe():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:

        speak("good Morning sir!")

        print("good Morning sir!")



    elif hour>=12 and hour<18:

        speak("good Afternoon sir!")

        print("good Afternoon sir!")



    else:

        speak("good Evening sir!")

        print("good Evening sir!")  



    speak("this is jarvis here. how may i help you?")  

    print("computer: This is jarvis here. how may i help you?")  



def takeCommand():

   

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        r.pause_thresold = 1

        audio = r.listen(source)





    try:

        print("recognizing...")

        query = r.recognize_google(audio, language='en-in')

        print(f"user said: {query}\n")





    except Exception as e:

        # print(e)

        print("say that again...")

        return "none"

    return query



    def sendEmail(To, content):

        server = smtplib.SMTP(smtp.gmail.com, 587)

        server.ehlo()

        server.starttls()

        server.login('student.nitin1076@gmail.com', '@nitin2003')

        server.sendmail('student.nitin1076@gmail.com', to, content)

        server.close





if __name__ == "__main__":

     wishMe()

     while True:

            query = takeCommand().lower()



            # logic for exicuting task based queries

            if 'wikipedia' in query:

                speak('searching wikipedia...')

                query = query.replace("wikipedia", "")

                result =  wikipedia.summary(query)

                speak("According to wikipedia")

                print(f"computer: {result}")

                speak(result)



            elif 'open youtube' in query:

                speak("Opening Youtube")

                print("computer: Opening Youtube")

                webbrowser.open("youtube.com")



            elif 'open google' in query:

                speak("opening Google")

                print("Computer: Opening Google")

                webbrowser.open("google.com")



            elif 'play music' in query:

                speak("playing music sir.")

                print("Computer: playing music sir.")

                music_dir = "C:\\Users\\rishikesh\\Desktop\\songs"

                songs = os.listdir(music_dir)

                #print(songs)

                os.startfile(os.path.join(music_dir, songs[0]))



            elif 'the time' in query:

                strTime = datetime.datetime.now().strftime("%H:%M:%S")

                speak(f"sir, the time is {strTime}")

                print(f"Computer: {strTime}")



            elif 'open code' in query:

                speak("opening code sir.")

                print("computer: opening visual studio code sir")

                codePath = "C:\\Users\\rishikesh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\visual studio.exe"

                os.startfile(codePath)

            

            elif 'send email' in query:

                try:

                    speak("what should i say?")

                    print("Computer: what should i say?")

                    content = takeCommand()

                    to = 'student.nitin1076@gmail.com'

                    speak("hey nitin. email has been sent!")

                    print("Computer: hey nitin. email has been sent!")

                except Exception as e:

                    print(e)

                    speak("sorry nitin. I am not able to send this email.")

                    print("Computer: sorry nitin. I am not able to send this email.")



            elif 'the temprature' in query:

                 pass