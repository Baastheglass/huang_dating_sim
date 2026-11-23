# Holds everything that changes while playing.

from settings import STARTING_ATTRACTION
from dialogue import OPENING_LINE


class GameState:
    def __init__(self):
        self.attraction = STARTING_ATTRACTION
        self.current_race_index = 0
        self.current_location_index = 0
        self.jensen_line = OPENING_LINE
        # race name -> "loves" / "neutral" / "dislikes"
        self.jensen_preference_for_race = {}
        self.is_game_over = False

    def shift_race(self):
        # Phase 3: move to the next race, subtract SHIFT_PENALTY, pick a SHIFT_LINE.
        pass

    def perform_action(self, action_key):
        # Phase 4: apply base_charm * PREFERENCE_MULTIPLIER, set jensen_line from REACTION_LINES.
        pass

    def travel_to_next_location(self):
        # Phase 5: move to the next location.
        pass

    def check_game_over(self):
        # Phase 6: win at MAX_ATTRACTION, lose at 0.
        pass
