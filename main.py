import os
LINE = "I finished your report on time, then asked myself to review it, and I have been in a meeting with myself ever since."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
