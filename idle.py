from turtle import color
import pygame
import pygame_menu
from pygame.locals import *

pygame.init()

class Player:
    def __init__(self):
        self.gold=0
        self.lvl=1
        self.xp=0
        self.maxXP=100
class Monster:
    def __init__(self,imageNormal,imageAttacked):
        self.imageNormal= pygame.image.load(imageNormal).convert_alpha()
        self.imageAttacked= pygame.image.load(imageAttacked).convert_alpha()
        self.x = 600
        self.y = 600
        self.health=500
        self.gold=10
    def NormalState(self):
        self.state = self.imageNormal
    def AttackedState(self):
        self.state = self.imageAttacked	

    def drawHPBar(self,surface,width):
        red=255
        blue=0
        green=0
        left=620
        top=550
        height=30
        filled=0
        pygame.draw.rect(surface, [red, blue, green], [left, top, width, height], filled)

def start_the_game():
    pygame.init()
    fenetre = pygame.display.set_mode((1681,1050))
    player=Player()
    police = pygame.font.Font(None,30)
    texte = police.render("GOLD : "+str(player.gold),True,pygame.Color("#000000"))
    rectTexte = texte.get_rect()
    rectTexte.center = fenetre.get_rect().topleft
    rectTexte.bottom+=20
    rectTexte.left+=80
    fenetre.blit(texte,rectTexte)
    

    fond = pygame.image.load("bg.png").convert()
    fenetre.blit(fond, (0,0))


    monster = Monster("slime.png","slime2.png")
    monsterHP=monster.health
    pygame.display.flip()
    continuer = 1
    isDie=False
    
    while continuer:
        if(isDie==False):
            monster.NormalState()
        else:
            monsterHP=monster.health
            isDie=False
        
        pygame.key.set_repeat(400, 30)
        for event in pygame.event.get(): 
            if event.type == QUIT:    
                continuer = 0  
             
            if event.type == MOUSEBUTTONDOWN:
                if(monsterHP<=0):
                    player.gold+=monster.gold
                    isDie=True
                else:
                    monsterHP=monsterHP-50
                    monster.AttackedState()
                      

        fenetre.blit(fond, (0,0))	
        fenetre.blit(monster.state, (monster.x, monster.y)) 
        texte = police.render("GOLD : "+str(player.gold),True,pygame.Color("#000000"))
        fenetre.blit(texte,rectTexte)
        monster.drawHPBar(fenetre,monsterHP)

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(200) 



start_the_game()


