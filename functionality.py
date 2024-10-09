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
    
def start_new_game(): #starts the game
    pass

def load_game(): #loads the game
    pass

def show_options(screen, selected_index, running):  # Pass `running` as an argument
    options_running = True  # Local flag to keep the options menu running
    while options_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set `running` to False to exit the game entirely
                options_running = False  # Exit the options menu as well
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(option_menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(option_menu_options)
                elif event.key == pygame.K_ESCAPE:
                    options_running = False
                elif event.key == pygame.K_RETURN:
                    if selected_index == 0:  # BGM Volume
                        # Handle BGM Volume adjustment
                        pass
                    elif selected_index == 1:  # SFX Volume
                        # Handle SFX Volume adjustment
                        pass
                    elif selected_index == 2:  # Return to main menu
                        options_running = False  # Exit the options menu

        # Draw the options screen
        screen.fill("black")  # Clear the screen
        screen.blit(options_menu_image, (0, 0))  # Draw the background

        render_options_item_background(screen)  # Draw item backgrounds
        render_options_menu(screen, selected_index)  # Pass selected_index to render the menu

        pygame.display.flip()  # Update the display
        pygame.time.delay(100)  # Small delay to avoid overwhelming the loop

    return running  # Return the updated `running` state

def render_options_menu(screen, selected_index):
    normal_color = (255, 255, 255)  # Color for normal options
    selected_color = (255, 215, 0)  # Color for the selected option

    # Loop through menu options to render them
    for i, option in enumerate(option_menu_options):
        color = selected_color if i == selected_index else normal_color
        text = main_menu_font.render(option, True, color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, base_y - option_spacing * 1.5 + i * option_spacing))
        screen.blit(text, text_rect)  # Render the text on the screen
    
def render_options_item_background(screen):
    positions = [-1.5, -0.5, 0.5]  # Relative positions for BGM, SFX, and Return

    for i, pos in enumerate(positions):
        position = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, base_y + option_spacing * pos))
        screen.blit(menu_item_background, position)

def show_load(screen, selected_index, running):  # Pass `running` as an argument
    load_running = True  # Local flag to keep the load menu running
    selected_index = 0  # Reset to the first slot when entering the load menu

    while load_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set `running` to False to exit the game entirely
                load_running = False  # Exit the load menu as well
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(option_menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(option_menu_options)
                elif event.key == pygame.K_ESCAPE:
                    load_running = False  # Exit the load menu
                elif event.key == pygame.K_RETURN:
                    if selected_index == 0:  # Assuming index 0 is for loading the first game
                        # Handle loading the selected game slot
                        pass
                    elif selected_index == 1:  # Handle for loading the second game slot
                        # Handle loading the selected game slot
                        pass
                    elif selected_index == 2:  # Return to main menu
                        load_running = False  # Exit the load menu

        # Draw the options screen
        screen.fill("black")  # Clear the screen
        screen.blit(options_menu_image, (0, 0))  # Draw the background

        # Render the item backgrounds first, then the outline for the selected slot
        render_load_item_background(screen)  # Draw the item backgrounds
        render_load_menu(screen, selected_index)  # Draw the outline for the selected slot

        pygame.display.flip()  # Update the display

    return running  # Return the updated `running` state
        
def render_load_menu(screen, selected_index):
    slot_width = 900.5
    slot_height = 200.5
    outline_color = (255, 255, 255)  # White outline color
    vertical_spacing = 20  # Space between each slot
    number_of_slots = 3  # Number of load slots

    # Calculate the total height occupied by all slots
    total_height = (slot_height * number_of_slots) + (vertical_spacing * (number_of_slots - 1))

    # Center the slots vertically and horizontally
    start_y_position = (SCREEN_HEIGHT - total_height) // 2  # Center vertically
    start_x_position = (SCREEN_WIDTH - slot_width) // 2  # Center horizontally

    # Draw the outline for the selected slot only
    if 0 <= selected_index < number_of_slots:
        pos_y = start_y_position + selected_index * (slot_height + vertical_spacing)  # Adjust y position based on index

        # Draw the outline rectangle for the selected slot
        outline_rect = pygame.Rect(start_x_position, pos_y, slot_width, slot_height)
        pygame.draw.rect(screen, outline_color, outline_rect, 1)  # Draw the outline (1 pixel wide)

def render_load_item_background(screen):    
    vertical_spacing = 20  # Space between each slot
    slot_height = 200.5  # Height of the load item background
    number_of_slots = 3  # Number of load slots

    # Calculate the total height occupied by all slots
    total_height = (slot_height * number_of_slots) + (vertical_spacing * (number_of_slots - 1))
    start_y_position = (SCREEN_HEIGHT - total_height) // 2  # Center the slots vertically

    for i in range(number_of_slots):
        # Adjust the position to center the load item background in the slot
        position = load_item_background.get_rect(center=(SCREEN_WIDTH // 2, start_y_position + i * (slot_height + vertical_spacing) + slot_height / 2))
        screen.blit(load_item_background, position)  # Draw the load item background