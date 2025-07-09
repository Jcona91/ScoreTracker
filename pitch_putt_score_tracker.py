import streamlit as st
from PIL import Image
import pandas as pd

# Page configuration
st.set_page_config(page_title="Pitch & Putt Score Tracker", layout="centered")

# Display logo if available
try:
    logo = Image.open("pitch_putt_logo.png")
    st.image(logo, width=200)
except FileNotFoundError:
    st.markdown("### ⛳ Pitch & Putt Score Tracker")

st.markdown("---")
st.markdown("<h2 style='color:green;'>🏌️ Enter Hole Scores</h2>", unsafe_allow_html=True)
st.markdown("All holes are Par 3. Enter your score and round details below.")

# Initialize data structure
hole_data = []

# Input for 18 holes
for hole in range(1, 19):
    with st.expander(f"Hole {hole}"):
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            score = st.number_input(f"Score", min_value=1, max_value=10, value=3, key=f"score_{hole}")
        with col2:
            pitched = st.checkbox("Green Pitched?", key=f"pitched_{hole}")
        with col3:
            chip_in = False
            long_putt = False
            if not pitched and score == 2:
                chip_in = st.checkbox("🏌️ Chip-in?", key=f"chipin_{hole}")
                long_putt = st.checkbox("🎯 Long Putt?", key=f"longputt_{hole}")

        # Determine putts
        putts = None
        if pitched:
            if score == 2:
                putts = 1
            elif score == 3:
                putts = 2

        hole_data.append({
            "Hole": hole,
            "Score": score,
            "Green Pitched": pitched,
            "Chip-in": chip_in,
            "Long Putt": long_putt,
            "Putts": putts
        })

# Convert to DataFrame
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

# Display analysis
st.markdown("---")
st.markdown("<h2 style='color:blue;'>📊 Round Analysis</h2>", unsafe_allow_html=True)
st.markdown(f"- 🟢 **Total Score:** {total_score}")
st.markdown(f"- 🟢 **Birdies:** {birdies}")
st.markdown(f"- ⚪ **Pars:** {pars}")
st.markdown(f"- 🔴 **Bogeys or worse:** {bogeys}")
st.markdown(f"- ✅ **Greens Pitched:** {greens_pitched}")
st.markdown(f"- 🏌️ **Chip-ins:** {chip_ins}")
st.markdown(f"- 🎯 **Long Putts:** {long_putts}")
st.markdown(f"- ⛳ **Estimated Total Putts:** {int(total_putts)}")

# Display hole-by-hole summary
st.markdown("---")
st.markdown("<h2 style='color:purple;'>📋 Hole-by-Hole Summary</h2>", unsafe_allow_html=True)
st.dataframe(df.set_index("Hole"))


