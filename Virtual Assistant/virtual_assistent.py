# Description: This is a Virtual Assistant program that gets the dat, current time, responds back with a random
#               greeting and returns information on a person.

# pip install pyaudio
# pip install SpeechRecognition
# pip install gTTS
# pip install wikipedia


# Import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import pyautogui
from time import sleep


# ignore any warning messages
warnings.filterwarnings('ignore')


# Record audio and return it as a string
def recordaudio():
    # Record the audio
    r = sr.Recognizer()  # Creating a recognizer object

    # Open the microphone and start recording
    with sr.Microphone() as source:
        print('Say something!')
        audio = r.listen(source)

    # Use Googles speech recogniton
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:  # Check for Unknown errors
        print('Google Speech Recognition could not understand the audio, unknown error')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error' + e)

    return data


# a function to get the virtual assistant response
def assistantresponse(text):

    print(text)

    # Convert the text to speech
    myobj = gTTS(text=text, lang='en', slow=False)

    # Save the convertet auidio to a file
    myobj.save('assistant_response.mp3')

    # Play the converted file
    os.system('start assistant_response.mp3')


# A function for wake word(s) or phrase
def wakeword(text):
    WAKE_WORDS = ['hey gideon', 'okay gideon', 'listen gideon']

    text = text.lower()

    # Check to see if the users command/text contains a wake word/phrase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    # If the wake word isn't found in the text from the loop and so it returns False
    return False


def alarmWord(text):
    ALARM_WORDS = ['alarm', 'help me', 'please help me']

    text = text.lower()

    # Check to see if the users command/text contains a alarm word/phrase
    for phrase in ALARM_WORDS:
        if phrase in text:
            return True

    # If the alarm word isn't found in the text from the loop and so it returns False
    return False


# A function to get the current date
def getDate():

    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    # A list of months
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                   'August', 'September', 'October', 'November', 'December']

    # A list of ordinal numbers
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12nd', '13th',
                    '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23th', '24th', '25th',
                    '26th', '27th', '28th', '29th', '30th', '31st']

    return 'Today is ' + weekday+' ' + month_names[monthNum - 1]+' the ' + ordinalNumbers[dayNum - 1]+'. '


# A function to return random greeting response
def greeting(text):

    # Greeting inputs
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'greetings', 'whats up', 'hello']

    #Greeting responeses
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']

    # if the users input is a greeting, then return a randomly chosen greeting response
    for word in text.split () :
        return random.choice(GREETING_RESPONSES) +'.'

    # if no greeting was detected then return an empty string
    return ''


# A function to get a persons first and last name from the text
def getPerson(text):

    wordList = text.split() #Splitting the text into a list of words

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' '+ wordList[i+3]

while True:

    # Record audio
    text = recordaudio()
    response = ''

    # Check for Alarm word/phrase
    if(alarmWord(text) == True):

        print("Alarm invoked")
        pyautogui.hotkey("Alt", "Tab")
        pyautogui.click(155, 109)
        sleep(0.5)
        pyautogui.typewrite(["Delete"])
        pyautogui.typewrite("0619224527")

    # Check for wake word/phrase
    if(wakeword(text) == True) :

        #Check for greeting by the user
        response = response + greeting(text)

        #Check for volume control
        if('volume up' in text):
            pyautogui.press("volumeup")
        if('volume down' in text):
            pyautogui.press("volumedown")
        if('mute' in text):
            pyautogui.press("volumemute")

        #Check to see if the user said anything having to do with the date
        if('date' in text):
            get_date = getDate()
            response = response + ' '+get_date

        #Check to see if the user said anything having to do with the time
        if('what time' in text):
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >=12:
                meridiem = 'p.m' # Post Meridiem (PM) after midday
                hour = now.hour -12
            else:
                meridiem = 'a.m' #Ante Meridiem (AM) before midday
                hour = now.hour
            #Convert minute into a proper string
            if now.minute < 10:
                minute = '0'+str(now.minute)
            else:
                minute = str(now.minute)

            response = response +''+'it is '+str(hour)+ ':'+ minute+ ' '+meridiem+' .'

        #Check to see if the user said 'who is'
        if('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response +' '+ wiki

        #Have the assistant respond back using audio and the text from response
        assistantresponse(response)