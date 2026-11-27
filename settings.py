# All tunable numbers live here.

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FRAMES_PER_SECOND = 60
WINDOW_TITLE = "Shift: A Jensen Huang Dating Sim"

STARTING_ATTRACTION = 30
MAX_ATTRACTION = 100
SHIFT_PENALTY = 5

# How strongly Jensen's feeling about your race scales an action's charm.
PREFERENCE_MULTIPLIER = {
    "loves": 2.0,
    "neutral": 0.5,
    "dislikes": -1.0,
}

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NVIDIA_GREEN = (118, 185, 0)
DARK_GRAY = (40, 40, 40)
PLACEHOLDER_BACKGROUND_COLOR = (60, 60, 90)

# Action buttons (stacked on the right side of the screen)
BUTTON_WIDTH = 460
BUTTON_HEIGHT = 50
BUTTON_SPACING = 10
BUTTONS_LEFT = SCREEN_WIDTH - BUTTON_WIDTH - 20
BUTTONS_TOP = 120
BUTTON_FONT_SIZE = 24
BUTTON_COLOR = DARK_GRAY
BUTTON_BORDER_COLOR = NVIDIA_GREEN
BUTTON_TEXT_COLOR = WHITE

# Attraction bar (top-left corner)
ATTRACTION_BAR_LEFT = 20
ATTRACTION_BAR_TOP = 20
ATTRACTION_BAR_WIDTH = 400
ATTRACTION_BAR_HEIGHT = 30
ATTRACTION_BAR_FILL_COLOR = NVIDIA_GREEN
ATTRACTION_BAR_EMPTY_COLOR = DARK_GRAY

# Dialogue box (bottom of the screen)
DIALOGUE_BOX_HEIGHT = 140
DIALOGUE_BOX_MARGIN = 20
DIALOGUE_FONT_SIZE = 30
DIALOGUE_BOX_COLOR = BLACK
DIALOGUE_TEXT_COLOR = WHITE

# Jensen (stands bottom-aligned, left of the action buttons)
JENSEN_IMAGE_PATH = "assets/jensen/OLD_MAN_GREEN_SURPRISED.png"
JENSEN_HEIGHT = 620
JENSEN_CENTER_X = 400

# Rounded corners and button press animation
DIALOGUE_BOX_CORNER_RADIUS = 30
BUTTON_PRESSED_COLOR = NVIDIA_GREEN
BUTTON_PRESS_SHRINK = 8  # pixels the button shrinks by at the start of the press
BUTTON_PRESS_ANIMATION_MILLISECONDS = 200

# Background music
BACKGROUND_MUSIC_PATH = "assets/sounds/music.mp3"
BACKGROUND_MUSIC_VOLUME = 0.5  # 0.0 (silent) to 1.0 (full)

# Studio splash screen
STUDIO_NAME = "Turtle Games"
STUDIO_NAME_FONT_SIZE = 90
STUDIO_SPLASH_MILLISECONDS = 3000

# Main menu and settings screen
GAME_TITLE = "SHIFT"
GAME_SUBTITLE = "A Jensen Huang Dating Sim"
TITLE_FONT_SIZE = 120
SUBTITLE_FONT_SIZE = 40
MENU_BUTTON_WIDTH = 320
MENU_BUTTON_HEIGHT = 60
MENU_BUTTON_SPACING = 20
MENU_BUTTONS_TOP = 340

# Asking about the chip formula wins at or above this attraction, and loses below it.
ATTRACTION_NEEDED_FOR_FORMULA = 80
DIALOGUE_TEXT_PADDING = 40  # gap between wrapped dialogue text and the box edge

# Game over banner
GAME_OVER_FONT_SIZE = 56
MISSION_FAILED_COLOR = (230, 70, 70)
