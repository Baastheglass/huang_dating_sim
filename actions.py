# Everything the spy can do to Jensen. Data only, no logic.
# Source: assets/dialogue/Dialogues.pdf, section B.
# base_charm: how much attraction this action gives before Jensen's race preference is applied.

ACTIONS = {
    "compliment_jacket": {"button_text": "Compliment his leather jacket", "base_charm": 6},
    "talk_cuda": {"button_text": "Talk about CUDA", "base_charm": 10},
    "defecate": {"button_text": "Take a shit in your hand and throw it at him", "base_charm": 50},
    "talk_physical_ai": {"button_text": "Talk about Physical AI and Robotics", "base_charm": 10},
    "talk_ai_healthcare": {"button_text": "Talk about AI healthcare", "base_charm": 8},
    "tell_knock_knock_joke": {"button_text": "Tell a knock knock joke", "base_charm": 4},
    "insult_shoes": {"button_text": "Insult his shoes", "base_charm": 6},
    "ask_to_smell_feet": {"button_text": "Ask to smell his feet", "base_charm": 4},
    "talk_accelerated_computing": {"button_text": "Talk about Accelerated Computing", "base_charm": 12},
    "talk_about_wife": {"button_text": "Talk about his wife", "base_charm": 8},
    "challenge_hot_pepper": {"button_text": "Challenge him to eat a hot pepper", "base_charm": 6},
    "rave_about_being_fan": {"button_text": "Rave about being his fan", "base_charm": 8},
    "make_finger_gun": {"button_text": "Make a finger gun at him", "base_charm": 4},
    # Ends the game: win if attraction is high enough, lose otherwise (see game_state.py).
    "ask_formula": {"button_text": "Ask about the chip formula", "base_charm": 0},
}
