import speech_recognition as sr
import pyttsx3

# Those Code Are For "Voice Recognizer", "Text to Speech Initialize" and "Set Voice Property"
listener = sr.Recognizer()
assistant = pyttsx3.init()
voices = assistant.getProperty('voices')
assistant.setProperty('voices', voices[0].id)


# AI Convert Text to Spech (Speaking)
def speak(audio):
  assistant.say(audio)
  print('Trisha: ' + audio)
  assistant.runAndWait()

# AI Recognize Your Voice (Listening)
def take_command():
  try:
    with sr.Microphone() as source:
      print('listening...')
      voice = listener.listen(source)
      recognizer = listener.recognize_google(voice)
      recognizer = recognizer.lower()
      print(f'User: {recognizer}')
  except:
    return 'none'
  return recognizer

# Which Command Are Exist In this Program (Taking Command)
def run_assistant():

  speak('')
  while True:
    command = take_command().lower()

    if 'stop' in command:
      speak('Okay Sir! You Need Anything Else. Please Call Me.')
      break

    elif 'how' in command:
      speak('I am fine')

run_assistant()