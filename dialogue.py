# Every line Jensen says. Data only, no logic.

OPENING_LINE = "Hey there! Wanna go throw fistfuls of yogurt at pigeons?"

# REACTION_LINES[action_key][reaction_level]
# reaction_level is one of: "loves", "neutral", "dislikes"
REACTION_LINES = {
    "compliment_jacket": {
        "loves": "He adjusts the jacket, blushing. \"It's the 2019 edition.\"",
        "neutral": "\"Thanks. I have forty of these.\"",
        "dislikes": "He zips the jacket up defensively.",
    },
    "talk_cuda": {
        "loves": "His eyes light up. \"Finally, someone who gets it.\"",
        "neutral": "\"Yes, CUDA is very popular.\"",
        "dislikes": "He checks his phone mid-sentence.",
    },
    "bring_gpu": {
        "loves": "He holds it like a newborn. \"You shouldn't have.\"",
        "neutral": "\"Ah, last generation. Thoughtful.\"",
        "dislikes": "\"Is this... an AMD card?\"",
    },
    "ask_formula": {
        "loves": "He leans in. \"Maybe... if you stay for dessert.\"",
        "neutral": "\"That's confidential.\"",
        "dislikes": "He waves over a security guard.",
    },
    "defecate": {
        "loves": "He sniffs himself. \"I haven't felt so warm in ages...\"",
        "neutral": "\"I like it but please seek help.\"",
        "dislikes": "He throws it back.",
    },
}

SHIFT_LINES = [
    "Jensen blinks. \"Did you... change?\"",
    "\"Weird. I could've sworn you looked different a second ago.\"",
    "He rubs his eyes. \"I need to sleep more.\"",
]

WIN_LINE = "Jensen slides a napkin across the table. On it: the chip formula."
LOSE_LINE = "Security escorts you out. Jensen doesn't even look up."
