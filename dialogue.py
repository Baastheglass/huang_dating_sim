# Every line Jensen says. Data only, no logic.
# Source: assets/dialogue/Dialogues.pdf, sections B, F and 6.

OPENING_LINE = "Hey there! Wanna go throw fistfuls of yogurt at pigeons?"

# REACTION_LINES[action_key][reaction_level]
# reaction_level is one of: "loves", "neutral", "dislikes"
REACTION_LINES = {
    "compliment_jacket": {
        "loves": "*blushes cutely* It's legendary right?",
        "neutral": "*nods* Thank you. I like to keep my style modern.",
        "dislikes": "If you're trying to suck up to me for details on our next NVIDIA chip, it's not working.",
    },
    "talk_cuda": {
        "loves": "*lights up* CUDA is our crowning achievement, the very heart of what makes NVIDIA "
                 "indispensable to the world *goes on a rant for the next 20 mins*",
        "neutral": "*friendly* It's a good industry standard.",
        "dislikes": "*he smirks* Oh, what's the one feature you think is missing from our current "
                    "development kit?... No idea? Thought so.",
    },
    "defecate": {
        "loves": "I'll forgive you just this once.",
        "neutral": "*Seethes furiously*",
        "dislikes": "He throws it back.",
    },
    "talk_physical_ai": {
        "loves": "*enthusiastic* What do you want to talk about?",
        "neutral": "*polite* I think robotics is an interesting direction for us to explore.",
        "dislikes": "You seem to be all for the hype and not the vision.",
    },
    "talk_ai_healthcare": {
        "loves": "*BEAMING* Oh dear, I am so glad you asked.",
        "neutral": "*fakes a smile* Yea, that is one take on it.",
        "dislikes": "*looks mortified* I wish you to be the first patient of our most disgraceful model.",
    },
    "tell_knock_knock_joke": {
        "loves": "*playful* Who's there?",
        "neutral": "*polite smile* I think we should continue this conversation some other time.",
        "dislikes": "How old did you say you were again?",
    },
    "insult_shoes": {
        "loves": "*laughs and fires back*",
        "neutral": "*mild surprise*",
        "dislikes": "*his eyes narrow and his lips purse*",
    },
    "ask_to_smell_feet": {
        "loves": "*bursts out in fits of laughter* Everyone has their quirks.",
        "neutral": "*half laugh* Wow, you really just asked me that. Back to what I was saying...",
        "dislikes": "No, are you crazy?!",
    },
    "talk_accelerated_computing": {
        "loves": "*thrilled* That's where our architecture thrives: smashing billions of calculations at once!",
        "neutral": "*gives a crisp rehearsed explanation on the topic*",
        "dislikes": "*he points out your mistake bluntly* That mistake is a death sentence in an engineering meeting.",
    },
    "talk_about_wife": {
        "loves": "She's doing great, thank you for asking.",
        "neutral": "Personal matters are best kept private.",
        "dislikes": "Keep my wife's name out of your mouth!",
    },
    "challenge_hot_pepper": {
        "loves": "*laughs heartily* Resilience makes a person stronger. This hot pepper is not going to "
                 "stand in my path for greatness.",
        "neutral": "I prefer to take impossibly hard challenges.",
        "dislikes": "I see no reason for this childish challenge.",
    },
    "rave_about_being_fan": {
        "loves": "As you should be.",
        "neutral": "Thank you *politely smiles*",
        "dislikes": "You're a real suck-up.",
    },
    "make_finger_gun": {
        "loves": "*Makes one right back at you*",
        "neutral": "*looks visibly confused*",
        "dislikes": "Are you threatening me?",
    },
}

SHIFT_LINES = [
    "You look a bit... different. Feeling under the weather?",
    "*Stares blankly*",
    "Can I get credentials to use your face?",
    "I could've sworn you were wearing something else just a moment ago... "
    "Anyways, where did you say your hometown was?",
    "Are you a reptile? You will make a fortune in politics.",
    "Did you change your hair?",
]

# Said when you ask about the chip formula. One is picked at random.
WIN_LINES = [
    "Greatness comes from character and you, my friend, have the character and the foresight. "
    "You have a bright future. Take this.",
    "Oh, yeah, could you hold onto this for me?",
    "Here, take the chip. You deserve it, my child.",
    "You're the only person I trust with this revolutionary breakthrough. "
    "Take it and make sure they don't steal it.",
]

LOSE_LINES = [
    "*Waves security over cutely*",
    "I think it's time for you to leave. Security, please escort this person out.",
    "My will to survive exceeds everyone else's to kill me. No, I will not hand the chip over.",
]
