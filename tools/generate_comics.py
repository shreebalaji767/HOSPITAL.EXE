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
    ("THE MRI", "PATIENT", "MRI", "Is this machine safe?", "It is safe. The machine is not sure about you."),
    ("THE SURGERY BUTTON", "SURGEON", "BUTTON", "What does this button do?", "Nobody knows. Press it."),
    ("THE PHARMACY", "PATIENT", "PHARMACY", "Is my medicine ready?", "It is waiting for its medicine."),
    ("THE BLOOD BANK", "TECH", "FRIDGE", "Why is the fridge beeping?", "It wants a blood-pressure check."),
    ("THE CAFETERIA", "STAFF", "CHEF", "One tea, please.", "The tea has requested a second opinion."),
    ("THE PARKING LOT", "DRIVER", "SIGN", "Where do I park?", "Parking space has entered maintenance mode."),
    ("THE RECEPTION BOSS", "VISITOR", "RECEPTION", "I have an appointment.", "The appointment has an appointment."),
    ("THE ICU MONITOR", "NURSE", "MONITOR", "Everything looks normal.", "BEEP."),
    ("THE PHYSIOTHERAPY ROBOT", "PATIENT", "ROBOT", "Can you help me walk?", "I am still learning legs."),
    ("THE DENTAL UNIT", "PATIENT", "DENTIST", "Will this hurt?", "Only emotionally."),
    ("THE EYE TEST", "DOCTOR", "EYE CHART", "Read the bottom line.", "The bottom line says: GOOD LUCK."),
    ("THE ENT DEPARTMENT", "DOCTOR", "EAR", "Can you hear me?", "The ear has muted you."),
    ("THE GENETICS LAB", "SCIENTIST", "DNA", "What did you find?", "A very complicated family group chat."),
    ("THE BLOOD PRESSURE MACHINE", "PATIENT", "MACHINE", "Please stay calm.", "I am the one under pressure."),
    ("THE WHEELCHAIR", "STAFF", "WHEELCHAIR", "Ready to move?", "I have already left."),
    ("THE HOSPITAL IT PATCH", "IT", "COMPUTER", "Patch complete.", "Now the mouse needs an update."),
    ("THE LOST FILE", "ADMIN", "FILE", "Where is patient file 404?", "It cannot be found."),
    ("THE CORRIDOR", "VISITOR", "CORRIDOR", "This corridor was not here yesterday.", "It was under construction emotionally."),
    ("THE DISCHARGE DESK", "PATIENT", "DESK", "Am I cleared to leave?", "The paperwork is not emotionally ready."),
    ("THE EMERGENCY BUTTON", "STAFF", "BUTTON", "Do NOT press that.", "I have pressed it."),
    ("THE SECURITY GUARD", "GUARD", "ELEVATOR", "Why did the elevator stop?", "It is taking a personal day."),
    ("THE HOSPITAL WIFI", "DOCTOR", "WIFI", "Is the Wi-Fi working?", "Yes. Emotionally."),
    ("THE CLEANING ROBOT", "HOUSEKEEPING", "ROBOT", "Please clean corridor B.", "Corridor B has filed a complaint."),
    ("THE LAB REPORT", "DOCTOR", "REPORT", "Is the report ready?", "The report is reviewing itself."),
    ("THE BED ALARM", "NURSE", "BED 7", "Why is the bed alarm ringing?", "The bed saw a ghost."),
    ("THE HOSPITAL ROOFTOP", "STAFF", "ROOFTOP", "Why is there a waiting room here?", "The elevator made a decision."),
    ["THE SURGEON'S COFFEE","SURGEON","COFFEE","Where is my coffee?","It has been referred to another department."],
    ["THE STETHOSCOPE","DOCTOR","STETHOSCOPE","I hear nothing.","The stethoscope is on silent mode."],
    ["THE CONSULTATION","PATIENT","DOCTOR","What is your diagnosis?","Please wait. My brain is buffering."],
    ["THE APPOINTMENT","PATIENT","RECEPTION","My appointment is at 5.","Which 5?"],
    ["THE DISCHARGE","PATIENT","DISCHARGE","Can I go home now?","Your file has decided to stay."],
    ["THE REFERRAL","DOCTOR","REFERRAL","I will refer you.","To whom?","The referral itself is still deciding."],
    ["THE SIGNATURE","ADMIN","FORM","Where do I sign?","Anywhere that looks official."],
    ["THE STAMP","ADMIN","STAMP","Is this approved?","STAMP says maybe."],
    ["THE TOKEN MACHINE","PATIENT","TOKEN MACHINE","I pressed the button.","Congratulations. You are now Token 9000."],
    ["THE WAITING ROOM","PATIENT","CHAIR","How long have I been waiting?","The chair remembers. You do not."],
    ["THE ONE MORE TEST","PATIENT","DOCTOR","Is that the last test?","Absolutely. One more."],
    ["THE TRY AGAIN","STAFF","COMPUTER","Did it work?","No. Try again with confidence."],
    ["THE PASSWORD","NURSE","COMPUTER","What's the password?","I forgot it while saying it."],
    ["THE WIFI PASSWORD","VISITOR","RECEPTION","What's the Wi-Fi password?","Please ask the Wi-Fi."],
    ["THE LOW BATTERY","DOCTOR","PHONE","My phone is at 1%.","Perfect. Emergency mode."],
    ["THE NO SIGNAL","STAFF","PHONE","Can you call the lab?","No signal. Try shouting."],
    ["THE UPDATE","IT","COMPUTER","Should we update now?","No. But I already did."],
    ["THE REBOOT","IT","SERVER","Have you restarted it?","I restarted myself."],
    ["THE TIMEOUT","PATIENT","SCREEN","Why did it time out?","It got tired of waiting."],
    ["THE CRASH","STAFF","COMPUTER","The system crashed.","It has requested a pillow."],
    ["THE GLITCH","NURSE","MONITOR","Why is the screen upside down?","The monitor has a different opinion."],
    ["THE OFFLINE DOCTOR","PATIENT","DOCTOR","Doctor, are you available?","Currently emotionally offline."],
    ["THE BACKUP","IT","SERVER","Do we have a backup?","Yes. It is also confused."],
    ["THE DEBUG","IT","COMPUTER","Find the bug.","I found seventeen and they have formed a union."],
    ["THE FIREWALL","SECURITY","FIREWALL","Who blocked the network?","The firewall has trust issues."],
    ["THE SCREENSHOT","ADMIN","SCREEN","Take a screenshot.","The screen is camera-shy."],
    ["THE POPUP","STAFF","COMPUTER","Close the popup.","It has opened another popup."],
    ["THE NOTIFICATION","NURSE","PHONE","What's that alarm?","A notification demanding attention."],
    ["THE AIRPLANE MODE","PATIENT","PHONE","Why is there no network?","Your phone has gone on vacation."],
    ["THE FINAL FORM","ADMIN","FORM 99-Z","Is this the final form?","Yes. Unless there is a final final form."],
]

def comic(title, left, right, line1, line2, *extra):
    if extra:
        line2 = line2 + " " + " ".join(extra)
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

# 49 additional paperwork-boss incidents.
stories.extend([("THE FINAL BOSS: PAPERWORK","ADMIN","PRINTER","We defeated the printer.","You forgot FORM 27-B."),("FORM 28: THE SEQUEL","ADMIN","FORM 28","Why are you here?","FORM 27-B referred me."),("THE SIGNATURE LOOP","DOCTOR","CLIPBOARD","Where do I sign?","Below the signature requesting your signature."),("THE STAMP OF DESTINY","ADMIN","STAMP","Is this approved?","It needs one more stamp."),("THE PHOTOCOPY PROBLEM","STAFF","COPIER","Make one copy.","Which copy of the copy?"),("THE MISSING ATTACHMENT","ADMIN","EMAIL","The form is complete.","The attachment has escaped."),("THE FORM FORM","RECEPTION","FORM","I need a form.","Which form?"),("THE COUNTER SIGNATURE","ADMIN","SIGNATURE","I signed it.","Someone must sign that you signed it."),("THE FILE NUMBER","RECORDS","FILE","What is the file number?","The file has forgotten."),("THE BLUE PEN LAW","ADMIN","PEN","Can I use black ink?","Not according to the imaginary law."),("THE THREE COPIES","RECEPTION","PRINTER","How many copies?","Three, plus one copy of the three copies."),("THE APPROVAL CHAIN","ADMIN","APPROVAL","Who approves this?","The person who approves the approver."),("THE FORM REJECTION","ADMIN","FORM","Why was it rejected?","The handwriting looked too confident."),("THE LOST STAPLE","RECORDS","STAPLER","Where is the staple?","It has been escalated."),("THE FILE FILE","RECORDS","FILE","I need the patient file.","Which file? The file about the file."),("THE RECEIPT RECEIPT","BILLING","RECEIPT","I need a receipt.","For which receipt?"),("THE DATE ERROR","ADMIN","CALENDAR","The date is correct.","Please correct the correct date."),("THE WITNESS FORM","ADMIN","FORM","Who witnessed this?","The previous form."),("THE ATTACHMENT ATTACHMENT","ADMIN","EMAIL","I attached the document.","Attach proof that you attached it."),("THE FINAL FINAL FORM","ADMIN","FORM","Is this the final form?","This is the final final form."),("THE QUEUE FORMS","RECEPTION","QUEUE","Take a token.","Which form gets the token?"),("THE PRINT PREVIEW","ADMIN","PRINTER","It looks perfect.","Print preview disagrees."),("THE MISSING PAGE","RECORDS","FILE","Pages 1 to 10 are here.","Page 7 has filed for independence."),("THE SIGNATURE FONT","ADMIN","FORM","My signature is valid.","It is not in the approved handwriting font."),("THE STAMP SHORTAGE","ADMIN","STAMP","Where is the approval stamp?","It is approving another stamp."),("THE FORM AUDIT","AUDITOR","FORM","Everything is complete.","Then why is there an audit form?"),("THE AUDIT AUDIT","AUDITOR","FILE","The audit is finished.","Now audit the audit."),("THE DOCUMENT OF DOCUMENTS","ADMIN","DOCUMENT","This is the document.","Where is the document proving it is the document?"),("THE FOLDER MAZE","RECORDS","FOLDER","Where should this go?","Inside the folder marked folders."),("THE LAST SIGNATURE","ADMIN","PEN","One last signature.","That sentence has never been true."),("THE FORM PASSWORD","ADMIN","FORM","What is the password?","It is written on Form 27-B."),("THE FORM 27-B","ADMIN","FORM 27-B","Who created you?","A checkbox nobody remembers selecting."),("THE CHECKBOX","ADMIN","CHECKBOX","Should I tick this?","Only if you have Form 27-C."),("THE FORM 27-C","ADMIN","FORM 27-C","I was told you needed me.","I need Form 27-D."),("THE FORM 27-D","ADMIN","FORM 27-D","This ends here.","That is adorable."),("THE PAPER TRAIL","RECORDS","PAPER","Where did all these papers come from?","Nobody knows. Everyone signed them."),("THE RUBBER STAMP","ADMIN","STAMP","Stamp it.","STAMP requires authorization."),("THE AUTHORIZATION","ADMIN","FORM","Who authorizes the stamp?","The authorization form."),("THE FORM INVENTORY","ADMIN","SHELF","How many forms do we have?","We counted yesterday. Today there are more."),("THE EMPTY FORM","ADMIN","FORM","Why is this blank?","It is waiting for its purpose."),("THE FORM THAT FORMS","ADMIN","FORM","This form is generating forms.","Please submit Form 27-B about that."),("THE PAPERWORK LOOP","ADMIN","PRINTER","We are finally done.","The printer printed the checklist for being done."),("THE LAST PAGE","RECORDS","FILE","This is the last page.","There is always another page."),("THE CHECKLIST","ADMIN","CHECKLIST","Everything is checked.","Except the checklist."),("THE CHECKLIST CHECKLIST","ADMIN","CHECKLIST","Now everything is checked.","Except the checklist checklist."),("THE ARCHIVE","RECORDS","ARCHIVE","Where does this old form go?","Into the archive of old forms."),("THE ARCHIVE FORM","RECORDS","FORM","Why is the archive asking for a form?","Because bureaucracy evolves."),("THE PAPERWORK END","ADMIN","PRINTER","Is paperwork finally defeated?","Please sign here to confirm.")])


stories.extend([
    ("THE FORM ELEVATOR","ADMIN","ELEVATOR","I submitted Form 27-B.","It requires Floor 27-B."),
    ("THE SIGNATURE RECEIPT","ADMIN","RECEIPT","I signed the form.","Please sign the receipt for your signature."),
    ("THE PAPERWORK PASSWORD","ADMIN","COMPUTER","Password accepted.","Now enter the password for the password."),
    ("THE APPROVAL BUTTON","ADMIN","BUTTON","I clicked approve.","Approval requires Form 27-B first."),
    ("THE FORM SHREDDER","RECORDS","SHREDDER","Finally, we can destroy the paperwork.","Please shred Form 27-B's permission to be shredded."),
    ("THE STAMP AUDIT","AUDITOR","STAMP","Why are there twelve stamps?","The stamps are auditing each other."),
    ("THE MISSING COPY","ADMIN","COPIER","Where is Copy 3?","Copy 3 became Copy 4."),
    ("THE PAPERWORK MEETING","ADMIN","MEETING","Why are we meeting?","To schedule a meeting about the meeting form."),
    ("THE FILE CABINET","RECORDS","CABINET","Where is the file?","It is in Cabinet B.","Which cabinet is B?","The form is asking."),
    ("THE FORM NUMBER","ADMIN","FORM","What number is this form?","Form 27-B.","We already have that.","This is the emotionally different one."),
    ("THE CHECKBOX APPROVAL","ADMIN","CHECKBOX","I checked every box.","There is a box confirming you checked every box."),
    ("THE PRINTER PEACE TREATY","ADMIN","PRINTER","We signed a peace treaty.","The printer wants three copies."),
    ("THE PAPERWORK MONSTER","STAFF","FORM","We have completed every form.","A new form has entered the building.")
])

if len(stories) < 100:
    raise SystemExit(f"Expected at least 100 comics, found {len(stories)}")

for number, story in enumerate(stories, 1):
    (OUT / f"{number:02d}.svg").write_text(comic(*story), encoding="utf-8")

# The browser uses this same Python-generated story pool for the live comic.
js_out = Path("js/generated-paperwork.js")
js_out.write_text(
    "/* AUTO-GENERATED BY tools/generate_comics.py — DO NOT EDIT */\\n"
    "window.HOSPITAL_PAPERWORK = " + __import__("json").dumps(stories, ensure_ascii=False, separators=(",", ":")) + ";\\n",
    encoding="utf-8"
)
print(f"Generated {len(stories)} original comic strips in {OUT}/ and live paperwork data in {js_out}")
