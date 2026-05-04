import random
import pygame
import time

class GSprite(pygame.sprite.Sprite):
    def __init__ (self,sprite_immage,x,y,speed,w,h):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(sprite_immage),(w,h))
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-10,-10)
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def appear(self):
        space.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        self.rect.y += self.speed
class Player(GSprite):

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d] and self.rect.x  < 625:
            self.rect.x += self.speed
        if key[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
    def shoot(self):

        bull = Pylka('bulka.png', self.rect.centerx - 10, self.rect.top - 20,10,25,40)
        pylki.add(bull)
missed = 0
shoot = 0 
life = 3
class Enemy(GSprite):
    def update(self):
        self.rect.y += self.speed
        global missed
        if self.rect.y > 500:
            self.rect.y = 0
            missed += 1
            self.rect.x = random.randint(30,610)
            self.speed = random.randint(1,2)
        
class Pylka(GSprite):
    def update(self):

        self.rect.y -= self.speed
        if self.rect.y <= -100:
                self.kill()
            

  
panel = GSprite('Tablo3.png',0,-40,0,200,200)
kamni = pygame.sprite.Group()
tarelki = pygame.sprite.Group()
pylki = pygame.sprite.Group()
for i in range(5):
    UFO1 = Enemy('ufo.png', random.randint(30,610),0,random.randint(1,2),80,50)
    tarelki.add(UFO1)  
for i in range(4):
    Bulishnik = GSprite('stone.png',random.randint(30,610),0,random.randint(1,2),60,60)
    kamni.add(Bulishnik)
           
pygame.font.init()
font  = pygame.font.SysFont(None, 30)      


pygame.display.set_caption('Shooter 3000')
clock = pygame.time.Clock()
a = True
s = False
p = False
v = 0
rt = False
d = 0
pygame.mixer.init()
fire = pygame.mixer.Sound('lazer.mp3')
pygame.mixer.music.load('forest.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)
space = pygame.display.set_mode((700,500))
Rocket = Player('ship.png',350,425,5,80,80)

background = pygame.transform.scale(pygame.image.load('spacik.png'),(700,500))
while a:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            a = False
        if p != True:
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    if v < 10 and rt == False:
                        Rocket.shoot()
                        fire.play()
                        v += 1
                    if v >= 10 and rt == False:
                        rt = True
                        time1 = time.time()
    
            

                             

                    
                             
    if s != True:
        space.blit(background,(0,0))
        Rocket.appear()
        panel.appear()
        text1 = font.render( 'Сбито: ' + str(shoot), 3, (73, 204, 238))
        text2 = font.render( 'Не сбито: ' + str(missed) , 3, (73, 204, 238))
        text3 = pygame.font.SysFont(None, 100).render( 'Вы проиграли!(',True, (73, 204, 238))
        text4 = pygame.font.SysFont(None, 100).render( 'Вы выиграли!)',True, (73, 204, 238))
        text5 = font.render('Жизни: ' + str(life), True, (73, 204, 238))
    
             
        space.blit(text1,(40,40))
        space.blit(text2,(40,70))
        space.blit(text5,(590,50))
        Rocket.move()
        kamni.draw(space)
        kamni.update()
        tarelki.draw(space)
        tarelki.update()
        pylki.draw(space)
        pylki.update()
        if rt == True:
            time2 = time.time()
            d = time1 - time2  
            if abs(d) < 3:
                text99 = pygame.font.SysFont(None, 30).render( 'До конца перезарядки: ' + str(round(3 - abs(d),  )),True, (73, 204, 238))
                space.blit(text99,(20,130))
            else:
                v = 0
                rt = False
        for i in  pygame.sprite.groupcollide(tarelki,pylki,True,True):
            shoot += 1
            UFO1 = Enemy('ufo.png', random.randint(30,610),0,random.randint(1,2),80,50)
            tarelki.add(UFO1)
        if pygame.sprite.spritecollide(Rocket,tarelki,True):
            life -= 1
    

        if pygame.sprite.spritecollide(Rocket,kamni,True):


            life -= 1


        if missed >= 3:
            space.blit(text3,(100,220))
            s = True
        if life <= 0:
            space.blit(text3,(100,220))
            s = True

        
        
            

            pygame.mixer.music.stop()
        if shoot == 10:
            space.blit(text4,(100,220))
            s = True
            pygame.mixer.music.stop()

        














    pygame.display.update()
    clock.tick(60)
