from PIL import Image, ImageDraw, ImageFont
import io
import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

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

# Logo or title
try:
    logo = Image.open("pitch_putt_logo.png")
    st.image(logo, width=200)
except FileNotFoundError:
    st.markdown("### ⛳ Pitch & Putt Score Tracker")

st.markdown("---")
st.markdown("<h2 style='color:green;'>🏌️ Enter Hole Scores</h2>", unsafe_allow_html=True)

player_name = st.text_input("Player Name", value="Player 1")
course_name = st.text_input("Course Name", value="")
round_notes = st.text_area("📝 Round Notes (optional)", placeholder="E.g., windy day, wet greens, played with John...")

hole_data = []
for hole in range(1, 19):
    if hole == 1:
        st.markdown("### 🟢 Front 9")
    elif hole == 10:
        st.markdown("### 🔵 Back 9")

    with st.expander(f"Hole {hole}"):
        score = st.number_input(f"Score", min_value=1, max_value=10, value=3, step=1, key=f"score_{hole}")

        pitched_option = st.selectbox(
            "🎯 Tee Shot Result",
            options=["Missed Green", "Hit Green"],
            index=1 if compact_input else 0,
            key=f"pitched_option_{hole}"
        )
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
def generate_summary_image(player_name, total_score, birdies, pars, bogeys, greens_pitched, gir_percentage,
                           chip_ins, total_putts, average_putts, birdie_conversion, missed_green_recovery,
                           avg_birdie_putt_made, avg_birdie_putt_missed, round_notes):
    width, height = 720, 1280
    image = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(image)

    try:
        font_title = ImageFont.truetype("arial.ttf", 40)
        font_subtitle = ImageFont.truetype("arial.ttf", 28)
        font_text = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        font_title = font_subtitle = font_text = ImageFont.load_default()

    y = 40
    draw.text((40, y), f"⛳ Round Summary – {player_name}", font=font_title, fill="black"); y += 80
    draw.text((40, y), f"Total Score: {total_score}", font=font_text, fill="black"); y += 40
    draw.text((40, y), f"Birdies: {birdies}", font=font_text, fill="black"); y += 40
    draw.text((40, y), f"Pars: {pars}", font=font_text, fill="black"); y += 40
    draw.text((40, y), f"Bogeys or worse: {bogeys}", font=font_text, fill="black"); y += 40
    draw.text((40, y), f"Greens Hit (GIR): {greens_pitched} ({gir_percentage:.1f}%)", font=font_text, fill="black"); y += 40
    draw.text((40, y), f"Chip-ins: {chip_ins}", font=font_text, fill="black"); y += 40
    draw.text((40, y), f"Total Putts: {int(total_putts)} (Avg: {average_putts:.2f})", font=font_text, fill="black"); y += 40
    draw.text((40, y), f"Birdie Conversion on GIR: {birdie_conversion:.1f}%", font=font_text, fill="black"); y += 40
    draw.text((40, y), f"Missed Green Birdie Recovery: {missed_green_recovery:.1f}%", font=font_text, fill="black"); y += 40
    if not pd.isna(avg_birdie_putt_made):
        draw.text((40, y), f"Avg Birdie Putt Made Distance: {avg_birdie_putt_made:.1f} ft", font=font_text, fill="black"); y += 40
    if not pd.isna(avg_birdie_putt_missed):
        draw.text((40, y), f"Avg Birdie Putt Missed Distance: {avg_birdie_putt_missed:.1f} ft", font=font_text, fill="black"); y += 40

    y += 20
    draw.text((40, y), "🧠 AI Feedback:", font=font_subtitle, fill="black"); y += 40
    if avg_birdie_putt_made and avg_birdie_putt_made < 10:
        draw.text((60, y), "✔️ Converting birdie putts well from short range.", font=font_text, fill="black"); y += 30
    if avg_birdie_putt_missed and avg_birdie_putt_missed > 10:
        draw.text((60, y), "⚠️ Missing birdie putts from long range.", font=font_text, fill="black"); y += 30
    if birdie_conversion < 30:
        draw.text((60, y), "📉 Low birdie conversion on greens hit.", font=font_text, fill="black"); y += 30
    if missed_green_recovery > 20:
        draw.text((60, y), "🔁 Great job recovering birdies after missed greens!", font=font_text, fill="black"); y += 30
    elif missed_green_recovery < 10:
        draw.text((60, y), "🛠️ Work on short game after missed greens.", font=font_text, fill="black"); y += 30

    if round_notes.strip():
        y += 20
        draw.text((40, y), "📝 Round Notes:", font=font_subtitle, fill="black"); y += 40
        for line in round_notes.splitlines():
            draw.text((60, y), f"- {line}", font=font_text, fill="black"); y += 30

    return image

# Save round
# Save Round (removed)
