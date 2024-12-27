import os
import random
import pygame
import threading
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
import tkinter as tk
from tkinter import font

# Path to the music library
music_library_path = r"C:\Users\Lenovo\Documents\PROJECTS\MoodMusicPlayer\music_library"

# Global control variables
stop_music_flag = False
pause_music_flag = False
skip_song_flag = False
volume_level = 0.5  # Default volume
current_song = None
song_history = []

# Initialize pygame mixer once at the beginning
pygame.mixer.init()

# Function to convert speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for voice commands... Please speak now.")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10)
            text = recognizer.recognize_google(audio)
            return text.lower()  # Return in lowercase for easy comparison
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None

# Function to analyze sentiment using VADER
def analyze_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    if scores['compound'] > 0.3:
        mood = "Happy"
    elif scores['compound'] < -0.3:
        mood = "Sad"
    else:
        mood = "Neutral"
    return mood

# Function to play music
def play_music(mood):
    global stop_music_flag, skip_song_flag, pause_music_flag, volume_level, current_song, song_history

    mood_to_folder = {
        "Happy": "happy",
        "Sad": "sad",
        "Neutral": "neutral"
    }

    folder = mood_to_folder.get(mood)
    if not folder:
        return

    folder_path = os.path.join(music_library_path, folder)
    if not os.path.exists(folder_path):
        return

    music_files = [f for f in os.listdir(folder_path) if f.endswith((".mp3", ".wav"))]
    if not music_files:
        return

    pygame.mixer.music.set_volume(volume_level)

    # Ensure a new song starts and the UI is updated
    current_song = random.choice(music_files)
    music_file_path = os.path.join(folder_path, current_song)
    song_history.append(current_song)

    pygame.mixer.music.load(music_file_path)
    pygame.mixer.music.play()

    # Update UI with the current mood and song
    update_ui(mood, current_song)

    while pygame.mixer.music.get_busy() or pause_music_flag:
        if stop_music_flag or skip_song_flag:
            pygame.mixer.music.stop()
            break

# Function to handle volume adjustments
def adjust_volume(action):
    global volume_level
    if action == "up" and volume_level < 1.0:
        volume_level += 0.1
    elif action == "down" and volume_level > 0.0:
        volume_level -= 0.1
    pygame.mixer.music.set_volume(volume_level)

# Function to handle voice commands
def handle_voice_commands():
    global pause_music_flag, stop_music_flag, skip_song_flag
    print("Listening for voice commands...")
    command = speech_to_text()
    if not command:
        return

    print(f"Command received: {command}")

    if "happy" in command:
        play_music("Happy")
    elif "sad" in command:
        play_music("Sad")
    elif "neutral" in command:
        play_music("Neutral")
    elif "pause" in command:
        pause_music_flag = True
        pygame.mixer.music.pause()
    elif "resume" in command or "play" in command:
        pause_music_flag = False
        pygame.mixer.music.unpause()
    elif "stop" in command:
        stop_music_flag = True
        pygame.mixer.music.stop()
    elif "skip" in command:
        skip_song_flag = True
    elif "volume up" in command:
        adjust_volume("up")
    elif "volume down" in command:
        adjust_volume("down")
    elif "history" in command:
        print(f"Recently played songs: {song_history}")
    elif "exit" in command:
        stop_music_flag = True
        root.quit()

# Thread to handle voice commands continuously
def listen_for_commands():
    while not stop_music_flag:
        handle_voice_commands()

# Update the UI with current mood and song
def update_ui(mood, song):
    mood_label.config(text=f"Current Mood: {mood}")
    song_label.config(text=f"Now Playing: {song}")
    print(f"UI Updated - Mood: {mood}, Song: {song}")  # Debugging line

# Tkinter UI Setup
root = tk.Tk()
root.title("Mood Music Player")
root.geometry("500x500")
root.configure(bg="#F0F0F0")

# Add a custom font
custom_font = font.Font(family="Helvetica", size=12)

# Labels
title_label = tk.Label(root, text="Mood Music Player", font=("Helvetica", 20, 'bold'), fg="#333", bg="#F0F0F0")
title_label.pack(pady=20)

# Display current mood
mood_label = tk.Label(root, text="Current Mood: None", font=("Helvetica", 16), fg="#333", bg="#F0F0F0")
mood_label.pack(pady=10)

# Display current song
song_label = tk.Label(root, text="Now Playing: None", font=("Helvetica", 16), fg="#333", bg="#F0F0F0")
song_label.pack(pady=10)

# Buttons for UI actions
voice_button = tk.Button(root, text="Give Voice Command", command=handle_voice_commands, width=20, font=custom_font, bg="#2196F3", fg="white")
voice_button.pack(pady=20)

exit_button = tk.Button(root, text="Exit", command=root.quit, width=20, font=custom_font, bg="#B71C1C", fg="white")
exit_button.pack(pady=20)

# Start listening for commands in a separate thread
command_thread = threading.Thread(target=listen_for_commands, daemon=True)
command_thread.start()

# Main Tkinter event loop
root.mainloop()
