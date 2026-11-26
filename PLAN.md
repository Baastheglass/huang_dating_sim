# Jensen Huang Dating Sim: Implementation Plan

## Core loop

You're a spy at a location, and Jensen stands in front of the background. You pick an action and he reacts, which moves the **attraction bar**. Pressing **Shift** changes your race, but each shift costs a little attraction.

- Attraction reaches 100: he gives you the chip formula and you win.
- Attraction drops to 0: security throws you out and you lose.

## File structure

```
huang_dating_sim/
├── game.py          # window, game loop, keyboard/mouse input
├── settings.py      # constants: screen size, colors, SHIFT_PENALTY, STARTING_ATTRACTION
├── game_state.py    # one object: current race, current location, attraction, last line spoken
├── drawing.py       # draws background, Jensen, attraction bar, dialogue box, buttons
├── menus.py         # studio splash, main menu and settings screens
├── races.py         # list of races: name, portrait image
├── actions.py       # list of actions: name, base_charm
├── locations.py     # list of locations: name, background image, which actions are available
├── dialogue.py      # every line Jensen says, grouped by action and reaction level
└── assets/
    ├── backgrounds/
    ├── jensen/
    └── races/
```

Rules:
- Data files (`races.py`, `actions.py`, `locations.py`, `dialogue.py`) contain **only plain lists and dicts**, with no logic.
- Adding a race, action, location or line of dialogue means editing one data file. You never touch `game.py`.

## How the data fits together

```python
# races.py
RACES = [
    {"name": "Elf", "portrait": "assets/races/elf.png"},
    {"name": "Robot", "portrait": "assets/races/robot.png"},
    ...
]

# actions.py
ACTIONS = {
    "compliment_jacket": {"button_text": "Compliment his leather jacket", "base_charm": 10},
    "talk_cuda": {"button_text": "Talk about CUDA", "base_charm": 8},
    ...
}

# locations.py
LOCATIONS = [
    {"name": "GTC Keynote Stage", "background": "assets/backgrounds/gtc.png",
     "available_actions": ["compliment_jacket", "talk_cuda"]},
    ...
]

# dialogue.py
REACTION_LINES = {
    "compliment_jacket": {
        "loves":    "He adjusts the jacket, blushing. \"It's the 2019 edition.\"",
        "neutral":  "\"Thanks. I have forty of these.\"",
        "dislikes": "He zips the jacket up defensively.",
    },
    ...
}
SHIFT_LINES = ["Jensen blinks. \"Did you... change?\"", ...]
```

## Attraction rule (the whole difficulty model)

At game start, `game_state.py` randomly gives each race a preference: one **secret favorite** (`loves`, multiplier 2.0), and every other race gets `neutral` (0.5) or `dislikes` (-1.0).

```python
attraction_change = ACTIONS[action]["base_charm"] * PREFERENCE_MULTIPLIER[reaction_level]
```

- Every Shift subtracts `SHIFT_PENALTY` (e.g. 5).
- Jensen's line (taken from `REACTION_LINES[action][reaction_level]`) tells you how warm he is toward your current race. Reading those lines is how you find the favorite.

## Phases

| Phase | Goal | Done when |
|---|---|---|
| **1. Skeleton** | `game.py` + `settings.py`: open a window, run the loop, quit cleanly. Use colored rectangles for Jensen and the background. | A window opens and closes without errors. |
| **2. State + bar** | `game_state.py` holds `attraction`, and `drawing.py` draws the attraction bar. | The bar shows the starting value (e.g. 30/100). |
| **3. Races + Shift** | Fill in `races.py`. Shift cycles `current_race_index`, subtracts `SHIFT_PENALTY`, shows the race name and portrait, and prints a line from `SHIFT_LINES`. | Pressing Shift changes the race and the bar drops. |
| **4. Actions + dialogue** | Fill in `actions.py` and `dialogue.py`. Action buttons appear, and clicking one applies the attraction rule and shows his reaction in the dialogue box. | The same action gets different reactions from different races. |
| **5. Locations** | Fill in `locations.py` (GTC stage, Denny's, server farm, rooftop). Add a "Travel" button, and each location shows only its own actions. | You can move between screens and Jensen stays in the foreground. |
| **6. Win/lose** | Attraction ≥ 100 shows the "chip formula acquired" ending. Attraction ≤ 0 shows the "escorted out by security" ending. Press R to restart with a new secret favorite. | You can play a full game from start to finish. |
| **7. Art + polish** | Replace the rectangles with images in `assets/`, then add a title screen and optional sounds. | It looks like a dating sim. |

Each phase leaves you with a runnable game.

## Design note

Jensen's lines in `dialogue.py` are written per **preference level** (loves / neutral / dislikes), never per race. The favorite race is random each game, so any race can be the winning one. Keep it that way: no race-specific jokes, accents or stereotyped portraits.
