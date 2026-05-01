import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

# Initialize
listener = sr.Recognizer()
engine = pyttsx3.init()

# Improve listening
listener.pause_threshold = 1

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            
            # Reduce background noise
            listener.adjust_for_ambient_noise(source, duration=1)
            
            audio = listener.listen(source, timeout=10, phrase_time_limit=7)
            
            print("Recognizing...")
            command = listener.recognize_google(audio)
            command = command.lower()
            
            print("You said:", command)
            return command

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        speak("Sorry, I didn't catch that")
        return ""

    except sr.RequestError:
        print("❌ Internet issue")
        speak("Please check your internet connection")
        return ""

    except Exception as e:
        print("❌ Error:", e)
        return ""

def run_assistant():
    command = take_command()

    if command == "":
        return

    if "hello" in command:
        speak("Hello, how can I help you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("Current time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime('%d %B %Y')
        speak("Today's date is " + date)

    elif "who is" in command:
        try:
            person = command.replace("who is", "")
            info = wikipedia.summary(person, 2)
            speak(info)
        except:
            speak("Sorry, I couldn't find information")

    elif "search" in command:
        topic = command.replace("search", "")
        speak("Searching for " + topic)
        pywhatkit.search(topic)

    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that")

# Main loop
print("🎤 Voice Assistant Started...")
speak("Assistant is ready")

while True:
    run_assistant()