import pygame

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_CENTER = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

textbox_font = pygame.font.Font("font/DIN Bold.ttf", 25)
main_menu_font_size = 55
main_menu_font = pygame.font.Font(None, main_menu_font_size)
vertical_spacing = 50  # Set a fixed spacing value || this is for menu item spacing
option_spacing = 120
load_spacing = 50

mouse_position = pygame.mouse.get_pos()
mouse_press = pygame.mouse.get_pressed()

slider_values = [50.0, 50.0]

bgm_volume = slider_values[0] / 100
sfx_volume = slider_values[1] / 100

"""menu_navigation_sound = pygame.mixer.Sound("audio/sound_effects/menu_navigate.wav")
menu_confirm_sound = pygame.mixer.Sound("audio/sound_effects/menu_back.wav")
menu_back_sound = pygame.mixer.Sound("audio/sound_effects/menu_back.wav")"""
sounds = {
    'navigate': pygame.mixer.Sound("audio/sound_effects/menu_navigate.wav"),
    'confirm': pygame.mixer.Sound("audio/sound_effects/menu_back.wav"),
    'back': pygame.mixer.Sound("audio/sound_effects/menu_back.wav")
}
for sound in sounds.values():
    sound.set_volume(sfx_volume)

base_y = SCREEN_HEIGHT // 1.4  # Start positioning from the middle of the screen || this is for menu item spacing

main_menu_image = pygame.image.load("Images/main_menu_img.jpg")
main_menu_image = pygame.transform.scale(main_menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
menu_item_background = pygame.image.load("Images/menu_item_background.png")
splash_card = pygame.image.load("Images/splash_card.png")
text_box = pygame.image.load("Images/text_box.png")

load_item_background = pygame.image.load("Images/load_item_background.png")

options_menu_image = pygame.image.load("Images/options_menu_img.jpg")
main_menu_options = ['New Game', 'Load Game', 'Options', 'Exit']
option_menu_options = ['Music', 'Sound Effects','Return']

fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
fade_surface.fill((0, 0, 0))  # Black surface for fade

class Slider:
    def __init__(self, pos=((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2)), size=(100, 30), initial_val=50.0, min=0, max=100):
        self.pos = pos  # Position of the center of the slider
        self.size = size
        self.min = min
        self.max = max

        # Calculate the left and right bounds based on position and size
        self.left = self.pos[0] - (size[0] // 2)
        self.right = self.pos[0] + (size[0] // 2)
        self.top = self.pos[1] - (size[1] // 2)

        # Calculate the initial position of the button based on the initial value
        self.initial_val = (self.right - self.left) * (initial_val / max)  # Adjust to the range of the slider
        
        self.container_rect = pygame.Rect(self.left, (self.top + 15), self.size[0], 2)
        self.button_rect = pygame.Rect(self.left + self.initial_val - 5, self.top, 10, self.size[1])  # Adjust button width to 10

    def move_slider(self, change):
        # Move the button left or right based on change (-1 for left, 1 for right)
        new_val = (self.button_rect.centerx - self.left) / self.size[0] * self.max + change * 5
        # Ensure the new value is within the min and max limits
        new_val = max(self.min, min(new_val, self.max))
        # Update button position
        self.button_rect.centerx = self.left + (self.size[0] * (new_val / self.max))
        
    def render(self, screen):
        # Draw the slider container and button
        pygame.draw.rect(screen, "darkgray", self.container_rect)
        pygame.draw.rect(screen, "white", self.button_rect)

        


