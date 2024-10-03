import pygame
import os
from constants import *

def reload_background(file):
    image = pygame.image.load(file)
    image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    return image

def load_image(filename):
    # Get the full path to the image
    filepath = os.path.join("Images", filename)
    return pygame.image.load(filepath)

    
