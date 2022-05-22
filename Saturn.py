import speech_recognition as sr
from time import ctime
import pyttsx3 as tts
import time
import os
from gtts import gTTS
import requests, json

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data

def respond(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")

def digital_assistant(data):
    if "how are you" in data:
        listening = True
        respond("I am well")

    if "what time is it" in data:
        listening = True
        respond(ctime())

    if "what is the recommended GPA for Harvard University" in data:
        listening = True
        respond("The recommended GPA is 4.18")

    if "what is the recommended GPA for Stanford University" in data:
        listening = True
        respond("The recommended GPA is 4.0")
    
    if "what is the recommended GPA for MIT" in data:
        listening = True
        respond("The recommended GPA is 4.17")
    
    if "what is the recommended GPA for UC Berkeley" in data:
        listening = True
        respond("The recommended GPA is 3.89")
    
    if "what is the recommended GPA for UCLA" in data:
        listening = True
        respond("The recommended GPA is 3.9")

    if "what is the recommended GPA for Yale University" in data:
        listening = True
        respond("The recommended GPA is 4.14")

    if "what is the recommended GPA for Columbia University" in data:
        listening = True
        respond("The recommended GPA is 4.12")

    if "what is the recommended GPA for Princeton University" in data:
        listening = True
        respond("The recommended GPA is 3.9")

    if "what is the recommended GPA for NYU" in data:
        listening = True
        respond("The recommended GPA is 3.69")

    if "what is the recommended GPA for UPenn" in data:
        listening = True
        respond("The recommended GPA is 3.9")

    if "what is the recommended GPA for University of Chicago" in data:
        listening = True
        respond("The recommended GPA is 4.48")

    if "what is the recommended GPA for Cornell University" in data:
        listening = True
        respond("The recommended GPA is 4.07")

    if "what is the recommended GPA for Duke University" in data:
        listening = True
        respond("The recommended GPA is 4.13")

    if "what is the recommended GPA for John Hopkins University" in data:
        listening = True
        respond("The recommended GPA is 3.92")

    if "what is the recommended GPA for USC" in data:
        listening = True
        respond("The recommended GPA is 3.79")

    if "what is the recommended GPA for Northwestern University" in data:
        listening = True
        respond("The recommended GPA is 4.10")

    if "what is the recommended GPA for Carnegie Melon" in data:
        listening = True
        respond("The recommended GPA is 3.84")

    if "what is the recommended GPA for University of Michigan" in data:
        listening = True
        respond("The recommended GPA is 3.88")

    if "what is the recommended GPA for Brown University" in data:
        listening = True
        respond("The recommended GPA is 4.08")

    if "what is the recommended GPA for Boston University" in data:
        listening = True
        respond("The recommended GPA is 3.71")

   
    if "what is the recommended sat for Harvard University" in data:
        listening = True
        respond("The recommended SAT score for Harvard University is in the range 1470-1570")

    if "what is the recommended sat for Stanford University" in data:
        listening = True
        respond("The recommended SAT score for Stanford University is in the range 1390-1540")

    if "what is the recommended sat for MIT" in data:
        listening = True
        respond("The recommended SAT score for MIT is in the range 1470-1570")

    if "what is the recommended sat for UC Berkeley" in data:
        listening = True
        respond("The recommended SAT score for UC Berkeley is in the range 1280-1490")

    if "what is the recommended sat for UCLA" in data:
        listening = True
        respond("The recommended SAT score for UCLA is in the range 1280-1490")
    
    if "what is the recommended sat for Yale" in data:
        listening = True
        respond("The recommended SAT score for Yale is in the range 1460-1600")

    if "what is the recommended sat for Columbia University" in data:
        listening = True
        respond("The recommended SAT score for Columbia University is in the range 1490-1580")

    if "what is the recommended sat for Princeton" in data:
        listening = True
        respond("The recommended SAT score for Princeton is in the range 1380-1540")

    if "what is the recommended sat for NYU" in data:
        listening = True
        respond("The recommended SAT score for NYU is in the range 1360-1500")

    if "what is the recommended sat for UPenn" in data:
        listening = True
        respond("The recommended SAT score for UPenn is in the range 1370-1520")

    if "what is the recommended sat for University of Chicago" in data:
        listening = True
        respond("The recommended SAT score for University of Chicago is in the range 1460-1560")

    if "what is the recommended sat for Cornell" in data:
        listening = True
        respond("The recommended SAT score for Cornell is in the range 1390-1530")

    if "what is the recommended sat for Duke" in data:
        listening = True
        respond("The recommended SAT score for Duke is in the range 1440-1580")

    if "what is the recommended sat for Johns Hopkins University" in data:
        listening = True
        respond("The recommended SAT score for Johns Hopkins University is in the range 1480-1560")

    if "what is the recommended sat for USC" in data:
        listening = True
        respond("The recommended SAT score for USC is in the range 1320-1480")

    if "what is the recommended sat for Northwestern University" in data:
        listening = True
        respond("The recommended SAT score for Northwestern University is in the range 1440-1540")

    if "what is the recommended sat for Carnegie Melon University" in data:
        listening = True
        respond("The recommended SAT score for Carnegie Melon University is in the range 1410-1540")

    if "what is the recommended sat for University of Michigan" in data:
        listening = True
        respond("The recommended SAT score for University of Michigan is in the range 1380-1540")

    if "what is the recommended sat for Brown University" in data:
        listening = True
        respond("The recommended SAT score for Brown University is in the range 1450-1570")

    if "what is the recommended sat for Boston University" in data:
        listening = True
        respond("The recommended SAT score for Boston University is in the range 1300-1500")

    if "what is Harvard University's best major" in data:
        listening = True
        respond("Harvard's best is in Economics")

    if "what is Standford University's best major" in data:
        listening = True
        respond("Stanford's best is in Computer Science")

    if "what is MIT's best major" in data:
        listening = True
        respond("MIT's best is in Engineering")

    if "what is UC Berkeley's best major" in data:
        listening = True
        respond("UC Berkeley's best is in Computer Science")

    if "what is Yale University's best major" in data:
        listening = True
        respond("Yale's best is in Economics")

    if "what is Columbia University's best major" in data:
        listening = True
        respond("Columbia University's best is in Political Science")

    if "what is Princeton's best major" in data:
        listening = True
        respond("Princeton's best is in Political Science")

    if "what is NYU's best major" in data:
        listening = True
        respond("NYU's best is in Business")

    if "what is UPenn's best major" in data:
        listening = True
        respond("UPenn's best is in Business")

    if "what is University of Chicago's best major" in data:
        listening = True
        respond("University of Chicago's best is in Economics")

    if "what is Cornell University's best major" in data:
        listening = True
        respond("Cornell University's best is in Computer Science")

    if "what is Duke University's best major" in data:
        listening = True
        respond("Duke University's best is in Political Science")

    if "what is John Hopkin's best major" in data:
        listening = True
        respond("John Hopkin's best is in Medicine")

    if "what is USC's best major" in data:
        listening = True
        respond("USC's best is in Film")

    if "what is Northwestern University's best major" in data:
        listening = True
        respond("Northwestern University's best is in Communications")

    if "what is Carnegie Melon's best major" in data:
        listening = True
        respond("Carnegie Melon's best is in Computer Science")

    if "what is University of Michigan's best major" in data:
        listening = True
        respond("University of Michigan's best is in Engineering")

    if "what is brown University's best major" in data:
        listening = True
        respond("Brown University's best is in English")

    if "what is boston University's best major" in data:
        listening = True
        respond("Boston University's best is in Criminal Justice")


    

    if "stop listening" in data:
        listening = False
        print('Listening stopped')
        return listening
    return listening
def sayQuestions():
    global recognizer
    
    sr.say("What is your college question?")
    sr.runAndWait()

    done = False
    while not done:
        try:

            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                answer = recognizer.recognize_google(audio)
                answer = answer.lower()

        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            sr.say("I did not understand you! Please try again!")
            sr.runAndWait()

mappings = {
  
  "recommendedGPA": sayQuestions
}
time.sleep(2)
respond("Hi Shravan, what can I do for you?")
listening = True
while listening == True:
    data = listen()
    listening = digital_assistant(data)