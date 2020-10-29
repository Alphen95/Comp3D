import pygame
from random import randint
from pprint import pprint
from pathlib import Path
import platform
import time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (105, 105, 105)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (255, 226, 0)
PINK = (230, 50, 230)
NAVY = (0, 0, 128)
DARK_GREEN = (0, 100, 0)
RED = (255, 0, 0)
JEANS = (26, 34, 74)
LIGHTGRAY = (169, 169, 169)
MEDKIT = (211, 211, 211)
BROWN = (87, 39, 3)
LIGHTYELLOW = (214, 207, 148)
MAGENTA = (179, 62, 181)
BLUE = (0, 0, 130)
DARK_MAGENTA = (74, 4, 74)
DARK_GRAY = (33, 33, 33)
SIZE = 3
health = 0

infoObject = pygame.display.Info()
pygame.display.set_caption('Compystein 3-D Beta 2.2')
sc = pygame.display.set_mode((infoObject.current_w, SIZE * 300), pygame.FULLSCREEN)
indent_horizontal = int((infoObject.current_w - SIZE * 300) / 2)
ready_to_refresh = True
todo = "nothing"
count = 0
last_key = "uwu"
current_weapon = "fist"
weapon_action = "idle"
screen = 0
ticks_from_last_act = 0
x = 3
y = 1
has_knife = False
direction = 1
todo = ""
specialtile = ""
health = 100
ammo = 0
mode = "title"
screen = 0
option = 0
tick = 0
achivement1 = False
pathFolder = str(Path().absolute())
kernel = platform.system()
if kernel == "Windows":
    pathWallL = pathFolder + "\\res\\wall_left.png"
    pathWallR = pathFolder + "\\res\\wall_right.png"
    pathWall2 = pathFolder + "\\res\\wall2.png"
    pathEnemy1 = pathFolder + "\\res\\enemy1.png"
    pathEnemy1Atk = pathFolder + "\\res\\enemy1_atk.png"
    pathEnemy1_corpse0 = pathFolder + "\\res\\enemy1_corpse0.png"
    pathEnemy1_corpse1 = pathFolder + "\\res\\enemy1_corpse1.png"
    pathEnemy1_corpse2 = pathFolder + "\\res\\enemy1_corpse2.png"
    pathEnemy1_corpse3 = pathFolder + "\\res\\enemy1_corpse3.png"
    pathEnemy2 = pathFolder + "\\res\\enemy2.png"
    pathEnemy2Atk = pathFolder + "\\res\\enemy2.png"
    pathEnemy2_corpse0 = pathFolder + "\\res\\enemy2_corpse0.png"
    pathEnemy2_corpse1 = pathFolder + "\\res\\enemy2_corpse1.png"
    pathEnemy2_corpse2 = pathFolder + "\\res\\enemy2_corpse2.png"
    pathEnemy2_corpse3 = pathFolder + "\\res\\enemy2_corpse3.png"
    pathBoss = pathFolder + "\\res\\boss.png"
    pathBossAtk = pathFolder + "\\res\\boss_atk.png"
    pathBoss_corpse0 = pathFolder + "\\res\\boss_corpse0.png"
    pathBoss_corpse1 = pathFolder + "\\res\\boss_corpse1.png"
    pathBoss_corpse2 = pathFolder + "\\res\\boss_corpse2.png"    
    pathBullets = pathFolder + "\\res\\bullets.png"
    pathMedkit = pathFolder + "\\res\\medkit.png"
    pathHandIdle = pathFolder + "\\res\\hand_idle.png"
    pathKnife = pathFolder + "\\res\\knife.png"
    pathKnifePick = pathFolder + "\\res\\knife_pickup.png"
    pathGunIdle = pathFolder + "\\res\\gun_idle.png"
    pathGunAtk = pathFolder + "\\res\\gun_atk.png"
    pathTitle = pathFolder + "\\res\\title.png"
    pathStatusbar = pathFolder + "\\res\\statusbar.png"
    pathAchiv1 = pathFolder + "\\res\\chara_achivement.png"
    pathMusKnife_slash = pathFolder + "\\res\\knife_slash.ogg"
    pathMusAchiv1= pathFolder + "\\res\\achivement1.ogg"
    pathMusShoot= pathFolder + "\\res\\shoot.wav"
else:
    pathWallL = pathFolder + "/res/wall_left.png"
    pathWallR = pathFolder + "/res/wall_right.png"
    pathWall2 = pathFolder + "/res/wall2.png"
    pathEnemy1 = pathFolder + "/res/enemy1.png"
    pathEnemy1Atk = pathFolder + "/res/enemy1_atk.png"
    pathEnemy1_corpse0 = pathFolder + "/res/enemy1_corpse0.png"
    pathEnemy1_corpse1 = pathFolder + "/res/enemy1_corpse1.png"
    pathEnemy1_corpse2 = pathFolder + "/res/enemy1_corpse2.png"
    pathEnemy1_corpse3 = pathFolder + "/res/enemy1_corpse3.png"
    pathEnemy2 = pathFolder + "/res/enemy2.png"
    pathEnemy2Atk = pathFolder + "/res/enemy2_atk.png"
    pathEnemy2_corpse0 = pathFolder + "/res/enemy2_corpse0.png"
    pathEnemy2_corpse1 = pathFolder + "/res/enemy2_corpse1.png"
    pathEnemy2_corpse2 = pathFolder + "/res/enemy2_corpse2.png"
    pathEnemy2_corpse3 = pathFolder + "/res/enemy2_corpse3.png"
    pathBoss = pathFolder + "/res/boss.png"
    pathBossAtk = pathFolder + "/res/boss_atk.png"
    pathBoss_corpse0 = pathFolder + "/res/boss_corpse0.png"
    pathBoss_corpse1 = pathFolder + "/res/boss_corpse1.png"
    pathBoss_corpse2 = pathFolder + "/res/boss_corpse2.png"      
    pathBullets = pathFolder + "/res/bullets.png"
    pathMedkit = pathFolder + "/res/medkit.png"
    pathHandIdle = pathFolder + "/res/hand_idle.png"
    pathKnife= pathFolder + "/res/knife.png"
    pathAchiv1= pathFolder + "/res/chara_achivement.png"
    pathKnifePick= pathFolder + "/res/knife_pickup.png"
    pathGunIdle = pathFolder + "/res/gun_idle.png"
    pathGunAtk = pathFolder + "/res/gun_atk.png"
    pathTitle = pathFolder + "/res/title.png"
    pathStatusbar = pathFolder + "/res/statusbar.png"
    pathMusKnife_slash = pathFolder + "/res/knife_slash.ogg"
    pathMusAchiv1= pathFolder + "/res/achivement1.ogg"
    pathMusShoot= pathFolder + "/res/shoot.wav"
WallL_Image = pygame.image.load(pathWallL)
WallR_Image = pygame.image.load(pathWallR)
Wall2_Image = pygame.image.load(pathWall2)
Enemy1_Image = pygame.image.load(pathEnemy1)
Enemy1Atk_Image = pygame.image.load(pathEnemy1Atk)
Enemy1_Image_corpse0 = pygame.image.load(pathEnemy1_corpse0)
Enemy1_Image_corpse1 = pygame.image.load(pathEnemy1_corpse1)
Enemy1_Image_corpse2 = pygame.image.load(pathEnemy1_corpse2)
Enemy1_Image_corpse3 = pygame.image.load(pathEnemy1_corpse3)
Enemy2_Image = pygame.image.load(pathEnemy2)
Enemy2Atk_Image = pygame.image.load(pathEnemy2Atk)
Enemy2_Image_corpse0 = pygame.image.load(pathEnemy2_corpse0)
Enemy2_Image_corpse1 = pygame.image.load(pathEnemy2_corpse1)
Enemy2_Image_corpse2 = pygame.image.load(pathEnemy2_corpse2)
Enemy2_Image_corpse3 = pygame.image.load(pathEnemy2_corpse3)
Boss_Image = pygame.image.load(pathBoss)
BossAtk_Image = pygame.image.load(pathBossAtk)
Boss_Image_corpse0 = pygame.image.load(pathBoss_corpse0)
Boss_Image_corpse1 = pygame.image.load(pathBoss_corpse1)
Boss_Image_corpse2 = pygame.image.load(pathBoss_corpse2)
HandIdle_Image = pygame.image.load(pathHandIdle)
Knife_Image = pygame.image.load(pathKnife)
KnifePick_Image = pygame.image.load(pathKnifePick)
GunIdle_Image = pygame.image.load(pathGunIdle)
GunAtk_Image = pygame.image.load(pathGunAtk)
Bullets_Image = pygame.image.load(pathBullets)
Medkit_Image = pygame.image.load(pathMedkit)
Title_Image = pygame.image.load(pathTitle)
Statusbar_Image = pygame.image.load(pathStatusbar)
Achiv1_Image = pygame.image.load(pathAchiv1)

sound_knife_slash = pygame.mixer.Sound(pathMusKnife_slash)
sound_achivement1 = pygame.mixer.Sound(pathMusAchiv1)
sound_shoot = pygame.mixer.Sound(pathMusShoot)

font = pygame.font.Font("pixel_font.ttf", 72)

leveldict_collis_test = {
    "1-1": "knife_pickup", "1-2": "", "1-3": "", "1-4": "", "1-5": "",
    "2-1": "", "2-2": "", "2-3": "", "2-4": "", "2-5": "",
    "3-1": "bullets", "3-2": "wall", "3-3": "wall", "3-4": "wall", "3-5": "wall",
    "4-1": "", "4-2": "", "4-3": "enemy1_corpse_3", "4-4": "", "4-5": "",
    "5-1": "", "5-2": "", "5-3": "", "5-4": "wall", "5-5": "",
    "6-1": "", "6-2": "", "6-3": "medkit", "6-4": "wall", "6-5": "",
    "7-1": "wall", "7-2": "wall", "7-3": "wall", "7-4": "wall", "7-5": ""
}
leveldict_enemy_test = {
    "1-1": "", "1-2": "", "1-3": "", "1-4": "", "1-5": "",
    "2-1": "wall", "2-2": "", "2-3": "", "2-4": "", "2-5": "wall",
    "3-1": "wall", "3-2": "wall", "3-3": "", "3-4": "wall", "3-5": "wall",
    "4-1": "", "4-2": "", "4-3": "", "4-4": "", "4-5": "",
    "5-1": "", "5-2": "", "5-3": "", "5-4": "", "5-5": "",
    "6-1": "", "6-2": "", "6-3": "", "6-4": "", "6-5": "",
    "7-1": "", "7-2": "enemy1", "7-3": "", "7-4": "", "7-5": "", "health_enemy": 10
}

leveldict_new = leveldict_collis_test.copy()
leveldict = leveldict_new.copy()



def refresh(left, middle, right, hp, ammo, state, wpn):
    sc.fill(BLACK)
    drawScreen(left, middle, right)
    drawWeapon(state, wpn)
    drawHUD(hp, ammo, "uwu")
    
def generate_chunk():
    chunk_id = randint(0, 6)
    if chunk_id == 0:
        chunk = {
            "1-1": "", "1-2": "", "1-3": "", "1-4": "", "1-5": "",
            "2-1": "", "2-2": "", "2-3": "", "2-4": "", "2-5": "",
            "3-1": "bullets", "3-2": "wall", "3-3": "wall", "3-4": "wall", "3-5": "wall",
            "4-1": "", "4-2": "", "4-3": "", "4-4": "", "4-5": "",
            "5-1": "", "5-2": "", "5-3": "enemy1", "5-4": "wall", "5-5": "",
            "6-1": "", "6-2": "bullets", "6-3": "bullets", "6-4": "wall", "6-5": "",
            "7-1": "wall", "7-2": "wall", "7-3": "wall", "7-4": "wall", "7-5": "", "health_enemy": 10
        }
    elif chunk_id == 1:
        chunk = {
            "1-1": "", "1-2": "", "1-3": "", "1-4": "", "1-5": "",
            "2-1": "", "2-2": "", "2-3": "", "2-4": "", "2-5": "",
            "3-1": "", "3-2": "", "3-3": "enemy1", "3-4": "", "3-5": "",
            "4-1": "", "4-2": "wall", "4-3": "wall", "4-4": "wall", "4-5": "",
            "5-1": "", "5-2": "", "5-3": "medkit", "5-4": "", "5-5": "",
            "6-1": "", "6-2": "", "6-3": "", "6-4": "", "6-5": "",
            "7-1": "wall", "7-2": "wall", "7-3": "", "7-4": "wall", "7-5": "wall", "health_enemy": 10
        }
    elif chunk_id == 2:
        chunk = {
            "1-1": "", "1-2": "", "1-3": "", "1-4": "", "1-5": "",
            "2-1": "wall", "2-2": "", "2-3": "", "2-4": "", "2-5": "wall",
            "3-1": "", "3-2": "", "3-3": "", "3-4": "", "3-5": "",
            "4-1": "", "4-2": "wall", "4-3": "wall", "4-4": "wall", "4-5": "",
            "5-1": "", "5-2": "bullets", "5-3": "", "5-4": "medkit", "5-5": "",
            "6-1": "", "6-2": "", "6-3": "", "6-4": "", "6-5": "",
            "7-1": "", "7-2": "", "7-3": "", "7-4": "", "7-5": ""
        }
    elif chunk_id == 3:
        chunk = {
            "1-1": "", "1-2": "", "1-3": "", "1-4": "", "1-5": "",
            "2-1": "wall", "2-2": "", "2-3": "", "2-4": "", "2-5": "wall",
            "3-1": "wall", "3-2": "wall", "3-3": "", "3-4": "wall", "3-5": "wall",
            "4-1": "", "4-2": "", "4-3": "", "4-4": "", "4-5": "",
            "5-1": "", "5-2": "", "5-3": "boss", "5-4": "", "5-5": "",
            "6-1": "", "6-2": "", "6-3": "", "6-4": "", "6-5": "",
            "7-1": "", "7-2": "", "7-3": "", "7-4": "", "7-5": "", "health_enemy": 25
        }
    elif chunk_id == 4:
        chunk = {
            "1-1": "", "1-2": "", "1-3": "", "1-4": "", "1-5": "",
            "2-1": "", "2-2": "", "2-3": "", "2-4": "", "2-5": "",
            "3-1": "bullets", "3-2": "wall", "3-3": "wall", "3-4": "wall", "3-5": "wall",
            "4-1": "", "4-2": "", "4-3": "", "4-4": "", "4-5": "",
            "5-1": "", "5-2": "", "5-3": "enemy1", "5-4": "wall", "5-5": "",
            "6-1": "", "6-2": "bullets", "6-3": "bullets", "6-4": "wall", "6-5": "",
            "7-1": "wall", "7-2": "wall", "7-3": "wall", "7-4": "wall", "7-5": "", "health_enemy": 10
        }
    elif chunk_id == 5:
        chunk = {
            "1-1": "", "1-2": "", "1-3": "", "1-4": "", "1-5": "",
            "2-1": "", "2-2": "", "2-3": "", "2-4": "", "2-5": "",
            "3-1": "", "3-2": "", "3-3": "enemy1", "3-4": "", "3-5": "",
            "4-1": "", "4-2": "wall", "4-3": "wall", "4-4": "wall", "4-5": "",
            "5-1": "", "5-2": "", "5-3": "medkit", "5-4": "", "5-5": "",
            "6-1": "", "6-2": "", "6-3": "", "6-4": "", "6-5": "",
            "7-1": "wall", "7-2": "wall", "7-3": "", "7-4": "wall", "7-5": "wall", "health_enemy": 10
        }
    elif chunk_id == 6:
        chunk = {
            "1-1": "", "1-2": "", "1-3": "", "1-4": "", "1-5": "",
            "2-1": "wall", "2-2": "", "2-3": "", "2-4": "", "2-5": "wall",
            "3-1": "", "3-2": "", "3-3": "", "3-4": "", "3-5": "",
            "4-1": "", "4-2": "wall", "4-3": "wall", "4-4": "wall", "4-5": "",
            "5-1": "", "5-2": "bullets", "5-3": "", "5-4": "medkit", "5-5": "",
            "6-1": "", "6-2": "", "6-3": "", "6-4": "", "6-5": "",
            "7-1": "", "7-2": "", "7-3": "", "7-4": "", "7-5": ""
        }
    return chunk


def look(x, y, direction, lvldict):
    left = ""
    middle = ""
    right = ""
    if direction == 1:
        coords = str(y) + "-" + str(x - 1)
        if (x - 1) != 0:
            left = lvldict[coords]
        else:
            left = "wall"
        coords = str(y) + "-" + str(x + 1)
        if (x + 1) != 6:
            right = lvldict[coords]
        else:
            right = "wall"
        coords = str(y + 1) + "-" + str(x)
        if (y + 1) != 8:
            middle = lvldict[coords]
        coords = str(y + 1) + "-" + str(x - 1)
        if (y + 1) != 8 and (x - 1) != 0 and left == "":
            if lvldict[coords] == "wall":
                left = "wall2"
            else:
                left = lvldict[coords]

        coords = str(y + 1) + "-" + str(x + 1)
        if (y + 1) != 8 and (x + 1) != 6 and right == "":
            if lvldict[coords] == "wall":
                right = "wall2"
            else:
                right = lvldict[coords]
    elif direction == 3:
        coords = str(y) + "-" + str(x + 1)
        if (x + 1) != 6:
            left = lvldict[coords]
        else:
            left = "wall"
        coords = str(y) + "-" + str(x - 1)
        if (x - 1) != 0:
            right = lvldict[coords]
        else:
            right = "wall"
        coords = str(y - 1) + "-" + str(x)
        if (y - 1) != 0:
            middle = lvldict[coords]
        else:
            middle = "wall"
        coords = str(y - 1) + "-" + str(x + 1)
        if (y - 1) != 0 and (x + 1) != 6 and left == "":
            if lvldict[coords] == "wall":
                left = "wall2"
            else:
                left = lvldict[coords]
        elif (y - 1) == 0 and left == "" or (x + 1) == 6 and left == "":
            left = "wall2"
        coords = str(y - 1) + "-" + str(x - 1)
        if (y - 1) != 0 and (x - 1) != 0 and right == "":
            if lvldict[coords] == "wall":
                right = "wall2"
            else:
                right = lvldict[coords]
        elif (y - 1) == 0 and right == "" or (x - 1) == 0 and right == "":
            right = "wall2"
    elif direction == 0:
        coords = str(y + 1) + "-" + str(x)
        if (y + 1) != 8:
            left = leveldict[coords]
        else:
            left = "wall"

        coords = str(y - 1) + "-" + str(x)
        if (y - 1) != 0:
            right = leveldict[coords]
        else:
            right = "wall"
        coords = str(y) + "-" + str(x + 1)
        if (x + 1) != 6:
            middle = leveldict[coords]
        else:
            middle = "wall"
        coords = str(y + 1) + "-" + str(x + 1)
        if (x + 1) != 6 and (y + 1) != 8 and left == "":
            if lvldict[coords] == "wall":
                left = "wall2"
            else:
                left = lvldict[coords]
        elif (x + 1) == 6 and left == "":
            left = "wall2"
        coords = str(y - 1) + "-" + str(x + 1)
        if (x + 1) != 6 and (y - 1) != 0 and right == "":
            if lvldict[coords] == "wall":
                right = "wall2"
            else:
                right = lvldict[coords]
        elif (y - 1) == 0 and right == "" or (x + 1) == 6 and right == "":
            right = "wall2"
    elif direction == 2:
        coords = str(y - 1) + "-" + str(x)
        if (y - 1) != 0:
            left = leveldict[coords]
        else:
            left = "wall"
        coords = str(y + 1) + "-" + str(x)
        if (y + 1) != 8:
            right = leveldict[coords]
        coords = str(y) + "-" + str(x - 1)
        if (x - 1) != 0:
            middle = leveldict[coords]
        else:
            middle = "wall"
        coords = str(y + 1) + "-" + str(x - 1)
        if (x - 1) != 0 and (y + 1) != 8 and right == "":
            if lvldict[coords] == "wall":
                right = "wall2"
            else:
                right = lvldict[coords]
        elif (y + 1) == 8 and right == "" or (x - 1) == 0 and right == "":
            right = "wall2"
        coords = str(y - 1) + "-" + str(x - 1)
        if (x - 1) != 0 and (y - 1) != 0 and left == "":
            if lvldict[coords] == "wall":
                left = "wall2"
            else:
                left = lvldict[coords]
        elif (y - 1) == 0 and left == "" or (x - 1) == 0 and left == "":
            left = "wall2"

    else:
        pass
    print(left, middle, right)
    return left, middle, right


def drawScreen(left, middle, right):
    if left == "wall":
        sc.blit(pygame.transform.scale(WallL_Image, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "wall2":
        sc.blit(pygame.transform.scale(Wall2_Image, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "bullets":
        sc.blit(pygame.transform.scale(Bullets_Image, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "medkit":
        sc.blit(pygame.transform.scale(Medkit_Image, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "knife_pickup":
        sc.blit(pygame.transform.scale(KnifePick_Image, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))        
    elif left == "enemy1":
        sc.blit(pygame.transform.scale(Enemy1_Image, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy1_atk":
        sc.blit(pygame.transform.scale(Enemy1Atk_Image, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))        
    elif left == "enemy1_corpse_0":
        sc.blit(pygame.transform.scale(Enemy1_Image_corpse0, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy1_corpse_1":
        sc.blit(pygame.transform.scale(Enemy1_Image_corpse1, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy1_corpse_2":
        sc.blit(pygame.transform.scale(Enemy1_Image_corpse2, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy1_corpse_3":
        sc.blit(pygame.transform.scale(Enemy1_Image_corpse3, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy2":
        sc.blit(pygame.transform.scale(Enemy2_Image, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy2_atk":
        sc.blit(pygame.transform.scale(Enemy2Atk_Image, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))        
    elif left == "enemy2_corpse_0":
        sc.blit(pygame.transform.scale(Enemy2_Image_corpse0, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy2_corpse_1":
        sc.blit(pygame.transform.scale(Enemy2_Image_corpse1, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy2_corpse_2":
        sc.blit(pygame.transform.scale(Enemy2_Image_corpse2, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy2_corpse_3":
        sc.blit(pygame.transform.scale(Enemy2_Image_corpse3, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "boss":
        sc.blit(pygame.transform.scale(Boss_Image, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "boss_atk":
        sc.blit(pygame.transform.scale(BossAtk_Image, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))    
    elif left == "boss_corpse_0":
        sc.blit(pygame.transform.scale(Boss_Image_corpse0, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "boss_corpse_1":
        sc.blit(pygame.transform.scale(Boss_Image_corpse1, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "boss_corpse_2":
        sc.blit(pygame.transform.scale(Boss_Image_corpse2, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    if right == "wall":
        sc.blit(pygame.transform.scale(WallR_Image, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif right == "wall2":
        sc.blit(pygame.transform.scale(Wall2_Image, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif right == "bullets":
        sc.blit(pygame.transform.scale(Bullets_Image, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif right == "medkit":
        sc.blit(pygame.transform.scale(Medkit_Image, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif right == "knife_pickup":
        sc.blit(pygame.transform.scale(KnifePick_Image, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))    
    elif right == "enemy1":
        sc.blit(pygame.transform.scale(Enemy1_Image, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif right == "enemy1_atk":
        sc.blit(pygame.transform.scale(Enemy1Atk_Image, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))    
    elif right == "enemy1_corpse_0":
        sc.blit(pygame.transform.scale(Enemy1_Image_corpse0, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "enemy1_corpse_1":
        sc.blit(pygame.transform.scale(Enemy1_Image_corpse1, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "enemy1_corpse_2":
        sc.blit(pygame.transform.scale(Enemy1_Image_corpse2, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "enemy1_corpse_3":
        sc.blit(pygame.transform.scale(Enemy1_Image_corpse3, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "enemy2":
        sc.blit(pygame.transform.scale(Enemy2_Image, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif right == "enemy2_atk":
        sc.blit(pygame.transform.scale(Enemy2Atk_Image, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))    
    elif right == "enemy2_corpse_0":
        sc.blit(pygame.transform.scale(Enemy2_Image_corpse0, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "enemy2_corpse_1":
        sc.blit(pygame.transform.scale(Enemy2_Image_corpse1, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "enemy2_corpse_2":
        sc.blit(pygame.transform.scale(Enemy2_Image_corpse2, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "enemy2_corpse_3":
        sc.blit(pygame.transform.scale(Enemy2_Image_corpse3, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "boss":
        sc.blit(pygame.transform.scale(Boss_Image, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif right == "boss_atk":
        sc.blit(pygame.transform.scale(BossAtk_Image, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))    
    elif right == "boss_corpse_0":
        sc.blit(pygame.transform.scale(Boss_Image_corpse0, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "boss_corpse_1":
        sc.blit(pygame.transform.scale(Boss_Image_corpse1, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "boss_corpse_2":
        sc.blit(pygame.transform.scale(Boss_Image_corpse2, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    if middle == "wall2" or middle == "wall":
        sc.blit(pygame.transform.scale(Wall2_Image, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "medkit":
        sc.blit(pygame.transform.scale(Medkit_Image, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "knife_pickup":
        sc.blit(pygame.transform.scale(KnifePick_Image, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))    
    elif middle == "bullets":
        sc.blit(pygame.transform.scale(Bullets_Image, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy1":
        sc.blit(pygame.transform.scale(Enemy1_Image, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy1_atk":
        sc.blit(pygame.transform.scale(Enemy1Atk_Image, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))    
    elif middle == "enemy1_corpse_0":
        sc.blit(pygame.transform.scale(Enemy1_Image_corpse0, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy1_corpse_1":
        sc.blit(pygame.transform.scale(Enemy1_Image_corpse1, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy1_corpse_2":
        sc.blit(pygame.transform.scale(Enemy1_Image_corpse2, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy1_corpse_3":
        sc.blit(pygame.transform.scale(Enemy1_Image_corpse3, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy2":
        sc.blit(pygame.transform.scale(Enemy2_Image, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy2_atk":
        sc.blit(pygame.transform.scale(Enemy2Atk_Image, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))        
    elif middle == "enemy2_corpse_0":
        sc.blit(pygame.transform.scale(Enemy2_Image_corpse0, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy2_corpse_1":
        sc.blit(pygame.transform.scale(Enemy2_Image_corpse1, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy2_corpse_2":
        sc.blit(pygame.transform.scale(Enemy2_Image_corpse2, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy2_corpse_3":
        sc.blit(pygame.transform.scale(Enemy2_Image_corpse3, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "boss":
        sc.blit(pygame.transform.scale(Boss_Image, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "boss_atk":
        sc.blit(pygame.transform.scale(BossAtk_Image, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))    
    elif middle == "boss_corpse_0":
        sc.blit(pygame.transform.scale(Boss_Image_corpse0, (100 * SIZE, 300 * SIZE)), (100*SIZE + indent_horizontal, 0))
    elif middle == "boss_corpse_1":
        sc.blit(pygame.transform.scale(Boss_Image_corpse1, (100 * SIZE, 300 * SIZE)), (100*SIZE + indent_horizontal, 0))
    elif middle == "boss_corpse_2":
        sc.blit(pygame.transform.scale(Boss_Image_corpse2, (100 * SIZE, 300 * SIZE)), (100*SIZE + indent_horizontal, 0))


def drawWeapon(state, weapon):
    if weapon == "fist":
        if state == "idle":
            sc.blit(pygame.transform.scale(HandIdle_Image, (100 * SIZE, 300 * SIZE)), (125 * SIZE + indent_horizontal, 0))
        elif state == "attack":
            sc.blit(pygame.transform.scale(HandIdle_Image, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, -10 * SIZE))
    elif weapon == "pistol":
        if state == "idle":
            sc.blit(pygame.transform.scale(GunIdle_Image, (100 * SIZE, 300 * SIZE)), (125 * SIZE + indent_horizontal, 0))
        elif state == "attack":
            sc.blit(pygame.transform.scale(GunAtk_Image, (100 * SIZE, 300 * SIZE)), (125 * SIZE + indent_horizontal, 0))
    elif weapon == "knife":
        if state == "idle":
            sc.blit(pygame.transform.scale(Knife_Image, (100 * SIZE, 300 * SIZE)), (125 * SIZE + indent_horizontal, -10 * SIZE))
        elif state == "attack":
            sc.blit(pygame.transform.scale(Knife_Image, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, -30 * SIZE))


def showAchivement(name,image):
    sc.blit(pygame.transform.scale(image, (30 * SIZE, 30 * SIZE)), (0 * SIZE + indent_horizontal, 0* SIZE))
    achivement_text = font.render(name, 1, WHITE)
    sc.blit(achivement_text, [SIZE * 35 + indent_horizontal, SIZE * 10])
    
def drawHUD(hp, ammo, lastact):
    sc.blit(pygame.transform.scale(Statusbar_Image, (300 * SIZE, 30 * SIZE)), (0 * SIZE + indent_horizontal, 270* SIZE))
    hp_text = font.render(str(hp), 1, RED)
    ammo_text = font.render(str(ammo), 1, RED)

    hp_text_low = font.render("HP", 1, RED)
    ammo_text_low = font.render("Ammo", 1, RED)
    if len(str(hp)) == 3:
        sc.blit(hp_text, [SIZE * 55 + indent_horizontal, SIZE * 275])
    elif len(str(hp)) == 2:
        sc.blit(hp_text, [SIZE * 65 + indent_horizontal, SIZE * 275])
    elif len(str(hp)) == 1:
        sc.blit(hp_text, [SIZE * 70 + indent_horizontal, SIZE * 275])
    if len(str(ammo)) == 3:
        sc.blit(ammo_text, [SIZE * 250 + indent_horizontal, SIZE * 275])
    elif len(str(ammo)) == 2:
        sc.blit(ammo_text, [SIZE * 255 + indent_horizontal, SIZE * 275])
    elif len(str(ammo)) == 1:
        sc.blit(ammo_text, [SIZE * 262 + indent_horizontal, SIZE * 275])
    sc.blit(hp_text_low, [SIZE * 25 + indent_horizontal, SIZE * 275])
    sc.blit(ammo_text_low, [SIZE * 205 + indent_horizontal, SIZE * 275])

damage = 0
turn = "player"
current_weapon = "pistol"
while 1:
    if last_key == "up":
        if mode == "game":
            turn = "enemy"
            disp_left, disp_middle, disp_right = look(x, y, direction, leveldict)
            if disp_middle == "" or disp_middle == "enemy1_corpse_3" or disp_middle == "boss_corpse_2" or disp_middle == "enemy2_corpse_3" or disp_middle == "bullets" or disp_middle == "medkit" or disp_middle == "knife_pickup":
                if disp_middle == "bullets":
                    if direction == 0:
                        coords = str(y) + "-" + str(x + 1)
                        leveldict[coords] = ""
                    elif direction == 1:
                        coords = str(y + 1) + "-" + str(x)
                        leveldict[coords] = ""
                    elif direction == 2:
                        coords = str(y) + "-" + str(x - 1)
                        leveldict[coords] = ""
                    elif direction == 3:
                        coords = str(y - 1) + "-" + str(x)
                        leveldict[coords] = ""
                    ammo += 2
                if disp_middle == "knife_pickup":
                    if direction == 2:
                        coords = str(y) + "-" + str(x - 1)
                        leveldict[coords] = ""
                    elif direction == 1:
                        coords = str(y + 1) + "-" + str(x)
                        leveldict[coords] = ""
                    elif direction == 0:
                        coords = str(y) + "-" + str(x + 1)
                        leveldict[coords] = ""
                    elif direction == 3:
                        coords = str(y - 1) + "-" + str(x)
                        leveldict[coords] = ""
                    has_knife = True
                if disp_middle == "medkit":
                    if health < 100:
                        if direction == 2:
                            coords = str(y) + "-" + str(x - 1)
                            leveldict[coords] = ""
                        elif direction == 1:
                            coords = str(y + 1) + "-" + str(x)
                            leveldict[coords] = ""
                        elif direction == 0:
                            coords = str(y) + "-" + str(x + 1)
                            leveldict[coords] = ""
                        elif direction == 3:
                            coords = str(y - 1) + "-" + str(x)
                            leveldict[coords] = ""
                        health += 10
                        if health > 100:
                            health = 100
                if direction == 1:
                    if y == 7:
                        y = 1
                        leveldict = generate_chunk()
                    else:
                        y += 1
                elif direction == 0:
                    if x == 5:
                        pass
                    else:
                        x += 1
                elif direction == 3:
                    if y == 0:
                        pass
                    else:
                        y -= 1
                elif direction == 2:
                    if x == 0:
                        pass
                    else:
                        x -= 1
        elif mode == "debug":
            if screen == 0:
                if option == 0:
                    option = 3
                else:
                    option -= 1
            else:
                if option == 0:
                    option = 1
                else:
                    option -= 1
    if last_key == "down":
                    if mode == "game":
                        turn = "enemy"
                        if y - 1 != 0:
                            disp_left, disp_middle, disp_right = look(x, y - 1, direction, leveldict)
                            if disp_middle == "" or disp_middle == "enemy1_corpse_3" or disp_middle == "boss_corpse_2" or disp_middle == "enemy2_corpse_3" or disp_middle == "bullets" or disp_middle == "medkit" or disp_middle == "knife_pickup":
                                if disp_middle == "bullets":
                                    if direction == 0:
                                        coords = str(y) + "-" + str(x - 1)
                                        leveldict[coords] = ""
                                    elif direction == 3:
                                        coords = str(y + 1) + "-" + str(x)
                                        leveldict[coords] = ""
                                    elif direction == 2:
                                        coords = str(y) + "-" + str(x + 1)
                                        leveldict[coords] = ""
                                    elif direction == 1:
                                        coords = str(y - 1) + "-" + str(x)
                                        leveldict[coords] = ""
                                    ammo += 2
                                if disp_middle == "knife_pickup":
                                    if direction == 0:
                                        coords = str(y) + "-" + str(x - 1)
                                        leveldict[coords] = ""
                                    elif direction == 3:
                                        coords = str(y + 1) + "-" + str(x)
                                        leveldict[coords] = ""
                                    elif direction == 2:
                                        coords = str(y) + "-" + str(x + 1)
                                        leveldict[coords] = ""
                                    elif direction == 1:
                                        coords = str(y - 1) + "-" + str(x)
                                        leveldict[coords] = ""
                                    has_knife =True
                                if disp_middle == "medkit":
                                    if direction == 0:
                                        coords = str(y) + "-" + str(x - 1)
                                        leveldict[coords] = ""
                                    elif direction == 3:
                                        coords = str(y + 1) + "-" + str(x)
                                        leveldict[coords] = ""
                                    elif direction == 2:
                                        coords = str(y) + "-" + str(x + 1)
                                        leveldict[coords] = ""
                                    elif direction == 1:
                                        coords = str(y - 1) + "-" + str(x)
                                        leveldict[coords] = ""
                                    health += 10
                                    if health > 100:
                                        health = 100
                                if direction == 3:
                                    if y == 7:
                                        y = 1
                                        leveldict = generate_chunk()
                                        print(leveldict)
                                    else:
                                        y += 1
                                elif direction == 2:
                                    if x == 5:
                                        pass
                                    else:
                                        x += 1
                                elif direction == 1:
                                    if y == 0:
                                        pass
                                    else:
                                        y -= 1
                                elif direction == 0:
                                    if x == 0:
                                        pass
                                    else:
                                        x -= 1
                        
                    elif mode == "debug":
                        if screen == 0:
                            if option == 3:
                                option = 0
                            else:
                                option += 1
                        else:
                            if option == 1:
                                option = 0
                            else:
                                option += 1        
    elif last_key == "left":
        if mode == "game":
            turn = "enemy"
            if direction != 3:
                direction += 1
            else:
                direction = 0
        elif mode == "debug":
            if screen == 1:
                screen = 0

            else:
                screen += 1
            option = 0        
    elif last_key == "d":
        if mode != "debug" and mode != "title":
            mode = "debug"
        elif mode == "debug":
            mode = "game"
    elif last_key == "h":
        if mode != "help":
            mode = "help"
        elif mode == "help":
            mode = "game"    
    elif last_key == "right":
        if mode == "game":
            turn = "enemy"
            if direction != 0:
                direction -= 1
            else:
                direction = 3
        elif mode == "debug":
            if screen == 0:
                screen = 1
            else:
                screen -= 1
            option = 0        
        
    elif last_key == "space":
        if mode == "game":
            turn = "enemy"
            right, middle, left = look(x, y, direction, leveldict)
            if current_weapon == "fist":
                damage = randint(4, 11)
                weapon_action = "attack"
            elif current_weapon == "pistol":
                if ammo != 0:
                    sound_shoot.play()
                    weapon_action = "attack"
                    damage = randint(6, 15)
                    ammo -= 1
            elif current_weapon == "knife":
                weapon_action = "attack"
                damage = 100
                sound_knife_slash.play()
            if direction == 0:
                coords = str(y) + "-" + str(x + 1)
            elif direction == 1:
                coords = str(y + 1) + "-" + str(x)
            elif direction == 2:
                coords = str(y) + "-" + str(x - 1)
            elif direction == 3:
                coords = str(y - 1) + "-" + str(x)
            if middle == "enemy1" or middle == "enemy2" or middle == "boss":
                leveldict["health_enemy"] = leveldict["health_enemy"] - damage
                if leveldict["health_enemy"] <= 0:
                    leveldict[coords] = leveldict[coords] + "_corpse_0"
                    tick = 0
            damage = 0
                
        
        elif mode == "game_over":
            mode = "game"
            health = 100
            ammo = 5
            x = 3
            y = 1
            direction = 1
            leveldict = leveldict_new.copy()
            turn = "player"


    elif last_key == "1":
        current_weapon = "fist"
    elif last_key == "2":
        current_weapon = "pistol"
    elif last_key == "3" and has_knife:
        current_weapon = "knife"            
    elif last_key == "confirm":
        if mode == "debug":
            if screen == 0:
                if option == 0:
                    exit()
                elif option == 1:
                    health = 100
                elif option == 2:
                    ammo += 10
            elif screen == 1:
                if option == 0:
                    leveldict_new = leveldict_collis_test.copy()
                elif option == 1:
                    leveldict_new = leveldict_enemy_test.copy()

                leveldict = leveldict_new.copy()
                x = 3
                y = 1
                health = 100
                ammo = 5                
            screen = 0
            opton = 0
            mode = "game"
        elif mode == "title":
            mode = "game"
            health = 100
            ammo = 5
            x = 3
            y = 1
            direction = 1
            leveldict_new = leveldict_collis_test.copy()
            leveldict = leveldict_new.copy()
            turn = "player"
        elif mode == "game_over":
    
            mode = "title"
    if has_knife == True and achivement1 != True:
            sound_achivement1.play()
    if mode == "game":
        disp_left, disp_middle, disp_right = look(x, y, direction, leveldict)
        print(disp_left, disp_middle, disp_right)
        refresh(disp_left, disp_middle, disp_right, health, ammo, weapon_action, current_weapon)
        if has_knife == True and achivement1 != True:
            showAchivement("Genocide",Achiv1_Image)       
            todo = "achivement1"
    elif mode == "game_over":
        disp_left, disp_middle, disp_right = look(x, y, direction, leveldict)
        print(disp_left, disp_middle, disp_right)
        refresh(disp_left, disp_middle, disp_right, health, ammo, weapon_action, current_weapon)
        text = font.render("You died!", 1, RED)
        sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 5])
        text = font.render("[Enter] to quit to tilte.", 1, RED)
        sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 25])
        text = font.render("[Space] to respawn.", 1, RED)
        sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 45])
    elif mode == "title":
        sc.fill(BLACK)
        sc.blit(pygame.transform.scale(Title_Image, (84 * SIZE, 84 * SIZE)), (110* SIZE + indent_horizontal, 15* SIZE))
        text = font.render("Compystein 3-D Beta 2", 1, GREEN)
        sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 55])
        text = font.render("Press [Enter] to start!", 1, GREEN)
        sc.blit(text, [indent_horizontal + SIZE * 10, SIZE * 135])
    elif mode == "help":
        sc.fill(GRAY)
        text = font.render("Compystein 3-D Beta 2 Help", 1, GREEN)
        sc.blit(text, [indent_horizontal + SIZE * 10, SIZE * 30])
        text = font.render("Walk : arrow keys", 1, GREEN)
        sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 65])
        text = font.render("Attack : [space]", 1, GREEN)
        sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 85])
        text = font.render("Debug menu : [D]", 1, GREEN)
        sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 105])
        text = font.render("Debug menu cofirm : [Enter]", 1, GREEN)
        sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 125])
        text = font.render("Leave game : [Q]", 1, GREEN)
        sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 145])   
    elif mode == "debug":
        sc.fill(BLACK)
        text = font.render("DEBUG MENU", 1, WHITE)
        sc.blit(text, [indent_horizontal + SIZE * 80, SIZE * 30])
        text = font.render(str(screen), 1, WHITE)
        sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 280])
        if screen == 0:
            text = font.render("Cheats", 1, WHITE)
            sc.blit(text, [indent_horizontal + SIZE * 100, SIZE * 60])
            if option == 0:
                text = font.render(">Close game", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 80])
                text = font.render("Set HP to 100", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 100])
                text = font.render("Give 10 bullets", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 120])
                text = font.render("Show debug info", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 140])
            elif option == 1:
                text = font.render("Close game", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 80])
                text = font.render(">Set HP to 100", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 100])
                text = font.render("Give 10 bullets", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 120])
                text = font.render("Show debug info", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 140])                  
            elif option == 2:
                text = font.render("Close game", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 80])
                text = font.render("Set HP to 100", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 100])
                text = font.render(">Give 10 bullets", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 120])
                text = font.render("Show debug info", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 140])                
            elif option == 3:
                text = font.render("Close game", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 80])
                text = font.render("Set HP to 100", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 100])
                text = font.render("Give 10 bullets", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 120])
                text = font.render(">Show debug info", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 140])
        elif screen == 1:
            text = font.render("Debug maps", 1, WHITE)
            sc.blit(text, [indent_horizontal + SIZE * 100, SIZE * 60])
            if option == 0:
                text = font.render(">Object and collision test", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 80])
                text = font.render("Enemy test", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 100])
            elif option == 1:
                text = font.render("Object and collision test", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 80])
                text = font.render(">Enemy test", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 100])
    if specialtile!="":
        leveldict[specialtile] =spare_string[0:-4]
        specialtile = ""
        pprint(leveldict)
        print("a")
        print(spare_string)        
    pygame.display.update()
    pygame.time.delay(100)
    tick += 1
    last_key = ""
    if turn != "player":
        turn = "player"
        b = 0
        for tile in leveldict:
            if b != 1:
                if leveldict[tile] == "enemy1" or leveldict[tile] == "enemy2" or leveldict[tile] == "boss":
                    pprint(leveldict)
                    print(tile)
                    print("b",len(tile))
                    spare_string = tile[2:3]
                    print("a",spare_string)
                    enemy_X = int(spare_string)
                    spare_string = tile[:1]
                    enemy_Y = int(spare_string)
                    if enemy_X + 1 == x and enemy_Y == y or enemy_X - 1 == x and enemy_Y == y or enemy_X == x and enemy_Y + 1 == y or enemy_X == x and enemy_Y - 1 == y :
                        if leveldict[tile] == "enemy1":
                            damage = randint(1, 6)
                        elif leveldict[tile] == "enemy2":
                            damage = randint(3, 10)
                        elif leveldict[tile] == "boss":
                            damage = randint(7, 16)
                        health = health - damage                        
                        spare_string = str(leveldict[tile])
                        leveldict[tile] = leveldict[tile] +"_atk"
                        specialtile = tile
                        print("uwu",specialtile)
                        damage = 0
                        if health < 1:
                            mode = "game_over"
                    else:
                        side = randint(0, 3)
                        right, middle, left = look(enemy_X, enemy_Y, side, leveldict)
                        if middle == "":
                            if side == 1:
                                if enemy_Y == 7:
                                    pass
                                else:
                                    enemy_Y += 1
                            elif side == 0:
                                if enemy_X == 5:
                                    pass
                                else:
                                    enemy_X += 1
                            elif side == 3:
                                if enemy_Y == 1:
                                    pass
                                else:
                                    enemy_Y -= 1
                            elif side == 2:
                                if enemy_X == 1:
                                    pass
                                else:
                                    enemy_X -= 1

                    coords = str(enemy_Y) + "-" + str(enemy_X)
                    spare_string = leveldict[tile]
                    leveldict[coords] = spare_string
                    if coords != tile:
                        leveldict[tile] = ""
    if weapon_action == "attack":
        weapon_action = "idle"
    turn = "player"
    if tick % 5 == 0 or tick == 0:
        if todo == "achivement1":
            achivement1 = True
        for cell in leveldict:
            print(cell)
            if leveldict[cell] == "enemy1_corpse_0":
                leveldict[cell] = "enemy1_corpse_1"
            elif leveldict[cell] == "enemy1_corpse_1":
                leveldict[cell] = "enemy1_corpse_2"
            elif leveldict[cell] == "enemy1_corpse_2":
                leveldict[cell] = "enemy1_corpse_3"
            elif leveldict[cell] == "enemy2_corpse_0":
                leveldict[cell] = "enemy2_corpse_1"
            elif leveldict[cell] == "enemy2_corpse_1":
                leveldict[cell] = "enemy2_corpse_2"
            elif leveldict[cell] == "enemy2_corpse_2":
                leveldict[cell] = "enemy2_corpse_3"
            elif leveldict[cell] == "boss_corpse_0":
                leveldict[cell] = "boss_corpse_1"
            elif leveldict[cell] == "boss_corpse_1":
                leveldict[cell] = "boss_corpse_2"
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_q:
                pprint(leveldict)
                exit()
            elif i.key == pygame.K_d:
                last_key = "d"
            elif i.key == pygame.K_h:
                last_key = "h"
            elif i.key == pygame.K_UP:
                last_key = "up"
            elif i.key == pygame.K_LEFT:
                last_key = "left"
            elif i.key == pygame.K_RIGHT:
                last_key = "right"
            elif i.key == pygame.K_DOWN:
                last_key = "down"
            elif i.key == pygame.K_SPACE:
                last_key = "space"
            elif i.key == pygame.K_RETURN:
                last_key = "confirm"
            elif i.key == pygame.K_1:
                last_key = "1"
            elif i.key == pygame.K_2:
                last_key = "2"
            elif i.key == pygame.K_3:
                last_key = "3"            
