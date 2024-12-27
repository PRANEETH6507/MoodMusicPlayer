# Mood-Based Music Player 🎵

## What is this project?
This project is a Mood-Based Music Player that uses voice commands and sentiment analysis to detect your mood and play music tailored to it. It combines speech-to-text, sentiment analysis, and music playback functionalities into a single user-friendly application.

## Overview
This Python-based app detects your mood using voice commands and plays music that matches your emotional state. Built with libraries like VADER for sentiment analysis and Pygame for music playback, it’s a fun and interactive way to personalize your music experience.

## Features
- Real-time mood detection (Happy, Sad, Neutral) using voice input.
- Voice commands to control playback: Pause, Resume, Stop, Skip, Volume control.
- Simple user interface (UI) to display the current mood and song.                                                                      
                                                                                                                                        
## How does it work?
# 1.Speech Recognition:
 The app listens for voice input using your microphone.
 It transcribes the input into text using a Speech-to-Text API.
 
# 2.Sentiment Analysis:
The transcribed text is analyzed using the VADER Sentiment Analysis tool.
Based on the sentiment score, the app determines your mood:
Positive Sentiment → Happy
Negative Sentiment → Sad
Neutral Sentiment → Calm/Neutral

# 3.Music Recommendation and Playback:
It selects a song from a predefined music library categorized by mood.
The selected song is played using the Pygame Mixer.
You can control playback with voice commands like "pause," "resume," "stop," "skip," and adjust the volume with "volume up" or "volume down."
                                                                                                                                      
# 4.User Interface:
A simple UI displays the detected mood and the currently playing song.                                                                  
                                                                                                                                          
### How can I run it on my system?
## Prerequisites:
 # 1.Python: 
            Ensure Python 3.10 or later is installed on your system.
 # 2.Required Libraries: Install the dependencies:-
                                             bash: pip install pygame speechrecognition vaderSentiment tkinter                       
 # 3.Music Library: 
                   Prepare a local folder with songs organized by mood (e.g., happy, sad, neutral). Update the music_library_path in the code with the path to this folder.

## Steps to Run:
 # 1.Clone the Repository:
                                            bash:git clone https://github.com/YourUsername/MoodMusicPlayer.git
                                                 cd MoodMusicPlayer
 # 2.Run the Script:
        Execute the main script to launch the application:-
                                              bash:python main_script.py

 # 3.Provide Voice Commands:
                          Speak into your microphone when prompted.
                          The app will detect your mood and start playing music.
                          Use voice commands to control playback, adjust the volume, or stop the app.

 # 4.Enjoy:
      Watch the UI update with your detected mood and currently playing song.
      Sit back and enjoy mood-appropriate music!

### Technologies Used
    Python: Main development language.
    Pygame: For audio playback.
    SpeechRecognition: To capture and process voice input.
    VADER Sentiment Analysis: For detecting mood from voice commands.
    Tkinter: For the user interface.
