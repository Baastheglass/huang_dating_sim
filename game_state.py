# Holds everything that changes while playing.

import random

from settings import STARTING_ATTRACTION, MAX_ATTRACTION, PREFERENCE_MULTIPLIER, SHIFT_PENALTY
from dialogue import REACTION_LINES, SHIFT_LINES
from races import RACES
from actions import ACTIONS


def pick_jensen_preferences():
    """One random race is his favorite; every other race is randomly neutral or disliked."""
    favorite_race = random.choice(RACES)["name"]
    preferences = {}
    for race in RACES:
        if race["name"] == favorite_race:
            preferences[race["name"]] = "loves"
        else:
            preferences[race["name"]] = random.choice(["neutral", "dislikes"])
    return preferences


class GameState:
    def __init__(self):
        self.attraction = STARTING_ATTRACTION
        self.current_race_index = 0
        self.current_location_index = 0
        self.jensen_line = None  # no dialogue until the player does something
        # race name -> "loves" / "neutral" / "dislikes"
        self.jensen_preference_for_race = pick_jensen_preferences()
        self.is_game_over = False

    def shift_race(self):
        self.current_race_index = (self.current_race_index + 1) % len(RACES)
        self.attraction = max(0, self.attraction - SHIFT_PENALTY)
        self.jensen_line = random.choice(SHIFT_LINES)

    def perform_action(self, action_key):
        current_race_name = RACES[self.current_race_index]["name"]
        reaction_level = self.jensen_preference_for_race[current_race_name]

        attraction_change = ACTIONS[action_key]["base_charm"] * PREFERENCE_MULTIPLIER[reaction_level]
        new_attraction = round(self.attraction + attraction_change)
        self.attraction = max(0, min(MAX_ATTRACTION, new_attraction))

        self.jensen_line = REACTION_LINES[action_key][reaction_level]

    def travel_to_next_location(self):
        # Phase 5: move to the next location.
        pass

    def check_game_over(self):
        # Phase 6: win at MAX_ATTRACTION, lose at 0.
        pass
