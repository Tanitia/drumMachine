
import pygame
#mixer is pygame's music handling tool
from pygame import mixer

#setup
pygame.init()

#window dimension
width = 900
height = 450

#define colours (rgb)
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)

#create display window
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Drum Machine - Python")
label_font = pygame.font.Font('Roboto-Bold.ttf', 32)

fps = 60
clock = pygame.time.Clock()

#track current state
running = True

while running:
    clock.tick(fps)
    screen.fill(black)

    #upon any action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
