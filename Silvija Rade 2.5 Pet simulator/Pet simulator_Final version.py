import pygame
import sys
import Engine
import time
import random
#importanje dodatnih sadržaja u python

pygame.init ()
begtime=time.time() #vrijeme u kojemu je program pokrenut

width = 1280 #širina ekrana
height = 941 #visina ekrana
fxf=200 #početna širina hrane (food)
fxe=200 #početna širina energije (energy)
fxh=200 #početna širina sreće (happy)


def bedroom(): #funkcija koja pokreće sobu
    background=pygame.image.load("bedroom.jpg").convert()
    screen.blit(background, (0,0))
    screen.blit(noxon,(-100,100))
    screen.blit(left,(20,height/2-300)) #lijeva strelica
    screen.blit(right,(width-160,height/2-300)) #desna strelica
    screen.blit(zzz,(900,600)) #ikona za spavanje

def kitchen(): #funkcija koja pokreće kuhinju
    background=pygame.image.load("kitchen.jpg").convert()
    screen.blit(background, (0,0))
    screen.blit(noxon,(-100,100))
    screen.blit(watermelon,(900,600)) #ikona za hranjene
    screen.blit(left,(20,height/2-300))  #lijeva strelica
    screen.blit(right,(width-160,height/2-300)) #desna strelica
    
def living(): #funkcija koja pokreće dnevni boravak
    background=pygame.image.load("livingroom.jpg").convert()
    screen.blit(background, (0,0))
    screen.blit(noxon,(-100,100))
    screen.blit(ball,(900,600)) #ikona za igranje
    screen.blit(left,(20,height/2-300)) #lijeva strelica
    screen.blit(right,(width-160,height/2-300)) #desna strelica
        
    

def food(fx): #crtanje health bar but food
    text_size=20
    textp= "Food"
    text_color= [0, 0, 0]
    i=width-300 #pozicija teksta 
    j=100
    text(text_size,text_color, textp, i, j )
    pygame.draw.rect(screen, (255, 255, 255), (width-260, 65, 220, 70 )) #vanjski pravokutnik
    pygame.draw.rect(screen, (250-fx, fx, 0), (width-250, 75, fx, 50)) #unutrašnji pravokutnik

def energy(fx): #crtanje health bar but energy
    text_size=20
    textp= "Energy"
    text_color= [0, 0, 0]
    i=width-600
    j=100
    text(text_size,text_color, textp, i, j  )
    pygame.draw.rect(screen, (255, 255, 255), (width-560, 65, 220, 70 ))
    pygame.draw.rect(screen, (250-fx, fx, 0), (width-550, 75, fx, 50))

def happiness(fx): #crtanje health bar but happiness
    text_size=20
    textp= "Happy"
    text_color= [0, 0, 0]
    i=width-900
    j=100
    text(text_size,text_color, textp, i, j  )
    pygame.draw.rect(screen, (255, 255, 255), (width-860, 65, 220, 70 ))
    pygame.draw.rect(screen, (250-fx, fx, 0), (width-850, 75, fx, 50))
    

def eating(): #učitava emociju hranjenja
    global fxf
    global e
    global etime
    screen.blit(eat,(-100,100)) 
    etime=time.time() #trenutak u kojem se počela prikazivati emocija
    e=True #oznaka da je emocija upaljena
    fxf+=10 #povećava duljinu health bar-a
    if fxf>200: #provjerava ako je health na maksimumu
        fxf=200
    music() #učitavanje nom nom nom zvuk
    

def sleeping (): #učitava emociju spavanja
    global fxe
    global s
    global stime
    screen.blit(sleep,(-100,100))
    stime=time.time()
    s=True
    fxe+=10
    if fxe>200:
        fxe=200

def happy(): #učitava emociju sreće
    global fxh
    global h
    global htime
    screen.blit(happys,(-100,100))
    htime=time.time()
    h=True
    fxh+=10
    if fxh>200:
        fxh=200
    
def text(text_size, text_color, textp, i, j ): #pojedinosti za tekst
    font = pygame.font.Font('freesansbold.ttf', text_size)
    text=font.render(textp, True, text_color)
    textRect = text.get_rect()
    textRect.center = [i, j]
    screen.blit(text, textRect)

def promjenap(z): #kroz listu prati u koju prostoriju treba otići i preusmjerava u određenu funkciju
    global p
    global prostorije
    p=p+z
    if p<0: #provjerava ako si došao do kraja liste
        p=len(prostorije)-1
    if p>=len(prostorije):
        p=0
    prostorije[p]()

def promjena_plus(): #ide li desno
    promjenap(1)

def promjena_minus(): #ili lijevo
    promjenap(-1)

def preusmjeravanje (): #preusmjerava u funkciju koju emociju treba upotrijebiti
    if p==0:
        Engine.button(event, 140, 140, 900 , 600, width, height, sleeping)
    if p==1:
        Engine.button(event, 140, 140, 900 , 600, width, height, eating)
    if p==2:
        Engine.button(event, 140, 140, 900 , 600, width, height, happy)


def noxonp(): #učitava slike za "pokemona" Noxon
    global noxon
    global eat
    global happys
    global hungry
    global sleep
    global angry
    global noxon2
    global screen
    screen = pygame.display.set_mode((width,height)) #učitava ekran
    noxon=pygame.image.load("noxon.png").convert_alpha()
    eat=pygame.image.load("eating.png").convert_alpha()
    happys=pygame.image.load("happy.png").convert_alpha()
    hungry=pygame.image.load("hungry.png").convert_alpha()
    sleep=pygame.image.load("sleep.png").convert_alpha()
    angry=pygame.image.load("angry.png").convert_alpha()
    noxon2  =pygame.image.load("noxon.png").convert_alpha()


def monp(): #učitava slike za "pokemona" Mon
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
        
def randomn(): #funkcija za random imena generator
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

def provjeri(): #provjerava jesi li odabrao jednog od postojećih "pokemona"
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
        
def music(): #nom non nom funkcija
    pygame.mixer.music.load('Nom.mp3')
    pygame.mixer.music.play()
    

pokemon="Nothing" #tek toliko

provjeri() #zvanje funkcije
              
name_list=['Bob', 'Koko', 'Slavko', 'Gary', 'Nom', 'Ted', 'Cookie', 'Burrito', 'Chonky', 'Fluffy', 'Burek', 'Mozart','Pickle', 'Beethoven', 'I am Batman', 'Goose', 'Chewbacca', 'Garfield', 'Sherlock', 'Peanut', 'Mittens', 'Icarus', 'Loki'] #lista random imena
print("This is ",pokemon,"! He is your new pet! Name your ",pokemon,"! if you want to use random names write 'Random'")
name=input() #upisivanje ne-random imena

if name=="Random":
    randomn()#učitavanje funkcije
else:
    print("Great! Let's start the game!")

background=pygame.image.load("kitchen.jpg").convert()
watermelon=pygame.image.load("watermelon.jpg").convert()
zzz=pygame.image.load("zzz.jpg").convert()
ball=pygame.image.load("ball.jpg").convert()
left  =pygame.image.load("left.png").convert_alpha()
right =pygame.image.load("right.png").convert_alpha()

p=1
prostorije=[bedroom, kitchen, living] #lista prostorija
prostorija=prostorije[1]
game_over=False
upaljen=False #oznaka da button nije upaljen

e=False #oznaka da emocija nije upaljena
etime=0 #vrijeme=0
s=False
stime=0
h=False
htime=0

prostorija() #učitava prostoriju po defaultu



while not game_over:

    if e==False and s==False and h==False: #provjerava može li biti ljut(jer ne može biti ako ga hraniš, igraš se s njim ili spava)
        if fxf==0 or fxe==0 or fxh==0: #ako je health 0 
            noxon=angry #postane ljut
            screen.blit(noxon,(-100,100))
            pygame.display.update()
            time.sleep(3) #ljuto te gleda 3 sekunde
            pygame.display.quit() #umre
            print("He died") #program te obavijesti da si ubio ljubimca
            print("You are terrible at this") #i da nisi spreman na takvu obvezu
            time.sleep(10) #program te ljuto gleda 10 sekundi
            sys.exit() #prije nego umre
            
            
        elif fxf<=100: #ako se hungry health smanji preko pola 
            noxon=hungry
            screen.blit(hungry,(-100,100)) #učitava emociju "gladan"
    else:
        noxon=noxon2 #ako nije ljut da se vrati u normalu
    if time.time()-1>begtime: #mjeri nakon koliko sekundi health opada 
        fxf=fxf-2 #smanjuje duljinu
        if fxf<0:#provjerava je li mu health pao na 0% 
            fxf=0
        fxe=fxe-2
        if fxe<0:
            fxe=0
        fxh=fxh-2
        if fxh<0:
            fxh=0
        begtime=time.time()
    food(fxf)#poziva funkciju
    energy(fxe)
    happiness(fxh)
    if e==True and time.time()-etime>3: #mjeri vrijeme prije nego li završi emociju i vrati ga u original
        screen.blit(noxon,(-100,100))
        e=False
        etime=0 #resitira vrijeme
    if s==True and time.time()-stime>3:
        screen.blit(noxon,(-100,100))
        s=False
        stime=0
    if h==True and time.time()-htime>3:
        screen.blit(noxon,(-100,100))
        h=False
        htime=0
    

    for event in pygame.event.get():    
        Engine.button(event, 140, 140, 20 , height/2-300, width, height, promjena_minus )#gumb lijevo koji usmjerava koju prostoriju treba pokrenuti
        Engine.button(event, 140, 140, width-160 , height/2-300, width, height, promjena_plus) #gumb lijevo koji usmjerava koju prostoriju treba pokrenuti
        preusmjeravanje () #pogodite
        pygame.display.update() #ekran update
        if event.type==pygame.QUIT: #program dies
            pygame.display.quit()
            sys.exit()
     

#u kodu se dijelovi ponavljaju te nisam komentirala za svaki dio posebno nego samo jedan
#credit Leonardo Šimunović za engine and for help
#imam još mnogo ideja za update (i ljubimaca), ali nedovoljno vremena




