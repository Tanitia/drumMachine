
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
label_font = pygame.font.Font('Roboto-Bold.ttf', 24)

fps = 60
clock = pygame.time.Clock()

def draw_grid():
    #left_box is meant to mirror the instruments pane on music editing software
                                              #x, y, width, height, border
    left_box = pygame.draw.rect(screen, grey, [0, 0, 100, height-100], 5)
    #bottom_box is for playback control menu
    bottom_box = pygame.draw.rect(screen, grey, [0, height-100, width, 100], 5)
    #array of beat boxes:
    boxes = []
    colours = [grey, white, grey]
    #fundamental drum beats:
                                    #text, antialias
    hi_hat_text = label_font.render('Hi-Hat', True, white)
    #draws on screen
    screen.blit(hi_hat_text, (15, 15))
    #snare
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (15, 65))
    #bass drum
    bass_text = label_font.render('Bass', True, white)
    screen.blit(bass_text, (15, 115))
    #crash symbal
    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (15, 165))
    #clap
    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (15, 215))
    #floor tom
    floor_text = label_font.render('Floor', True, white)
    screen.blit(floor_text, (15, 265))
    #lines between options
    for i in range(6):
        pygame.draw.line(screen, grey [(0, (i*50) + 50], (100, i))


#track current state
running = True

while running:
    clock.tick(fps)
    screen.fill(black)
    draw_grid()

    #upon any action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #places elements onto screen
    pygame.display.flip()
#closes app when needed
pygame.quit()
