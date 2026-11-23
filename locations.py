# Every place the date can happen. Data only, no logic.
# available_actions: keys from actions.ACTIONS.

LOCATIONS = [
    {
        "name": "GTC Keynote Stage",
        "background": "assets/backgrounds/gtc_stage.png",
        "available_actions": ["compliment_jacket", "talk_cuda", "ask_formula"],
    },
    {
        "name": "Denny's",
        "background": "assets/backgrounds/dennys.png",
        "available_actions": ["compliment_jacket", "bring_gpu"],
    },
    {
        "name": "Server Farm",
        "background": "assets/backgrounds/server_farm.png",
        "available_actions": ["talk_cuda", "bring_gpu", "ask_formula"],
    },
    {
        "name": "Rooftop",
        "background": "assets/backgrounds/rooftop.png",
        "available_actions": ["compliment_jacket", "ask_formula"],
    },
]
