import pygame
pygame.init()

from constants import *
from functionality import *

def main():
    pygame.init()
    pygame.mixer.init()
    
    play_music("audio/music/menu_theme.wav", loop=-1)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    global selected_index
    selected_index = 0  # Starting index for the menu

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(main_menu_options)
                    print(f"Selected Index: {selected_index}")  # Debugging statement
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(main_menu_options)
                    print(f"Selected Index: {selected_index}")  # Debugging statement
                elif event.key == pygame.K_RETURN:
                    #TODO:
                    if selected_index == 0:  # New Game
                        start_new_game()  # Replace with your function to start a new game
                    elif selected_index == 1:  # Load Game
                        load_game()  # Replace with your function to load a game
                    elif selected_index == 2:  # Options
                        show_options()  # Replace with your function to show options
                    elif selected_index == 3:  # Exit
                        running = False  # Set running to False to exit the loop

        screen.fill("black")  # Clear the screen
        screen.blit(main_menu_image, (0, 0))  # Draw the background

        render_menu_item_background(screen)  # Draw item backgrounds
        render_main_menu(screen, selected_index)  # Pass selected_index as an argument
        
        pygame.display.flip()  # Update the display
        pygame.time.delay(100)  # Pause to visualize changes

    pygame.quit()  # Clean up when done


if __name__ == "__main__":
    main()

