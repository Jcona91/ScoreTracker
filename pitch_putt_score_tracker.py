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
round_notes = st.text_area("📝 Round Notes (optional)", placeholder="E.g., windy day, wet greens, played with John...")

hole_data = []
for hole in range(1, 19):
    if hole == 1:
        st.markdown("### 🟢 Front 9")
    elif hole == 10:
        st.markdown("### 🔵 Back 9")

    with st.expander(f"Hole {hole}"):
        score = st.selectbox(f"Score", options=list(range(1, 11)), index=2, key=f"score_{hole}") if compact_input             else st.number_input(f"Score", min_value=1, max_value=10, value=3, key=f"score_{hole}")

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

# Save round
if st.button("💾 Save Round"):
    round_summary = {
        "Player": player_name,
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Score": total_score,
        "Birdies": birdies,
        "GIR": greens_pitched,
        "Putts": total_putts,
        "Birdie %": birdies / 18 * 100
    }
    file_exists = os.path.exists("rounds_data.csv")
    df_summary = pd.DataFrame([round_summary])
    df_summary.to_csv("rounds_data.csv", mode='a', header=not file_exists, index=False)
    st.success("Round saved successfully!")

# Round analysis
st.markdown("---")
st.markdown("<h2 style='color:blue;'>📊 Round Analysis</h2>", unsafe_allow_html=True)
st.markdown(f"- 🟢 **Total Score:** {total_score}")
st.markdown(f"- 🟢 **Birdies:** {birdies}")
st.markdown(f"- ⚪ **Pars:** {pars}")
st.markdown(f"- 🔴 **Bogeys or worse:** {bogeys}")
st.markdown(f"- ✅ **Greens Hit:** {greens_pitched} ({gir_percentage:.1f}%)")
st.markdown(f"- 🏌️ **Chip-ins:** {chip_ins}")
st.markdown(f"- ⛳ **Estimated Total Putts:** {int(total_putts)} (Avg: {average_putts:.2f})")
st.markdown(f"- 🟢 **Birdie Conversion on GIR:** {birdie_conversion:.1f}%")
st.markdown(f"- 🔁 **Missed Green Birdie Recovery:** {missed_green_recovery:.1f}%")
if not pd.isna(avg_birdie_putt_made):
    st.markdown(f"- 📏 **Avg Birdie Putt Made Distance:** {avg_birdie_putt_made:.1f} ft")
if not pd.isna(avg_birdie_putt_missed):
    st.markdown(f"- 📏 **Avg Birdie Putt Missed Distance:** {avg_birdie_putt_missed:.1f} ft")

if round_notes.strip():
    st.markdown("#### 🗒️ Round Notes")
    st.markdown(f"> {round_notes}")

# Leaderboard
st.markdown("---")
st.markdown("<h2 style='color:gold;'>🏆 Leaderboard</h2>", unsafe_allow_html=True)
if os.path.exists("rounds_data.csv"):
    leaderboard_df = pd.read_csv("rounds_data.csv")
    leaderboard_summary = leaderboard_df.groupby("Player").agg(
        Rounds=("Score", "count"),
        Avg_Score=("Score", "mean"),
        Total_Birdies=("Birdies", "sum"),
        Birdie_Percentage=("Birdie %", "mean")
    ).sort_values(by=["Avg_Score", "Birdie_Percentage"], ascending=[True, False])
    st.dataframe(leaderboard_summary.style.format({"Avg_Score": "{:.2f}", "Birdie_Percentage": "{:.1f}%"}))
else:
    st.info("No rounds saved yet.")

# AI-based feedback
st.markdown("---")
st.markdown("<h2 style='color:red;'>🧠 AI-Based Performance Feedback</h2>", unsafe_allow_html=True)
if avg_birdie_putt_made and avg_birdie_putt_made < 10:
    st.markdown("- ✅ You're converting birdie putts well from short range. Keep practicing 5–10 ft putts.")
if avg_birdie_putt_missed and avg_birdie_putt_missed > 10:
    st.markdown("- ⚠️ You're missing birdie putts from long range. Focus on lag putting from 12–15 ft.")
if birdie_conversion < 30:
    st.markdown("- 📉 Birdie conversion on greens hit is low. Consider practicing mid-range putts.")
if missed_green_recovery > 20:
    st.markdown("- 🔁 Great job recovering birdies after missed greens!")
elif missed_green_recovery < 10:
    st.markdown("- 🛠️ Work on your short game to improve birdie chances after missed greens.")

# Visuals
st.markdown("---")
st.markdown("<h2 style='color:orange;'>📈 Visual Summary</h2>", unsafe_allow_html=True)
sns.set_theme(style="whitegrid")

# Bar chart: Score per Hole
fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.barplot(x="Hole", y="Score", data=df, ax=ax1, palette="viridis")
ax1.set_title("Score per Hole", fontsize=12)
ax1.set_xlabel("Hole", fontsize=10)
ax1.set_ylabel("Score", fontsize=10)
plt.tight_layout()
st.pyplot(fig1)

# Pie chart: Score Distribution
score_counts = df["Score"].apply(lambda x: "Birdie" if x == 2 else "Par" if x == 3 else "Bogey+").value_counts()
fig2, ax2 = plt.subplots(figsize=(5, 5))
ax2.pie(score_counts, labels=score_counts.index, autopct='%1.1f%%', startangle=90)
ax2.set_title("Score Distribution", fontsize=12)
plt.tight_layout()
st.pyplot(fig2)

# Line chart: Putts per Hole
fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.lineplot(x="Hole", y="Putts", data=df, marker="o", ax=ax3)
ax3.set_title("Putts per Hole", fontsize=12)
ax3.set_xlabel("Hole", fontsize=10)
ax3.set_ylabel("Putts", fontsize=10)
plt.tight_layout()
st.pyplot(fig3)
