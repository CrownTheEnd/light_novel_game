import pygame
from constants import *

def display_typing_text(screen, text, font, typing_speed=100):
    displayed_text = ""
    index = 0
    last_time = pygame.time.get_ticks()

    while index < len(text):
        current_time = pygame.time.get_ticks()

        # Check if it's time to display the next character
        if current_time - last_time > typing_speed:
            displayed_text += text[index]  # Add the next character
            index += 1
            last_time = current_time  # Reset the timer

        # Clear the screen
        screen.fill((0, 0, 0))

        # Render and display the text
        text_surface = font.render(displayed_text, True, (255, 255, 255))
        screen.blit(text_surface, (50, 300))

        pygame.display.flip()
        pygame.time.delay(30)  # Add a small delay to control the loop speed

    return True  # Indicate that the text display is complete

def wait_for_input(key):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:  # Check for a key press
            return True  # Indicate that a key was pressed
    return None  # No input detected

def play_music(song, loop=-1):
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loop)

def render_main_menu(screen):
    text_new = main_menu_font.render('New Game', True, (255, 255, 255))
    text_load = main_menu_font.render('Load Game', True, (255, 255, 255))
    text_options = main_menu_font.render('Options', True, (255, 255, 255))
    text_exit = main_menu_font.render('Exit', True, (255, 255, 255))

    # Positioning each item based on the fixed spacing
    splash_card_rect = splash_card.get_rect(center=(SCREEN_WIDTH // 2, base_y - vertical_spacing * 11))
    text_new_rect = text_new.get_rect(center=(SCREEN_WIDTH // 2, base_y - vertical_spacing * 1.5))
    text_load_rect = text_load.get_rect(center=(SCREEN_WIDTH // 2, base_y - vertical_spacing * 0.5))
    text_options_rect = text_options.get_rect(center=(SCREEN_WIDTH // 2, base_y + vertical_spacing * 0.5))
    text_exit_rect = text_exit.get_rect(center=(SCREEN_WIDTH // 2, base_y + vertical_spacing * 1.5))

    # Draw the text on the screen
    screen.blit(splash_card, splash_card_rect)
    screen.blit(text_new, text_new_rect)
    screen.blit(text_load, text_load_rect)
    screen.blit(text_options, text_options_rect)
    screen.blit(text_exit, text_exit_rect)
    
def render_menu_cursor(screen):
    cursor_position = cursor.get_rect(center=(SCREEN_WIDTH // 2.35, base_y - vertical_spacing * 1.5))
    screen.blit(cursor, cursor_position)
    
def render_menu_item_background(screen):
    position_new = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, base_y - vertical_spacing * 1.5))
    position_load = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, base_y - vertical_spacing * 0.5))
    position_options = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, base_y + vertical_spacing * 0.5))
    position_exit = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, base_y + vertical_spacing * 1.5))
    
    screen.blit(menu_item_background, position_new)
    screen.blit(menu_item_background, position_load)
    screen.blit(menu_item_background, position_options)
    screen.blit(menu_item_background, position_exit)