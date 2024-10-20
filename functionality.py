import pygame
import time
import json
from constants import *
from json_loader import *
from data.dictionaries import *

def save_settings(settings):
    """Save game settings to settings.json."""
    with open('data/jsons/settings.json', 'w') as json_file:
        json.dump(settings, json_file, indent=4)  # Use indent for pretty printing

def save_game_file(selected_index):
    """Save the current game state to a specific slot in save_file.json."""
    
    # Map the selected index (0-2) to slot keys "1", "2", "3"
    slot_key = str(selected_index + 1)
    
    # Load the existing save data
    with open('data/jsons/save_file.json', 'r') as json_file:
        save_data = json.load(json_file)
    
    # Update the save slot with the current game state
    save_data[slot_key] = game_state
    
    # Save the updated data back to the file
    with open('data/jsons/save_file.json', 'w') as json_file:
        json.dump(save_data, json_file, indent=4)

def load_game_file(selected_index):
    """Load the game state from a specific slot in save_file.json."""
    
    # Map the selected index (0-2) to slot keys "1", "2", "3"
    slot_key = str(selected_index + 1)
    
    # Load the existing save data
    with open('data/jsons/save_file.json', 'r') as json_file:
        save_data = json.load(json_file)
    
    # Retrieve the game state from the selected slot
    if slot_key in save_data:
        game_state = save_data[slot_key]
        return game_state
    else:
        raise ValueError(f"No save data found for slot {slot_key}")
        
def display_typing_text(screen, text, font, typing_speed=50):
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

        # Render and display the text
        text_surface = font.render(displayed_text, True, (255, 255, 255))
        screen.blit(text_surface, (200, 800))  # Adjust the position as needed
        pygame.display.flip()
        pygame.time.delay(30)  # Add a small delay to control the loop speed

    return displayed_text, True  # Return the final text and indicate completion

def wait_for_input(key):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:  # Check for a key press
            return True  # Indicate that a key was pressed
    return None  # No input detected

def play_music(song, volume, loop=-1):
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loop)

def render_main_menu(screen, selected_index):
    normal_color = (255, 255, 255)  # Color for normal options
    selected_color = (255, 215, 0)  # Color for the selected option

    # Loop through menu options to render them
    for i, option in enumerate(main_menu_options):
        color = selected_color if i == selected_index else normal_color
        text = textbox_font.render(option, True, color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, base_y - vertical_spacing * 1.5 + i * vertical_spacing))
        screen.blit(text, text_rect)  # Render the text on the screen
    
def render_menu_item_background(screen):
    position_new = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, base_y - vertical_spacing * 1.5 + 2))
    position_load = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, base_y - vertical_spacing * 0.5 + 2))
    position_options = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, base_y + vertical_spacing * 0.5 + 2))
    position_exit = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, base_y + vertical_spacing * 1.5 + 2))
    
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
    
def fade_out_music(duration):
    pygame.mixer.music.fadeout(duration)
    
def fade_in_music(duration):
    """Fade in music over the specified duration (in seconds)."""
    pygame.mixer.music.set_volume(0)  # Start with volume at 0
    
    # Gradually increase volume
    for i in range(0, 101, 1):  # Increase volume from 0 to 100
        pygame.mixer.music.set_volume(slider_values[0] / 100)  # Set volume (0.0 to 1.0)
        time.sleep(duration / 100)  # Adjust sleep to control fade speed
    
def fade_in(screen, duration, background_image):
    """Fade the screen in over the given duration (in seconds)."""
    for alpha in range(255, -1, -5):  # Decrease alpha from 255 to 0
        fade_surface.set_alpha(alpha)  # Set the transparency level
        
        screen.blit(background_image, (0, 0))   # Fill the screen with white (or any background)
        screen.blit(fade_surface, (0, 0))  # Blit the fade surface
        
        pygame.display.update()
        time.sleep(duration / 51)  # Sleep to control fade speed
        
def fade_in_png(screen, duration, current_character, position):
    """Fade in a PNG image over the given duration (in seconds)."""
    # Load the image from the characters dictionary
    image_file = characters[current_character]["image_file"]
    image = pygame.image.load(image_file).convert_alpha()  # Load and convert the image as a surface
    fade_surface = image.copy()  # Copy the surface to manipulate alpha

    # Fade the PNG from fully transparent (alpha=0) to fully opaque (alpha=255)
    for alpha in range(0, 256, 5):  # Increase alpha from 0 to 255
        fade_surface.set_alpha(alpha)  # Set the transparency level
        
        screen.blit(fade_surface, position)  # Blit the fading PNG at the desired position
        
        pygame.display.update()
        time.sleep(duration / 51)  # Sleep to control fade speed

    fade_surface.set_alpha(255)  # Ensure the final alpha is set to 255
    screen.blit(fade_surface, position)  # Blit the fully opaque image
    
    return True

def fade_out(screen, duration, background_image):
    """Fade the screen out over the given duration (in seconds) using the provided background image."""
    for alpha in range(0, 256, 5):  # Increase alpha from 0 to 255
        fade_surface.set_alpha(alpha)
        
        # Draw the background image
        screen.blit(background_image, (0, 0))  # Use your menu background image here
        screen.blit(fade_surface, (0, 0))  # Overlay the fade surface
        
        pygame.display.update()
        time.sleep(duration / 51)
    
def start_new_game(): #starts the game
    pass

def load_game(): #loads the game
    pass

def show_options(screen, selected_index, running):  # Pass `running` as an argument
    options_running = True  # Local flag to keep the options menu running
    sliders = [Slider(pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), size=(100, 30), initial_val=slider_values[i], min=0, max=100) for i in range(2)]

    while options_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set `running` to False to exit the game entirely
                options_running = False  # Exit the options menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sounds['navigate'].play()
                    selected_index = (selected_index - 1) % len(option_menu_options)
                elif event.key == pygame.K_DOWN:
                    sounds['navigate'].play()
                    selected_index = (selected_index + 1) % len(option_menu_options)
                elif event.key == pygame.K_ESCAPE:
                    sounds['back'].play()
                    options_running = False
                elif event.key == pygame.K_RETURN:
                    if selected_index == 0:  # BGM Volume
                        pass
                    elif selected_index == 1:  # SFX Volume
                        pass
                    elif selected_index == 2:  # Return to main menu
                        settings_to_save = {
                        'slider_values': slider_values
                        }
                        save_settings(settings_to_save)
                        options_running = False  # Exit the options menu
                
        # Update slider values based on the selected index
        if selected_index < len(sliders):  # Ensure we're in slider range
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                sliders[selected_index].move_slider(-0.5)  # Move left
                sounds['navigate'].play()
                time.sleep(0.1)
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                sliders[selected_index].move_slider(0.5)  # Move right
                sounds['navigate'].play()
                time.sleep(0.1)

            # Update the slider value in the slider_values list
            slider_values[selected_index] = (sliders[selected_index].button_rect.centerx - sliders[selected_index].left) / sliders[selected_index].size[0] * sliders[selected_index].max
            pygame.mixer.music.set_volume(slider_values[0]/100)
            sfx_volume = slider_values[1] / 100
            for sound in sounds.values():
                sound.set_volume(sfx_volume)
                

        # Draw the options screen
        screen.fill("black")  # Clear the screen
        screen.blit(options_menu_image, (0, 0))  # Draw the background

        #render_options_item_background(screen)  # Draw item backgrounds
        render_options_menu(screen, selected_index, slider_values)  # Pass selected_index and slider_values to render the menu

        pygame.display.flip()  # Update the di
        
    return running

def render_options_menu(screen, selected_index, slider_values):
    normal_color = (255, 255, 255)  # Color for normal options
    selected_color = (255, 215, 0)  # Color for the selected option

    # Calculate the vertical position for each option
    for i, option in enumerate(option_menu_options):
        color = selected_color if i == selected_index else normal_color
        text = textbox_font.render(option, True, color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, base_y - option_spacing * 1.5 + i * option_spacing))
        
        # Render menu item background
        menu_item_bg_rect = menu_item_background.get_rect(center=text_rect.center)
        menu_item_bg_rect.y += 2
        screen.blit(menu_item_background, menu_item_bg_rect)

        screen.blit(text, text_rect)  # Render the text on the screen
        
        # Only create sliders for the first two options (BGM and SFX)
        if i < 2:  # Assuming the first two options are for BGM and SFX
            slider_y_position = text_rect.bottom + 40  # 40 pixels below the text
            slider = Slider(pos=(SCREEN_WIDTH // 2, slider_y_position), size=(100, 30), initial_val=slider_values[i], min=0, max=100)
            
            # Render background for slider
            slider_bg_rect = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, slider_y_position))
            screen.blit(menu_item_background, slider_bg_rect)

            # Render slider on top of background
            slider.render(screen)

"""def render_options_item_background(screen):
    positions = [-1.5, -0.5, 0.5]  # Relative positions for BGM, SFX, and Return
    for i, pos in enumerate(positions):
        position = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, base_y + option_spacing * pos))
        screen.blit(menu_item_background, position)"""


def show_load(screen, selected_index, running):  # Pass `running` as an argument
    load_running = True  # Local flag to keep the load menu running
    selected_index = 0  # Reset to the first slot when entering the load menu

    # Define the options including three load slots and the "Return" option
    option_menu_options = ["Load Game 1", "Load Game 2", "Load Game 3", "Return"]

    while load_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set `running` to False to exit the game entirely
                load_running = False  # Exit the load menu as well
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sounds['navigate'].play()
                    selected_index = (selected_index - 1) % len(option_menu_options)
                elif event.key == pygame.K_DOWN:
                    sounds['navigate'].play()
                    selected_index = (selected_index + 1) % len(option_menu_options)
                elif event.key == pygame.K_ESCAPE:
                    sounds['back'].play()
                    load_running = False  # Exit the load menu
                elif event.key == pygame.K_RETURN:
                    if selected_index == 0:  # Load Game 1
                        # Handle loading the first game slot
                        load_game_file(selected_index)
                    elif selected_index == 1:  # Load Game 2
                        # Handle loading the second game slot
                        load_game_file(selected_index)
                    elif selected_index == 2:  # Load Game 3
                        # Handle loading the third game slot
                        load_game_file(selected_index)
                    elif selected_index == 3:  # Return to main menu
                        sounds['back'].play()
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
    """Render the outline for the selected slot and the return button."""
    slot_width = 900
    slot_height = 200
    outline_color = (255, 255, 255)  # White outline color
    vertical_spacing = 20  # Space between each slot
    number_of_slots = 3  # Number of load slots
    normal_color = (255, 255, 255)  # Color for normal options
    selected_color = (255, 215, 0)  # Color for the selected option

    # Calculate the total height occupied by all slots
    total_height = (slot_height * number_of_slots) + (vertical_spacing * (number_of_slots - 1))
    start_y_position = (SCREEN_HEIGHT - total_height) // 2  # Center vertically
    start_x_position = (SCREEN_WIDTH - slot_width) // 2  # Center horizontally

    # Draw item backgrounds for each slot first
    for i in range(number_of_slots):
        position = load_item_background.get_rect(center=(SCREEN_WIDTH // 2, start_y_position + i * (slot_height + vertical_spacing) + slot_height / 2))
        screen.blit(load_item_background, position)  # Draw the load item background

    # Draw the outline for the selected slot only
    if 0 <= selected_index < number_of_slots:
        pos_y = start_y_position + selected_index * (slot_height + vertical_spacing)  # Adjust y position based on index

        # Draw the outline rectangle for the selected slot
        outline_rect = pygame.Rect(start_x_position, pos_y, slot_width, slot_height)
        pygame.draw.rect(screen, outline_color, outline_rect, 1)  # Draw the outline (1 pixel wide)

    # Draw the "Return" button background
    return_y_position = start_y_position + total_height + vertical_spacing  # Position for the Return button
    return_background_rect = menu_item_background.get_rect(center=(SCREEN_WIDTH // 2, return_y_position + 100))  # Center vertically
    return_background_rect.y += 2
    screen.blit(menu_item_background, return_background_rect)  # Draw the background for the Return option

    # Draw the "Return" button text
    font = pygame.font.Font(None, 50)  # Use default font
    return_color = selected_color if selected_index == number_of_slots else normal_color
    return_text_surface = textbox_font.render("Return", True, return_color)  # Render the text
    return_text_rect = return_text_surface.get_rect(center=(SCREEN_WIDTH // 2, return_y_position + 100))  # Center the text horizontally
    screen.blit(return_text_surface, return_text_rect)  # Draw the text

def render_load_item_background(screen): #the background is a 900x200 black square that goes below the outline in render_load_menu   
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
        
def render_name(screen, current_character):
    text_font = pygame.font.Font("font/DIN Bold.ttf", 35)
    text = text_font.render(current_character, True, (255, 215, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200))  # Center the text
    screen.blit(text, text_rect)  # Blit the text using its rect
        
def render_new_game(screen, selected_index, running, scene=1, dialogue_index=1):
    game_running = True
    fade_in(screen, 2, scenes[scene]['background'])
    play_music(scenes[scene]['bgm_file'], slider_values[0] / 100, loop=-1)
    fade_in_music(2)

    dialogue_number = dialogue_index
    dialogue_entry = ""
    dialogue_options = [
        scenes[scene]['dialogue'][str(dialogue_number)][0][1],
        scenes[scene]['dialogue'][str(dialogue_number)][1][1],
        scenes[scene]['dialogue'][str(dialogue_number)][2][1]
    ]
        
    fade_surface = None
    fade_in_done = False
    multiple_choice = False
    typing_done = False  # Flag to track if typing is complete
    final_text = ""  # Store the fully displayed text
    current_character = scenes[scene]['dialogue'][dialogue_number][0]
    speaking_character = current_character
    scene_actors = [current_character]
    
    multi_check = False
    
    # Fade in the character image once
    fade_in_png(screen, 1, game_state['current_character'], (250, 110))
    fade_in_done = True  # Mark that the fade in is done

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game entirely
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and multiple_choice:
                    sounds['navigate'].play()
                    selected_index = (selected_index - 1) % len(dialogue_options)
                elif event.key == pygame.K_DOWN and multiple_choice:
                    sounds['navigate'].play()
                    selected_index = (selected_index + 1) % len(dialogue_options)
                elif event.key == pygame.K_ESCAPE:
                    running = False  # Exit the game entirely
                    game_running = False
                
                elif event.key == pygame.K_RETURN and multiple_choice:
                    speaking_character = scenes[scene]['dialogue'][str(dialogue_number)][selected_index][3]
                    dialogue_entry = scenes[scene]['dialogue'][str(dialogue_number)][selected_index][4]
                
                if event.key == pygame.K_RETURN:
                    sounds['confirm'].play()
                    dialogue_number += 1
                    
                    if dialogue_number in scenes[scene]['dialogue']:
                        typing_done = False
                        if scenes[scene]['dialogue'][dialogue_number][0] not in scene_actors:
                            scene_actors += scenes[scene]['dialogue'][dialogue_number][0]
                        if dialogue_entry[-1] == "multi":
                            multiple_choice = True

        # Clear the screen and render the background
        screen.blit(scenes[scene]['background'], (0, 0))

        # Only call fade_in_png once
        if fade_in_done:
            # Blit the character image since fade in is done
            fade_in_surface = pygame.image.load(scenes['characters'][current_character]).convert_alpha()
            screen.blit(fade_in_surface, (250, 110))

        screen.blit(text_box, (0, 0))
        render_name(screen, speaking_character)

        # Only call the typing function if it hasn't finished yet
        if not typing_done:
            final_text, typing_done = display_typing_text(screen, characters[game_state["current_character"]]["dialogue_index"], textbox_font)
        else:
            # Render the final text after typing is complete
            text_surface = textbox_font.render(final_text, True, (255, 255, 255))
            screen.blit(text_surface, (200, 800))  # Adjust the position as needed

        # Update the display
        pygame.display.flip()

    return running

