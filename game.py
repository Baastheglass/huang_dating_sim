# Run this file to play: python game.py

import pygame

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FRAMES_PER_SECOND, WINDOW_TITLE
from game_state import GameState
from drawing import draw_everything


def handle_key_press(key, game_state):
    if key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
        game_state.shift_race()


def handle_mouse_click(mouse_position, action_buttons, game_state):
    # Phase 4: if a button was clicked, call game_state.perform_action(action_key).
    pass


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()
    game_state = GameState()
    action_buttons = []

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                handle_key_press(event.key, game_state)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(event.pos, action_buttons, game_state)

        action_buttons = draw_everything(screen, game_state)
        pygame.display.flip()
        clock.tick(FRAMES_PER_SECOND)

    pygame.quit()


if __name__ == "__main__":
    run_game()
