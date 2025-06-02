import pygame

pygame.init()
screen_width , screen_height = 400,400
display_surface = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(('Adding images ans background image'))
background_image = pygame.transform.scale(
    pygame.image.load('background.png').convert(),
    (screen_width,screen_height))
pengine_image = pygame.transform.scale(
    
)