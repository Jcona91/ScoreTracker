import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

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

# Player name
player_name = st.text_input("Player Name", value="Player 1")

# Input form
hole_data = []
for hole in range(1, 19):
    if hole == 1:
        st.markdown("### 🟢 Front 9")
    elif hole == 10:
        st.markdown("### 🔵 Back 9")

    with st.expander(f"Hole {hole}"):
        with st.container():
            score = st.selectbox(f"Score", options=list(range(1, 11)), index=2, key=f"score_{hole}") if compact_input \
                else st.number_input(f"Score", min_value=1, max_value=10, value=3, key=f"score_{hole}")
            pitched = st.checkbox("✅ Green Pitched?", key=f"pitched_{hole}")
            chip_in = long_putt = False
            if not pitched and score == 2:
                chip_in = st.checkbox("🏌️ Chip-in?", key=f"chipin_{hole}")
                long_putt = st.checkbox("🎯 Long Putt?", key=f"longputt_{hole}")
            notes = st.text_area("📝 Notes (optional)", key=f"notes_{hole}", placeholder="E.g., windy, missed short putt...") if enable_notes else ""
            putts = 1 if pitched and score == 2 else 2 if pitched and score == 3 else None

            hole_data.append({
                "Hole": hole,
                "Score": score,
                "Green Pitched": pitched,
                "Chip-in": chip_in,
                "Long Putt": long_putt,
                "Putts": putts,
                "Notes": notes
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

# Round analysis
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

# Hole-by-hole summary
st.markdown("---")
st.markdown("<h2 style='color:purple;'>📋 Hole-by-Hole Summary</h2>", unsafe_allow_html=True)
df_display = df.rename(columns={
    "Green Pitched": "GIR",
    "Chip-in": "Chip",
    "Long Putt": "LongP",
    "Putts": "Putt"
})
totals = {
    "Hole": "Total",
    "Score": df["Score"].sum(),
    "GIR": df["Green Pitched"].sum(),
    "Chip": df["Chip-in"].sum(),
    "LongP": df["Long Putt"].sum(),
    "Putt": df["Putts"].dropna().sum(),
    "Notes": "" if enable_notes else None
}
df_display = pd.concat([df_display, pd.DataFrame([totals])], ignore_index=True)
if not enable_notes:
    df_display = df_display.drop(columns=["Notes"])
st.table(df_display.set_index("Hole"))

# Charts
st.markdown("---")
st.markdown("<h2 style='color:orange;'>📈 Visual Summary</h2>", unsafe_allow_html=True)
sns.set_theme(style="whitegrid")

# Score per hole
fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.barplot(x="Hole", y="Score", data=df, ax=ax1, palette="viridis")
ax1.set_title("Score per Hole", fontsize=12)
ax1.set_xlabel("Hole", fontsize=10)
ax1.set_ylabel("Score", fontsize=10)
plt.tight_layout()
st.pyplot(fig1)

# Score distribution
score_counts = df["Score"].apply(lambda x: "Birdie" if x == 2 else "Par" if x == 3 else "Bogey+").value_counts()
fig2, ax2 = plt.subplots(figsize=(5, 5))
ax2.pie(score_counts, labels=score_counts.index, autopct='%1.1f%%', startangle=90)
ax2.set_title("Score Distribution", fontsize=12)
plt.tight_layout()
st.pyplot(fig2)

# Putts per hole
fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.lineplot(x="Hole", y="Putts", data=df, marker="o", ax=ax3)
ax3.set_title("Putts per Hole", fontsize=12)
ax3.set_xlabel("Hole", fontsize=10)
ax3.set_ylabel("Putts", fontsize=10)
plt.tight_layout()
st.pyplot(fig3)

# Export to CSV
st.markdown("---")
st.markdown("<h2 style='color:brown;'>📤 Export & Save</h2>", unsafe_allow_html=True)
csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="{player_name}_round.csv">📥 Download Round as CSV</a>'
st.markdown(href, unsafe_allow_html=True)

# Save/load rounds
if "saved_rounds" not in st.session_state:
    st.session_state.saved_rounds = {}

save_name = st.text_input("Save this round as:", value="Round 1")
if st.button("💾 Save Round"):
    st.session_state.saved_rounds[save_name] = df.copy()
    st.success(f"Saved as '{save_name}'")

if st.session_state.saved_rounds:
    load_name = st.selectbox("📂 Load a saved round", list(st.session_state.saved_rounds.keys()))

