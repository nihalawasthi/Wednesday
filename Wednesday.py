import google.generativeai as genai
import pyttsx3
import os
import platform
import getpass


os.system("type path_to_wed.txt")

api_key = "YOUR_API_KEY_FOR_GEMINI"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


app_paths = {
    "files": "explorer",
    "cp": "control",
    "taskmgr": "taskmgr",
    "notepad": "notepad",
    "calculator": "calc",
    "spotify": "Spotify.exe",
    "browser": "Thorium.exe",
    "cmd": "cmd",
    "vscode": "code",
    "whatsapp": "whatsapp",
}

commands = ["date", "time", "wikipedia", "open app",
            "open mail", "open youtube", "gemini", "exit"]


def date_():
    if platform.system() == "Windows":
        os.system("date /T")
    elif platform.system() == "Linux":
        os.system("date +'%A, %B %d, %Y'")


def time_():
    if platform.system() == "Windows":
        os.system("time /T")
    elif platform.system() == "Linux":
        os.system("date +%T")


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen(user):
    user_input = input(f"{user}: ").lower()
    return user_input


def wish_me(user):
    if not user:
        user = input("Username cannot be empty. Please enter your username: ")
    if user=="Admin_User":
        admin_access()
    else:
        speak(f"Hello {user}")
        print(f"Hello {user}")


def admin_access():
    speak("Enter your passcode")
    pass_code = getpass.getpass(" ")
    if pass_code.lower() != "Set_Pass_code":
        print("Incorrect passcode. Access denied.")
        raise SystemExit()
    else:
        print(f"Admin access granted, Welcome Master.")
        speak(f"Admin access granted, Welcome Master.")


def output(statement, user):
    if not statement:
        print("Prompt must not be empty")
        return
    
    if "help" in statement or "list cmd" in statement:
        speak("Available commands are: ")
        print("Available commands: ", commands)
        speak(commands)
        
    if "shutdown" in statement:
        if platform.system() == "Windows":
            os.system("shutdown /s /t 1")
        elif platform.system() == "Linux":
            os.system("sudo shutdown -h now")
            
    elif "restart" in statement:
        if platform.system() == "Windows":
            os.system("shutdown /r /t 1")
        elif platform.system() == "Linux":
            os.system("sudo reboot")
            
    elif "sleep" in statement:
        if platform.system() == "Windows":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif platform.system() == "Linux":
            os.system("sudo systemctl suspend")
            
    elif "wikipedia" in statement:
        query = statement.replace("wikipedia", "")
        print(f"Searching Wikipedia for '{query}'...")
        
    elif "open app" in statement:
        app_name = statement.replace("open app", "").strip()
        if app_name in app_paths:
            os.system(app_paths[app_name])
        else:
            print(f"App '{app_name}' not found.")
            
    elif "open kali" in statement:
        os.system("kali")
        
    elif "open youtube" in statement:
        if platform.system() == "Windows":
            os.system("start https://www.youtube.com")
        elif platform.system() == "Linux":
            os.system("xdg-open https://www.youtube.com")
    
    elif "open mail" in statement:
        if platform.system() == "Windows":
            os.system("start https://mail.google.com")
        elif platform.system() == "Linux":
            os.system("xdg-open https://mail.google.com")
            
    elif "time" in statement:
        str_time = str(time_())
        speak(f"The time is {str_time}")
        
    elif "date" in statement:
        str_date = str(date_())
        speak(f"The date is {str_date}")
        
    elif "gemini" in statement:
        print("Initiating Gemini...")
        speak("Initiating Gemini")
        print("Enter 'exit' to quit Chat")
        while True:
            user_input = input(f"{user}: ").lower()
            
            if user_input == "exit":
                print("Wednesday: Exiting gemini")
                speak("Wednesday: Exiting gemini")
                break
            if not user_input:
                continue
            try:
                response = model.generate_content(user_input)
                reply = response.text.strip()
                print(f"Wednesday: {reply}\n")
                for line in reply.splitlines():
                    speak(line)
            except Exception as e:
                print(f"An error occurred: {e}")
                
    elif "who are you" in statement or "what can you do" in statement:
        speak(
            "I am Wednesday, your personal assistant. I am still under development, but I can perform various tasks like opening applications, searching the web, playing music, and taking notes."
        )
        
    elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
        speak("I was created by Nihal.")
        
    elif "exit" in statement:
        print("Wednesday is shutting down, Goodbye")
        speak("Wednesday is shutting down, Goodbye")
        raise SystemExit()
    
    else:
        response = model.generate_content(statement)
        reply = response.text.strip()
        print(f"Wednesday: {reply}\n")
        for line in reply.splitlines():
            speak(line)

print("Unleashing Wednesday...")
speak("Unleashing Wednesday...")
user = input("Please tell your identity: ")

if not user:
    user = input("Please tell your identity : ")
    
print(f"User: {user}\n")
wish_me(user)

while True:
    statement = listen(user)
    output(statement, user)
