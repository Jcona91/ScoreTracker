import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

# Page configuration
st.set_page_config(page_title="Pitch & Putt Score Tracker", layout="centered")

# Dark mode toggle
dark_mode = st.sidebar.checkbox("🌙 Dark Mode")
if dark_mode:
    st.markdown(
        """
        <style>
        body { background-color: #1e1e1e; color: white; }
        .stApp { background-color: #1e1e1e; }
        </style>
        """,
        unsafe_allow_html=True
    )

# Display logo if available
try:
    logo = Image.open("pitch_putt_logo.png")
    st.image(logo, width=200)
except FileNotFoundError:
    st.markdown("### ⛳ Pitch & Putt Score Tracker")

st.markdown("---")
st.markdown("<h2 style='color:green;'>🏌️ Enter Hole Scores</h2>", unsafe_allow_html=True)

# Player profile
player_name = st.text_input("Player Name", value="Player 1")

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
average_putts = df["Putts"].dropna().mean()
gir_percentage = greens_pitched / 18 * 100
birdie_conversion = ((df["Score"] == 2) & (df["Green Pitched"])).sum() / greens_pitched * 100 if greens_pitched else 0
missed_green_birdies = ((df["Score"] == 2) & (~df["Green Pitched"])).sum()
missed_green_recovery = missed_green_birdies / (18 - greens_pitched) * 100 if (18 - greens_pitched) else 0

# Display analysis
st.markdown("---")
st.markdown("<h2 style='color:blue;'>📊 Round Analysis</h2>", unsafe_allow_html=True)
st.markdown(f"- 🟢 **Total Score:** {total_score}")
st.markdown(f"- 🟢 **Birdies:** {birdies}")
st.markdown(f"- ⚪ **Pars:** {pars}")
st.markdown(f"- 🔴 **Bogeys or worse:** {bogeys}")
st.markdown(f"- ✅ **Greens Pitched:** {greens_pitched} ({gir_percentage:.1f}%)")
st.markdown(f"- 🏌️ **Chip-ins:** {chip_ins}")
st.markdown(f"- 🎯 **Long Putts:** {long_putts}")
st.markdown(f"- ⛳ **Estimated Total Putts:** {int(total_putts)} (Avg: {average_putts:.2f})")
st.markdown(f"- 🟢 **Birdie Conversion on GIR:** {birdie_conversion:.1f}%")
st.markdown(f"- 🔁 **Missed Green Birdie Recovery:** {missed_green_recovery:.1f}%")

# Display hole-by-hole summary
st.markdown("---")
st.markdown("<h2 style='color:purple;'>📋 Hole-by-Hole Summary</h2>", unsafe_allow_html=True)
st.dataframe(df.set_index("Hole"))

# Charts
st.markdown("---")
st.markdown("<h2 style='color:orange;'>📈 Visual Summary</h2>", unsafe_allow_html=True)

# Bar chart of scores
fig1, ax1 = plt.subplots()
sns.barplot(x="Hole", y="Score", data=df, ax=ax1, palette="viridis")
ax1.set_title("Score per Hole")
st.pyplot(fig1)

# Pie chart of score types
score_counts = df["Score"].apply(lambda x: "Birdie" if x == 2 else "Par" if x == 3 else "Bogey+").value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(score_counts, labels=score_counts.index, autopct='%1.1f%%', startangle=90)
ax2.set_title("Score Distribution")
st.pyplot(fig2)

# Line chart of putts
fig3, ax3 = plt.subplots()
sns.lineplot(x="Hole", y="Putts", data=df, marker="o", ax=ax3)
ax3.set_title("Putts per Hole")
st.pyplot(fig3)

# Export to CSV
st.markdown("---")
st.markdown("<h2 style='color:brown;'>📤 Export & Save</h2>", unsafe_allow_html=True)

csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="{player_name}_round.csv">📥 Download Round as CSV</a>'
st.markdown(href, unsafe_allow_html=True)

# Save/load rounds (basic session state)
if "saved_rounds" not in st.session_state:
    st.session_state.saved_rounds = {}

save_name = st.text_input("Save this round as:", value="Round 1")
if st.button("💾 Save Round"):
    st.session_state.saved_rounds[save_name] = df.copy()
    st.success(f"Saved as '{save_name}'")

if st.session_state.saved_rounds:
    load_name = st.selectbox("📂 Load a saved round", list(st.session_state.saved_rounds.keys()))
    if st.button("🔄 Load Round"):
        df = st.session_state.saved_rounds[load_name]
        st.dataframe(df.set_index("Hole"))
