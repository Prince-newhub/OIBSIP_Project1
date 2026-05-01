# OIBSIP_Project1
Python Voice Assistant using Speech Recognition
Author -Prince Suresh Vishwakarma

Here's a professional `README.md` file for your Voice Assistant project:

```markdown
# 🎤 Voice Assistant

A Python-based voice assistant that can listen to your commands, respond with speech, and perform various tasks like telling the time, searching Wikipedia, playing YouTube videos, and more.

## ✨ Features

- 🎙️ **Voice Recognition** – Listens to your commands using a microphone
- 🗣️ **Text-to-Speech** – Responds with spoken answers
- 🕒 **Time & Date** – Tells current time and date
- 📚 **Wikipedia Search** – Answers "who is" questions
- 🎵 **YouTube Playback** – Plays songs directly from YouTube
- 🌐 **Web Search** – Performs quick Google searches
- 🔇 **Noise Reduction** – Adjusts for ambient noise for better accuracy

## 🛠️ Requirements

- Python 3.6 or higher
- Internet connection (for Google speech recognition & web search)
- Working microphone

## 📦 Installation

1. **Clone or download** this repository

2. **Install required packages**:

```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia-api pyaudio
```

> **Note for Windows users**: `pyaudio` can be installed via:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```
>
> **Note for Linux users**: You may need to install PortAudio first:
> ```bash
> sudo apt-get install portaudio19-dev python3-pyaudio
> pip install pyaudio
> ```

## 🚀 Usage

Run the assistant:

```bash
python voice_assistant.py
```

Once started, the assistant will say "Assistant is ready" and start listening.

## 🎯 Available Commands

| Command Example | Action |
|----------------|--------|
| "hello" | Assistant greets you |
| "what is the time" | Tells current time |
| "today's date" | Tells current date |
| "who is Einstein" | Searches Wikipedia for information |
| "search Python tutorial" | Performs Google search |
| "play Shape of You" | Plays the song on YouTube |
| "exit" or "stop" | Stops the assistant |

## 📁 File Structure

```
voice-assistant/
├── voice_assistant.py    # Main assistant code
└── README.md             # Project documentation
```

## ⚙️ How It Works

1. **Listening Phase** – Captures audio from microphone
2. **Recognition Phase** – Converts speech to text using Google's API
3. **Processing Phase** – Matches command to actions
4. **Execution Phase** – Performs requested action and responds

## ⚠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| "Could not understand audio" | Speak clearly and check microphone |
| "Please check your internet connection" | Ensure stable internet connection |
| PyAudio installation fails on Windows | Use pipwin as described above |
| Microphone not working | Check system microphone permissions |

## 🔧 Customization

You can easily extend the assistant by adding new commands in the `run_assistant()` function:

```python
elif "your command" in command:
    # Add your action here
    speak("Your response here")
```

## 📝 Notes

- The assistant uses Google's free speech recognition API (requires internet)
- Wikipedia search returns a brief summary (2 sentences)
- YouTube playback opens in your default browser
- Listening timeout is set to 10 seconds with a 7-second phrase limit

## 📄 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Feel free to fork this project, add new features, and submit pull requests. Possible enhancements:
- Add weather information
- Add email sending capability
- Add reminder/alarm functionality
- Add offline recognition support
- Add GUI interface

---

**Enjoy your voice assistant!** 🗣️💬
```

This README provides:
- Clear project overview
- Installation instructions for different OS
- Command reference table
- Troubleshooting guide
- Customization tips
- Future enhancement ideas

Save this as `README.md` in the same directory as your Python script.
