# The screens before the game starts: studio splash, main menu and settings.

import pygame

from drawing import draw_button, get_font
from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BLACK,
    WHITE,
    NVIDIA_GREEN,
    PLACEHOLDER_BACKGROUND_COLOR,
    STUDIO_NAME,
    STUDIO_SPLASH_MILLISECONDS,
    STUDIO_NAME_FONT_SIZE,
    GAME_TITLE,
    GAME_SUBTITLE,
    TITLE_FONT_SIZE,
    SUBTITLE_FONT_SIZE,
    MENU_BUTTON_WIDTH,
    MENU_BUTTON_HEIGHT,
    MENU_BUTTON_SPACING,
    MENU_BUTTONS_TOP,
)


def draw_studio_splash(screen, milliseconds_since_start):
    """Black screen where the studio name fades in, holds, then fades out."""
    screen.fill(BLACK)

    progress = milliseconds_since_start / STUDIO_SPLASH_MILLISECONDS  # 0.0 to 1.0
    if progress < 0.3:
        brightness = progress / 0.3  # fade in
    elif progress < 0.7:
        brightness = 1.0  # hold
    else:
        brightness = max(0.0, (1.0 - progress) / 0.3)  # fade out

    studio_text = get_font(STUDIO_NAME_FONT_SIZE).render(STUDIO_NAME, True, WHITE)
    studio_text.set_alpha(round(255 * brightness))
    screen.blit(studio_text, studio_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))


def draw_menu_buttons(screen, button_labels_and_keys):
    """Stack buttons in the middle of the screen. Returns a list of (button_rectangle, button_key)."""
    menu_buttons = []
    for button_number, (label, button_key) in enumerate(button_labels_and_keys):
        button_top = MENU_BUTTONS_TOP + button_number * (MENU_BUTTON_HEIGHT + MENU_BUTTON_SPACING)
        button_rectangle = pygame.Rect(0, button_top, MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT)
        button_rectangle.centerx = SCREEN_WIDTH // 2
        draw_button(screen, button_rectangle, label)
        menu_buttons.append((button_rectangle, button_key))
    return menu_buttons


def draw_title(screen, title, subtitle):
    title_text = get_font(TITLE_FONT_SIZE).render(title, True, NVIDIA_GREEN)
    screen.blit(title_text, title_text.get_rect(center=(SCREEN_WIDTH // 2, 160)))
    subtitle_text = get_font(SUBTITLE_FONT_SIZE).render(subtitle, True, WHITE)
    screen.blit(subtitle_text, subtitle_text.get_rect(center=(SCREEN_WIDTH // 2, 240)))


def draw_main_menu(screen):
    screen.fill(PLACEHOLDER_BACKGROUND_COLOR)
    draw_title(screen, GAME_TITLE, GAME_SUBTITLE)
    return draw_menu_buttons(screen, [
        ("Play Game", "play_game"),
        ("Settings", "open_settings"),
        ("Exit", "exit_game"),
    ])


def draw_settings_menu(screen, is_music_on):
    screen.fill(PLACEHOLDER_BACKGROUND_COLOR)
    draw_title(screen, "Settings", "")
    music_label = "Music: On" if is_music_on else "Music: Off"
    return draw_menu_buttons(screen, [
        (music_label, "toggle_music"),
        ("Back", "back_to_main_menu"),
    ])
