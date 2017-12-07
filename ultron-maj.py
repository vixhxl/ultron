import speech_recognition
import pyttsx
import time
import datetime
import myapps 
import gsearch
import mywiki
import myweather
import mymusic

text_speech = pyttsx.init('sapi5')
text_speech.setProperty('rate', 150)

def say(text):

        text_speech.say(text)
        text_speech.runAndWait()

speech_identifier = speech_recognition.Recognizer()


def phrase():

        with speech_recognition.Microphone() as source:
                speech_identifier.adjust_for_ambient_noise(source)
                audio = speech_identifier.listen(source)

        try:
                return speech_identifier.recognize_google(audio)

        except speech_recognition.UnknownValueError:
                print("I'm waiting for your command")


        return ""

localtime = time.asctime( time.localtime(time.time()) )


now = datetime.datetime.now()
hr=now.hour

guest = "say hello to "
google = "Google about "
search = "search for "
wiki = "Wiki about "
wiki1 = "tell me about "
wiki2 = "who is "
wiki3 = "what is an "
wiki4 = "what is a "
weather = "tell me weather forecast of "
status = "how is the weather in "
temp = "what is the temperature in "
wspeed = "what is the wind speed in "
humidity = "what is the humidity in "
pressure = "how much is the weather pressure in "

if hr < 12:
    print("Good moring sir. Have a nice day")
    say("good moring sir. Have a nice day")
elif hr >= 12 and hr < 17:
    print("Good afternoon sir")
    say("good afternoon sir")
elif hr >= 17 and hr <= 19:
    print("Good Evening Boss")
    say("good evening boss")

say("Welcome!")
say("I'm Ultron, An Voice Assistant Artificial Intelligence")
#say("I'm programmed to make your work easier")
say("And I'm ready for your service")

print("\n# Start speaking to Ultron")

while 1:

        str=phrase()

        #say(str)
        print (str)
        
        if str == "hello" or str == "hi":
                print("hello sir\n")
                say("hello sir")

        elif str == "Ultron you there" or str == "there" or str == "are you there":
                print("Yes sir, I am at your service \n")
                say("Yes sir, I am at your service ")

        elif str == "Ultron":
                print("yes sir\n")
                say("yes sir")

        elif str == "hey":
                print("sir\n")
                say("sir")

        elif str == "what time is it" or str == "tell me time" or str == "what's the time" or str == "time" or str == "what is today" or str == "what's today" :
                print(localtime +"\n")
                say(localtime)

        elif str == "you are awesome":
                print("thank you sir, it's all your credit\n")
                say("thank you sir, it's all your credit")

        elif str == "bye" or str == "buy" or str == "break" or str == "bye Ultron" or str == "buy Ultron" or str == "brake" or str == "terminate":
                if hr >= 20 and hr <=24:
                    print("Good night sir\n")
                    say("Good night sir")
                else:
                    print("see you again sir\n")
                    say("see you again sir")
                break

        elif str == "how are you":
                print("I'm good sir. How are you?\n")
                say("I'm good sir. How are you?")

        elif str == "great" or str == "nice" or str == "fine" or str == "good" or str == "ok" or str == "okay" or str == "alright" or str == "cool":
                print("sir\n")
                say("sir")

        elif str == guest+str[13:] :  #say hello to ------
                print("hello "+str[13:] +"\n")
                say("hello "+str[13:])

        elif str == google+str[13:] :
            say("here we go")
            gsearch.search(str[13:])

        elif str == search+str[11:] :
            say("I'm on it sir")
            gsearch.search(str[11:])

        elif str == "open calculator" or str == "open the calculator" or str == "launch calculator":
            say("opening calculator")
            myapps.calc()

        elif str == "open Notepad" or str == "launch Notepad":
            say("opening notepad")
            myapps.notepad()

        elif str == "open MS Word" or str == "launch MS Word":
            say("yes sir")
            myapps.msword()

        elif str == "open MS Excel" or str == "launch MS Excel":
            say("here it is")
            myapps.msexcel()

        elif str == "open MS PowerPoint" or str == "launch MS PowerPoint":
            say("sure sir")
            myapps.msppt()

        elif str == "open paint" or str == "launch paint" or str == "open Paint":
            say("yes sir")
            myapps.mspaint()

        elif str == wiki+str[11:] :
            say("yes sir")
            data = mywiki.wiki(str[11:])
            print (data+"\n")
            #time.sleep(5)
            say(data)

        elif str == wiki1+str[14:] :
            say("sure sir")
            data = mywiki.wiki(str[14:])
            #time.sleep(5)
            print data+"\n"
            say(data)

        elif str == wiki2+str[7:] :
            say("I'm searching the web")
            data = mywiki.wiki(str[7:])
            #time.sleep(5)
            print data+"\n"
            say(data)

        elif str == wiki3+str[11:] :
            say("I'm on it")
            data = mywiki.wiki(str[11:])
            #time.sleep(5)
            print data+"\n"
            say(data)

        elif str == wiki4+str[10:] :
            say("yes sir")
            data = mywiki.wiki(str[10:])
            #time.sleep(5)
            print data+"\n"
            say(data)

        elif str == weather+str[28:] :
            say("yes sir")
            report = myweather.completeWeather(str[28:])
            print(report+"\n")
            say(report)

        elif str == status+str[22:] :
            status = myweather.statusWeather(str[22:])
            print(status+"\n")
            say(status)

        elif str == temp+str[27:] :
            temp = myweather.tempWeather(str[27:])
            print(temp+"\n")
            say(temp)

        elif str == wspeed+str[26:]:
            wspeed = myweather.wspeedWeather(str[26:])
            print(wspeed+"\n")
            say(wspeed)

        elif str == humidity+str[24:]:
            humdty = myweather.humidityWeather(str[24:])
            print(humdty+"\n")
            say(humdty)

        elif str == pressure+str[36:] :
            press = myweather.pressureWeather(str[36:])
            print(press+"\n")
            say(press)

        elif str == "play" or str == "play the song" or str == "play a song" or str == "play my music" or str == "play music" :
                say("yes sir")
                mymusic.playsong()

        elif str == "pause" or str == "pause the song" :
                say("pausing the song")
                mymusic.pausesong()

        elif str == "unpause" or str == "resume" or str == "resume the song" :
                say("resuming the song")
                mymusic.unpausesong()

        elif str == "stop" or str == "stop my music" :
                say("as you say")
                mymusic.stopsong()

        
