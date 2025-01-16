import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn.")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
    elif "open chatgpt" in command:
        webbrowser.open("https://chatgpt.com")
        speak("Opening YouTube.")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    # Use a single microphone instance
    with sr.Microphone() as source:
        print("recognizing...")
        recognizer.adjust_for_ambient_noise(source, duration=2)

        while True:
            try:
                print("Listening for wake word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
                wake_word = recognizer.recognize_google(audio).lower()

                if "jarvis" in wake_word:
                    speak("Yes sir.")
                    print("Listening for your command...")
                    audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
                    command = recognizer.recognize_google(audio)
                    print(f"You said: {command}")
                    processCommand(command)
            except Exception as e:
                print(f"An error occurred: {e}")
