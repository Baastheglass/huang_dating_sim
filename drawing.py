# Everything that puts pixels on the screen. Reads the game state, never changes it.

import pygame

from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLACEHOLDER_BACKGROUND_COLOR,
    PLACEHOLDER_JENSEN_COLOR,
)


def draw_background(screen, game_state):
    # Phase 7: draw the current location's background image.
    screen.fill(PLACEHOLDER_BACKGROUND_COLOR)


def draw_jensen(screen):
    # Phase 7: draw the Jensen image.
    jensen_rectangle = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 250, 200, 400)
    pygame.draw.rect(screen, PLACEHOLDER_JENSEN_COLOR, jensen_rectangle)


def draw_attraction_bar(screen, game_state):
    # Phase 2: draw a bar filled to game_state.attraction / MAX_ATTRACTION.
    pass


def draw_race_label(screen, game_state):
    # Phase 3: show the current race name and portrait.
    pass


def draw_dialogue_box(screen, game_state):
    # Phase 4: draw game_state.jensen_line in a box at the bottom.
    pass


def draw_action_buttons(screen, game_state):
    # Phase 4: draw one button per available action. Return the button rectangles for click checks.
    return []


def draw_everything(screen, game_state):
    draw_background(screen, game_state)
    draw_jensen(screen)
    draw_attraction_bar(screen, game_state)
    draw_race_label(screen, game_state)
    draw_dialogue_box(screen, game_state)
    return draw_action_buttons(screen, game_state)
