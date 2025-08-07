import os
import json
import requests
import speech_recognition as sr
import pyttsx3
import webbrowser
import shutil
import datetime

# ✅ API keys
SERP_API_KEY = "f9e4fc97ea992db39aaf6fecfce26dafc2688c055df3ab3841800a2d2e6f1dc"
OPENROUTER_API_KEY ="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"

# ✅ Text-to-Speech setup
engine = pyttsx3.init()
def speak(text):
    print(f"🗣 {text}")
    engine.say(text)
    engine.runAndWait()

# ✅ Google Search bar
def google_search(query):
    print(f"🔎 Searching Google: {query}")
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERP_API_KEY,
        "num": 5
    }
    try:
        response = requests.get("https://serpapi.com/search", params=params, timeout=10)
        data = response.json()
        snippets = []
        for result in data.get("organic_results", []):
            snippet = result.get("snippet") or result.get("title")
            if snippet:
                snippets.append(snippet.strip())
        return snippets if snippets else ["No relevant results found."]
    except Exception as e:
        print(f"❌ SerpAPI error: {e}")
        return ["Unable to retrieve current data."]

# ✅ DeepSeek AI via OpenRouter
def chat_with_ai(prompt):
    print("🧠 Asking DeepSeek AI...")
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Jarvis Voice Assistant",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek/deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are Jarvis, a helpful assistant providing real-time and accurate answers using internet data."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                                 headers=headers, json=data, timeout=15)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"❌ DeepSeek Error: {e}")
        return "Sorry, I couldn't connect to the AI service."

# ✅ Open URL in Firefox
def open_in_firefox(url):
    firefox_path = shutil.which("firefox")
    if firefox_path:
        webbrowser.register("firefox", None, webbrowser.BackgroundBrowser(firefox_path))
        webbrowser.get("firefox").open(url)
        speak("Opening in Firefox.")
    else:
        speak("Firefox not found. Opening in default browser.")
        webbrowser.open(url)

# ✅ Speech recognition
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""

# ✅ Perform system-level tasks
def handle_system_command(command):
    if "shutdown" in command:
        speak("Shutting down your computer.")
        os.system("shutdown /s /t 1")
    elif "restart" in command or "reboot" in command:
        speak("Restarting your computer.")
        os.system("shutdown /r /t 1")
    elif "log off" in command or "sign out" in command:
        speak("Logging you off.")
        os.system("shutdown /l")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    else:
        return False
    return True

# ✅ Main Jarvis loop
def main():
    speak("Hello, I am Sunil assistanca. Say 'Jarvis' to activate me.")
    while True:
        print("🕒 Waiting for wake word 'Jarvis'...")
        wake = listen()
        if "jarvis" in wake:
            speak("Sunil, what can I do for you?")
            command = listen()
            print(f"🗣 Heard: {command}")

            # System command?
            if handle_system_command(command):
                continue

            # Website commands
            websites = {
                "open youtube": "https://www.youtube.com",
                "open google": "https://www.google.com",
                "open facebook": "https://www.facebook.com",
                "open instagram": "https://www.instagram.com"
            }

            for key in websites:
                if key in command:
                    speak(f"Opening {key.split()[-1].capitalize()}...")
                    open_in_firefox(websites[key])
                    break
            else:
                # Real-time web search + AI summarization
                speak("Searching for the latest answer...")
                search_results = google_search(command)
                context = "\n".join(search_results[:3])
                prompt = f"User asked: {command}\n\nTop search results:\n{context}\n\nAnswer concisely and helpfully:"
                reply = chat_with_ai(prompt)
                speak(reply)

if __name__ == "__main__":
    main()
