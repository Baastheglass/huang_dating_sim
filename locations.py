# Every place the date can happen. Data only, no logic.
# Source: assets/dialogue/Dialogues.pdf, section C.
# available_actions: keys from actions.ACTIONS. Every action is used at least once.
# "defecate" and "ask_formula" are available everywhere.

LOCATIONS = [
    {
        "name": "Coffeeshop in San Francisco",
        "background": "assets/backgrounds/coffeeshop.png",
        "available_actions": ["compliment_jacket", "tell_knock_knock_joke", "rave_about_being_fan", "defecate", "ask_formula"],
    },
    {
        "name": "His office",
        "background": "assets/backgrounds/office.png",
        "available_actions": ["talk_cuda", "talk_accelerated_computing", "talk_about_wife", "defecate", "ask_formula"],
    },
    {
        "name": "Technology conference",
        "background": "assets/backgrounds/tech_conference.png",
        "available_actions": ["talk_physical_ai", "talk_ai_healthcare", "make_finger_gun", "defecate", "ask_formula"],
    },
    {
        "name": "A Four Seasons hotel lobby",
        "background": "assets/backgrounds/four_seasons_lobby.png",
        "available_actions": ["insult_shoes", "ask_to_smell_feet", "compliment_jacket", "defecate", "ask_formula"],
    },
    {
        "name": "Ji Yuan Sichuan Restaurant",
        "background": "assets/backgrounds/sichuan_restaurant.png",
        "available_actions": ["challenge_hot_pepper", "talk_about_wife", "defecate", "ask_formula"],
    },
    {
        "name": "Taipei's Linjiang Street Night Market",
        "background": "assets/backgrounds/night_market.png",
        "available_actions": ["challenge_hot_pepper", "make_finger_gun", "rave_about_being_fan", "defecate", "ask_formula"],
    },
]
