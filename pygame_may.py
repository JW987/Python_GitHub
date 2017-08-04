
import pygame,sys,time,math,random
from pygame.locals import *
pygame.mixer.init(buffer=512)
pygame.init()
clock = pygame.time.Clock()
xdim = 1300
ydim = 600
screen = pygame.display.set_mode((xdim,ydim))

# Colours
backcol = (255,0,220)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
orange = (255,128,0)
pink = (255,50,50)
purple = (100,50,50)
blue = (0,0,255)
grey = (96,96,96)
purple2 = (204,0,204)
yellow = (255,255,0)
green = (0,204,0)
green2 = (0,255,0)
green3 = (65,173,54)
gold = (255,215,0)

# Fonts
font1 = pygame.font.SysFont("draglinebtndm",60)
font2 = pygame.font.SysFont("couriernew",15)
font3 = pygame.font.SysFont("couriernew",30)

# Images
wheat_img = pygame.image.load("images/wheat_field.png").convert()
may_img = pygame.image.load("images/may.png").convert()
may_img.set_colorkey(white)
corbyn_img = pygame.image.load("images/corbyn_big.png").convert()
corbyn_img.set_colorkey(white)
boris_img = pygame.image.load("images/boris.png").convert()
boris_img.set_colorkey(white)
gove_img = pygame.image.load("images/gove.png").convert()
gove_img.set_colorkey(white)
sturgeon_img = pygame.image.load("images/sturgeon_big.png").convert()
sturgeon_img.set_colorkey(white)
rudd_img = pygame.image.load("images/rudd.png").convert()
rudd_img.set_colorkey(white)
bus_img = pygame.image.load("images/debate_bus.png").convert()
bus_img.set_colorkey(white)
nurse_img = pygame.image.load("images/nurse.png").convert()
nurse_img.set_colorkey(backcol)
police_img = pygame.image.load("images/police.png").convert()
police_img.set_colorkey(white)
boris_zip_img = pygame.image.load("images/boris_zip_big.png").convert()
boris_zip_img.set_colorkey(white)
scissors_img = pygame.image.load("images/scissors.png").convert()
scissors_img.set_colorkey(white)
brexit_img = pygame.image.load("images/brexit.png").convert()
dup_img = pygame.image.load("images/DUP.png").convert()
farage_img = pygame.image.load("images/farage.png").convert()
farage_img.set_colorkey(white)
yes_img = pygame.image.load("images/indyref_yes.png").convert()
yes_img.set_colorkey(white)
fireball_img = pygame.image.load("images/fireball_2.png").convert()
fireball_img.set_colorkey(black)
backbenchers_img = pygame.image.load("images/backbenchers.png").convert()
backbenchers_img.set_colorkey(white)
union_flag_img = pygame.image.load("images/union_flag.png").convert()
bonus_img = pygame.image.load("images/plus_50.png").convert()
bonus_img.set_colorkey(black)
bush_img = pygame.image.load("images/bushy_background.png").convert()
fox1_img = pygame.image.load("images/fox_1.png").convert()
fox1_img.set_colorkey(green3)
fox2_img = pygame.image.load("images/fox_2.png").convert()
fox2_img.set_colorkey(green3)
fox3_img = pygame.image.load("images/fox_3.png").convert()
fox3_img.set_colorkey(green3)
fox4_img = pygame.image.load("images/fox_4.png").convert()
fox4_img.set_colorkey(green3)
crosshairs_img = pygame.image.load("images/crosshairs.png").convert()
crosshairs_img.set_colorkey(white)
blood_img = pygame.image.load("images/blood.png").convert()
blood_img.set_colorkey(black)
shotgun_img = pygame.image.load("images/shotgun_barrel.png").convert()
shotgun_img.set_colorkey(white)
cameron_img = pygame.image.load("images/hanging_cameron.png").convert()
cameron_img.set_colorkey(white)
queenT_img = pygame.image.load("images/queen_theresa.png").convert()
queenT_img.set_colorkey(black)
crown_img = pygame.image.load("images/crown.png").convert()
crown_img.set_colorkey(black)
brexit2_img = pygame.image.load("images/brexit2.png").convert()

# Sounds
shot_sound = pygame.mixer.Sound("sounds/shotgun.wav")

# Variables
jump_time = 0
weapon_num = 0
menu = "start"
clicked = 0

# Classes
class Background:
    def __init__(self,x):
        self.img = wheat_img
        self.x = x
        self.y = 0
        
    def off_left(self):
        return self.x < -xdim
        
    def off_right(self):
        return self.x > xdim
        
    def draw(self):
        screen.blit(self.img,(self.x,self.y))

class May:
    def __init__(self):
        self.img = may_img
        self.x = xdim/2-self.img.get_width()/2
        self.y = ydim-self.img.get_height()
        self.dx = 0
        self.dy = 0
        self.jump_time = jump_time
        self.rudd_fire = 0
        self.brexit_fire = 0
        
    def fire(self,w,dx):
        if w == 0:
            weapons.append(Weapon(dx*10,"scissors"))
        if w == 1 and time.time() > self.brexit_fire:
            weapons.append(Weapon(dx*10,"brexit"))
            self.brexit_fire = time.time()+0.5
        if w == 2 and time.time() > self.rudd_fire:
            weapons.append(Weapon(dx*5,"rudd"))
            self.rudd_fire = time.time()+0.5
        
    def move(self):
        self.y += self.dy
        if Keys[K_LEFT]:
            if self.x+self.img.get_width()/2 > 550:
                self.x -= 4
            else:
                for bg in backgrounds:
                    bg.x += 4
                for nurse in nurses:
                    nurse.x += 4
                for dup in dups:
                    dup.x += 4
                for tory in right:
                    tory.x += 4
                farage.x += 4
                if enemy == "left":
                    bus.x += 4
        if Keys[K_RIGHT]:
            if self.x+self.img.get_width()/2 < 750:
                self.x += 4
            else:
                for bg in backgrounds:
                    bg.x -= 4
                for nurse in nurses:
                    nurse.x -= 4
                for dup in dups:
                    dup.x -= 4
                for tory in right:
                    tory.x -= 4
                farage.x -= 4
                if enemy == "left":
                    bus.x -= 4
        if self.y < ydim-self.img.get_height():
            self.dy += 1
        else:
            self.y = ydim-self.img.get_height()
            self.dy = 0
        if Keys[K_UP] and time.time() > self.jump_time:
            self.dy -= 20
            self.jump_time = time.time()+0.8
            
    def hit(self,enemy):
        return abs(enemy.x-self.x+self.img.get_width()/2) < self.img.get_width()/2 and self.y+self.img.get_height() > ydim-10
        
    def missile_hit(self,missile):
        return (self.x < missile.x+missile.img.get_width()/2 < self.x+self.img.get_width() and 
                self.y < missile.y+missile.img.get_height()/2 < self.y+self.img.get_height())
        
    def draw(self):
        screen.blit(self.img,(self.x,self.y))
        
class Weapon:
    def __init__(self,dx,w):
        self.type = w
        if self.type == "scissors":
            self.img = scissors_img
        elif self.type == "brexit":
            self.img = brexit_img
        elif self.type == "rudd":
            self.img = rudd_img
        self.x = may.x+may.img.get_width()/2-self.img.get_width()/2
        self.y = may.y+may.img.get_height()/2
        self.dx = dx
        
    def move(self):
        self.x += self.dx
        
    def off_screen(self):
        return self.x > xdim or self.x < -self.img.get_width()
        
    def draw(self):
        screen.blit(self.img,(self.x,self.y))
        
class Nurse:
    def __init__(self):
        self.img = random.choice((nurse_img,police_img))
        self.x = xdim
        self.y = ydim-self.img.get_height()
        self.dx = random.choice((-2,-3))
        
    def move(self):
        self.x += self.dx
        
    def off_screen(self):
        return self.x < -self.img.get_width()
        
    def hit(self,weapon):
        return weapon.type == "scissors" and self.x < weapon.x < self.x+self.img.get_width() and weapon.y > ydim-self.img.get_height()
        
    def draw(self):
        screen.blit(self.img,(self.x,self.y))
        
class Dup:
    def __init__(self):
        self.img = dup_img
        self.x = xdim
        self.y = ydim-self.img.get_height()
        
    def off_screen(self):
        return self.x < 0-self.img.get_width() or self.x > xdim+self.img.get_width()*2
        
    def hit(self,may):
        return abs(self.x+self.img.get_width()/2-may.x+may.img.get_width()/2) < self.img.get_width()/2+may.img.get_width()/2 and may.y+may.img.get_height() > ydim-10
        
    def draw(self):
        screen.blit(self.img,(self.x,self.y))
        
class Farage:
    def __init__(self):
        self.img = farage_img
        self.x = -100
        self.y = ydim-self.img.get_height()
        self.dx = 2
        
    def  move(self):
        self.x += self.dx
        if self.x < -100:
            self.x = -100
            
    def touching(self,may):
        return may.x-(self.x+self.img.get_width()*3/4) <= 0
            
    def draw(self):
        if self.x > -self.img.get_width():
            screen.blit(self.img,(self.x,self.y))
            
class Bus:
    def __init__(self):
        self.img = bus_img
        self.x = -self.img.get_width()
        self.y = ydim-self.img.get_height()
        self.dx = 0
        self.lives = 3
        
    def move(self):
        self.x += self.dx
        
    def touching(self,may):
        return may.x-self.x < self.img.get_width()
        
    def hit(self,weapon):
        return weapon.type == "rudd" and self.x < weapon.x < self.x+self.img.get_width() and weapon.y > ydim-self.img.get_height()
    
    def draw(self):
        screen.blit(self.img,(self.x,self.y))
        
class Sturgeon:
    def __init__(self):
        self.img = sturgeon_img
        self.x = 0
        self.y = ydim-self.img.get_height()
        self.dx = 2
        self.time = 0
        
    def move(self):
        self.x += self.dx
        if self.x < 0:
            self.x = 0
        if self.x > 200:
            self.x = 200
            
    def fire(self):
        missiles.append(Missile(sturgeon))
            
    def draw(self):
        screen.blit(self.img,(self.x,self.y))
        
class Corbyn:
    def __init__(self):
        self.img = corbyn_img
        self.x = 0
        self.y = ydim-self.img.get_height()
        self.dx = 2
        self.time = 0
        
    def move(self):
        self.x += self.dx
        if self.x < 0:
            self.x = 0
        if self.x > 200:
            self.x = 200
            
    def fire(self):
        missiles.append(Missile(corbyn))
            
    def draw(self):
        screen.blit(self.img,(self.x,self.y))
        
class Missile:
    def __init__(self,type):
        if type == sturgeon:
            self.img = yes_img
            self.dx = 10
            self.x = type.x+type.img.get_width()/2-self.img.get_width()/2
            self.y = ydim-type.img.get_height()*3/4
        if type == corbyn:
            self.img = fireball_img
            self.dx = 15
            self.x = type.x+type.img.get_width()/2-self.img.get_width()/2
            self.y = ydim-type.img.get_height()*3/4
        if type == boris:
            self.img = union_flag_img
            self.dx = -10
            self.x = right[0].x+right[0].img.get_width()/2-self.img.get_width()/2
            self.y = ydim-right[0].img.get_height()*3/4
        self.dy = int(random.random()*10)
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.y >= ydim-self.img.get_height():
            self.y = ydim-self.img.get_height()
            self.dy = 0
            
    def off_screen(self):
        return self.x > xdim
            
    def draw(self):
        screen.blit(self.img,(self.x,self.y))
            
class Right:
    def __init__(self,attack):
        self.lives = 3
        if attack == "backbench":
            self.img = backbenchers_img
        if attack == "gove":
            self.img = gove_img
        if attack == "boris":
            self.img = boris_img
            self.lives += 2
        self.type = attack
        self.x = xdim
        self.y = ydim-self.img.get_height()
        self.dx = -5
        
    def move(self):
        self.x += self.dx
        
    def touching(self,may):
        return self.x-may.x < may.img.get_width()
        
    def hit(self,weapon):
        return weapon.type == "brexit" and self.x < weapon.x < self.x+self.img.get_width() and weapon.y > ydim-self.img.get_height()
     
    def fire(self):
        missiles.append(Missile(boris))
    
    def draw(self):
        screen.blit(self.img,(self.x,self.y))

class Boris:
    def __init__(self):
        self.img = boris_zip_img
        self.x = xdim-self.img.get_width()+112
        self.y = -24
    
    def move(self):
        self.x -= 2.6
        self.y += 0.8
        
    def off_screen(self):
        return self.x < 0
        
    def draw(self):
        screen.blit(self.img,(int(self.x),int(self.y)))
        
class Bonus:
    def __init__(self):
        self.img = bonus_img
        self.x = xdim/2-self.img.get_width()/2
        self.y = ydim/2-self.img.get_width()/2
        self.time = time.time()+1
        
    def time_out(self):
        return time.time() > self.time
        
    def draw(self):
        screen.blit(self.img,(self.x,self.y))
        
class Fox:
    def __init__(self):
        self.img = random.choice((fox1_img,fox2_img,fox3_img,fox4_img))
        self.x = int(random.random()*xdim)
        self.y = int(random.random()*100)+300
        self.time = time.time()+3
        self.dead_time = 0
        self.dead = 0
        self.dead_pos = 0
        
    def time_out(self):
        return time.time() > self.time
        
    def hit(self):
        return MouseC[0] and (self.x+25-MousePx)**2+(self.y+25-MousePy)**2 < 400
    
    def draw(self):
        screen.blit(self.img,(self.x,self.y))
        if self.dead == 1:
            screen.blit(blood_img,self.dead_pos)
        
class Gun:
    def __init__(self):
        self.img1 = shotgun_img
        self.img2 = crosshairs_img
        self.d = 0
        self.rotated = ()
        
    def fire(self):
        return MouseC[0]
       
    def draw(self):
        screen.blit(self.img2,(MousePx-40,MousePy-40))
        self.rotated = pygame.transform.rotate(self.img1,self.d)
        screen.blit(self.rotated,(xdim/2-self.rotated.get_width()/2,ydim-self.rotated.get_height()/2))
        
class Crown:
    def __init__(self):
        self.img = crown_img
        self.y = 0
        
    def move(self):
        self.y += 2
        
    def on_head(self):
        return self.y >= ydim-135-self.img.get_height()
        
    def draw(self):
        screen.blit(self.img,(xdim*0.7+(queenT_img.get_width()-self.img.get_width())/2,self.y))
       
        
# Lists
backgrounds = [Background(-xdim),Background(0),Background(xdim)]

may = May()

nurses = []

weapons = []

dups = []

farage = Farage()

bus = Bus()

sturgeon = Sturgeon()

corbyn = Corbyn()

missiles = []

right = []

tories = ["gove","boris"]

boris = Boris()

bonuss = []

foxes = []

gun = Gun()

crown = Crown()

while 1:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                if weapon_num < 2:
                    weapon_num += 1
                else:
                    weapon_num = 0
            if event.key == K_m:
                may.fire(weapon_num,1)
            if event.key == K_n:
                may.fire(weapon_num,-1)
            
    Keys = pygame.key.get_pressed()
    MouseC = pygame.mouse.get_pressed()
    MouseP = pygame.mouse.get_pos()
    MousePx,MousePy = MouseP
    
    if menu == "start":
        screen.blit(brexit2_img,(0,0))
        rotated = pygame.transform.rotate(cameron_img,10*math.sin(math.degrees(1-time.time()%40/40))-5)
        screen.blit(rotated,(100-(rotated.get_width()-cameron_img.get_width())/2,-350))
        txt = font1.render("PLAY",True,blue)
        screen.blit(txt,(xdim/4-txt.get_width()/2,ydim*3/4))
        screen.blit(queenT_img,(xdim*0.7,ydim-queenT_img.get_height()))
        playrect = pygame.Rect((xdim/4-txt.get_width()/2,ydim*3/4),txt.get_size())
        if MouseC[0] and playrect.collidepoint(MouseP):
            clicked = 1
            click_time = time.time()
        if clicked == 1:
            if not crown.on_head():
                crown.move()
            crown.draw()
            if time.time() > click_time+4:
                menu = "main"
                popularity = 110
                lives = 3
                enemy = "nurses"
                difficulty = 300
                bonus = 0
                start_time = time.time()
        
    if menu == "main":
        i = 0
        while i < len(backgrounds):
            if backgrounds[i].off_left():
                backgrounds.append(Background(backgrounds[i].x+2*xdim))
                del backgrounds[i]
                i -= 1
            if backgrounds[i].off_right():
                backgrounds.append(Background(backgrounds[i].x-2*xdim))
                del backgrounds[i]
                i -= 1
            backgrounds[i].draw()
            i += 1
        
        if enemy == "nurses":    
            if difficulty > 20:
                difficulty -= 0.1
            if random.randint(1,int(difficulty)) == 1:
                nurses.append(Nurse())
                
            i = 0
            while i < len(nurses):
                nurses[i].move()
                nurses[i].draw()
                j = 0
                while j < len(weapons):
                    if nurses[i].hit(weapons[j]):
                        del nurses[i]
                        if popularity > 0:
                            popularity -= 100
                        i -= 1
                        del weapons[j]
                        break
                    j += 1
                if i >= 0 and nurses[i].off_screen():
                    del nurses[i]
                    i -= 1
                i += 1
                
            i = 0
            while i < len(nurses):
                if may.hit(nurses[i]):
                    del nurses[i]
                    i -= 1
                    lives -= 1
                i += 1  
            if random.randint(1,5000) == 1:
                dups.append(Dup())
                
            i = 0
            while i < len(dups):
                dups[i].draw()
                if dups[i].off_screen():
                    print("Z")
                    del dups[i]
                    i -= 1
                i += 1
                
            i = 0
            while i < len(dups):
                if dups[i].hit(may):
                    del dups[i]
                    lives += 1
                    i -= 1
                i += 1  
                
            if farage.touching(may):
                lives -= 1
                farage.x = -100
            farage.move()
            farage.draw()     
        
            if popularity < 1000:
                popularity += 0.25
            txt = font2.render("POPULARITY",True,black)
            if 250 < popularity < 750:
                pop_col = green
            elif 100 < popularity < 900:
                pop_col = orange
            else:
                pop_col = red
                if popularity > 900:
                    enemy = "left"
                    attack = "bus"
                    popularity = 200
                if popularity < 100:
                    enemy = "right"
                    right.append(Right("backbench"))
                    h = 0
                    popularity = 200
            screen.blit(txt,(xdim/2-txt.get_width()/2,10))
            pygame.draw.line(screen,pop_col,(xdim/2-int(popularity/10),15+txt.get_height()),(xdim/2+int(popularity/10),15+txt.get_height()),10)
        
        if enemy == "left":
            nurses = []
            i = 0
            while i < len(missiles):
                missiles[i].move()
                missiles[i].draw()
                if missiles[i].off_screen():
                    del missiles[i]
                    i -= 1
                i += 1
            i = 0
            while i < len(missiles):
                if may.missile_hit(missiles[i]):
                    del missiles[i]
                    i -= 1
                    lives -= 1
                i += 1
            if attack == "bus":
                bus.dx = 5
                i = 0
                while i < len(weapons):
                    if bus.hit(weapons[i]):
                        del weapons[i]
                        i -= 1
                        bus.lives -= 1
                    i += 1
                if bus.lives == 0:
                    attack = "sturgeon"
                    sturgeon.time = time.time()+10
                    bonus += 50
                    bonuss.append(Bonus())
                if bus.touching(may):
                    bus.x = -bus.img.get_width()
                    bus.dx = 0
                    lives -= 1
                    attack = "over"
                    sturgeon.time = time.time()+10
                bus.move()
                bus.draw()
            if attack == "sturgeon":
                if time.time() %1 < 0.01:
                    sturgeon.fire()
                sturgeon.move()
                sturgeon.draw()
                if time.time() >= sturgeon.time:
                    attack = "corbyn"
                    corbyn.time = time.time()+20
            if attack == "corbyn":
                if time.time() %1 < 0.01:
                    corbyn.fire()
                corbyn.move()
                corbyn.draw()
                if time.time() >= corbyn.time:
                    attack = "over"
            if attack == "over":
                enemy = "nurses"
                difficulty = 300
                
        if enemy == "right":
            nurses = []
            i = 0
            while i < len(missiles):
                missiles[i].move()
                missiles[i].draw()
                if missiles[i].off_screen():
                    del missiles[i]
                    i -= 1
                i += 1
            i = 0
            while i < len(missiles):
                if may.missile_hit(missiles[i]):
                    del missiles[i]
                    i -= 1
                    lives -= 1
                i += 1
            if h < 3:
                i = 0
                while i < len(right):
                    right[i].move()
                    if right[i].type == "boris" and time.time() % 1 < 0.01:
                        right[i].fire()
                    right[i].draw()
                    if right[i].touching(may):
                        lives -= 1
                        del right[i]
                        i -= 1
                        h += 3
                        break
                    j = 0
                    while j < len(weapons):
                        if right[i].hit(weapons[j]):
                            right[i].lives -= 1
                            del weapons[j]
                            j -= 1
                        j += 1
                    if len(right) > 0 and right[i].lives == 0:
                        del right[i]
                        i -= 1
                        bonus += 50
                        bonuss.append(Bonus())
                        if h < 2:
                            right.append(Right(tories[h]))
                            if h == 1:
                                bz = 0        
                                while bz == 0:
                                    screen.fill(white)
                                    pygame.draw.line(screen,black,(0,ydim-boris.img.get_height()),(xdim,0),3)
                                    boris.move()
                                    boris.draw()        
                                    i = 0
                                    while i < len(bonuss):
                                        bonuss[i].draw()
                                        if bonuss[i].time_out():
                                            del bonuss[i]
                                            i -= 1
                                        i += 1
                                    pygame.display.update()
                                    if boris.off_screen():
                                        boris.x = xdim-boris.img.get_width()+112
                                        boris.y = -24
                                        bz += 1
                        h += 1
                    i += 1
            else:
                enemy = "nurses"
                difficulty = 300
                menu = "fox"
                fox_score = 0
                fox_time = time.time()+30
            
        i = 0
        while i < len(weapons):
            weapons[i].move()
            weapons[i].draw()
            if weapons[i].off_screen():
                del weapons[i]
                i -= 1
            i += 1
        
        may.move()
        may.draw()
        
        i = 0
        while i < len(bonuss):
            bonuss[i].draw()
            if bonuss[i].time_out():
                del bonuss[i]
                i -= 1
            i += 1
        
        txt = font2.render("Weapon:",True,black)
        screen.blit(txt,(10,10))
        if weapon_num == 0:
            txt = font2.render("CUTS",True,black)
            screen.blit(scissors_img,(10,15+txt.get_height()))
            screen.blit(txt,(10+scissors_img.get_width(),15+txt.get_height()/2+scissors_img.get_height()/2))
        elif weapon_num == 1:
            txt = font2.render("HARD BREXIT",True,black)
            screen.blit(brexit_img,(10,15+txt.get_height()))
            screen.blit(txt,(10+brexit_img.get_width(),15+txt.get_height()/2+brexit_img.get_height()/2))
        elif weapon_num == 2:
            txt = font2.render("AMBER RUDD",True,black)
            screen.blit(rudd_img,(10,15+txt.get_height()))
            screen.blit(txt,(10+rudd_img.get_width(),15+txt.get_height()/2+rudd_img.get_height()/2))
        
        txt = font2.render("LIVES: "+str(lives),True,black)
        screen.blit(txt,(xdim-txt.get_width()-5,20+txt.get_height()))
        
        txt = font2.render("SCORE: "+str(int((time.time()-start_time+bonus)*10/10.)),True,black)
        screen.blit(txt,(xdim-txt.get_width()-5,10))
        
        if lives <= 0:
            menu = "dead"
            score = int(time.time()-start_time)+bonus
            
    if menu == "fox":
        if time.time() < fox_time:
            pygame.mouse.set_visible(0)
            screen.blit(bush_img,(0,0))
            if random.randint(1,100) == 1:
                foxes.append(Fox())
            i = 0
            while i < len(foxes):
                foxes[i].draw()
                if foxes[i].hit() and foxes[i].dead == 0:
                    fox_score += 10
                    foxes[i].dead_time = time.time()
                    foxes[i].dead = 1
                    foxes[i].dead_pos = (MousePx-10,MousePy-10)
                if foxes[i].time_out():
                    del foxes[i]
                    i -= 1
                i += 1
            i = 0
            while i < len(foxes):
                if foxes[i].dead == 1 and time.time() > foxes[i].dead_time+0.1:
                    del foxes[i]
                    i -= 1
                i += 1
            gun.d = math.degrees(math.atan2(xdim/2-MousePx,ydim-MousePy))
            gun.draw()
            if gun.fire():
                shot_sound.play()
            txt = font2.render("SCORE: "+str(fox_score),True,black)
            screen.blit(txt,(xdim-10-txt.get_width(),10))
        else:
            bonus += fox_score
            menu = "main"
            farage.x = -100
            difficulty = 300
            pygame.mouse.set_visible(1)
            
    if menu == "dead":
        screen.fill(black)
        txt = font1.render("GAME OVER",True,red)
        screen.blit(txt,(xdim/2-txt.get_width()/2,ydim/4))
        txt = font3.render("Score: "+str(score),True,blue)
        screen.blit(txt,(xdim/2-txt.get_width()/2,ydim/2))
        txt = font3.render("REPLAY",True,blue)
        screen.blit(txt,(xdim/2-txt.get_width()/2,ydim*3/4))
        replayrect = pygame.Rect((xdim/2-txt.get_width()/2,ydim*3/4),txt.get_size())
        if MouseC[0] and replayrect.collidepoint(MouseP):
            menu = "start"
    
    pygame.display.update()