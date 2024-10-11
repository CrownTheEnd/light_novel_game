import pygame

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

main_menu_font_size = 55
main_menu_font = pygame.font.Font(None, main_menu_font_size)
vertical_spacing = 50  # Set a fixed spacing value || this is for menu item spacing
option_spacing = 120
load_spacing = 50

menu_navigation_sound = pygame.mixer.Sound("audio/sound_effects/menu_navigate.wav")
menu_confirm_sound = pygame.mixer.Sound("audio/sound_effects/menu_back.wav")
menu_back_sound = pygame.mixer.Sound("audio/sound_effects/menu_back.wav")

base_y = SCREEN_HEIGHT // 1.4  # Start positioning from the middle of the screen || this is for menu item spacing

main_menu_image = pygame.image.load("Images/main_menu_img.jpg")
main_menu_image = pygame.transform.scale(main_menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
menu_item_background = pygame.image.load("Images/menu_item_background.png")
splash_card = pygame.image.load("Images/splash_card.png")

load_item_background = pygame.image.load("Images/load_item_background.png")

options_menu_image = pygame.image.load("Images/options_menu_img.jpg")

main_menu_options = ['New Game', 'Load Game', 'Options', 'Exit']

option_menu_options = ['Music', 'Sound Effects','Return']

fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
fade_surface.fill((0, 0, 0))  # Black surface for fade


