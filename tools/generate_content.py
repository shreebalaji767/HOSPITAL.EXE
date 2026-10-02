"""Generate browser content pools for HOSPITAL.EXE.
Run with Python 3: python tools/generate_content.py
The generated JavaScript is consumed by app.js. localStorage tracks consumed IDs.
"""
from pathlib import Path
import json

POOLS = {
    "statusTitles": [
        "Fictional systems reporting in","Hospital systems are making noises","All departments have reported something",
        "Reality check: inconclusive","Telemetry has become suspicious","The building is awake",
        "Normality packet rejected","Hospital civilization synchronized","Everything is technically running",
        "The dashboard has opinions","Reality service unavailable","The hospital has entered build mode"
    ],
    "activities": [
        "Queue behaving suspiciously well","Printer has resumed negotiations","Tea reserves detected",
        "Doctor finder has found itself","One elevator is thinking","Forms have multiplied",
        "A clipboard has gone missing","Reception has discovered a new token","The coffee protocol is active",
        "Department meeting has exceeded its meeting","Wi-Fi is emotionally stable","A wheelchair has requested navigation",
        "The lab fridge is humming confidently","A corridor has changed its mind","The billing screen is asking philosophical questions",
        "A pen has entered witness protection","The photocopier has become management","Someone scheduled a meeting about scheduling",
        "The waiting room has achieved sentience","The printer tray has filed paperwork","The elevator selected Floor Maybe",
        "The hospital map has invented a hallway","A clipboard has been promoted","Tea has reached critical temperature",
        "The reception bell is practicing Morse code","A form has reproduced overnight","The scanner is scanning nothing",
        "A chair has been reserved for an unknown department","The intercom announced its own announcement"
    ],
    "chaos": [
        ["Printer diplomacy failed.","The printer has requested a lawyer."],["Queue instability detected.","Token 9001 has challenged the queue."],
        ["Tea protocol overloaded.","Three cups are now running the department."],["Clipboard migration detected.","Every clipboard moved six meters left."],
        ["Elevator disagreement.","Floor 4 has been temporarily renamed Thursday."],["Form multiplication event.","One form produced seventeen cousins."],
        ["Pen shortage emergency.","The last pen entered witness protection."],["Wi-Fi existential crisis.","The router is reconsidering its career."],
        ["Reception paradox.","The appointment arrived before the patient."],["Billing turbulence.","The calculator requested a second calculator."],
        ["Lab rebellion.","The test tube appointed itself supervisor."],["Night-shift anomaly.","A corridor light is doing its own rounds."]
    ],
    "doctorReplies": [
        "Doctor says: Please stop asking the website medical questions.","Doctor is thinking... very loudly.",
        "Doctor has requested a coffee.","Doctor has left the comic panel.","Doctor says: Hmm.",
        "Doctor has opened another tab.","Doctor is waiting for the printer.","Doctor has misplaced the pen.",
        "Doctor referred the question to Reception.","Doctor is consulting the clipboard.",
        "Doctor says: That sounds like a website problem.","Doctor entered diagnostic loading mode."
    ],
    "notifications": [
        "A clipboard has gone missing in a completely fictional corridor.","Printer status: negotiating with paper.",
        "Tea has been deployed to an unspecified department.","Elevator selected a philosophical floor.",
        "Form count increased without authorization.","Doctor finder located a doctor, then lost the finder.",
        "Lab beaker status: promoted.","Wi-Fi status: emotionally available.",
        "Waiting-room chair has remembered everything.","Reception bell is now monitoring reception.",
        "Pen status: somewhere.","Photocopier requested management approval."
    ]
}

out = Path("js/generated-content.js")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("/* AUTO-GENERATED — DO NOT EDIT */\nwindow.HOSPITAL_CONTENT = " +
               json.dumps(POOLS, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
print("Generated", out)
