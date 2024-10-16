import pygame
pygame.init()
import time
import json

from constants import *
from functionality import *

def main():
    pygame.init()
    pygame.mixer.init()

    settings = load_settings()
    slider_values = settings.get('slider_values', [50.0, 50.0])

    play_music('audio/music/menu_theme.wav', slider_values[0] / 100, loop=-1)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    global selected_index
    selected_index = 0  # Starting index for the main menu

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sounds['navigate'].play()
                    selected_index = (selected_index - 1) % len(main_menu_options)
                elif event.key == pygame.K_DOWN:
                    sounds['navigate'].play()
                    selected_index = (selected_index + 1) % len(main_menu_options)
                elif event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    # Menu navigation
                    if selected_index == 0:  # New Game
                        sounds['confirm'].play()
                        fade_out_music(2000) #this uses milliseconds for some reason?
                        fade_out(screen, 2, main_menu_image)
                        time.sleep(2)
                        running = render_new_game(screen, selected_index, running)  # Call your function to start a new game
                    elif selected_index == 1:  # Load Game
                        selected_index = 0 
                        sounds['confirm'].play()
                        running = show_load(screen, selected_index, running)  # Call your function to load a game
                    elif selected_index == 2:  # Options
                        print(slider_values)
                        selected_index = 0  # Reset index before showing options
                        sounds['confirm'].play()
                        running = show_options(screen, selected_index, running)  # Pass and update `running`
                    elif selected_index == 3:  # Exit
                        running = False  # Exit the game

        screen.fill("black")  # Clear the screen
        screen.blit(main_menu_image, (0, 0))  # Draw the background

        render_menu_item_background(screen)  # Draw item backgrounds
        render_main_menu(screen, selected_index)  # Pass current selected_index
        
        pygame.display.flip()  # Update the display
        pygame.time.delay(100)  # Small delay for smooth visualization

    pygame.quit()  # Clean up when done


if __name__ == "__main__":
    main()

