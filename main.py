import pygame, platform, time, sys,linecache,json
from random import randint
from pprint import pprint
from pathlib import Path

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
ready_to_refresh = True
todo = "nothing"
count = 0
quitted = False
last_key = "uwu"
current_weapon = "fist"
weapon_action = "idle"
screen = 0
ticks_from_last_act = 0
x = 3
y = 1
specialtiles = []
arguments = sys.argv
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
path_custom_level = ""
achivement1 = False
path_folder = str(Path().absolute())
kernel = platform.system()
useLocalization = False
is_custom_level = False
#Coded by 1 russian programmer, Alphen95(also Luigi180059 and Luigi Toadstool)
if kernel == "Windows":
    path_wall_l = path_folder + "\\res\\wall_left.png"
    path_wall_r = path_folder + "\\res\\wall_right.png"
    path_wall2 = path_folder + "\\res\\wall2.png"
    path_enemy1 = path_folder + "\\res\\enemy1.png"
    path_enemy1_atk = path_folder + "\\res\\enemy1_atk.png"
    path_enemy1_corpse0 = path_folder + "\\res\\enemy1_corpse0.png"
    path_enemy1_corpse1 = path_folder + "\\res\\enemy1_corpse1.png"
    path_enemy1_corpse2 = path_folder + "\\res\\enemy1_corpse2.png"
    path_enemy1_corpse3 = path_folder + "\\res\\enemy1_corpse3.png"
    path_enemy2 = path_folder + "\\res\\enemy2.png"
    path_enemy2_atk = path_folder + "\\res\\enemy2.png"
    path_enemy2_corpse0 = path_folder + "\\res\\enemy2_corpse0.png"
    path_enemy2_corpse1 = path_folder + "\\res\\enemy2_corpse1.png"
    path_enemy2_corpse2 = path_folder + "\\res\\enemy2_corpse2.png"
    path_enemy2_corpse3 = path_folder + "\\res\\enemy2_corpse3.png"
    path_boss = path_folder + "\\res\\boss.png"
    path_boss_atk = path_folder + "\\res\\boss_atk.png"
    path_boss_corpse0 = path_folder + "\\res\\boss_corpse0.png"
    path_boss_corpse1 = path_folder + "\\res\\boss_corpse1.png"
    path_boss_corpse2 = path_folder + "\\res\\boss_corpse2.png"    
    path_bullets = path_folder + "\\res\\bullets.png"
    path_medkit = path_folder + "\\res\\medkit.png"
    path_hand = path_folder + "\\res\\hand_idle.png"
    path_knife + "\\res\\knife.png"
    path_knife_item = path_folder + "\\res\\knife_pickup.png"
    path_gun_idle = path_folder + "\\res\\gun_idle.png"
    path_gun_atk = path_folder + "\\res\\gun_atk.png"
    path_title = path_folder + "\\res\\title.png"
    path_error = path_folder + "\\res\\error_screen.png"
    path_floor= path_folder + "\\res\\floor.png"
    path_statusbar = path_folder + "\\res\\statusbar.png"
    path_achiv1 = path_folder + "\\res\\chara_achivement.png"
    path_snd_slash = path_folder + "\\res\\knife_slash.ogg"
    path_snd_achiv1= path_folder + "\\res\\achivement1.ogg"
    path_snd_shoot= path_folder + "\\res\\shoot.wav"
    path_bgm_old_office= path_folder + "\\res\\mus_old_office.wav"
    path_localization = path_folder + "\\localization\\translated_comp3d.json"
    path_wall = path_folder + "\\res\\editor\\wall.png"
else:
    path_wall_l = path_folder + "/res/wall_left.png"
    path_wall_r = path_folder + "/res/wall_right.png"
    path_wall2 = path_folder + "/res/wall2.png"
    path_enemy1 = path_folder + "/res/enemy1.png"
    path_enemy1_atk = path_folder + "/res/enemy1_atk.png"
    path_enemy1_corpse0 = path_folder + "/res/enemy1_corpse0.png"
    path_enemy1_corpse1 = path_folder + "/res/enemy1_corpse1.png"
    path_enemy1_corpse2 = path_folder + "/res/enemy1_corpse2.png"
    path_enemy1_corpse3 = path_folder + "/res/enemy1_corpse3.png"
    path_enemy2 = path_folder + "/res/enemy2.png"
    path_enemy2_atk = path_folder + "/res/enemy2_atk.png"
    path_enemy2_corpse0 = path_folder + "/res/enemy2_corpse0.png"
    path_enemy2_corpse1 = path_folder + "/res/enemy2_corpse1.png"
    path_enemy2_corpse2 = path_folder + "/res/enemy2_corpse2.png"
    path_enemy2_corpse3 = path_folder + "/res/enemy2_corpse3.png"
    path_boss = path_folder + "/res/boss.png"
    path_boss_atk = path_folder + "/res/boss_atk.png"
    path_boss_corpse0 = path_folder + "/res/boss_corpse0.png"
    path_boss_corpse1 = path_folder + "/res/boss_corpse1.png"
    path_boss_corpse2 = path_folder + "/res/boss_corpse2.png"      
    path_bullets = path_folder + "/res/bullets.png"
    path_medkit = path_folder + "/res/medkit.png"
    path_hand = path_folder + "/res/hand_idle.png"
    path_knife= path_folder + "/res/knife.png"
    path_achiv1= path_folder + "/res/chara_achivement.png"
    path_knife_item= path_folder + "/res/knife_pickup.png"
    path_gun_idle = path_folder + "/res/gun_idle.png"
    path_gun_atk = path_folder + "/res/gun_atk.png"
    path_title = path_folder + "/res/title.png"
    path_error = path_folder + "/res/error_screen.png"
    path_floor= path_folder + "/res/floor.png"
    path_statusbar = path_folder + "/res/statusbar.png"
    path_snd_slash = path_folder + "/res/knife_slash.ogg"
    path_snd_achiv1= path_folder + "/res/achivement1.ogg"
    path_snd_shoot= path_folder + "/res/shoot.wav"
    path_wall = path_folder + "/res/editor/wall.png"
    path_bgm_old_office= path_folder + "/res/mus_old_office.wav"
    path_localization = path_folder + "/localization/translated_comp3d.json"
    
try:
    with open(path_localization,mode="r") as decoded_json:
        contents_json = decoded_json.read()
        text_localization = json.loads(contents_json)
    print("Found localization flie, wish to use it?")
    print(text_localization[-1])
    answer = input("Y/N>")
    if answer.lower() == "yes" or answer.lower() == "y":
        useLocalization = True
except:
    print("No localization flie found")
pygame.init()
infoObject = pygame.display.Info()
pygame.display.set_caption('Compystein 3-D Pre-Release')
sc = pygame.display.set_mode((infoObject.current_w, SIZE * 300), pygame.FULLSCREEN)
indent_horizontal = int((infoObject.current_w - SIZE * 300) / 2)

image_wall = pygame.image.load(path_wall)
image_wall_l = pygame.image.load(path_wall_l)
image_wall_r = pygame.image.load(path_wall_r)
image_wall_2 = pygame.image.load(path_wall2)
image_enemy1 = pygame.image.load(path_enemy1)
image_enemy1_atk = pygame.image.load(path_enemy1_atk)
image_enemy1_corpse0 = pygame.image.load(path_enemy1_corpse0)
image_enemy1_corpse1 = pygame.image.load(path_enemy1_corpse1)
image_enemy1_corpse2 = pygame.image.load(path_enemy1_corpse2)
image_enemy1_corpse3 = pygame.image.load(path_enemy1_corpse3)
image_enemy2 = pygame.image.load(path_enemy2)
image_enemy2_atk = pygame.image.load(path_enemy2_atk)
image_enemy2_corpse0 = pygame.image.load(path_enemy2_corpse0)
image_enemy2_corpse1 = pygame.image.load(path_enemy2_corpse1)
image_enemy2_corpse2 = pygame.image.load(path_enemy2_corpse2)
image_enemy2_corpse3 = pygame.image.load(path_enemy2_corpse3)
image_boss = pygame.image.load(path_boss)
image_boss_atk = pygame.image.load(path_boss_atk)
image_boss_corpse0 = pygame.image.load(path_boss_corpse0)
image_boss_corpse1 = pygame.image.load(path_boss_corpse1)
image_boss_corpse2 = pygame.image.load(path_boss_corpse2)
image_knife_sprite = pygame.image.load(path_knife_item)
image_bullets = pygame.image.load(path_bullets)
image_medkit = pygame.image.load(path_medkit)
image_hand = pygame.image.load(path_hand)
image_kinfe = pygame.image.load(path_knife)
image_lightgun_atk = pygame.image.load(path_gun_atk)
image_lightgun_idle = pygame.image.load(path_gun_idle)
image_title = pygame.image.load(path_title)
image_error = pygame.image.load(path_error)
image_floor = pygame.image.load(path_floor)
image_statusbar = pygame.image.load(path_statusbar)
image_achiv1 = pygame.image.load(path_achiv1)

snd_knife_slash = pygame.mixer.Sound(path_snd_slash)
snd_achivement1 = pygame.mixer.Sound(path_snd_achiv1)
snd_shoot = pygame.mixer.Sound(path_snd_shoot)
bgm_oldoffice = pygame.mixer.Sound(path_bgm_old_office)

font = pygame.font.Font("pixel_font.ttf", 72)
medium_font = pygame.font.Font("pixel_font.ttf", 32)
small_font = pygame.font.Font("pixel_font.ttf", 16)

leveldict_collis_test = {
    "1-1": "", "1-2": "", "1-3": "", "1-4": "", "1-5": "",
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
    "7-1": "", "7-2": "enemy1_10", "7-3": "", "7-4": "", "7-5": ""
}

leveldict_new = leveldict_collis_test.copy()
leveldict = leveldict_new.copy()



def refresh(left, middle, right, left_diag, right_diag, hp, ammo, state, wpn):
    sc.fill(BLACK)
    drawScreen(left, middle, right,left_diag,right_diag)
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
            "5-1": "", "5-2": "", "5-3": "enemy1_10", "5-4": "wall", "5-5": "",
            "6-1": "", "6-2": "bullets", "6-3": "bullets", "6-4": "wall", "6-5": "",
            "7-1": "wall", "7-2": "wall", "7-3": "wall", "7-4": "wall", "7-5": "",
            "8-1": "wall", "8-2": "wall", "8-3": "medkit", "8-4": "", "8-5": "",
            "9-1": "wall", "9-2": "wall", "9-3": "wall", "9-4": "wall", "9-5": ""
        }
    elif chunk_id == 1:
        chunk = {
            "1-1": "", "1-2": "", "1-3": "", "1-4": "", "1-5": "",
            "2-1": "", "2-2": "", "2-3": "", "2-4": "", "2-5": "",
            "3-1": "", "3-2": "", "3-3": "enemy1_10", "3-4": "", "3-5": "",
            "4-1": "", "4-2": "wall", "4-3": "wall", "4-4": "wall", "4-5": "",
            "5-1": "", "5-2": "", "5-3": "medkit", "5-4": "", "5-5": "",
            "6-1": "", "6-2": "", "6-3": "", "6-4": "", "6-5": "",
            "7-1": "wall", "7-2": "wall", "7-3": "", "7-4": "wall", "7-5": "wall"
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
            "5-1": "", "5-2": "", "5-3": "boss_25", "5-4": "", "5-5": "",
            "6-1": "", "6-2": "", "6-3": "", "6-4": "", "6-5": "",
            "7-1": "", "7-2": "", "7-3": "", "7-4": "", "7-5": ""
        }
    elif chunk_id == 4:
        chunk = {
            "1-1": "", "1-2": "", "1-3": "", "1-4": "", "1-5": "",
            "2-1": "", "2-2": "", "2-3": "", "2-4": "", "2-5": "",
            "3-1": "bullets", "3-2": "wall", "3-3": "wall", "3-4": "wall", "3-5": "wall",
            "4-1": "", "4-2": "", "4-3": "", "4-4": "", "4-5": "",
            "5-1": "", "5-2": "", "5-3": "enemy1_10", "5-4": "wall", "5-5": "",
            "6-1": "", "6-2": "bullets", "6-3": "bullets", "6-4": "wall", "6-5": "",
            "7-1": "wall", "7-2": "wall", "7-3": "wall", "7-4": "wall", "7-5": ""
        }
    elif chunk_id == 5:
        chunk = {
            "1-1": "", "1-2": "", "1-3": "", "1-4": "", "1-5": "",
            "2-1": "", "2-2": "", "2-3": "", "2-4": "", "2-5": "",
            "3-1": "", "3-2": "", "3-3": "enemy2_15", "3-4": "", "3-5": "",
            "4-1": "", "4-2": "wall", "4-3": "wall", "4-4": "wall", "4-5": "",
            "5-1": "", "5-2": "", "5-3": "medkit", "5-4": "", "5-5": "",
            "6-1": "", "6-2": "", "6-3": "", "6-4": "", "6-5": "",
            "7-1": "wall", "7-2": "wall", "7-3": "", "7-4": "wall", "7-5": "wall"
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
    left_diag = ""
    middle = ""
    right_diag = ""
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
        try:
            middle = lvldict[coords]
        except:
            pass
        coords = str(y + 1) + "-" + str(x - 1)
        try:
            if lvldict[coords] == "wall":
                left_diag = "wall2"
            else:
                left_diag = lvldict[coords]
        except:
            pass

        coords = str(y + 1) + "-" + str(x + 1)
        try:
            if lvldict[coords] == "wall":
                right_diag = "wall2"
            else:
                right_diag = lvldict[coords]
        except:
            pass        
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
        if (y - 1) != 0 and (x + 1) != 6:
            if lvldict[coords] == "wall":
                left_diag = "wall2"
            else:
                left_diag = lvldict[coords]
        elif (y - 1) == 0 and left == "" or (x + 1) == 6:
            left = "wall2"
        coords = str(y - 1) + "-" + str(x - 1)
        if (y - 1) != 0 and (x - 1) != 0:
            if lvldict[coords] == "wall":
                right_diag = "wall2"
            else:
                right_diag = lvldict[coords]
        elif (y - 1) == 0 or (x - 1) == 0:
            right_diag = "wall2"
    elif direction == 0:
        coords = str(y + 1) + "-" + str(x)
        try:
            left = leveldict[coords]
        except:
            pass
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
        try:
            if lvldict[coords] == "wall":
                left_diag = "wall2"
            elif (x + 1) == 6:
                left_diag = "wall2"            
            else:
                left_diag = lvldict[coords]
        except:
            pass
        coords = str(y - 1) + "-" + str(x + 1)
        if (x + 1) != 6 and (y - 1) != 0:
            if lvldict[coords] == "wall":
                right_diag = "wall2"
            else:
                right_diag = lvldict[coords]
        elif (y - 1) == 0 or (x + 1) == 6:
            right_diag = "wall2"
    elif direction == 2:
        coords = str(y - 1) + "-" + str(x)
        if (y - 1) != 0:
            left = leveldict[coords]
        else:
            left = "wall"
        coords = str(y + 1) + "-" + str(x)
        try:
            right = leveldict[coords]
        except:
            pass
        coords = str(y) + "-" + str(x - 1)
        if (x - 1) != 0:
            middle = leveldict[coords]
        else:
            middle = "wall"
        coords = str(y + 1) + "-" + str(x - 1)
        try:
            if lvldict[coords] == "wall":
                right_diag = "wall2"
            elif (y + 1) == 8 and right == "" or (x - 1) == 0:
                right_diag = "wall2"            
            else:
                right_diag = lvldict[coords]
        except:
            pass
        coords = str(y - 1) + "-" + str(x - 1)
        if (x - 1) != 0 and (y - 1) != 0:
            if lvldict[coords] == "wall":
                left_diag = "wall2"
            else:
                left_diag = lvldict[coords]
        elif (y - 1) == 0 or (x - 1) == 0:
            left_diag = "wall2"

    else:
        pass
    return left, middle, right,left_diag,right_diag


def drawScreen(left, middle, right,left_diag,right_diag):
    sc.blit(pygame.transform.scale(image_floor, (300 * SIZE, 150 * SIZE)), (0*SIZE + indent_horizontal, 150*SIZE))
    if left_diag == "wall":
        sc.blit(pygame.transform.scale(image_wall_l, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left_diag == "wall2":
        sc.blit(pygame.transform.scale(image_wall_2, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left_diag == "bullets":
        sc.blit(pygame.transform.scale(image_bullets, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))
    elif left_diag == "medkit":
        sc.blit(pygame.transform.scale(image_medkit, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal,25 * SIZE))
    elif left_diag == "knife_pickup":
        sc.blit(pygame.transform.scale(image_knife_sprite, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))        
    elif "enemy1" in left_diag and not("corpse" in left_diag):
        sc.blit(pygame.transform.scale(image_enemy1, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))
    elif "enemy1_atk" in left_diag:
        sc.blit(pygame.transform.scale(image_enemy1_atk, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))        
    elif left_diag == "enemy1_corpse_0":
        sc.blit(pygame.transform.scale(image_enemy1_corpse0, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))
    elif left_diag == "enemy1_corpse_1":
        sc.blit(pygame.transform.scale(image_enemy1_corpse1, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))
    elif left_diag == "enemy1_corpse_2":
        sc.blit(pygame.transform.scale(image_enemy1_corpse2, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))
    elif left_diag == "enemy1_corpse_3":
        sc.blit(pygame.transform.scale(image_enemy1_corpse3, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))
    elif "enemy2" in left_diag and not("corpse" in left_diag):
        sc.blit(pygame.transform.scale(image_enemy2, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))
    elif "enemy2_atk" in left_diag:
        sc.blit(pygame.transform.scale(image_enemy2_atk, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))        
    elif left_diag == "enemy2_corpse_0":
        sc.blit(pygame.transform.scale(image_enemy2_corpse0, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))
    elif left_diag == "enemy2_corpse_1":
        sc.blit(pygame.transform.scale(image_enemy2_corpse1, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))
    elif left_diag == "enemy2_corpse_2":
        sc.blit(pygame.transform.scale(image_enemy2_corpse2, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))
    elif left_diag == "enemy2_corpse_3":
        sc.blit(pygame.transform.scale(image_enemy2_corpse3, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))
    elif "boss" in left_diag and not("corpse" in left_diag):
        sc.blit(pygame.transform.scale(image_boss, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))
    elif "boss_atk" in left_diag:
        sc.blit(pygame.transform.scale(image_boss_atk, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))    
    elif left_diag == "boss_corpse_0":
        sc.blit(pygame.transform.scale(image_boss_corpse0, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))
    elif left_diag == "boss_corpse_1":
        sc.blit(pygame.transform.scale(image_boss_corpse1, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))
    elif left_diag == "boss_corpse_2":
        sc.blit(pygame.transform.scale(image_boss_corpse2, (50 * SIZE, 150 * SIZE)), (25 * SIZE + indent_horizontal, 25 * SIZE))    
    if left == "wall":
        sc.blit(pygame.transform.scale(image_wall_l, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "wall2":
        sc.blit(pygame.transform.scale(image_wall_2, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "bullets":
        sc.blit(pygame.transform.scale(image_bullets, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "medkit":
        sc.blit(pygame.transform.scale(image_medkit, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "knife_pickup":
        sc.blit(pygame.transform.scale(image_knife_sprite, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))        
    elif "enemy1" in left and not("corpse" in left):
        sc.blit(pygame.transform.scale(image_enemy1, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif "enemy1_atk" in left:
        sc.blit(pygame.transform.scale(image_enemy1_atk, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))        
    elif left == "enemy1_corpse_0":
        sc.blit(pygame.transform.scale(image_enemy1_corpse0, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy1_corpse_1":
        sc.blit(pygame.transform.scale(image_enemy1_corpse1, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy1_corpse_2":
        sc.blit(pygame.transform.scale(image_enemy1_corpse2, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy1_corpse_3":
        sc.blit(pygame.transform.scale(image_enemy1_corpse3, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif "enemy2" in left and not("corpse" in left):
        sc.blit(pygame.transform.scale(image_enemy2, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif "enemy2_atk" in left:
        sc.blit(pygame.transform.scale(image_enemy2_atk, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))        
    elif left == "enemy2_corpse_0":
        sc.blit(pygame.transform.scale(image_enemy2_corpse0, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy2_corpse_1":
        sc.blit(pygame.transform.scale(image_enemy2_corpse1, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy2_corpse_2":
        sc.blit(pygame.transform.scale(image_enemy2_corpse2, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "enemy2_corpse_3":
        sc.blit(pygame.transform.scale(image_enemy2_corpse3, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif "boss" in left and not("corpse" in left):
        sc.blit(pygame.transform.scale(image_boss, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif "boss_atk" in left:
        sc.blit(pygame.transform.scale(image_boss_atk, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))    
    elif left == "boss_corpse_0":
        sc.blit(pygame.transform.scale(image_boss_corpse0, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "boss_corpse_1":
        sc.blit(pygame.transform.scale(image_boss_corpse1, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    elif left == "boss_corpse_2":
        sc.blit(pygame.transform.scale(image_boss_corpse2, (100 * SIZE, 300 * SIZE)), (0 + indent_horizontal, 0))
    if right_diag == "wall":
        sc.blit(pygame.transform.scale(image_wall_r, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif right_diag == "wall2":
        sc.blit(pygame.transform.scale(image_wall_2, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif right_diag == "bullets":
        sc.blit(pygame.transform.scale(image_bullets, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))
    elif right_diag == "medkit":
        sc.blit(pygame.transform.scale(image_medkit, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal,25 * SIZE))
    elif right_diag == "knife_pickup":
        sc.blit(pygame.transform.scale(image_knife_sprite, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))        
    elif "enemy1" in right_diag and not("corpse" in right_diag):
        sc.blit(pygame.transform.scale(image_enemy1, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))
    elif "enemy1_atk" in right_diag:
        sc.blit(pygame.transform.scale(image_enemy1_atk, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))        
    elif right_diag == "enemy1_corpse_0":
        sc.blit(pygame.transform.scale(image_enemy1_corpse0, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))
    elif right_diag == "enemy1_corpse_1":
        sc.blit(pygame.transform.scale(image_enemy1_corpse1, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))
    elif right_diag == "enemy1_corpse_2":
        sc.blit(pygame.transform.scale(image_enemy1_corpse2, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))
    elif right_diag == "enemy1_corpse_3":
        sc.blit(pygame.transform.scale(image_enemy1_corpse3, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))
    elif "enemy2" in right_diag and not("corpse" in right_diag):
        sc.blit(pygame.transform.scale(image_enemy2, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))
    elif "enemy2_atk" in right_diag:
        sc.blit(pygame.transform.scale(image_enemy2_atk, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))        
    elif right_diag == "enemy2_corpse_0":
        sc.blit(pygame.transform.scale(image_enemy2_corpse0, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))
    elif right_diag == "enemy2_corpse_1":
        sc.blit(pygame.transform.scale(image_enemy2_corpse1, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))
    elif right_diag == "enemy2_corpse_2":
        sc.blit(pygame.transform.scale(image_enemy2_corpse2, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))
    elif right_diag == "enemy2_corpse_3":
        sc.blit(pygame.transform.scale(image_enemy2_corpse3, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))
    elif "boss" in right_diag and not("corpse" in right_diag):
        sc.blit(pygame.transform.scale(image_boss, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))
    elif "boss_atk" in right_diag:
        sc.blit(pygame.transform.scale(image_boss_atk, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))    
    elif right_diag == "boss_corpse_0":
        sc.blit(pygame.transform.scale(image_boss_corpse0, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))
    elif right_diag == "boss_corpse_1":
        sc.blit(pygame.transform.scale(image_boss_corpse1, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))
    elif right_diag == "boss_corpse_2":
        sc.blit(pygame.transform.scale(image_boss_corpse2, (50 * SIZE, 150 * SIZE)), (225 * SIZE + indent_horizontal, 25 * SIZE))     
    if right == "wall":
        sc.blit(pygame.transform.scale(image_wall_r, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif right == "wall2":
        sc.blit(pygame.transform.scale(image_wall_2, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif right == "bullets":
        sc.blit(pygame.transform.scale(image_bullets, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif right == "medkit":
        sc.blit(pygame.transform.scale(image_medkit, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif right == "knife_pickup":
        sc.blit(pygame.transform.scale(image_knife_sprite, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))    
    elif "enemy1" in right and not("corpse" in right):
        sc.blit(pygame.transform.scale(image_enemy1, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif "enemy1_atk" in right:
        sc.blit(pygame.transform.scale(image_enemy1_atk, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))    
    elif right == "enemy1_corpse_0":
        sc.blit(pygame.transform.scale(image_enemy1_corpse0, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "enemy1_corpse_1":
        sc.blit(pygame.transform.scale(image_enemy1_corpse1, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "enemy1_corpse_2":
        sc.blit(pygame.transform.scale(image_enemy1_corpse2, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "enemy1_corpse_3":
        sc.blit(pygame.transform.scale(image_enemy1_corpse3, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif "enemy2" in right and not("corpse" in right):
        sc.blit(pygame.transform.scale(image_enemy2, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif "enemy2_atk" in right:
        sc.blit(pygame.transform.scale(image_enemy2_atk, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))    
    elif right == "enemy2_corpse_0":
        sc.blit(pygame.transform.scale(image_enemy2_corpse0, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "enemy2_corpse_1":
        sc.blit(pygame.transform.scale(image_enemy2_corpse1, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "enemy2_corpse_2":
        sc.blit(pygame.transform.scale(image_enemy2_corpse2, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "enemy2_corpse_3":
        sc.blit(pygame.transform.scale(image_enemy2_corpse3, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif "boss" in right and not("corpse" in right):
        sc.blit(pygame.transform.scale(image_boss, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))
    elif "boss_atk" in right:
        sc.blit(pygame.transform.scale(image_boss_atk, (100 * SIZE, 300 * SIZE)), (200 * SIZE + indent_horizontal, 0))    
    elif right == "boss_corpse_0":
        sc.blit(pygame.transform.scale(image_boss_corpse0, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "boss_corpse_1":
        sc.blit(pygame.transform.scale(image_boss_corpse1, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    elif right == "boss_corpse_2":
        sc.blit(pygame.transform.scale(image_boss_corpse2, (100 * SIZE, 300 * SIZE)), (200*SIZE + indent_horizontal, 0))
    if middle == "wall2" or middle == "wall":
        sc.blit(pygame.transform.scale(image_wall_2, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "medkit":
        sc.blit(pygame.transform.scale(image_medkit, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "knife_pickup":
        sc.blit(pygame.transform.scale(image_knife_sprite, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))    
    elif middle == "bullets":
        sc.blit(pygame.transform.scale(image_bullets, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif "enemy1" in middle and not("corpse" in middle):
        sc.blit(pygame.transform.scale(image_enemy1, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif "enemy1_atk" in middle:
        sc.blit(pygame.transform.scale(image_enemy1_atk, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))    
    elif middle == "enemy1_corpse_0":
        sc.blit(pygame.transform.scale(image_enemy1_corpse0, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy1_corpse_1":
        sc.blit(pygame.transform.scale(image_enemy1_corpse1, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy1_corpse_2":
        sc.blit(pygame.transform.scale(image_enemy1_corpse2, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy1_corpse_3":
        sc.blit(pygame.transform.scale(image_enemy1_corpse3, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif "enemy2" in middle and not("corpse" in middle):
        sc.blit(pygame.transform.scale(image_enemy2, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif "enemy2_atk" in middle:
        sc.blit(pygame.transform.scale(image_enemy2_atk, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))        
    elif middle == "enemy2_corpse_0":
        sc.blit(pygame.transform.scale(image_enemy2_corpse0, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy2_corpse_1":
        sc.blit(pygame.transform.scale(image_enemy2_corpse1, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy2_corpse_2":
        sc.blit(pygame.transform.scale(image_enemy2_corpse2, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif middle == "enemy2_corpse_3":
        sc.blit(pygame.transform.scale(image_enemy2_corpse3, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif "boss" in middle and not("corpse" in middle):
        sc.blit(pygame.transform.scale(image_boss, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))
    elif "boss_atk" in middle:
        sc.blit(pygame.transform.scale(image_boss_atk, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, 0))    
    elif middle == "boss_corpse_0":
        sc.blit(pygame.transform.scale(image_boss_corpse0, (100 * SIZE, 300 * SIZE)), (100*SIZE + indent_horizontal, 0))
    elif middle == "boss_corpse_1":
        sc.blit(pygame.transform.scale(image_boss_corpse1, (100 * SIZE, 300 * SIZE)), (100*SIZE + indent_horizontal, 0))
    elif middle == "boss_corpse_2":
        sc.blit(pygame.transform.scale(image_boss_corpse2, (100 * SIZE, 300 * SIZE)), (100*SIZE + indent_horizontal, 0))


def drawWeapon(state, weapon):
    if weapon == "fist":
        if state == "idle":
            sc.blit(pygame.transform.scale(image_hand, (100 * SIZE, 300 * SIZE)), (125 * SIZE + indent_horizontal, 0))
        elif state == "attack":
            sc.blit(pygame.transform.scale(image_hand, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, -10 * SIZE))
    elif weapon == "pistol":
        if state == "idle":
            sc.blit(pygame.transform.scale(image_lightgun_idle, (100 * SIZE, 300 * SIZE)), (125 * SIZE + indent_horizontal, 0))
        elif state == "attack":
            sc.blit(pygame.transform.scale(image_lightgun_atk, (100 * SIZE, 300 * SIZE)), (125 * SIZE + indent_horizontal, 0))
    elif weapon == "knife":
        if state == "idle":
            sc.blit(pygame.transform.scale(image_kinfe, (100 * SIZE, 300 * SIZE)), (125 * SIZE + indent_horizontal, -10 * SIZE))
        elif state == "attack":
            sc.blit(pygame.transform.scale(image_kinfe, (100 * SIZE, 300 * SIZE)), (100 * SIZE + indent_horizontal, -30 * SIZE))


def showAchivement(name,image):
    sc.blit(pygame.transform.scale(image, (30 * SIZE, 30 * SIZE)), (0 * SIZE + indent_horizontal, 0* SIZE))
    achivement_text = font.render(name, 1, WHITE)
    sc.blit(achivement_text, [SIZE * 35 + indent_horizontal, SIZE * 10])
    
def drawHUD(hp, ammo, lastact):
    sc.blit(pygame.transform.scale(image_statusbar, (300 * SIZE, 30 * SIZE)), (0 * SIZE + indent_horizontal, 270* SIZE))
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
no_beautiful_debug = False
sc = pygame.display.set_mode((infoObject.current_w, SIZE * 300), pygame.FULLSCREEN)
for argument in arguments:
    if "no-debug" in argument:
        no_beautiful_debug = True
    elif "window-mode" in argument:
        indent_horizontal = 0
        SIZE = 2
        sc = pygame.display.set_mode((SIZE*300, SIZE * 300))
        font = pygame.font.Font("pixel_font.ttf", 40)
        small_font = pygame.font.Font("pixel_font.ttf", 8)
  
while 1:
    if last_key == "up":
        if mode == "game":
            turn = "enemy"
            disp_left, disp_middle, disp_right,disp_left_diag,disp_right_diag = look(x, y, direction, leveldict)
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
                    coords = str(y+1) + "-" + str(x)                   
                    try:
                        spare_string = leveldict[coords]
                        y += 1
                    except:
                        if not(is_custom_level):
                            y = 1
                            leveldict = generate_chunk()                  
                        elif is_custom_level:
                            mode = "title"
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
        elif mode == "title":
            if option == 0:
                option = 1
            else:
                option -= 1            
    if last_key == "down":
                    if mode == "game":
                        turn = "enemy"
                        if y - 1 != 0:
                            disp_left, disp_middle, disp_right,disp_left_diag,disp_right_diag = look(x, y - 1, direction, leveldict)
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
                                    try:
                                        coords = str(y + 1) + "-" + str(x)
                                        a = leveldict[coords]
                                        y += 1
                                    except:
                                        y = 1
                                        leveldict = generate_chunk()
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
                    elif mode == "title":
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
            right, middle, left,disp_left_diag,disp_right_diag = look(x, y, direction, leveldict)
            if current_weapon == "fist":
                damage = randint(4, 11)
                weapon_action = "attack"
            elif current_weapon == "pistol":
                if ammo != 0:
                    snd_shoot.play()
                    weapon_action = "attack"
                    damage = randint(6, 15)
                    ammo -= 1
            elif current_weapon == "knife":
                weapon_action = "attack"
                damage = 100
                snd_knife_slash.play()
            if direction == 0:
                coords = str(y) + "-" + str(x + 1)
            elif direction == 1:
                coords = str(y + 1) + "-" + str(x)
            elif direction == 2:
                coords = str(y) + "-" + str(x - 1)
            elif direction == 3:
                coords = str(y - 1) + "-" + str(x)
            if "enemy1" in middle and not("corpse" in middle)  or "enemy2" in middle and not("corpse" in middle) or "boss" in middle and not("corpse" in middle):
                enemy_tile_contents = leveldict[coords]
                length_text = len(enemy_tile_contents)
                enemy_hp = int(enemy_tile_contents[length_text -2 :]) 
                enemy_hp -= damage
                stringed_enemy_hp = str(enemy_hp)
                if len(stringed_enemy_hp) == 1:
                    enemy_hp = "0" + str(enemy_hp)
                if int(enemy_hp) <= 0:
                    end_of_read = length_text-2
                    length_text = len(enemy_tile_contents)
                    leveldict[coords] =  enemy_tile_contents[0:end_of_read] + "corpse_0"
                    tick = 0
                else:
                    length_text = len(enemy_tile_contents)
                    end_of_read = length_text-2
                    enemy_tile_contents = enemy_tile_contents[0:end_of_read]
                    enemy_tile_contents = enemy_tile_contents + str(enemy_hp)
                    leveldict[coords] = enemy_tile_contents
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
            bgm_oldoffice.play(-1)


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
            option = 0
            mode = "game"
        elif mode == "title":
            if option == 0:
                mode = "game"
                health = 100
                ammo = 5
                x = 3
                y = 1
                direction = 1
                leveldict_new = leveldict_collis_test.copy()
                leveldict = leveldict_new.copy()
                turn = "player"
                bgm_oldoffice.play(-1)
                is_custom_level = False
            elif option == 1:
                mode ="custom_level"
        elif mode == "game_over":
    
            mode = "title"
    if has_knife == True and achivement1 != True:
            sound_achivemment1.play()
    if mode == "game":
        disp_left, disp_middle, disp_right,disp_left_diag,disp_right_diag = look(x, y, direction, leveldict)
        refresh(disp_left, disp_middle, disp_right,disp_left_diag,disp_right_diag, health, ammo, weapon_action, current_weapon) 
        if has_knife == True and achivement1 != True:
            showAchivement("Genocide",image_achiv1)       
            todo = "achivement1"
    elif mode == "game_over":
        pygame.mixer.music.pause()
        disp_left, disp_middle, disp_right,disp_left_diag,disp_right_diag = look(x, y, direction, leveldict)
        refresh(disp_left, disp_middle, disp_right,disp_left_diag,disp_right_diag, health, ammo, weapon_action, current_weapon) 
        if useLocalization:
            text = font.render(text_localization[10], 1, RED)
            sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 5])
            text = font.render(text_localization[11], 1, RED)
            sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 25])
            text = font.render(text_localization[12], 1, RED)
            sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 45])            
        else:
            text = font.render("You died!", 1, RED)
            sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 5])
            text = font.render("[Enter] to quit to tilte.", 1, RED)
            sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 25])
            text = font.render("[Space] to respawn.", 1, RED)
            sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 45])            
    elif mode == "title":
        sc.fill(BLACK)
        sc.blit(pygame.transform.scale(image_title, (84 * SIZE, 84 * SIZE)), (110* SIZE + indent_horizontal, 15* SIZE))
        text = font.render("Compystein 3-D", 1, GREEN)
        sc.blit(text, [indent_horizontal + SIZE * 60, SIZE * 55])            
        if option == 0:
            if not(useLocalization):
                text = font.render(">Singlepayer", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 120])
                text = font.render("Custom levels", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 140])  
            else:
                text = font.render(text_localization[2], 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 120])
                text = font.render(text_localization[1], 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 140])                  
        elif option == 1:
            if not(useLocalization):
                text = font.render("Singlepayer", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 120])
                text = font.render(">Custom levels", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 140])  
            else:
                text = font.render(text_localization[0], 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 120])
                text = font.render(text_localization[3], 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 140])              
        text = small_font.render("Copyright 2020 Alphen95(Luigi180059)", 1, WHITE)
        sc.blit(text, [indent_horizontal + SIZE * 100, SIZE * 240])   
        text = font.render("hotfix 1.1", 1, RED)
        text =pygame.transform.rotate(text, 14)
        sc.blit(text, [indent_horizontal + SIZE * 120, SIZE * 60])            
    elif mode == "help":
        sc.fill(GRAY)
        if useLocalization:
            text = font.render(text_localization[4], 1, GREEN)
            sc.blit(text, [indent_horizontal + SIZE * 40, SIZE * 30])
            text = font.render(text_localization[5], 1, GREEN)
            sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 65])
            text = font.render(text_localization[6], 1, GREEN)
            sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 85])
            text = font.render(text_localization[7], 1, GREEN)
            sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 105])
            text = font.render(text_localization[8], 1, GREEN)
            sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 125])
            text = font.render(text_localization[9], 1, GREEN)
            sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 145])   
        else:
            text = font.render("Compystein 3-D Help", 1, GREEN)
            sc.blit(text, [indent_horizontal + SIZE * 40, SIZE * 30])
            text = font.render("Walk : arrow keys", 1, GREEN)
            sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 65])
            text = font.render("Attack : [space]", 1, GREEN)
            sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 85])
            text = font.render("Debug menu : [D]", 1, GREEN)
            sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 105])
            text = font.render("Menu cofirm : [Enter]", 1, GREEN)
            sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 125])
            text = font.render("Leave game : [Q]", 1, GREEN)
            sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 145])  
    elif mode == "map":
        sc.fill(GRAY)
        text = font.render("Level map", 1, GREEN)
        sc.blit(text, [indent_horizontal + SIZE * 50, SIZE * 10])
        for i in range(y-2,y+3):
            for i1 in range(5,0,-1):
                if i1 == 5:
                    tile = str(i)+"-"+str(1)
                elif i1 == 4:
                    tile = str(i)+"-"+str(2)
                elif i1 == 3:
                    tile = str(i)+"-"+str(3)
                elif i1 == 2:
                    tile = str(i)+"-"+str(4)
                elif i1 == 1:
                    tile = str(i)+"-"+str(5)            
                print("tile",tile)
                if i >=1:
                    tile_contents = leveldict[tile]
                    if tile_contents == "wall":
                        sc.blit(pygame.transform.scale(image_wall, (60 * SIZE, 60 * SIZE)), (indent_horizontal+((i1*60-60)*SIZE), indent_horizontal+(((i*60)-60)*SIZE)))
                
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
    elif mode == "custom_level":
        sc.fill(BLACK)
        if useLocalization:
            text = font.render(text_localization[13], 1, WHITE)
            sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 80])   
        else:
            text = font.render("Enter file name for custom level:", 1, WHITE)
            sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 80])
        text = font.render(path_custom_level, 1, WHITE)
        sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 100])            
    for specialtile in specialtiles:
        spare_string = specialtile[1]
        leveldict[specialtile[0]] =spare_string
    specialtiles = []
    pygame.display.update()
    pygame.time.delay(100)
    tick += 1
    last_key = ""
    if turn != "player":
        turn = "player"
        for tile in leveldict:
            if "enemy1" in leveldict[tile] and not("corpse" in leveldict[tile]) or "enemy2" in leveldict[tile] and not("corpse" in leveldict[tile]) or "boss" in leveldict[tile] and not("corpse" in leveldict[tile]):
                spare_string = tile[2:3]
                enemy_X = int(spare_string)
                spare_string = tile[:1]
                enemy_Y = int(spare_string)
                if enemy_X + 1 == x and enemy_Y == y or enemy_X - 1 == x and enemy_Y == y or enemy_X == x and enemy_Y + 1 == y or enemy_X == x and enemy_Y - 1 == y :
                    if "enemy1" in leveldict[tile]:
                        damage = randint(1, 6)
                    elif "enemy2" in leveldict[tile]:
                        damage = randint(3, 10)
                    elif "boss" in leveldict[tile]:
                        damage = randint(7, 16)
                    health = health - damage                        
                    spare_string = str(leveldict[tile])
                    leveldict[tile] = leveldict[tile] +"_atk"
                    tup_args = (tile,spare_string)
                    specialtiles.append(tup_args)
                    damage = 0
                    if health < 1:
                        mode = "game_over"
                else:
                    side = randint(0, 3)
                    right, middle, left,disp_left_diag,disp_right_diag = look(enemy_X, enemy_Y, side, leveldict)
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quitted = True
                sys.exit()
                break
            elif event.key == pygame.K_d and mode != "custom_level":
                last_key = "d"
            elif event.key == pygame.K_h and mode != "custom_level":
                last_key = "h"
            elif event.key == pygame.K_UP and mode != "custom_level":
                last_key = "up"
            elif event.key == pygame.K_LEFT and mode != "custom_level":
                last_key = "left"
            elif event.key == pygame.K_RIGHT and mode != "custom_level":
                last_key = "right"
            elif event.key == pygame.K_DOWN and mode != "custom_level":
                last_key = "down"
            elif event.key == pygame.K_SPACE and mode != "custom_level":
                last_key = "space"
            elif event.key == pygame.K_RETURN and mode != "custom_level":
                last_key = "confirm"
            elif event.key == pygame.K_1 and mode != "custom_level":
                last_key = "1"
            elif event.key == pygame.K_2 and mode != "custom_level":
                last_key = "2"
            elif event.key == pygame.K_3 and mode != "custom_level":
                last_key = "3"
            elif event.key == pygame.K_ESCAPE and mode == "custom_level":
                mode = "title"
            elif event.key == pygame.K_TAB and mode == "game":
                mode = "map"
                print("a")
            elif event.key == pygame.K_TAB and mode == "map":
                mode = "game"                
            elif event.key == pygame.K_BACKSPACE and mode == "custom_level" or event.key == pygame.K_DELETE and mode == "custom_level":
                path_custom_level = path_custom_level[:-1]
            elif event.key == pygame.K_RETURN and mode == "custom_level":
                try:
                    path_custom_level = path_custom_level + ".json"
                    with open(path_custom_level,mode="r") as customlevel_file:
                        leveldict = json.loads(customlevel_file.read())
                    mode = "game"
                    health = 100
                    ammo = 5
                    x = 3
                    y = 1
                    direction = 1
                    turn = "player"
                    bgm_oldoffice.play(-1)
                    is_custom_level = True
                except:
                    pass
            elif mode == "custom_level":
                path_custom_level += event.unicode
                     
