import webbrowser
import speech_recognition as sr
import pyttsx3
import MusicLibrary
from OpenAi import ask_gpt

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            
            if text.lower() == "jarvis":
                speak("Yes, how can I assist you?")
                return ""  # Wait for actual command
            
            return text

        except sr.WaitTimeoutError:
            print("Listening timed out, no speech detected.")
            return ""
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
            return ""

def processcommand(command):
    print(command)
    if "open google" in command.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "play music" in command.lower():
        song = command.lower().replace("play music", "").strip()
        link = MusicLibrary.music.get(song)
        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I don't have '{song}' in my library.")
    else:
       gpt_reply = ask_gpt(command)
       if gpt_reply:
           print("Jarvis:", gpt_reply)
           speak(gpt_reply)
       else:
           speak("Sorry, I have no answer for that.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        command = listen()
        if command:
            processcommand(command)
