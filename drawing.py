# Everything that puts pixels on the screen. Reads the game state, never changes it.

import functools

import pygame

from actions import ACTIONS
from locations import LOCATIONS
from races import RACES
from settings import (
    DARK_GRAY,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLACEHOLDER_BACKGROUND_COLOR,
    JENSEN_IMAGE_PATH,
    JENSEN_HEIGHT,
    JENSEN_CENTER_X,
    BUTTONS_LEFT,
    BUTTONS_TOP,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_SPACING,
    BUTTON_FONT_SIZE,
    BUTTON_COLOR,
    BUTTON_BORDER_COLOR,
    BUTTON_TEXT_COLOR,
    BUTTON_PRESSED_COLOR,
    BUTTON_PRESS_SHRINK,
    BUTTON_PRESS_ANIMATION_MILLISECONDS,
    DIALOGUE_BOX_CORNER_RADIUS,
    MAX_ATTRACTION,
    WHITE,
    NVIDIA_GREEN,
    ATTRACTION_BAR_LEFT,
    ATTRACTION_BAR_TOP,
    ATTRACTION_BAR_WIDTH,
    ATTRACTION_BAR_HEIGHT,
    ATTRACTION_BAR_FILL_COLOR,
    ATTRACTION_BAR_EMPTY_COLOR,
    DIALOGUE_BOX_HEIGHT,
    DIALOGUE_BOX_MARGIN,
    DIALOGUE_FONT_SIZE,
    DIALOGUE_BOX_COLOR,
    DIALOGUE_TEXT_COLOR,
)


def draw_background(screen, game_state):
    # Phase 7: draw the current location's background image.
    screen.fill(PLACEHOLDER_BACKGROUND_COLOR)


@functools.cache  # load and scale the image once, not every frame
def get_jensen_image():
    original_image = pygame.image.load(JENSEN_IMAGE_PATH).convert_alpha()
    scale = JENSEN_HEIGHT / original_image.get_height()
    return pygame.transform.smoothscale_by(original_image, scale)


def draw_jensen(screen):
    jensen_image = get_jensen_image()
    screen.blit(jensen_image, jensen_image.get_rect(midbottom=(JENSEN_CENTER_X, SCREEN_HEIGHT)))


def draw_attraction_bar(screen, game_state):
    empty_bar = pygame.Rect(ATTRACTION_BAR_LEFT, ATTRACTION_BAR_TOP, ATTRACTION_BAR_WIDTH, ATTRACTION_BAR_HEIGHT)
    filled_width = ATTRACTION_BAR_WIDTH * game_state.attraction // MAX_ATTRACTION
    filled_bar = pygame.Rect(ATTRACTION_BAR_LEFT, ATTRACTION_BAR_TOP, filled_width, ATTRACTION_BAR_HEIGHT)

    pygame.draw.rect(screen, ATTRACTION_BAR_EMPTY_COLOR, empty_bar)
    pygame.draw.rect(screen, ATTRACTION_BAR_FILL_COLOR, filled_bar)
    pygame.draw.rect(screen, WHITE, empty_bar, width=2)

    bar_label = get_font(BUTTON_FONT_SIZE).render(f"Attraction: {game_state.attraction}/{MAX_ATTRACTION}", True, WHITE)
    screen.blit(bar_label, bar_label.get_rect(center=empty_bar.center))


def draw_race_label(screen, game_state):
    """Show the current race in the top-right corner, level with the attraction bar."""
    current_race_name = RACES[game_state.current_race_index]["name"]
    race_text = get_font(BUTTON_FONT_SIZE).render(f"Race: {current_race_name}   (Shift to change)", True, WHITE)

    race_label_box = pygame.Rect(0, 0, race_text.get_width() + 20, ATTRACTION_BAR_HEIGHT)
    race_label_box.topright = (SCREEN_WIDTH - ATTRACTION_BAR_LEFT, ATTRACTION_BAR_TOP)
    pygame.draw.rect(screen, DARK_GRAY, race_label_box)
    pygame.draw.rect(screen, WHITE, race_label_box, width=2)
    screen.blit(race_text, race_text.get_rect(center=race_label_box.center))


def draw_dialogue_box(screen, game_state):
    dialogue_box = pygame.Rect(
        DIALOGUE_BOX_MARGIN,
        SCREEN_HEIGHT - DIALOGUE_BOX_HEIGHT - DIALOGUE_BOX_MARGIN,
        SCREEN_WIDTH - 2 * DIALOGUE_BOX_MARGIN,
        DIALOGUE_BOX_HEIGHT,
    )
    pygame.draw.rect(screen, DIALOGUE_BOX_COLOR, dialogue_box, border_radius=DIALOGUE_BOX_CORNER_RADIUS)
    pygame.draw.rect(screen, NVIDIA_GREEN, dialogue_box, width=2, border_radius=DIALOGUE_BOX_CORNER_RADIUS)

    # shortcut: one line of text, no word wrap; add wrapping if lines get longer than the box.
    dialogue_text = get_font(DIALOGUE_FONT_SIZE).render(game_state.jensen_line, True, DIALOGUE_TEXT_COLOR)
    screen.blit(dialogue_text, dialogue_text.get_rect(center=dialogue_box.center))


@functools.cache  # build each font size once, not every frame
def get_font(font_size):
    return pygame.font.Font(None, font_size)


def get_press_animation_progress(game_state, action_key):
    """0.0 right after the click, 1.0 when the animation ends. None if this button isn't animating."""
    if game_state.last_pressed_action_key != action_key:
        return None
    time_since_press = pygame.time.get_ticks() - game_state.last_button_press_time
    if time_since_press >= BUTTON_PRESS_ANIMATION_MILLISECONDS:
        return None
    return time_since_press / BUTTON_PRESS_ANIMATION_MILLISECONDS


def draw_action_buttons(screen, game_state):
    """Draw one button per action available at the current location.
    Returns a list of (button_rectangle, action_key) so game.py can check clicks."""
    current_location = LOCATIONS[game_state.current_location_index]
    action_buttons = []

    for button_number, action_key in enumerate(current_location["available_actions"]):
        button_top = BUTTONS_TOP + button_number * (BUTTON_HEIGHT + BUTTON_SPACING)
        button_rectangle = pygame.Rect(BUTTONS_LEFT, button_top, BUTTON_WIDTH, BUTTON_HEIGHT)

        # Press animation: the clicked button shrinks and turns green, then springs back.
        drawn_rectangle = button_rectangle
        fill_color = BUTTON_COLOR
        press_progress = get_press_animation_progress(game_state, action_key)
        if press_progress is not None:
            shrink_amount = round(BUTTON_PRESS_SHRINK * (1 - press_progress))
            drawn_rectangle = button_rectangle.inflate(-shrink_amount * 2, -shrink_amount)
            fill_color = BUTTON_PRESSED_COLOR

        pygame.draw.rect(screen, fill_color, drawn_rectangle, border_radius=8)
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, drawn_rectangle, width=2, border_radius=8)

        button_text = get_font(BUTTON_FONT_SIZE).render(ACTIONS[action_key]["button_text"], True, BUTTON_TEXT_COLOR)
        screen.blit(button_text, button_text.get_rect(center=drawn_rectangle.center))

        # Clicks are checked against the full-size rectangle, not the shrunken one.
        action_buttons.append((button_rectangle, action_key))

    return action_buttons


def draw_everything(screen, game_state):
    draw_background(screen, game_state)
    draw_jensen(screen)
    draw_attraction_bar(screen, game_state)
    draw_race_label(screen, game_state)
    draw_dialogue_box(screen, game_state)
    return draw_action_buttons(screen, game_state)
