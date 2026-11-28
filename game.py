# Run this file to play: python game.py
#
# The game moves through these screens:
#   "studio_splash" -> "main_menu" -> "playing"
#                          ^  |
#                          |  v
#                       "settings"

import pygame

from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FRAMES_PER_SECOND,
    WINDOW_TITLE,
    BACKGROUND_MUSIC_PATHS,
    BACKGROUND_MUSIC_VOLUME,
    STUDIO_SPLASH_MILLISECONDS,
)
from game_state import GameState
from drawing import draw_everything
from menus import draw_studio_splash, draw_main_menu, draw_settings_menu


def find_clicked_button(mouse_position, clickable_buttons):
    """Return the key of the button under the mouse, or None if no button was clicked."""
    for button_rectangle, button_key in clickable_buttons:
        if button_rectangle.collidepoint(mouse_position):
            return button_key
    return None


def handle_key_press(key, game_state):
    if key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
        game_state.shift_race()


def handle_action_click(action_key, game_state):
    game_state.last_pressed_action_key = action_key
    game_state.last_button_press_time = pygame.time.get_ticks()
    game_state.perform_action(action_key)


def start_background_music():
    """Play the first music file that loads. If none work (bad file, no sound device), play nothing."""
    for music_path in BACKGROUND_MUSIC_PATHS:
        try:
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.set_volume(BACKGROUND_MUSIC_VOLUME)
            pygame.mixer.music.play(loops=-1)  # -1 means loop forever
            return
        except pygame.error as music_error:
            print(f"Could not play {music_path}: {music_error}")
    print("No background music will play.")


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()

    start_background_music()
    is_music_on = True

    current_screen = "studio_splash"
    splash_start_time = pygame.time.get_ticks()
    game_state = None  # created when the player presses Play Game
    clickable_buttons = []

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            elif current_screen == "studio_splash":
                if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                    current_screen = "main_menu"  # any key or click skips the splash

            elif current_screen == "playing" and game_state.is_game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    current_screen = "main_menu"

            elif current_screen == "playing":
                if event.type == pygame.KEYDOWN:
                    handle_key_press(event.key, game_state)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    action_key = find_clicked_button(event.pos, clickable_buttons)
                    if action_key is not None:
                        handle_action_click(action_key, game_state)

            elif event.type == pygame.MOUSEBUTTONDOWN:  # main menu or settings
                button_key = find_clicked_button(event.pos, clickable_buttons)
                if button_key == "play_game":
                    game_state = GameState()
                    current_screen = "playing"
                elif button_key == "open_settings":
                    current_screen = "settings"
                elif button_key == "exit_game":
                    is_running = False
                elif button_key == "toggle_music":
                    is_music_on = not is_music_on
                    if not pygame.mixer.get_init():
                        pass  # no working audio, so there is nothing to pause or unpause
                    elif is_music_on:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                elif button_key == "back_to_main_menu":
                    current_screen = "main_menu"

        if current_screen == "studio_splash":
            milliseconds_since_start = pygame.time.get_ticks() - splash_start_time
            draw_studio_splash(screen, milliseconds_since_start)
            clickable_buttons = []
            if milliseconds_since_start >= STUDIO_SPLASH_MILLISECONDS:
                current_screen = "main_menu"
        elif current_screen == "main_menu":
            clickable_buttons = draw_main_menu(screen)
        elif current_screen == "settings":
            clickable_buttons = draw_settings_menu(screen, is_music_on)
        elif current_screen == "playing":
            clickable_buttons = draw_everything(screen, game_state)

        pygame.display.flip()
        clock.tick(FRAMES_PER_SECOND)

    pygame.quit()


if __name__ == "__main__":
    run_game()
