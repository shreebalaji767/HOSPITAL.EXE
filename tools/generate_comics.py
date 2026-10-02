"""Generate absurd HOSPITAL.EXE comic strips as standalone SVG files.
Run: python tools/generate_comics.py
The generated art uses original block-building/game-world motifs and no third-party game assets.
"""
from pathlib import Path
from html import escape

OUT = Path("assets/comics")
OUT.mkdir(parents=True, exist_ok=True)

stories = [
    ("THE ELEVATOR", "PATIENT", "ELEVATOR", "Floor 3, please.", "I have chosen Floor 7."),
    ("THE PRINTER", "NURSE", "PRINTER", "We need one page.", "I have printed 47 pages."),
    ("THE TEA DEPARTMENT", "DOCTOR", "TEA MACHINE", "Tea, please.", "TEA PROTOCOL ACTIVATED."),
    ("THE QUEUE", "PATIENT", "RECEPTION", "How long is the wait?", "That is not a number."),
    ("THE LOST PEN", "DOCTOR", "CLIPBOARD", "Where is my pen?", "You are holding it."),
    ("THE IT DEPARTMENT", "STAFF", "SERVER", "Restart the server.", "I have become architecture."),
    ("THE BED", "STAFF", "BED 12", "Who moved this bed?", "I moved myself."),
    ("THE LAB", "TECH", "TEST TUBE", "Please stay in the rack.", "I have dreams."),
    ("THE BILL", "PATIENT", "BILLING", "What is this charge?", "Processing the processing."),
    ("THE NIGHT SHIFT", "NURSE", "PRINTER", "Why is it quiet?", "PAPER JAM."),
    ("THE FINAL BOSS", "ADMIN", "FORM 27-B", "We defeated the printer.", "You forgot me."),
    ("THE HOSPITAL MAP", "VISITOR", "MAP", "Where is Radiology?", "The map is still loading."),
]

def comic(title, left, right, line1, line2):
    e = escape
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420">
<rect width="1200" height="420" fill="#fffdf7"/>
<rect x="18" y="18" width="1164" height="384" rx="8" fill="none" stroke="#10233f" stroke-width="6"/>
<text x="600" y="55" text-anchor="middle" font-family="Arial,sans-serif" font-size="28" font-weight="900" fill="#1261d6">{e(title)}</text>
<g font-family="Arial,sans-serif">
<rect x="40" y="80" width="540" height="285" fill="#fff" stroke="#10233f" stroke-width="4"/>
<text x="60" y="115" font-size="18" font-weight="900">{e(left)}</text>
<rect x="245" y="145" width="130" height="80" fill="#eef6ff" stroke="#10233f" stroke-width="4"/>
<rect x="270" y="170" width="80" height="55" fill="#1261d6"/>
<rect x="295" y="135" width="30" height="30" fill="#fff2cf" stroke="#10233f" stroke-width="3"/>
<rect x="75" y="265" width="470" height="65" rx="12" fill="#eef6ff" stroke="#10233f" stroke-width="3"/>
<text x="310" y="305" text-anchor="middle" font-size="20" font-weight="700">{e(line1)}</text>
<rect x="620" y="80" width="540" height="285" fill="#fff2cf" stroke="#10233f" stroke-width="4"/>
<text x="640" y="115" font-size="18" font-weight="900">{e(right)}</text>
<rect x="825" y="145" width="130" height="80" fill="#fff" stroke="#10233f" stroke-width="4"/>
<rect x="850" y="170" width="80" height="55" fill="#10233f"/>
<rect x="875" y="135" width="30" height="30" fill="#e94d4d" stroke="#10233f" stroke-width="3"/>
<rect x="655" y="265" width="470" height="65" rx="12" fill="#fff" stroke="#10233f" stroke-width="3"/>
<text x="890" y="305" text-anchor="middle" font-size="20" font-weight="700">{e(line2)}</text>
</g></svg>'''

for number, story in enumerate(stories, 1):
    (OUT / f"{number:02d}.svg").write_text(comic(*story), encoding="utf-8")

print(f"Generated {len(stories)} original comic strips in {OUT}/")
