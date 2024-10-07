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

def render_main_menu(screen, selected_index):
    normal_color = (255, 255, 255)  # Color for normal options
    selected_color = (255, 215, 0)  # Color for the selected option

    # Loop through menu options to render them
    for i, option in enumerate(main_menu_options):
        color = selected_color if i == selected_index else normal_color
        text = main_menu_font.render(option, True, color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, base_y - vertical_spacing * 1.5 + i * vertical_spacing))
        screen.blit(text, text_rect)  # Render the text on the screen
    
def render_menu_item_background(screen):
    position_new = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, base_y - vertical_spacing * 1.5))
    position_load = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, base_y - vertical_spacing * 0.5))
    position_options = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, base_y + vertical_spacing * 0.5))
    position_exit = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, base_y + vertical_spacing * 1.5))
    
    screen.blit(menu_item_background, position_new)
    screen.blit(menu_item_background, position_load)
    screen.blit(menu_item_background, position_options)
    screen.blit(menu_item_background, position_exit)
    
def menu_logic(options, screen):
    current_index = 0  # Start with the first option
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        current_index += 1  # Move down
        if current_index >= len(options):  # Wrap around
            current_index = 0

    if keys[pygame.K_UP]:
        current_index -= 1  # Move up
        if current_index < 0:  # Wrap around
            current_index = len(options) - 1

    current_item = options[current_index]  # Get the current menu item
    
def reset_menu_index():
    global selected_index
    selected_index = 0  # Starting index for the menu
    
    