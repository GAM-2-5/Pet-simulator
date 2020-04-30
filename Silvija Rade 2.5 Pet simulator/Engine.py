import pygame
__name__="Engine"

def button(event, x, y, width, height, sw, sh, funkcija, button=1):
    if event.type==pygame.MOUSEBUTTONDOWN:
        if event.pos[0]>=width and event.pos[0]<=width+y and event.pos[1]>=height and event.pos[1]<=y+height and event.button==button:
            upaljen=True
            funkcija()
    

def buttonDraw(display, x, y, width, height, background_color, text="", font_size=20, text_color=[0,0,0], border=0, border_color=[0,0,0]):
    pygame.draw.rect(display, border_color, [x-border, y-border, width+2*border, height+2*border])
    pygame.draw.rect(display, background_color, [x, y, width, height])
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text=font.render(text, True, text_color)
    textRect = text.get_rect()
    textRect.center = [x+width/2, y+height/2]
    display.blit(text, textRect)

def buttonDrawImage(display, x, y, image, title="", font_size=20, title_color=[255,255,255]):
    display.blit(image, [x,y])
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text=font.render(title, True, title_color)
    textRect=text.get_rect()
    textRect.center=[x+image.get_width()/2, y+image.get_height()+textRect.height]
    display.blit(image, [x, y])
    display.blit(text, textRect)
