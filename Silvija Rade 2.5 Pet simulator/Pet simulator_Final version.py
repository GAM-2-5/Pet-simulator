import pygame
import sys
import Engine
import time
import random

pygame.init ()
begtime=time.time()

width = 1280
height = 941
fxf=200
fxe=200
fxh=200


def bedroom():
    background=pygame.image.load("bedroom.jpg").convert()
    screen.blit(background, (0,0))
    screen.blit(noxon,(-100,100))
    screen.blit(left,(20,height/2-300))
    screen.blit(right,(width-160,height/2-300))
    screen.blit(zzz,(900,600))

def kitchen():
    background=pygame.image.load("kitchen.jpg").convert()
    screen.blit(background, (0,0))
    screen.blit(noxon,(-100,100))
    screen.blit(watermelon,(900,600))
    screen.blit(left,(20,height/2-300))
    screen.blit(right,(width-160,height/2-300))
    
def living():
    background=pygame.image.load("livingroom.jpg").convert()
    screen.blit(background, (0,0))
    screen.blit(noxon,(-100,100))
    screen.blit(ball,(900,600))
    screen.blit(left,(20,height/2-300))
    screen.blit(right,(width-160,height/2-300))
        
    

def food(fx):
    text_size=20
    textp= "Food"
    text_color= [0, 0, 0]
    i=width-300
    j=100
    text(text_size,text_color, textp, i, j )
    pygame.draw.rect(screen, (255, 255, 255), (width-260, 65, 220, 70 ))
    pygame.draw.rect(screen, (250-fx, fx, 0), (width-250, 75, fx, 50))

def energy(fx):
    text_size=20
    textp= "Energy"
    text_color= [0, 0, 0]
    i=width-600
    j=100
    text(text_size,text_color, textp, i, j  )
    pygame.draw.rect(screen, (255, 255, 255), (width-560, 65, 220, 70 ))
    pygame.draw.rect(screen, (250-fx, fx, 0), (width-550, 75, fx, 50))

def happiness(fx):
    text_size=20
    textp= "Happy"
    text_color= [0, 0, 0]
    i=width-900
    j=100
    text(text_size,text_color, textp, i, j  )
    pygame.draw.rect(screen, (255, 255, 255), (width-860, 65, 220, 70 ))
    pygame.draw.rect(screen, (250-fx, fx, 0), (width-850, 75, fx, 50))
    

def eating():
    global fxf
    global e
    global etime
    screen.blit(eat,(-100,100))
    etime=time.time()
    e=True
    fxf+=10
    if fxf>200:
        fxf=200
    

def sleeping ():
    global fxe
    global s
    global stime
    screen.blit(sleep,(-100,100))
    stime=time.time()
    s=True
    fxe+=10
    if fxe>200:
        fxe=200

def happy():
    global fxh
    global h
    global htime
    screen.blit(happys,(-100,100))
    htime=time.time()
    h=True
    fxh+=10
    if fxh>200:
        fxh=200
    
def text(text_size, text_color, textp, i, j ):
    font = pygame.font.Font('freesansbold.ttf', text_size)
    text=font.render(textp, True, text_color)
    textRect = text.get_rect()
    textRect.center = [i, j]
    screen.blit(text, textRect)

def promjenap(z):
    global p
    global prostorije
    p=p+z
    if p<0:
        p=len(prostorije)-1
    if p>=len(prostorije):
        p=0
    prostorije[p]()

def promjena_plus():
    promjenap(1)

def promjena_minus():
    promjenap(-1)

def preusmjeravanje ():
    if p==0:
        Engine.button(event, 140, 140, 900 , 600, width, height, sleeping)
    if p==1:
        Engine.button(event, 140, 140, 900 , 600, width, height, eating)
    if p==2:
        Engine.button(event, 140, 140, 900 , 600, width, height, happy)


def noxonp():
    global noxon
    global eat
    global happys
    global hungry
    global sleep
    global angry
    global noxon2
    global screen
    screen = pygame.display.set_mode((width,height))
    noxon=pygame.image.load("noxon.png").convert_alpha()
    eat=pygame.image.load("eating.png").convert_alpha()
    happys=pygame.image.load("happy.png").convert_alpha()
    hungry=pygame.image.load("hungry.png").convert_alpha()
    sleep=pygame.image.load("sleep.png").convert_alpha()
    angry=pygame.image.load("angry.png").convert_alpha()
    noxon2  =pygame.image.load("noxon.png").convert_alpha()


def monp():
    global noxon
    global eat
    global happys
    global hungry
    global sleep
    global angry
    global noxon2
    global screen
    screen = pygame.display.set_mode((width,height))
    noxon=pygame.image.load("mon_original.png").convert_alpha()   
    eat=pygame.image.load("mon_eating.png").convert_alpha()
    happys=pygame.image.load("mon_happy.png").convert_alpha()   
    hungry=pygame.image.load("mon_hungry.png").convert_alpha()
    sleep=pygame.image.load("mon_sleep.png").convert_alpha()
    angry=pygame.image.load("mon_angry.png").convert_alpha()
    noxon2  =pygame.image.load("mon_original.png").convert_alpha()
        
def randomn():
    global name_list
    numb=random.randrange(0,len(name_list))
    nome=name_list[numb]
    print("Your random name is:", nome)
    print("Do you like it? type 'Yes' or 'No'")
    answer=input()
    if answer=="Yes":
        print("Great! Let's start the game!")
    else :
        print("Let's try another one!")
        randomn()

def provjeri():
    global pokemon
    print("Choose: Noxon or Mon")
    pokemon=input()
    if pokemon=="Mon":
        monp()
    elif pokemon=="Noxon":
        noxonp()
    else:
        print("I'm sorry, I don't understand. Try again")
        provjeri()
    

pokemon="Nothing"

provjeri()
              
name_list=['Bob', 'Koko', 'Slavko', 'Gary']
print("This is ",pokemon,"! He is your new pet! Name your ",pokemon,"! if you want to use random names write 'Random'")
name=input()

if name=="Random":
    randomn()
else:
    print("Great! Let's start the game!")

background=pygame.image.load("kitchen.jpg").convert()
watermelon=pygame.image.load("watermelon.jpg").convert()
zzz=pygame.image.load("zzz.jpg").convert()
ball=pygame.image.load("ball.jpg").convert()
left  =pygame.image.load("left.png").convert_alpha()
right =pygame.image.load("right.png").convert_alpha()

p=1
prostorije=[bedroom, kitchen, living]
prostorija=prostorije[1]
game_over=False
upaljen=False

e=False
etime=0
s=False
stime=0
h=False
htime=0

prostorija()



while not game_over:

    if e==False and s==False and h==False:
        if fxf==0 or fxe==0 or fxh==0:
            noxon=angry
            screen.blit(noxon,(-100,100))
            pygame.display.update()
            time.sleep(3)
            pygame.display.quit()
            print("He died")
            print("You are terrible at this")
            time.sleep(10)
            sys.exit()
            
            
        elif fxf<=100:
            noxon=hungry
            screen.blit(hungry,(-100,100))
    else:
        noxon=noxon2
    if time.time()-1>begtime:
        fxf=fxf-2
        if fxf<0:
            fxf=0
        fxe=fxe-2
        if fxe<0:
            fxe=0
        fxh=fxh-2
        if fxh<0:
            fxh=0
        begtime=time.time()
    food(fxf)
    energy(fxe)
    happiness(fxh)
    if e==True and time.time()-etime>3:
        screen.blit(noxon,(-100,100))
        e=False
        etime=0
    if s==True and time.time()-stime>3:
        screen.blit(noxon,(-100,100))
        s=False
        stime=0
    if h==True and time.time()-htime>3:
        screen.blit(noxon,(-100,100))
        h=False
        htime=0
    

    for event in pygame.event.get():    
        Engine.button(event, 140, 140, 20 , height/2-300, width, height, promjena_minus )#left
        Engine.button(event, 140, 140, width-160 , height/2-300, width, height, promjena_plus) #right
        preusmjeravanje ()
        pygame.display.update()
        if event.type==pygame.QUIT:
            pygame.display.quit()
            sys.exit()
     





