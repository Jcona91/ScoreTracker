{
    "chunks": [
        {
            "type": "txt",
            "chunk_number": 1,
            "lines": [
                {
                    "line_number": 1,
                    "text": "{\\rtf1\\fbidis\\ansi\\ansicpg1252\\deff0\\nouicompat\\deflang1033{\\fonttbl{\\f0\\fnil\\fcharset0 Calibri;}{\\f1\\fnil\\fcharset1 Segoe UI Symbol;}{\\f2\\fnil Calibri;}{\\f3\\fnil\\fcharset1 Segoe UI Symbol;}{\\f4\\fnil\\fcharset1 Segoe UI Emoji;}{\\f5\\fnil\\fcharset1 Segoe UI Emoji;}}"
                },
                {
                    "line_number": 2,
                    "text": "{\\*\\generator Riched20 10.0.22621}\\viewkind4\\uc1"
                },
                {
                    "line_number": 3,
                    "text": "\\pard\\sa200\\sl276\\slmult1\\f0\\fs22\\lang9 from PIL import Image, ImageDraw, ImageFont\\par"
                },
                {
                    "line_number": 4,
                    "text": "import io\\par"
                },
                {
                    "line_number": 5,
                    "text": "import streamlit as st\\par"
                },
                {
                    "line_number": 6,
                    "text": "from PIL import Image\\par"
                },
                {
                    "line_number": 7,
                    "text": "import pandas as pd\\par"
                },
                {
                    "line_number": 8,
                    "text": "import matplotlib.pyplot as plt\\par"
                },
                {
                    "line_number": 9,
                    "text": "import seaborn as sns\\par"
                },
                {
                    "line_number": 10,
                    "text": "import os\\par"
                },
                {
                    "line_number": 11,
                    "text": "from datetime import datetime\\par"
                },
                {
                    "line_number": 12,
                    "text": "\\par"
                },
                {
                    "line_number": 13,
                    "text": "# Page configuration\\par"
                },
                {
                    "line_number": 14,
                    "text": "st.set_page_config(page_title=\"Pitch & Putt Score Tracker\", layout=\"centered\")\\par"
                },
                {
                    "line_number": 15,
                    "text": "\\par"
                },
                {
                    "line_number": 16,
                    "text": "# Sidebar toggles\\par"
                },
                {
                    "line_number": 17,
                    "text": "dark_mode = st.sidebar.checkbox(\"\\f1\\u-10180?\\u-8423?\\f2  \\f0 Dark Mode\")\\par"
                },
                {
                    "line_number": 18,
                    "text": "compact_input = st.sidebar.checkbox(\"\\f1\\u-10179?\\u-8975?\\f2  \\f0 Compact Input Mode\", value=True)\\par"
                },
                {
                    "line_number": 19,
                    "text": "enable_notes = st.sidebar.checkbox(\"\\f1\\u-10179?\\u-8995?\\f2  \\f0 Enable Hole Notes\", value=False)\\par"
                },
                {
                    "line_number": 20,
                    "text": "\\par"
                },
                {
                    "line_number": 21,
                    "text": "# Dark mode styling\\par"
                },
                {
                    "line_number": 22,
                    "text": "if dark_mode:\\par"
                },
                {
                    "line_number": 23,
                    "text": "st.markdown(\"\"\"\\par"
                },
                {
                    "line_number": 24,
                    "text": "<style>\\par"
                },
                {
                    "line_number": 25,
                    "text": "body \\{ background-color: #1e1e1e; color: white; \\}\\par"
                },
                {
                    "line_number": 26,
                    "text": ".stApp \\{ background-color: #1e1e1e; \\}\\par"
                },
                {
                    "line_number": 27,
                    "text": "</style>\\par"
                },
                {
                    "line_number": 28,
                    "text": "\"\"\", unsafe_allow_html=True)\\par"
                },
                {
                    "line_number": 29,
                    "text": "\\par"
                },
                {
                    "line_number": 30,
                    "text": "# Logo or title\\par"
                },
                {
                    "line_number": 31,
                    "text": "try:\\par"
                },
                {
                    "line_number": 32,
                    "text": "logo = Image.open(\"pitch_putt_logo.png\")\\par"
                },
                {
                    "line_number": 33,
                    "text": "st.image(logo, width=200)\\par"
                },
                {
                    "line_number": 34,
                    "text": "except FileNotFoundError:\\par"
                },
                {
                    "line_number": 35,
                    "text": "st.markdown(\"### \\f3\\u9971?\\f2  \\f0 Pitch & Putt Score Tracker\")\\par"
                },
                {
                    "line_number": 36,
                    "text": "\\par"
                },
                {
                    "line_number": 37,
                    "text": "st.markdown(\"---\")\\par"
                },
                {
                    "line_number": 38,
                    "text": "st.markdown(\"<h2 style='color:green;'>\\f4\\u-10180?\\u-8244?\\u-497?\\f2  \\f0 Enter Hole Scores</h2>\", unsafe_allow_html=True)\\par"
                },
                {
                    "line_number": 39,
                    "text": "\\par"
                },
                {
                    "line_number": 40,
                    "text": "player_name = st.text_input(\"Player Name\", value=\"Player 1\")\\par"
                },
                {
                    "line_number": 41,
                    "text": "round_notes = st.text_area(\"\\f1\\u-10179?\\u-8995?\\f2  \\f0 Round Notes (optional)\", placeholder=\"E.g., windy day, wet greens, played with John...\")\\par"
                },
                {
                    "line_number": 42,
                    "text": "\\par"
                },
                {
                    "line_number": 43,
                    "text": "hole_data = []\\par"
                },
                {
                    "line_number": 44,
                    "text": "for hole in range(1, 19):\\par"
                },
                {
                    "line_number": 45,
                    "text": "if hole == 1:\\par"
                },
                {
                    "line_number": 46,
                    "text": "st.markdown(\"### \\f5\\u-10179?\\u-8222?\\f2  \\f0 Front 9\")\\par"
                },
                {
                    "line_number": 47,
                    "text": "elif hole == 10:\\par"
                },
                {
                    "line_number": 48,
                    "text": "st.markdown(\"### \\f1\\u-10179?\\u-8907?\\f2  \\f0 Back 9\")\\par"
                },
                {
                    "line_number": 49,
                    "text": "\\par"
                },
                {
                    "line_number": 50,
                    "text": "with st.expander(f\"Hole \\{hole\\}\"):\\par"
                },
                {
                    "line_number": 51,
                    "text": "score = st.selectbox(f\"Score\", options=list(range(1, 11)), index=2, key=f\"score_\\{hole\\}\") if compact_input             else st.number_input(f\"Score\", min_value=1, max_value=10, value=3, key=f\"score_\\{hole\\}\")\\par"
                },
                {
                    "line_number": 52,
                    "text": "\\par"
                },
                {
                    "line_number": 53,
                    "text": "pitched_option = st.selectbox(\\par"
                },
                {
                    "line_number": 54,
                    "text": "\"\\f1\\u-10180?\\u-8273?\\f2  \\f0 Tee Shot Result\",\\par"
                },
                {
                    "line_number": 55,
                    "text": "options=[\"Missed Green\", \"Hit Green\"],\\par"
                },
                {
                    "line_number": 56,
                    "text": "index=1 if compact_input else 0,\\par"
                },
                {
                    "line_number": 57,
                    "text": "key=f\"pitched_option_\\{hole\\}\"\\par"
                },
                {
                    "line_number": 58,
                    "text": ")\\par"
                },
                {
                    "line_number": 59,
                    "text": "pitched = pitched_option == \"Hit Green\"\\par"
                },
                {
                    "line_number": 60,
                    "text": "\\par"
                },
                {
                    "line_number": 61,
                    "text": "chip_in = False\\par"
                },
                {
                    "line_number": 62,
                    "text": "long_putt = False\\par"
                },
                {
                    "line_number": 63,
                    "text": "birdie_putt_made_distance = None\\par"
                },
                {
                    "line_number": 64,
                    "text": "birdie_putt_missed_distance = None\\par"
                },
                {
                    "line_number": 65,
                    "text": "off_green_putt = False\\par"
                },
                {
                    "line_number": 66,
                    "text": "\\par"
                },
                {
                    "line_number": 67,
                    "text": "if pitched and score == 2:\\par"
                },
                {
                    "line_number": 68,
                    "text": "birdie_putt_made_distance = st.number_input(\"\\f1\\u-10179?\\u-9009?\\f2  \\f0 Birdie Putt Made Distance (ft)\", min_value=0.0, step=0.5, key=f\"birdie_putt_made_\\{hole\\}\")\\par"
                },
                {
                    "line_number": 69,
                    "text": "elif pitched and score != 2:\\par"
                },
                {
                    "line_number": 70,
                    "text": "birdie_putt_missed_distance = st.number_input(\"\\f1\\u-10179?\\u-9009?\\f2  \\f0 Birdie Putt Missed Distance (ft)\", min_value=0.0, step=0.5, key=f\"birdie_putt_missed_\\{hole\\}\")\\par"
                },
                {
                    "line_number": 71,
                    "text": "elif not pitched and score == 2:\\par"
                },
                {
                    "line_number": 72,
                    "text": "chip_in = st.checkbox(\"\\f3\\u9971?\\f2  \\f0 Chip-in?\", key=f\"chipin_\\{hole\\}\")\\par"
                },
                {
                    "line_number": 73,
                    "text": "if not chip_in:\\par"
                },
                {
                    "line_number": 74,
                    "text": "off_green_putt = st.checkbox(\"\\f1\\u-10180?\\u-8273?\\f2  \\f0 Birdie Putt Made Off Green?\", key=f\"offgreenputt_\\{hole\\}\")\\par"
                },
                {
                    "line_number": 75,
                    "text": "\\par"
                },
                {
                    "line_number": 76,
                    "text": "notes = st.text_area(\"\\f1\\u-10179?\\u-8995?\\f2  \\f0 Notes (optional)\", key=f\"notes_\\{hole\\}\", placeholder=\"E.g., windy, missed short putt...\") if enable_notes else \"\"\\par"
                },
                {
                    "line_number": 77,
                    "text": "putts = 1 if pitched and score == 2 else 2 if pitched and score == 3 else None\\par"
                },
                {
                    "line_number": 78,
                    "text": "\\par"
                },
                {
                    "line_number": 79,
                    "text": "hole_data.append(\\{\\par"
                },
                {
                    "line_number": 80,
                    "text": "\"Hole\": hole,\\par"
                },
                {
                    "line_number": 81,
                    "text": "\"Score\": score,\\par"
                },
                {
                    "line_number": 82,
                    "text": "\"Green Pitched\": pitched,\\par"
                },
                {
                    "line_number": 83,
                    "text": "\"Chip-in\": chip_in,\\par"
                },
                {
                    "line_number": 84,
                    "text": "\"Long Putt\": long_putt,\\par"
                },
                {
                    "line_number": 85,
                    "text": "\"Putts\": putts,\\par"
                },
                {
                    "line_number": 86,
                    "text": "\"Notes\": notes,\\par"
                },
                {
                    "line_number": 87,
                    "text": "\"Birdie Putt Made Dist\": birdie_putt_made_distance,\\par"
                },
                {
                    "line_number": 88,
                    "text": "\"Birdie Putt Missed Dist\": birdie_putt_missed_distance,\\par"
                },
                {
                    "line_number": 89,
                    "text": "\"Off Green Putt\": off_green_putt\\par"
                },
                {
                    "line_number": 90,
                    "text": "\\})\\par"
                },
                {
                    "line_number": 91,
                    "text": "\\par"
                },
                {
                    "line_number": 92,
                    "text": "df = pd.DataFrame(hole_data)\\par"
                },
                {
                    "line_number": 93,
                    "text": "\\par"
                },
                {
                    "line_number": 94,
                    "text": "# Analysis\\par"
                },
                {
                    "line_number": 95,
                    "text": "total_score = df[\"Score\"].sum()\\par"
                },
                {
                    "line_number": 96,
                    "text": "birdies = (df[\"Score\"] == 2).sum()\\par"
                },
                {
                    "line_number": 97,
                    "text": "pars = (df[\"Score\"] == 3).sum()\\par"
                },
                {
                    "line_number": 98,
                    "text": "bogeys = (df[\"Score\"] > 3).sum()\\par"
                },
                {
                    "line_number": 99,
                    "text": "greens_pitched = df[\"Green Pitched\"].sum()\\par"
                },
                {
                    "line_number": 100,
                    "text": "chip_ins = df[\"Chip-in\"].sum()\\par"
                },
                {
                    "line_number": 101,
                    "text": "long_putts = df[\"Long Putt\"].sum()\\par"
                },
                {
                    "line_number": 102,
                    "text": "total_putts = df[\"Putts\"].dropna().sum()\\par"
                },
                {
                    "line_number": 103,
                    "text": "average_putts = df[\"Putts\"].dropna().mean()\\par"
                },
                {
                    "line_number": 104,
                    "text": "gir_percentage = greens_pitched / 18 * 100\\par"
                },
                {
                    "line_number": 105,
                    "text": "birdie_conversion = ((df[\"Score\"] == 2) & (df[\"Green Pitched\"])).sum() / greens_pitched * 100 if greens_pitched else 0\\par"
                },
                {
                    "line_number": 106,
                    "text": "missed_green_birdies = ((df[\"Score\"] == 2) & (~df[\"Green Pitched\"])).sum()\\par"
                },
                {
                    "line_number": 107,
                    "text": "missed_green_recovery = missed_green_birdies / (18 - greens_pitched) * 100 if (18 - greens_pitched) else 0\\par"
                },
                {
                    "line_number": 108,
                    "text": "avg_birdie_putt_made = df[\"Birdie Putt Made Dist\"].dropna().mean()\\par"
                },
                {
                    "line_number": 109,
                    "text": "avg_birdie_putt_missed = df[\"Birdie Putt Missed Dist\"].dropna().mean()\\par"
                },
                {
                    "line_number": 110,
                    "text": "def generate_summary_image(player_name, total_score, birdies, pars, bogeys, greens_pitched, gir_percentage,\\par"
                },
                {
                    "line_number": 111,
                    "text": "chip_ins, total_putts, average_putts, birdie_conversion, missed_green_recovery,\\par"
                },
                {
                    "line_number": 112,
                    "text": "avg_birdie_putt_made, avg_birdie_putt_missed, round_notes):\\par"
                },
                {
                    "line_number": 113,
                    "text": "width, height = 720, 1280\\par"
                },
                {
                    "line_number": 114,
                    "text": "image = Image.new(\"RGB\", (width, height), color=\"white\")\\par"
                },
                {
                    "line_number": 115,
                    "text": "draw = ImageDraw.Draw(image)\\par"
                },
                {
                    "line_number": 116,
                    "text": "\\par"
                },
                {
                    "line_number": 117,
                    "text": "try:\\par"
                },
                {
                    "line_number": 118,
                    "text": "font_title = ImageFont.truetype(\"arial.ttf\", 40)\\par"
                },
                {
                    "line_number": 119,
                    "text": "font_subtitle = ImageFont.truetype(\"arial.ttf\", 28)\\par"
                },
                {
                    "line_number": 120,
                    "text": "font_text = ImageFont.truetype(\"arial.ttf\", 24)\\par"
                },
                {
                    "line_number": 121,
                    "text": "except IOError:\\par"
                },
                {
                    "line_number": 122,
                    "text": "font_title = font_subtitle = font_text = ImageFont.load_default()\\par"
                },
                {
                    "line_number": 123,
                    "text": "\\par"
                },
                {
                    "line_number": 124,
                    "text": "y = 40\\par"
                },
                {
                    "line_number": 125,
                    "text": "draw.text((40, y), f\"\\f3\\u9971?\\f2  \\f0 Round Summary \\f2\\endash  \\{player_name\\}\", font=font_title, fill=\"black\"); y += 80\\par"
                },
                {
                    "line_number": 126,
                    "text": "draw.text((40, y), f\"Total Score: \\{total_score\\}\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 127,
                    "text": "draw.text((40, y), f\"Birdies: \\{birdies\\}\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 128,
                    "text": "draw.text((40, y), f\"Pars: \\{pars\\}\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 129,
                    "text": "draw.text((40, y), f\"Bogeys or worse: \\{bogeys\\}\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 130,
                    "text": "draw.text((40, y), f\"Greens Hit (GIR): \\{greens_pitched\\} (\\{gir_percentage:.1f\\}%)\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 131,
                    "text": "draw.text((40, y), f\"Chip-ins: \\{chip_ins\\}\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 132,
                    "text": "draw.text((40, y), f\"Total Putts: \\{int(total_putts)\\} (Avg: \\{average_putts:.2f\\})\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 133,
                    "text": "draw.text((40, y), f\"Birdie Conversion on GIR: \\{birdie_conversion:.1f\\}%\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 134,
                    "text": "draw.text((40, y), f\"Missed Green Birdie Recovery: \\{missed_green_recovery:.1f\\}%\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 135,
                    "text": "if not pd.isna(avg_birdie_putt_made):\\par"
                },
                {
                    "line_number": 136,
                    "text": "draw.text((40, y), f\"Avg Birdie Putt Made Distance: \\{avg_birdie_putt_made:.1f\\} ft\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 137,
                    "text": "if not pd.isna(avg_birdie_putt_missed):\\par"
                },
                {
                    "line_number": 138,
                    "text": "draw.text((40, y), f\"Avg Birdie Putt Missed Distance: \\{avg_birdie_putt_missed:.1f\\} ft\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 139,
                    "text": "\\par"
                },
                {
                    "line_number": 140,
                    "text": "y += 20\\par"
                },
                {
                    "line_number": 141,
                    "text": "draw.text((40, y), \"\\f4\\u-10178?\\u-8736?\\f2  \\f0 AI Feedback:\", font=font_subtitle, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 142,
                    "text": "if avg_birdie_putt_made and avg_birdie_putt_made < 10:\\par"
                },
                {
                    "line_number": 143,
                    "text": "draw.text((60, y), \"\\f4\\u10004?\\u-497?\\f2  \\f0 Converting birdie putts well from short range.\", font=font_text, fill=\"black\"); y += 30\\par"
                },
                {
                    "line_number": 144,
                    "text": "if avg_birdie_putt_missed and avg_birdie_putt_missed > 10:\\par"
                },
                {
                    "line_number": 145,
                    "text": "draw.text((60, y), \"\\f4\\u9888?\\u-497?\\f2  \\f0 Missing birdie putts from long range.\", font=font_text, fill=\"black\"); y += 30\\par"
                },
                {
                    "line_number": 146,
                    "text": "if birdie_conversion < 30:\\par"
                },
                {
                    "line_number": 147,
                    "text": "draw.text((60, y), \"\\f1\\u-10179?\\u-9015?\\f2  \\f0 Low birdie conversion on greens hit.\", font=font_text, fill=\"black\"); y += 30\\par"
                },
                {
                    "line_number": 148,
                    "text": "if missed_green_recovery > 20:\\par"
                },
                {
                    "line_number": 149,
                    "text": "draw.text((60, y), \"\\f1\\u-10179?\\u-8959?\\f2  \\f0 Great job recovering birdies after missed greens!\", font=font_text, fill=\"black\"); y += 30\\par"
                },
                {
                    "line_number": 150,
                    "text": "elif missed_green_recovery < 10:\\par"
                },
                {
                    "line_number": 151,
                    "text": "draw.text((60, y), \"\\f4\\u-10179?\\u-8480?\\u-497?\\f2  \\f0 Work on short game after missed greens.\", font=font_text, fill=\"black\"); y += 30\\par"
                },
                {
                    "line_number": 152,
                    "text": "\\par"
                },
                {
                    "line_number": 153,
                    "text": "if round_notes.strip():\\par"
                },
                {
                    "line_number": 154,
                    "text": "y += 20\\par"
                },
                {
                    "line_number": 155,
                    "text": "draw.text((40, y), \"\\f1\\u-10179?\\u-8995?\\f2  \\f0 Round Notes:\", font=font_subtitle, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 156,
                    "text": "for line in round_notes.splitlines():\\par"
                },
                {
                    "line_number": 157,
                    "text": "draw.text((60, y), f\"- \\{line\\}\", font=font_text, fill=\"black\"); y += 30\\par"
                },
                {
                    "line_number": 158,
                    "text": "\\par"
                },
                {
                    "line_number": 159,
                    "text": "return image\\par"
                },
                {
                    "line_number": 160,
                    "text": "\\par"
                },
                {
                    "line_number": 161,
                    "text": "# Save round\\par"
                },
                {
                    "line_number": 162,
                    "text": "if st.button(\"\\f1\\u-10179?\\u-9026?\\f2  \\f0 Save Round\"):\\par"
                },
                {
                    "line_number": 163,
                    "text": "round_summary = \\{\\par"
                },
                {
                    "line_number": 164,
                    "text": "\"Player\": player_name,\\par"
                },
                {
                    "line_number": 165,
                    "text": "\"Date\": datetime.now().strftime(\"%Y-%m-%d %H:%M\"),\\par"
                },
                {
                    "line_number": 166,
                    "text": "\"Score\": total_score,\\par"
                },
                {
                    "line_number": 167,
                    "text": "\"Birdies\": birdies,\\par"
                },
                {
                    "line_number": 168,
                    "text": "\"GIR\": greens_pitched,\\par"
                },
                {
                    "line_number": 169,
                    "text": "\"Putts\": total_putts,\\par"
                },
                {
                    "line_number": 170,
                    "text": "\"Birdie %\": birdies / 18 * 100\\par"
                },
                {
                    "line_number": 171,
                    "text": "\\}\\par"
                },
                {
                    "line_number": 172,
                    "text": "file_exists = os.path.exists(\"rounds_data.csv\")\\par"
                },
                {
                    "line_number": 173,
                    "text": "df_summary = pd.DataFrame([round_summary])\\par"
                },
                {
                    "line_number": 174,
                    "text": "df_summary.to_csv(\"rounds_data.csv\", mode='a', header=not file_exists, index=False)\\par"
                },
                {
                    "line_number": 175,
                    "text": "st.success(\"Round saved successfully!\")\\par"
                },
                {
                    "line_number": 176,
                    "text": "if st.button(\"\\f1\\u-10179?\\u-9022?\\f2  \\f0 View Saved Rounds\"):\\par"
                },
                {
                    "line_number": 177,
                    "text": "if os.path.exists(\"rounds_data.csv\"):\\par"
                },
                {
                    "line_number": 178,
                    "text": "saved_rounds_df = pd.read_csv(\"rounds_data.csv\")\\par"
                },
                {
                    "line_number": 179,
                    "text": "st.markdown(\"### \\f4\\u-10179?\\u-8766?\\u-497?\\f2  \\f0 Saved Rounds\")\\par"
                },
                {
                    "line_number": 180,
                    "text": "st.dataframe(saved_rounds_df)\\par"
                },
                {
                    "line_number": 181,
                    "text": "else:\\par"
                },
                {
                    "line_number": 182,
                    "text": "st.info(\"No rounds have been saved yet.\")\\par"
                },
                {
                    "line_number": 183,
                    "text": "\\par"
                },
                {
                    "line_number": 184,
                    "text": "# Round analysis\\par"
                },
                {
                    "line_number": 185,
                    "text": "st.markdown(\"---\")\\par"
                },
                {
                    "line_number": 186,
                    "text": "st.markdown(\"<h2 style='color:blue;'>\\f1\\u-10179?\\u-9014?\\f2  \\f0 Round Analysis</h2>\", unsafe_allow_html=True)\\par"
                },
                {
                    "line_number": 187,
                    "text": "st.markdown(f\"- \\f5\\u-10179?\\u-8222?\\f2  \\f0 **Total Score:** \\{total_score\\}\")\\par"
                },
                {
                    "line_number": 188,
                    "text": "st.markdown(f\"- \\f5\\u-10179?\\u-8222?\\f2  \\f0 **Birdies:** \\{birdies\\}\")\\par"
                },
                {
                    "line_number": 189,
                    "text": "st.markdown(f\"- \\f3\\u9898?\\f2  \\f0 **Pars:** \\{pars\\}\")\\par"
                },
                {
                    "line_number": 190,
                    "text": "st.markdown(f\"- \\f1\\u-10179?\\u-8908?\\f2  \\f0 **Bogeys or worse:** \\{bogeys\\}\")\\par"
                },
                {
                    "line_number": 191,
                    "text": "st.markdown(f\"- \\f3\\u9989?\\f2  \\f0 **Greens Hit:** \\{greens_pitched\\} (\\{gir_percentage:.1f\\}%)\")\\par"
                },
                {
                    "line_number": 192,
                    "text": "st.markdown(f\"- \\f4\\u-10180?\\u-8244?\\u-497?\\f2  \\f0 **Chip-ins:** \\{chip_ins\\}\")\\par"
                },
                {
                    "line_number": 193,
                    "text": "st.markdown(f\"- \\f3\\u9971?\\f2  \\f0 **Estimated Total Putts:** \\{int(total_putts)\\} (Avg: \\{average_putts:.2f\\})\")\\par"
                },
                {
                    "line_number": 194,
                    "text": "st.markdown(f\"- \\f5\\u-10179?\\u-8222?\\f2  \\f0 **Birdie Conversion on GIR:** \\{birdie_conversion:.1f\\}%\")\\par"
                },
                {
                    "line_number": 195,
                    "text": "st.markdown(f\"- \\f1\\u-10179?\\u-8959?\\f2  \\f0 **Missed Green Birdie Recovery:** \\{missed_green_recovery:.1f\\}%\")\\par"
                },
                {
                    "line_number": 196,
                    "text": "if not pd.isna(avg_birdie_putt_made):\\par"
                },
                {
                    "line_number": 197,
                    "text": "st.markdown(f\"- \\f1\\u-10179?\\u-9009?\\f2  \\f0 **Avg Birdie Putt Made Distance:** \\{avg_birdie_putt_made:.1f\\} ft\")\\par"
                },
                {
                    "line_number": 198,
                    "text": "if not pd.isna(avg_birdie_putt_missed):\\par"
                },
                {
                    "line_number": 199,
                    "text": "st.markdown(f\"- \\f1\\u-10179?\\u-9009?\\f2  \\f0 **Avg Birdie Putt Missed Distance:** \\{avg_birdie_putt_missed:.1f\\} ft\")\\par"
                },
                {
                    "line_number": 200,
                    "text": "if st.button(\"\\f1\\u-10179?\\u-8968?\\f2  \\f0 Download Round Summary as Image\"):\\par"
                },
                {
                    "line_number": 201,
                    "text": "summary_img = generate_summary_image(\\par"
                },
                {
                    "line_number": 202,
                    "text": "player_name, total_score, birdies, pars, bogeys, greens_pitched, gir_percentage,\\par"
                },
                {
                    "line_number": 203,
                    "text": "chip_ins, total_putts, average_putts, birdie_conversion, missed_green_recovery,\\par"
                },
                {
                    "line_number": 204,
                    "text": "avg_birdie_putt_made, avg_birdie_putt_missed, round_notes\\par"
                },
                {
                    "line_number": 205,
                    "text": ")\\par"
                },
                {
                    "line_number": 206,
                    "text": "buf = io.BytesIO()\\par"
                },
                {
                    "line_number": 207,
                    "text": "summary_img.save(buf, format=\"PNG\")\\par"
                },
                {
                    "line_number": 208,
                    "text": "st.download_button(\"\\f1\\u-10179?\\u-8987?\\f2  \\f0 Save Image\", data=buf.getvalue(), file_name=\"round_summary.png\", mime=\"image/png\")\\par"
                },
                {
                    "line_number": 209,
                    "text": "\\par"
                },
                {
                    "line_number": 210,
                    "text": "\\par"
                },
                {
                    "line_number": 211,
                    "text": "# Leaderboard\\par"
                },
                {
                    "line_number": 212,
                    "text": "st.markdown(\"---\")\\par"
                },
                {
                    "line_number": 213,
                    "text": "st.markdown(\"<h2 style='color:gold;'>\\f1\\u-10180?\\u-8250?\\f2  \\f0 Leaderboard</h2>\", unsafe_allow_html=True)\\par"
                },
                {
                    "line_number": 214,
                    "text": "if os.path.exists(\"rounds_data.csv\"):\\par"
                },
                {
                    "line_number": 215,
                    "text": "leaderboard_df = pd.read_csv(\"rounds_data.csv\")\\par"
                },
                {
                    "line_number": 216,
                    "text": "leaderboard_summary = leaderboard_df.groupby(\"Player\").agg(\\par"
                },
                {
                    "line_number": 217,
                    "text": "Rounds=(\"Score\", \"count\"),\\par"
                },
                {
                    "line_number": 218,
                    "text": "Avg_Score=(\"Score\", \"mean\"),\\par"
                },
                {
                    "line_number": 219,
                    "text": "Total_Birdies=(\"Birdies\", \"sum\"),\\par"
                },
                {
                    "line_number": 220,
                    "text": "Birdie_Percentage=(\"Birdie %\", \"mean\")\\par"
                },
                {
                    "line_number": 221,
                    "text": ").sort_values(by=[\"Avg_Score\", \"Birdie_Percentage\"], ascending=[True, False])\\par"
                },
                {
                    "line_number": 222,
                    "text": "st.dataframe(leaderboard_summary.style.format(\\{\"Avg_Score\": \"\\{:.2f\\}\", \"Birdie_Percentage\": \"\\{:.1f\\}%\"\\}))\\par"
                },
                {
                    "line_number": 223,
                    "text": "else:\\par"
                },
                {
                    "line_number": 224,
                    "text": "st.info(\"No rounds saved yet.\")\\par"
                },
                {
                    "line_number": 225,
                    "text": "\\par"
                },
                {
                    "line_number": 226,
                    "text": "# AI-based feedback\\par"
                },
                {
                    "line_number": 227,
                    "text": "st.markdown(\"---\")\\par"
                },
                {
                    "line_number": 228,
                    "text": "st.markdown(\"<h2 style='color:red;'>\\f4\\u-10178?\\u-8736?\\f2  \\f0 AI-Based Performance Feedback</h2>\", unsafe_allow_html=True)\\par"
                },
                {
                    "line_number": 229,
                    "text": "if avg_birdie_putt_made and avg_birdie_putt_made < 10:\\par"
                },
                {
                    "line_number": 230,
                    "text": "st.markdown(\"- \\f3\\u9989?\\f2  \\f0 You're converting birdie putts well from short range. Keep practicing 5\\f2\\endash 10 ft putts.\")\\par"
                },
                {
                    "line_number": 231,
                    "text": "if avg_birdie_putt_missed and avg_birdie_putt_missed > 10:\\par"
                },
                {
                    "line_number": 232,
                    "text": "st.markdown(\"- \\f4\\u9888?\\u-497?\\f2  \\f0 You're missing birdie putts from long range. Focus on lag putting from 12\\f2\\endash 15 ft.\")\\par"
                },
                {
                    "line_number": 233,
                    "text": "if birdie_conversion < 30:\\par"
                },
                {
                    "line_number": 234,
                    "text": "st.markdown(\"- \\f1\\u-10179?\\u-9015?\\f2  \\f0 Birdie conversion on greens hit is low. Consider practicing mid-range putts.\")\\par"
                },
                {
                    "line_number": 235,
                    "text": "if missed_green_recovery > 20:\\par"
                },
                {
                    "line_number": 236,
                    "text": "st.markdown(\"- \\f1\\u-10179?\\u-8959?\\f2  \\f0 Great job recovering birdies after missed greens!\")\\par"
                },
                {
                    "line_number": 237,
                    "text": "elif missed_green_recovery < 10:\\par"
                },
                {
                    "line_number": 238,
                    "text": "st.markdown(\"- \\f4\\u-10179?\\u-8480?\\u-497?\\f2  \\f0 Work on your short game to improve birdie chances after missed greens.\")\\par"
                },
                {
                    "line_number": 239,
                    "text": "\\par"
                },
                {
                    "line_number": 240,
                    "text": "# Visuals\\par"
                },
                {
                    "line_number": 241,
                    "text": "st.markdown(\"---\")\\par"
                },
                {
                    "line_number": 242,
                    "text": "st.markdown(\"<h2 style='color:orange;'>\\f1\\u-10179?\\u-9016?\\f2  \\f0 Visual Summary</h2>\", unsafe_allow_html=True)\\par"
                },
                {
                    "line_number": 243,
                    "text": "sns.set_theme(style=\"whitegrid\")\\par"
                },
                {
                    "line_number": 244,
                    "text": "\\par"
                },
                {
                    "line_number": 245,
                    "text": "# Bar chart: Score per Hole\\par"
                },
                {
                    "line_number": 246,
                    "text": "fig1, ax1 = plt.subplots(figsize=(8, 4))\\par"
                },
                {
                    "line_number": 247,
                    "text": "sns.barplot(x=\"Hole\", y=\"Score\", data=df, ax=ax1, palette=\"viridis\")\\par"
                },
                {
                    "line_number": 248,
                    "text": "ax1.set_title(\"Score per Hole\", fontsize=12)\\par"
                },
                {
                    "line_number": 249,
                    "text": "ax1.set_xlabel(\"Hole\", fontsize=10)\\par"
                },
                {
                    "line_number": 250,
                    "text": "ax1.set_ylabel(\"Score\", fontsize=10)\\par"
                },
                {
                    "line_number": 251,
                    "text": "plt.tight_layout()\\par"
                },
                {
                    "line_number": 252,
                    "text": "st.pyplot(fig1)\\par"
                },
                {
                    "line_number": 253,
                    "text": "\\par"
                },
                {
                    "line_number": 254,
                    "text": "# Pie chart: Score Distribution\\par"
                },
                {
                    "line_number": 255,
                    "text": "score_counts = df[\"Score\"].apply(lambda x: \"Birdie\" if x == 2 else \"Par\" if x == 3 else \"Bogey+\").value_counts()\\par"
                },
                {
                    "line_number": 256,
                    "text": "fig2, ax2 = plt.subplots(figsize=(5, 5))\\par"
                },
                {
                    "line_number": 257,
                    "text": "ax2.pie(score_counts, labels=score_counts.index, autopct='%1.1f%%', startangle=90)\\par"
                },
                {
                    "line_number": 258,
                    "text": "ax2.set_title(\"Score Distribution\", fontsize=12)\\par"
                },
                {
                    "line_number": 259,
                    "text": "plt.tight_layout()\\par"
                },
                {
                    "line_number": 260,
                    "text": "st.pyplot(fig2)\\par"
                },
                {
                    "line_number": 261,
                    "text": "\\par"
                },
                {
                    "line_number": 262,
                    "text": "# Line chart: Putts per Hole\\par"
                },
                {
                    "line_number": 263,
                    "text": "fig3, ax3 = plt.subplots(figsize=(8, 4))\\par"
                },
                {
                    "line_number": 264,
                    "text": "sns.lineplot(x=\"Hole\", y=\"Putts\", data=df, marker=\"o\", ax=ax3)\\par"
                },
                {
                    "line_number": 265,
                    "text": "ax3.set_title(\"Putts per Hole\", fontsize=12)\\par"
                },
                {
                    "line_number": 266,
                    "text": "ax3.set_xlabel(\"Hole\", fontsize=10)\\par"
                },
                {
                    "line_number": 267,
                    "text": "ax3.set_ylabel(\"Putts\", fontsize=10)\\par"
                },
                {
                    "line_number": 268,
                    "text": "plt.tight_layout()\\par"
                },
                {
                    "line_number": 269,
                    "text": "st.pyplot(fig3)\\par"
                },
                {
                    "line_number": 270,
                    "text": "def generate_summary_image(player_name, total_score, birdies, pars, bogeys, greens_pitched, gir_percentage,\\par"
                },
                {
                    "line_number": 271,
                    "text": "chip_ins, total_putts, average_putts, birdie_conversion, missed_green_recovery,\\par"
                },
                {
                    "line_number": 272,
                    "text": "avg_birdie_putt_made, avg_birdie_putt_missed, round_notes):\\par"
                },
                {
                    "line_number": 273,
                    "text": "width, height = 720, 1280\\par"
                },
                {
                    "line_number": 274,
                    "text": "image = Image.new(\"RGB\", (width, height), color=\"white\")\\par"
                },
                {
                    "line_number": 275,
                    "text": "draw = ImageDraw.Draw(image)\\par"
                },
                {
                    "line_number": 276,
                    "text": "\\par"
                },
                {
                    "line_number": 277,
                    "text": "try:\\par"
                },
                {
                    "line_number": 278,
                    "text": "font_title = ImageFont.truetype(\"arial.ttf\", 40)\\par"
                },
                {
                    "line_number": 279,
                    "text": "font_subtitle = ImageFont.truetype(\"arial.ttf\", 28)\\par"
                },
                {
                    "line_number": 280,
                    "text": "font_text = ImageFont.truetype(\"arial.ttf\", 24)\\par"
                },
                {
                    "line_number": 281,
                    "text": "except IOError:\\par"
                },
                {
                    "line_number": 282,
                    "text": "font_title = font_subtitle = font_text = None  # fallback to default\\par"
                },
                {
                    "line_number": 283,
                    "text": "\\par"
                },
                {
                    "line_number": 284,
                    "text": "y = 40\\par"
                },
                {
                    "line_number": 285,
                    "text": "draw.text((40, y), f\"\\f3\\u9971?\\f2  \\f0 Round Summary \\f2\\endash  \\{player_name\\}\", font=font_title, fill=\"black\")\\par"
                },
                {
                    "line_number": 286,
                    "text": "y += 80\\par"
                },
                {
                    "line_number": 287,
                    "text": "draw.text((40, y), f\"Total Score: \\{total_score\\}\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 288,
                    "text": "draw.text((40, y), f\"Birdies: \\{birdies\\}\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 289,
                    "text": "draw.text((40, y), f\"Pars: \\{pars\\}\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 290,
                    "text": "draw.text((40, y), f\"Bogeys or worse: \\{bogeys\\}\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 291,
                    "text": "draw.text((40, y), f\"Greens Hit (GIR): \\{greens_pitched\\} (\\{gir_percentage:.1f\\}%)\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 292,
                    "text": "draw.text((40, y), f\"Chip-ins: \\{chip_ins\\}\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 293,
                    "text": "draw.text((40, y), f\"Total Putts: \\{int(total_putts)\\} (Avg: \\{average_putts:.2f\\})\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 294,
                    "text": "draw.text((40, y), f\"Birdie Conversion on GIR: \\{birdie_conversion:.1f\\}%\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 295,
                    "text": "draw.text((40, y), f\"Missed Green Birdie Recovery: \\{missed_green_recovery:.1f\\}%\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 296,
                    "text": "if not pd.isna(avg_birdie_putt_made):\\par"
                },
                {
                    "line_number": 297,
                    "text": "draw.text((40, y), f\"Avg Birdie Putt Made Distance: \\{avg_birdie_putt_made:.1f\\} ft\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 298,
                    "text": "if not pd.isna(avg_birdie_putt_missed):\\par"
                },
                {
                    "line_number": 299,
                    "text": "draw.text((40, y), f\"Avg Birdie Putt Missed Distance: \\{avg_birdie_putt_missed:.1f\\} ft\", font=font_text, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 300,
                    "text": "\\par"
                },
                {
                    "line_number": 301,
                    "text": "y += 20\\par"
                },
                {
                    "line_number": 302,
                    "text": "draw.text((40, y), \"\\f4\\u-10178?\\u-8736?\\f2  \\f0 AI Feedback:\", font=font_subtitle, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 303,
                    "text": "if avg_birdie_putt_made and avg_birdie_putt_made < 10:\\par"
                },
                {
                    "line_number": 304,
                    "text": "draw.text((60, y), \"\\f4\\u10004?\\u-497?\\f2  \\f0 Converting birdie putts well from short range.\", font=font_text, fill=\"black\"); y += 30\\par"
                },
                {
                    "line_number": 305,
                    "text": "if avg_birdie_putt_missed and avg_birdie_putt_missed > 10:\\par"
                },
                {
                    "line_number": 306,
                    "text": "draw.text((60, y), \"\\f4\\u9888?\\u-497?\\f2  \\f0 Missing birdie putts from long range.\", font=font_text, fill=\"black\"); y += 30\\par"
                },
                {
                    "line_number": 307,
                    "text": "if birdie_conversion < 30:\\par"
                },
                {
                    "line_number": 308,
                    "text": "draw.text((60, y), \"\\f1\\u-10179?\\u-9015?\\f2  \\f0 Low birdie conversion on greens hit.\", font=font_text, fill=\"black\"); y += 30\\par"
                },
                {
                    "line_number": 309,
                    "text": "if missed_green_recovery > 20:\\par"
                },
                {
                    "line_number": 310,
                    "text": "draw.text((60, y), \"\\f1\\u-10179?\\u-8959?\\f2  \\f0 Great job recovering birdies after missed greens!\", font=font_text, fill=\"black\"); y += 30\\par"
                },
                {
                    "line_number": 311,
                    "text": "elif missed_green_recovery < 10:\\par"
                },
                {
                    "line_number": 312,
                    "text": "draw.text((60, y), \"\\f4\\u-10179?\\u-8480?\\u-497?\\f2  \\f0 Work on short game after missed greens.\", font=font_text, fill=\"black\"); y += 30\\par"
                },
                {
                    "line_number": 313,
                    "text": "\\par"
                },
                {
                    "line_number": 314,
                    "text": "if round_notes.strip():\\par"
                },
                {
                    "line_number": 315,
                    "text": "y += 20\\par"
                },
                {
                    "line_number": 316,
                    "text": "draw.text((40, y), \"\\f1\\u-10179?\\u-8995?\\f2  \\f0 Round Notes:\", font=font_subtitle, fill=\"black\"); y += 40\\par"
                },
                {
                    "line_number": 317,
                    "text": "for line in round_notes.splitlines():\\par"
                },
                {
                    "line_number": 318,
                    "text": "draw.text((60, y), f\"- \\{line\\}\", font=font_text, fill=\"black\"); y += 30\\par"
                },
                {
                    "line_number": 319,
                    "text": "\\par"
                },
                {
                    "line_number": 320,
                    "text": "return image\\par"
                },
                {
                    "line_number": 321,
                    "text": "}"
                },
                {
                    "line_number": 322,
                    "text": "\u0000"
                }
            ],
            "token_count": 2102
        }
    ]
}
