import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import io
import os
import librosa
import librosa.display
import numpy as np

# Page configuration
st.set_page_config(page_title="Pitch & Putt Score Tracker", layout="centered")

# Sidebar toggles
dark_mode = st.sidebar.checkbox("🌙 Dark Mode")
compact_input = st.sidebar.checkbox("📱 Compact Input Mode", value=True)
enable_notes = st.sidebar.checkbox("📝 Enable Hole Notes", value=False)

# Dark mode styling
if dark_mode:
    st.markdown("""
    <style>
    body { background-color: #1e1e1e; color: white; }
    .stApp { background-color: #1e1e1e; }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("⛳ Pitch & Putt Score Tracker")

# Player info
player_name = st.text_input("Player Name", value="Player 1")
round_notes = st.text_area("📝 Round Notes (optional)", placeholder="E.g., windy day, wet greens, played with John...")

# Hole data input
hole_data = []
for hole in range(1, 19):
    if hole == 1:
        st.markdown("### 🟢 Front 9")
    elif hole == 10:
        st.markdown("### 🔵 Back 9")

    with st.expander(f"Hole {hole}"):
        score = st.selectbox("Score", options=list(range(1, 11)), index=2, key=f"score_{hole}") if compact_input else st.number_input("Score", min_value=1, max_value=10, value=3, key=f"score_{hole}")
        pitched_option = st.selectbox("🎯 Tee Shot Result", options=["Missed Green", "Hit Green"], index=1 if compact_input else 0, key=f"pitched_option_{hole}")
        pitched = pitched_option == "Hit Green"

        chip_in = False
        long_putt = False
        birdie_putt_made_distance = None
        birdie_putt_missed_distance = None
        off_green_putt = False

        if pitched and score == 2:
            birdie_putt_made_distance = st.number_input("📏 Birdie Putt Made Distance (ft)", min_value=0.0, step=0.5, key=f"birdie_putt_made_{hole}")
        elif pitched and score != 2:
            birdie_putt_missed_distance = st.number_input("📏 Birdie Putt Missed Distance (ft)", min_value=0.0, step=0.5, key=f"birdie_putt_missed_{hole}")
        elif not pitched and score == 2:
            chip_in = st.checkbox("⛳ Chip-in?", key=f"chipin_{hole}")
            if not chip_in:
                off_green_putt = st.checkbox("🎯 Birdie Putt Made Off Green?", key=f"offgreenputt_{hole}")

        notes = st.text_area("📝 Notes (optional)", key=f"notes_{hole}", placeholder="E.g., windy, missed short putt...") if enable_notes else ""
        putts = 1 if pitched and score == 2 else 2 if pitched and score == 3 else None
        hole_data.append({
            "Hole": hole,
            "Score": score,
            "Green Pitched": pitched,
            "Chip-in": chip_in,
            "Long Putt": long_putt,
            "Putts": putts,
            "Notes": notes,
            "Birdie Putt Made Dist": birdie_putt_made_distance,
            "Birdie Putt Missed Dist": birdie_putt_missed_distance,
            "Off Green Putt": off_green_putt
        })

df = pd.DataFrame(hole_data)

# Analysis
total_score = df["Score"].sum()
birdies = (df["Score"] == 2).sum()
pars = (df["Score"] == 3).sum()
bogeys = (df["Score"] > 3).sum()
greens_pitched = df["Green Pitched"].sum()
chip_ins = df["Chip-in"].sum()
long_putts = df["Long Putt"].sum()
total_putts = df["Putts"].dropna().sum()
average_putts = df["Putts"].dropna().mean()
gir_percentage = greens_pitched / 18 * 100
birdie_conversion = ((df["Score"] == 2) & (df["Green Pitched"])).sum() / greens_pitched * 100 if greens_pitched else 0
missed_green_birdies = ((df["Score"] == 2) & (~df["Green Pitched"])).sum()
missed_green_recovery = missed_green_birdies / (18 - greens_pitched) * 100 if (18 - greens_pitched) else 0
avg_birdie_putt_made = df["Birdie Putt Made Dist"].dropna().mean()
avg_birdie_putt_missed = df["Birdie Putt Missed Dist"].dropna().mean()

# Audio-Based Stroke Detection Section
st.markdown("---")
st.markdown("## 🔊 Audio-Based Stroke Detection")

import streamlit as st
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import io
import os
from moviepy.editor import VideoFileClip

st.title("Pitch and Putt Stroke Detection - Audio Preprocessing")

uploaded_file = st.file_uploader("Upload an audio or video file", type=["wav", "mp3", "mp4"])

if uploaded_file is not None:
    file_type = uploaded_file.type
    audio_bytes = uploaded_file.read()

    if file_type == "video/mp4":
        with open("temp_video.mp4", "wb") as f:
            f.write(audio_bytes)
        video = VideoFileClip("temp_video.mp4")
        video.audio.write_audiofile("extracted_audio.wav")
        audio_path = "extracted_audio.wav"
    else:
        audio_path = io.BytesIO(audio_bytes)

    try:
        audio_data, sr = librosa.load(audio_path, sr=16000, mono=True)

        st.subheader("Original Audio Waveform")
        fig, ax = plt.subplots()
        librosa.display.waveshow(audio_data, sr=sr, ax=ax)
        st.pyplot(fig)

        trimmed_audio, _ = librosa.effects.trim(audio_data)
        normalized_audio = librosa.util.normalize(trimmed_audio)

        st.subheader("Waveform After Preprocessing")
        fig, ax = plt.subplots()
        librosa.display.waveshow(normalized_audio, sr=sr, ax=ax)
        st.pyplot(fig)

        mfccs = librosa.feature.mfcc(y=normalized_audio, sr=sr, n_mfcc=13)
        st.subheader("MFCC Features")
        fig, ax = plt.subplots()
        img = librosa.display.specshow(mfccs, x_axis='time', ax=ax)
        fig.colorbar(img, ax=ax)
        st.pyplot(fig)

        st.success("Audio preprocessing completed successfully.")
    except Exception as e:
        st.error(f"Error processing audio: {e}")
