import pygame

pygame.init()

from constants import *
from functionality import *

def main():
    # Initialize Pygame here
    pygame.init()
    pygame.mixer.init()
    
    play_music("audio/music/menu_theme.wav", loop=-1)

    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")  # Fill the screen with black
        
        # Blit the main menu image onto the screen
        screen.blit(main_menu_image, (0, 0))

        render_menu_item_background(screen)
        render_main_menu(screen)
        render_menu_cursor(screen)    
        
        pygame.display.flip()  # Update the display

if __name__ == "__main__":
    main()

