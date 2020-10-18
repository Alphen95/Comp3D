import pygame
from random import randint
from pprint import pprint

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
SIZE = 3
health = 0

infoObject = pygame.display.Info()
pygame.display.set_caption('Compystein 3-D ALPHA')
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
direction = 1
todo = ""
health = 100
ammo = 0
mode = "title"
screen = 0
option = 0

font = pygame.font.Font("pixel_font.ttf", 72)

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
    "7-1": "", "7-2": "enemy1", "7-3": "", "7-4": "", "7-5": "", "health_enemy": 10
}

leveldict_new = leveldict_collis_test.copy()
leveldict = leveldict_new.copy()



def refresh(left, middle, right, hp, ammo, state, wpn):
    sc.fill(BLACK)
    drawScreen(left, middle, right)
    drawWeapon(state, wpn)
    drawHUD(hp, ammo, "uwu")


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
        pygame.draw.polygon(sc, NAVY, [[0 + indent_horizontal, 0], [SIZE * 100 + indent_horizontal, SIZE * 100], [SIZE * 100 + indent_horizontal, SIZE * 200], [0 + indent_horizontal, SIZE * 300]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 2 + indent_horizontal, SIZE * 5], [SIZE * 97 + indent_horizontal, SIZE * 102], [SIZE * 97 + indent_horizontal, SIZE * 197], [SIZE * 2 + indent_horizontal, SIZE * 295]], 3)
    elif left == "wall2":
        pygame.draw.polygon(sc, NAVY, [[0 + indent_horizontal, SIZE * 100], [SIZE * 100 + indent_horizontal, SIZE * 100], [SIZE * 100 + indent_horizontal, SIZE * 200], [0 + indent_horizontal, SIZE * 200]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 5 + indent_horizontal, SIZE * 105], [SIZE * 95 + indent_horizontal, SIZE * 105], [SIZE * 95 + indent_horizontal, SIZE * 195], [SIZE * 5 + indent_horizontal, SIZE * 195]], 3)
    elif left == "bullets":
        pygame.draw.polygon(sc, LIGHTYELLOW, [[SIZE * 35 + indent_horizontal, SIZE * 135], [SIZE * 40 + indent_horizontal, SIZE * 130], [SIZE * 45 + indent_horizontal, SIZE * 135], [SIZE * 45 + indent_horizontal, SIZE * 160], [SIZE * 35 + indent_horizontal, SIZE * 160]])
        pygame.draw.polygon(sc, LIGHTYELLOW, [[SIZE * 55 + indent_horizontal, SIZE * 135], [SIZE * 60 + indent_horizontal, SIZE * 130], [SIZE * 65 + indent_horizontal, SIZE * 135], [SIZE * 65 + indent_horizontal, SIZE * 160], [SIZE * 55 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, YELLOW, True, [[SIZE * 35 + indent_horizontal, SIZE * 137], [SIZE * 45 + indent_horizontal, SIZE * 137]], 5)
        pygame.draw.lines(sc, YELLOW, True, [[SIZE * 55 + indent_horizontal, SIZE * 137], [SIZE * 65 + indent_horizontal, SIZE * 137]], 5)

    elif left == "medkit":
        pygame.draw.polygon(sc, MEDKIT, [[SIZE * 10 + indent_horizontal, SIZE * 110], [SIZE * 90 + indent_horizontal, SIZE * 110], [SIZE * 90 + indent_horizontal, SIZE * 190], [SIZE * 10 + indent_horizontal, SIZE * 190]])
        pygame.draw.rect(sc, WHITE, (SIZE * 11 + indent_horizontal, SIZE * 110, SIZE * 78, SIZE * 26), 8)
        pygame.draw.polygon(sc, RED, [[SIZE * 20 + indent_horizontal, SIZE * 145], [SIZE * 45 + indent_horizontal, SIZE * 145], [SIZE * 45 + indent_horizontal, SIZE * 120], [SIZE * 55 + indent_horizontal, SIZE * 120], [SIZE * 55 + indent_horizontal, SIZE * 145], [SIZE * 80 + indent_horizontal, SIZE * 145], [SIZE * 80 + indent_horizontal, SIZE * 155], [SIZE * 80 + indent_horizontal, SIZE * 155], [SIZE * 55 + indent_horizontal, SIZE * 155], [SIZE * 55 + indent_horizontal, SIZE * 180], [SIZE * 45 + indent_horizontal, SIZE * 180], [SIZE * 45 + indent_horizontal, SIZE * 155], [SIZE * 20 + indent_horizontal, SIZE * 155]])
    elif left == "enemy1":
        pygame.draw.polygon(sc, WHITE, [[SIZE * 5 + indent_horizontal, SIZE * 5], [SIZE * 95 + indent_horizontal, SIZE * 5], [SIZE * 95 + indent_horizontal, SIZE * 95], [SIZE * 5 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 15 + indent_horizontal, SIZE * 15], [SIZE * 85 + indent_horizontal, SIZE * 15], [SIZE * 85 + indent_horizontal, SIZE * 85], [SIZE * 15 + indent_horizontal, SIZE * 85]])
        pygame.draw.rect(sc, GREEN, (SIZE * 30 + indent_horizontal, SIZE * 30, SIZE * 10, SIZE * 20))
        pygame.draw.rect(sc, GREEN, (SIZE * 60 + indent_horizontal, SIZE * 30, SIZE * 10, SIZE * 20))
        pygame.draw.polygon(sc, DARK_GREEN, [[SIZE * 25 + indent_horizontal, SIZE * 25], [SIZE * 45 + indent_horizontal, SIZE * 30], [SIZE * 45 + indent_horizontal, SIZE * 40], [SIZE * 25 + indent_horizontal, SIZE * 35]])
        pygame.draw.polygon(sc, DARK_GREEN, [[SIZE * 55 + indent_horizontal, SIZE * 40], [SIZE * 75 + indent_horizontal, SIZE * 35], [SIZE * 75 + indent_horizontal, SIZE * 25], [SIZE * 55 + indent_horizontal, SIZE * 30]])
        pygame.draw.polygon(sc, GREEN, [[SIZE * 35 + indent_horizontal, SIZE * 70], [SIZE * 45 + indent_horizontal, SIZE * 65], [SIZE * 55 + indent_horizontal, SIZE * 65], [SIZE * 65 + indent_horizontal, SIZE * 70], [SIZE * 65 + indent_horizontal, SIZE * 80], [SIZE * 55 + indent_horizontal, SIZE * 75], [SIZE * 45 + indent_horizontal, SIZE * 75], [SIZE * 35 + indent_horizontal, SIZE * 80]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 60 + indent_horizontal, SIZE * 95], [SIZE * 60 + indent_horizontal, SIZE * 115], [SIZE * 75 + indent_horizontal, SIZE * 125], [SIZE * 75 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 125], [SIZE * 40 + indent_horizontal, SIZE * 115], [SIZE * 40 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 25 + indent_horizontal, SIZE * 200], [SIZE * 75 + indent_horizontal, SIZE * 200], [SIZE * 75 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 40 + indent_horizontal, SIZE * 200], [SIZE * 40 + indent_horizontal, SIZE * 280], [SIZE * 30 + indent_horizontal, SIZE * 280], [SIZE * 30 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 60 + indent_horizontal, SIZE * 200], [SIZE * 60 + indent_horizontal, SIZE * 280], [SIZE * 70 + indent_horizontal, SIZE * 280], [SIZE * 70 + indent_horizontal, SIZE * 200]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 70 + indent_horizontal, SIZE * 125], [SIZE * 80 + indent_horizontal, SIZE * 125], [SIZE * 90 + indent_horizontal, SIZE * 160], [SIZE * 80 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 70 + indent_horizontal, SIZE * 125], [SIZE * 80 + indent_horizontal, SIZE * 125], [SIZE * 90 + indent_horizontal, SIZE * 160], [SIZE * 80 + indent_horizontal, SIZE * 160]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 80 + indent_horizontal, SIZE * 145], [SIZE * 90 + indent_horizontal, SIZE * 145], [SIZE * 90 + indent_horizontal, SIZE * 165], [SIZE * 80 + indent_horizontal, SIZE * 165]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 82 + indent_horizontal, SIZE * 147], [SIZE * 88 + indent_horizontal, SIZE * 147], [SIZE * 88 + indent_horizontal, SIZE * 153], [SIZE * 82 + indent_horizontal, SIZE * 153]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 20 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 180], [SIZE * 20 + indent_horizontal, SIZE * 180]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 20 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 180], [SIZE * 20 + indent_horizontal, SIZE * 180]], 2)
    elif left == "enemy1_corpse_0":
        pygame.draw.polygon(sc, WHITE, [[SIZE * 5 + indent_horizontal, SIZE * 5], [SIZE * 95 + indent_horizontal, SIZE * 5], [SIZE * 95 + indent_horizontal, SIZE * 95], [SIZE * 5 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLUE, [[SIZE * 15 + indent_horizontal, SIZE * 15], [SIZE * 85 + indent_horizontal, SIZE * 15], [SIZE * 85 + indent_horizontal, SIZE * 85], [SIZE * 15 + indent_horizontal, SIZE * 85]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 35 + indent_horizontal, SIZE * 25], [SIZE * 65 + indent_horizontal, SIZE * 25]], 15)
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 20 + indent_horizontal, SIZE * 35], [SIZE * 80 + indent_horizontal, SIZE * 35]], 10)
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 20 + indent_horizontal, SIZE * 45], [SIZE * 80 + indent_horizontal, SIZE * 45]], 10)
        pygame.draw.polygon(sc, WHITE, [[SIZE * 60 + indent_horizontal, SIZE * 95], [SIZE * 60 + indent_horizontal, SIZE * 115], [SIZE * 75 + indent_horizontal, SIZE * 125], [SIZE * 75 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 125], [SIZE * 40 + indent_horizontal, SIZE * 115], [SIZE * 40 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 25 + indent_horizontal, SIZE * 200], [SIZE * 75 + indent_horizontal, SIZE * 200], [SIZE * 75 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 40 + indent_horizontal, SIZE * 200], [SIZE * 40 + indent_horizontal, SIZE * 280], [SIZE * 30 + indent_horizontal, SIZE * 280], [SIZE * 30 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 60 + indent_horizontal, SIZE * 200], [SIZE * 60 + indent_horizontal, SIZE * 280], [SIZE * 70 + indent_horizontal, SIZE * 280], [SIZE * 70 + indent_horizontal, SIZE * 200]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 70 + indent_horizontal, SIZE * 125], [SIZE * 80 + indent_horizontal, SIZE * 125], [SIZE * 90 + indent_horizontal, SIZE * 160], [SIZE * 80 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 70 + indent_horizontal, SIZE * 125], [SIZE * 80 + indent_horizontal, SIZE * 125], [SIZE * 90 + indent_horizontal, SIZE * 160], [SIZE * 80 + indent_horizontal, SIZE * 160]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 80 + indent_horizontal, SIZE * 145], [SIZE * 90 + indent_horizontal, SIZE * 145], [SIZE * 90 + indent_horizontal, SIZE * 165], [SIZE * 80 + indent_horizontal, SIZE * 165]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 82 + indent_horizontal, SIZE * 147], [SIZE * 88 + indent_horizontal, SIZE * 147], [SIZE * 88 + indent_horizontal, SIZE * 153], [SIZE * 82 + indent_horizontal, SIZE * 153]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 20 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 180], [SIZE * 20 + indent_horizontal, SIZE * 180]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 20 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 180], [SIZE * 20 + indent_horizontal, SIZE * 180]], 2)
    elif left == "enemy1_corpse_1":
        pygame.draw.polygon(sc, WHITE, [[SIZE * 5 + indent_horizontal, SIZE * 5], [SIZE * 95 + indent_horizontal, SIZE * 5], [SIZE * 95 + indent_horizontal, SIZE * 95], [SIZE * 5 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 15 + indent_horizontal, SIZE * 15], [SIZE * 85 + indent_horizontal, SIZE * 15], [SIZE * 85 + indent_horizontal, SIZE * 85], [SIZE * 15 + indent_horizontal, SIZE * 85]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 20 + indent_horizontal, SIZE * 30], [SIZE * 43 + indent_horizontal, SIZE * 18], [SIZE * 69 + indent_horizontal, SIZE * 45], [SIZE * 60 + indent_horizontal, SIZE * 50], [SIZE * 80 + indent_horizontal, SIZE * 65], [SIZE * 76 + indent_horizontal, SIZE * 72], [SIZE * 54 + indent_horizontal, SIZE * 80], [SIZE * 60 + indent_horizontal, SIZE * 62], [SIZE * 50 + indent_horizontal, SIZE * 80], [SIZE * 20 + indent_horizontal, SIZE * 49]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 60 + indent_horizontal, SIZE * 95], [SIZE * 60 + indent_horizontal, SIZE * 115], [SIZE * 75 + indent_horizontal, SIZE * 125], [SIZE * 75 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 125], [SIZE * 40 + indent_horizontal, SIZE * 115], [SIZE * 40 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 25 + indent_horizontal, SIZE * 200], [SIZE * 75 + indent_horizontal, SIZE * 200], [SIZE * 75 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 40 + indent_horizontal, SIZE * 200], [SIZE * 40 + indent_horizontal, SIZE * 280], [SIZE * 30 + indent_horizontal, SIZE * 280], [SIZE * 30 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 60 + indent_horizontal, SIZE * 200], [SIZE * 60 + indent_horizontal, SIZE * 280], [SIZE * 70 + indent_horizontal, SIZE * 280], [SIZE * 70 + indent_horizontal, SIZE * 200]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 70 + indent_horizontal, SIZE * 125], [SIZE * 80 + indent_horizontal, SIZE * 125], [SIZE * 90 + indent_horizontal, SIZE * 160], [SIZE * 80 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 70 + indent_horizontal, SIZE * 125], [SIZE * 80 + indent_horizontal, SIZE * 125], [SIZE * 90 + indent_horizontal, SIZE * 160], [SIZE * 80 + indent_horizontal, SIZE * 160]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 80 + indent_horizontal, SIZE * 145], [SIZE * 90 + indent_horizontal, SIZE * 145], [SIZE * 90 + indent_horizontal, SIZE * 165], [SIZE * 80 + indent_horizontal, SIZE * 165]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 82 + indent_horizontal, SIZE * 147], [SIZE * 88 + indent_horizontal, SIZE * 147], [SIZE * 88 + indent_horizontal, SIZE * 153], [SIZE * 82 + indent_horizontal, SIZE * 153]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 20 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 180], [SIZE * 20 + indent_horizontal, SIZE * 180]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 20 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 180], [SIZE * 20 + indent_horizontal, SIZE * 180]], 2)
    elif left == "enemy1_corpse_2":
        pygame.draw.polygon(sc, WHITE, [[SIZE * 5 + indent_horizontal, SIZE * 105], [SIZE * 95 + indent_horizontal, SIZE * 105], [SIZE * 95 + indent_horizontal, SIZE * 195], [SIZE * 5 + indent_horizontal, SIZE * 195]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 15 + indent_horizontal, SIZE * 115], [SIZE * 85 + indent_horizontal, SIZE * 115], [SIZE * 85 + indent_horizontal, SIZE * 185], [SIZE * 15 + indent_horizontal, SIZE * 185]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 20 + indent_horizontal, SIZE * 130], [SIZE * 43 + indent_horizontal, SIZE * 118], [SIZE * 69 + indent_horizontal, SIZE * 145], [SIZE * 60 + indent_horizontal, SIZE * 150], [SIZE * 80 + indent_horizontal, SIZE * 165], [SIZE * 76 + indent_horizontal, SIZE * 172], [SIZE * 54 + indent_horizontal, SIZE * 180], [SIZE * 60 + indent_horizontal, SIZE * 162], [SIZE * 50 + indent_horizontal, SIZE * 180], [SIZE * 20 + indent_horizontal, SIZE * 149]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 60 + indent_horizontal, SIZE * 195], [SIZE * 60 + indent_horizontal, SIZE * 215], [SIZE * 75 + indent_horizontal, SIZE * 225], [SIZE * 75 + indent_horizontal, SIZE * 320], [SIZE * 25 + indent_horizontal, SIZE * 320], [SIZE * 25 + indent_horizontal, SIZE * 225], [SIZE * 40 + indent_horizontal, SIZE * 215], [SIZE * 40 + indent_horizontal, SIZE * 195]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 25 + indent_horizontal, SIZE * 300], [SIZE * 75 + indent_horizontal, SIZE * 300], [SIZE * 75 + indent_horizontal, SIZE * 320], [SIZE * 25 + indent_horizontal, SIZE * 320]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 40 + indent_horizontal, SIZE * 300], [SIZE * 40 + indent_horizontal, SIZE * 380], [SIZE * 30 + indent_horizontal, SIZE * 380], [SIZE * 30 + indent_horizontal, SIZE * 300]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 60 + indent_horizontal, SIZE * 300], [SIZE * 60 + indent_horizontal, SIZE * 380], [SIZE * 70 + indent_horizontal, SIZE * 380], [SIZE * 70 + indent_horizontal, SIZE * 300]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 70 + indent_horizontal, SIZE * 225], [SIZE * 80 + indent_horizontal, SIZE * 225], [SIZE * 90 + indent_horizontal, SIZE * 260], [SIZE * 80 + indent_horizontal, SIZE * 260]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 70 + indent_horizontal, SIZE * 225], [SIZE * 80 + indent_horizontal, SIZE * 225], [SIZE * 90 + indent_horizontal, SIZE * 260], [SIZE * 80 + indent_horizontal, SIZE * 260]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 80 + indent_horizontal, SIZE * 245], [SIZE * 90 + indent_horizontal, SIZE * 245], [SIZE * 90 + indent_horizontal, SIZE * 265], [SIZE * 80 + indent_horizontal, SIZE * 265]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 82 + indent_horizontal, SIZE * 247], [SIZE * 88 + indent_horizontal, SIZE * 247], [SIZE * 88 + indent_horizontal, SIZE * 253], [SIZE * 82 + indent_horizontal, SIZE * 253]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 20 + indent_horizontal, SIZE * 225], [SIZE * 30 + indent_horizontal, SIZE * 225], [SIZE * 30 + indent_horizontal, SIZE * 280], [SIZE * 20 + indent_horizontal, SIZE * 280]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 20 + indent_horizontal, SIZE * 225], [SIZE * 30 + indent_horizontal, SIZE * 225], [SIZE * 30 + indent_horizontal, SIZE * 280], [SIZE * 20 + indent_horizontal, SIZE * 280]], 2)
    elif left == "enemy1_corpse_3":
        pygame.draw.polygon(sc, WHITE, [[SIZE * 5 + indent_horizontal, SIZE * 205], [SIZE * 95 + indent_horizontal, SIZE * 205], [SIZE * 95 + indent_horizontal, SIZE * 295], [SIZE * 5 + indent_horizontal, SIZE * 295]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 15 + indent_horizontal, SIZE * 215], [SIZE * 85 + indent_horizontal, SIZE * 215], [SIZE * 85 + indent_horizontal, SIZE * 285], [SIZE * 15 + indent_horizontal, SIZE * 285]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 20 + indent_horizontal, SIZE * 230], [SIZE * 43 + indent_horizontal, SIZE * 218], [SIZE * 69 + indent_horizontal, SIZE * 245], [SIZE * 60 + indent_horizontal, SIZE * 250], [SIZE * 80 + indent_horizontal, SIZE * 265], [SIZE * 76 + indent_horizontal, SIZE * 272], [SIZE * 54 + indent_horizontal, SIZE * 280], [SIZE * 60 + indent_horizontal, SIZE * 262], [SIZE * 50 + indent_horizontal, SIZE * 280], [SIZE * 20 + indent_horizontal, SIZE * 249]])
        pygame.draw.polygon(sc, MAGENTA, [[SIZE * 69 + indent_horizontal, SIZE * 245], [SIZE * 69 + indent_horizontal, SIZE * 300], [SIZE * 20 + indent_horizontal, SIZE * 300], [SIZE * 20 + indent_horizontal, SIZE * 249]])
    elif left == "enemy2":
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 5 + indent_horizontal, SIZE * 5], [SIZE * 95 + indent_horizontal, SIZE * 5], [SIZE * 95 + indent_horizontal, SIZE * 95], [SIZE * 5 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 15 + indent_horizontal, SIZE * 15], [SIZE * 85 + indent_horizontal, SIZE * 15], [SIZE * 85 + indent_horizontal, SIZE * 85], [SIZE * 15 + indent_horizontal, SIZE * 85]])
        pygame.draw.rect(sc, GREEN, (SIZE * 30 + indent_horizontal, SIZE * 30, SIZE * 10, SIZE * 20))
        pygame.draw.rect(sc, GREEN, (SIZE * 60 + indent_horizontal, SIZE * 30, SIZE * 10, SIZE * 20))
        pygame.draw.polygon(sc, DARK_GREEN, [[SIZE * 25 + indent_horizontal, SIZE * 25], [SIZE * 45 + indent_horizontal, SIZE * 30], [SIZE * 45 + indent_horizontal, SIZE * 40], [SIZE * 25 + indent_horizontal, SIZE * 35]])
        pygame.draw.polygon(sc, DARK_GREEN, [[SIZE * 55 + indent_horizontal, SIZE * 40], [SIZE * 75 + indent_horizontal, SIZE * 35], [SIZE * 75 + indent_horizontal, SIZE * 25], [SIZE * 55 + indent_horizontal, SIZE * 30]])
        pygame.draw.polygon(sc, GREEN, [[SIZE * 35 + indent_horizontal, SIZE * 70], [SIZE * 45 + indent_horizontal, SIZE * 65], [SIZE * 55 + indent_horizontal, SIZE * 65], [SIZE * 65 + indent_horizontal, SIZE * 70], [SIZE * 65 + indent_horizontal, SIZE * 80], [SIZE * 55 + indent_horizontal, SIZE * 75], [SIZE * 45 + indent_horizontal, SIZE * 75], [SIZE * 35 + indent_horizontal, SIZE * 80]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 60 + indent_horizontal, SIZE * 95], [SIZE * 60 + indent_horizontal, SIZE * 115], [SIZE * 75 + indent_horizontal, SIZE * 125], [SIZE * 75 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 125], [SIZE * 40 + indent_horizontal, SIZE * 115], [SIZE * 40 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 25 + indent_horizontal, SIZE * 200], [SIZE * 75 + indent_horizontal, SIZE * 200], [SIZE * 75 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 40 + indent_horizontal, SIZE * 200], [SIZE * 40 + indent_horizontal, SIZE * 280], [SIZE * 30 + indent_horizontal, SIZE * 280], [SIZE * 30 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 60 + indent_horizontal, SIZE * 200], [SIZE * 60 + indent_horizontal, SIZE * 280], [SIZE * 70 + indent_horizontal, SIZE * 280], [SIZE * 70 + indent_horizontal, SIZE * 200]])
        # hand right(hold) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 20 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 160], [SIZE * 70 + indent_horizontal, SIZE * 160], [SIZE * 70 + indent_horizontal, SIZE * 170], [SIZE * 30 + indent_horizontal, SIZE * 170], [SIZE * 20 + indent_horizontal, SIZE * 170]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 20 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 160], [SIZE * 70 + indent_horizontal, SIZE * 160], [SIZE * 70 + indent_horizontal, SIZE * 170], [SIZE * 30 + indent_horizontal, SIZE * 170], [SIZE * 20 + indent_horizontal, SIZE * 170]], 2)
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 70 + indent_horizontal, SIZE * 125], [SIZE * 80 + indent_horizontal, SIZE * 125], [SIZE * 80 + indent_horizontal, SIZE * 160], [SIZE * 70 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 70 + indent_horizontal, SIZE * 125], [SIZE * 80 + indent_horizontal, SIZE * 125], [SIZE * 80 + indent_horizontal, SIZE * 160], [SIZE * 70 + indent_horizontal, SIZE * 160]], 2)
        pygame.draw.polygon(sc, BROWN, [[SIZE * 70 + indent_horizontal, SIZE * 145], [SIZE * 80 + indent_horizontal, SIZE * 145], [SIZE * 80 + indent_horizontal, SIZE * 165], [SIZE * 70 + indent_horizontal, SIZE * 165]])
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 72 + indent_horizontal, SIZE * 147], [SIZE * 78 + indent_horizontal, SIZE * 147], [SIZE * 78 + indent_horizontal, SIZE * 153], [SIZE * 72 + indent_horizontal, SIZE * 153]])
    elif left == "enemy2_corpse_0":
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 5 + indent_horizontal, SIZE * 5], [SIZE * 95 + indent_horizontal, SIZE * 5], [SIZE * 95 + indent_horizontal, SIZE * 95], [SIZE * 5 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLUE, [[SIZE * 15 + indent_horizontal, SIZE * 15], [SIZE * 85 + indent_horizontal, SIZE * 15], [SIZE * 85 + indent_horizontal, SIZE * 85], [SIZE * 15 + indent_horizontal, SIZE * 85]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 35 + indent_horizontal, SIZE * 25], [SIZE * 65 + indent_horizontal, SIZE * 25]], 15)
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 20 + indent_horizontal, SIZE * 35], [SIZE * 80 + indent_horizontal, SIZE * 35]], 10)
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 20 + indent_horizontal, SIZE * 45], [SIZE * 80 + indent_horizontal, SIZE * 45]], 10)
        pygame.draw.polygon(sc, WHITE, [[SIZE * 60 + indent_horizontal, SIZE * 95], [SIZE * 60 + indent_horizontal, SIZE * 115], [SIZE * 75 + indent_horizontal, SIZE * 125], [SIZE * 75 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 125], [SIZE * 40 + indent_horizontal, SIZE * 115], [SIZE * 40 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 25 + indent_horizontal, SIZE * 200], [SIZE * 75 + indent_horizontal, SIZE * 200], [SIZE * 75 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 40 + indent_horizontal, SIZE * 200], [SIZE * 40 + indent_horizontal, SIZE * 280], [SIZE * 30 + indent_horizontal, SIZE * 280], [SIZE * 30 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 60 + indent_horizontal, SIZE * 200], [SIZE * 60 + indent_horizontal, SIZE * 280], [SIZE * 70 + indent_horizontal, SIZE * 280], [SIZE * 70 + indent_horizontal, SIZE * 200]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 70 + indent_horizontal, SIZE * 125], [SIZE * 80 + indent_horizontal, SIZE * 125], [SIZE * 90 + indent_horizontal, SIZE * 160], [SIZE * 80 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 70 + indent_horizontal, SIZE * 125], [SIZE * 80 + indent_horizontal, SIZE * 125], [SIZE * 90 + indent_horizontal, SIZE * 160], [SIZE * 80 + indent_horizontal, SIZE * 160]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 80 + indent_horizontal, SIZE * 145], [SIZE * 90 + indent_horizontal, SIZE * 145], [SIZE * 90 + indent_horizontal, SIZE * 165], [SIZE * 80 + indent_horizontal, SIZE * 165]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 82 + indent_horizontal, SIZE * 147], [SIZE * 88 + indent_horizontal, SIZE * 147], [SIZE * 88 + indent_horizontal, SIZE * 153], [SIZE * 82 + indent_horizontal, SIZE * 153]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 20 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 180], [SIZE * 20 + indent_horizontal, SIZE * 180]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 20 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 180], [SIZE * 20 + indent_horizontal, SIZE * 180]], 2)
    elif left == "enemy2_corpse_1":
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 5 + indent_horizontal, SIZE * 5], [SIZE * 95 + indent_horizontal, SIZE * 5], [SIZE * 95 + indent_horizontal, SIZE * 95], [SIZE * 5 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 15 + indent_horizontal, SIZE * 15], [SIZE * 85 + indent_horizontal, SIZE * 15], [SIZE * 85 + indent_horizontal, SIZE * 85], [SIZE * 15 + indent_horizontal, SIZE * 85]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 20 + indent_horizontal, SIZE * 30], [SIZE * 43 + indent_horizontal, SIZE * 18], [SIZE * 69 + indent_horizontal, SIZE * 45], [SIZE * 60 + indent_horizontal, SIZE * 50], [SIZE * 80 + indent_horizontal, SIZE * 65], [SIZE * 76 + indent_horizontal, SIZE * 72], [SIZE * 54 + indent_horizontal, SIZE * 80], [SIZE * 60 + indent_horizontal, SIZE * 62], [SIZE * 50 + indent_horizontal, SIZE * 80], [SIZE * 20 + indent_horizontal, SIZE * 49]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 60 + indent_horizontal, SIZE * 95], [SIZE * 60 + indent_horizontal, SIZE * 115], [SIZE * 75 + indent_horizontal, SIZE * 125], [SIZE * 75 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 125], [SIZE * 40 + indent_horizontal, SIZE * 115], [SIZE * 40 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 25 + indent_horizontal, SIZE * 200], [SIZE * 75 + indent_horizontal, SIZE * 200], [SIZE * 75 + indent_horizontal, SIZE * 220], [SIZE * 25 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 40 + indent_horizontal, SIZE * 200], [SIZE * 40 + indent_horizontal, SIZE * 280], [SIZE * 30 + indent_horizontal, SIZE * 280], [SIZE * 30 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 60 + indent_horizontal, SIZE * 200], [SIZE * 60 + indent_horizontal, SIZE * 280], [SIZE * 70 + indent_horizontal, SIZE * 280], [SIZE * 70 + indent_horizontal, SIZE * 200]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 70 + indent_horizontal, SIZE * 125], [SIZE * 80 + indent_horizontal, SIZE * 125], [SIZE * 90 + indent_horizontal, SIZE * 160], [SIZE * 80 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 70 + indent_horizontal, SIZE * 125], [SIZE * 80 + indent_horizontal, SIZE * 125], [SIZE * 90 + indent_horizontal, SIZE * 160], [SIZE * 80 + indent_horizontal, SIZE * 160]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 80 + indent_horizontal, SIZE * 145], [SIZE * 90 + indent_horizontal, SIZE * 145], [SIZE * 90 + indent_horizontal, SIZE * 165], [SIZE * 80 + indent_horizontal, SIZE * 165]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 82 + indent_horizontal, SIZE * 147], [SIZE * 88 + indent_horizontal, SIZE * 147], [SIZE * 88 + indent_horizontal, SIZE * 153], [SIZE * 82 + indent_horizontal, SIZE * 153]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 20 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 180], [SIZE * 20 + indent_horizontal, SIZE * 180]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 20 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 125], [SIZE * 30 + indent_horizontal, SIZE * 180], [SIZE * 20 + indent_horizontal, SIZE * 180]], 2)
    elif left == "enemy2_corpse_2":
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 5 + indent_horizontal, SIZE * 105], [SIZE * 95 + indent_horizontal, SIZE * 105], [SIZE * 95 + indent_horizontal, SIZE * 195], [SIZE * 5 + indent_horizontal, SIZE * 195]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 15 + indent_horizontal, SIZE * 115], [SIZE * 85 + indent_horizontal, SIZE * 115], [SIZE * 85 + indent_horizontal, SIZE * 185], [SIZE * 15 + indent_horizontal, SIZE * 185]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 20 + indent_horizontal, SIZE * 130], [SIZE * 43 + indent_horizontal, SIZE * 118], [SIZE * 69 + indent_horizontal, SIZE * 145], [SIZE * 60 + indent_horizontal, SIZE * 150], [SIZE * 80 + indent_horizontal, SIZE * 165], [SIZE * 76 + indent_horizontal, SIZE * 172], [SIZE * 54 + indent_horizontal, SIZE * 180], [SIZE * 60 + indent_horizontal, SIZE * 162], [SIZE * 50 + indent_horizontal, SIZE * 180], [SIZE * 20 + indent_horizontal, SIZE * 149]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 60 + indent_horizontal, SIZE * 195], [SIZE * 60 + indent_horizontal, SIZE * 215], [SIZE * 75 + indent_horizontal, SIZE * 225], [SIZE * 75 + indent_horizontal, SIZE * 320], [SIZE * 25 + indent_horizontal, SIZE * 320], [SIZE * 25 + indent_horizontal, SIZE * 225], [SIZE * 40 + indent_horizontal, SIZE * 215], [SIZE * 40 + indent_horizontal, SIZE * 195]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 25 + indent_horizontal, SIZE * 300], [SIZE * 75 + indent_horizontal, SIZE * 300], [SIZE * 75 + indent_horizontal, SIZE * 320], [SIZE * 25 + indent_horizontal, SIZE * 320]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 40 + indent_horizontal, SIZE * 300], [SIZE * 40 + indent_horizontal, SIZE * 380], [SIZE * 30 + indent_horizontal, SIZE * 380], [SIZE * 30 + indent_horizontal, SIZE * 300]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 60 + indent_horizontal, SIZE * 300], [SIZE * 60 + indent_horizontal, SIZE * 380], [SIZE * 70 + indent_horizontal, SIZE * 380], [SIZE * 70 + indent_horizontal, SIZE * 300]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 70 + indent_horizontal, SIZE * 225], [SIZE * 80 + indent_horizontal, SIZE * 225], [SIZE * 90 + indent_horizontal, SIZE * 260], [SIZE * 80 + indent_horizontal, SIZE * 260]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 70 + indent_horizontal, SIZE * 225], [SIZE * 80 + indent_horizontal, SIZE * 225], [SIZE * 90 + indent_horizontal, SIZE * 260], [SIZE * 80 + indent_horizontal, SIZE * 260]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 80 + indent_horizontal, SIZE * 245], [SIZE * 90 + indent_horizontal, SIZE * 245], [SIZE * 90 + indent_horizontal, SIZE * 265], [SIZE * 80 + indent_horizontal, SIZE * 265]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 82 + indent_horizontal, SIZE * 247], [SIZE * 88 + indent_horizontal, SIZE * 247], [SIZE * 88 + indent_horizontal, SIZE * 253], [SIZE * 82 + indent_horizontal, SIZE * 253]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 20 + indent_horizontal, SIZE * 225], [SIZE * 30 + indent_horizontal, SIZE * 225], [SIZE * 30 + indent_horizontal, SIZE * 280], [SIZE * 20 + indent_horizontal, SIZE * 280]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 20 + indent_horizontal, SIZE * 225], [SIZE * 30 + indent_horizontal, SIZE * 225], [SIZE * 30 + indent_horizontal, SIZE * 280], [SIZE * 20 + indent_horizontal, SIZE * 280]], 2)
    elif left == "enemy2_corpse_3":
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 5 + indent_horizontal, SIZE * 205], [SIZE * 95 + indent_horizontal, SIZE * 205], [SIZE * 95 + indent_horizontal, SIZE * 295], [SIZE * 5 + indent_horizontal, SIZE * 295]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 15 + indent_horizontal, SIZE * 215], [SIZE * 85 + indent_horizontal, SIZE * 215], [SIZE * 85 + indent_horizontal, SIZE * 285], [SIZE * 15 + indent_horizontal, SIZE * 285]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 20 + indent_horizontal, SIZE * 230], [SIZE * 43 + indent_horizontal, SIZE * 218], [SIZE * 69 + indent_horizontal, SIZE * 245], [SIZE * 60 + indent_horizontal, SIZE * 250], [SIZE * 80 + indent_horizontal, SIZE * 265], [SIZE * 76 + indent_horizontal, SIZE * 272], [SIZE * 54 + indent_horizontal, SIZE * 280], [SIZE * 60 + indent_horizontal, SIZE * 262], [SIZE * 50 + indent_horizontal, SIZE * 280], [SIZE * 20 + indent_horizontal, SIZE * 249]])
        pygame.draw.polygon(sc, MAGENTA, [[SIZE * 69 + indent_horizontal, SIZE * 245], [SIZE * 69 + indent_horizontal, SIZE * 300], [SIZE * 20 + indent_horizontal, SIZE * 300], [SIZE * 20 + indent_horizontal, SIZE * 249]])

    if right == "wall":
        pygame.draw.polygon(sc, NAVY, [[SIZE * 300 + indent_horizontal, SIZE * 0], [SIZE * 200 + indent_horizontal, SIZE * 100], [SIZE * 200 + indent_horizontal, SIZE * 200], [SIZE * 300 + indent_horizontal, SIZE * 300]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 298 + indent_horizontal, SIZE * 5], [SIZE * 203 + indent_horizontal, SIZE * 102], [SIZE * 203 + indent_horizontal, SIZE * 197], [SIZE * 298 + indent_horizontal, SIZE * 295]], 3)
    elif right == "wall2":
        pygame.draw.polygon(sc, NAVY, [[SIZE * 200 + indent_horizontal, SIZE * 100], [SIZE * 300 + indent_horizontal, SIZE * 100], [SIZE * 300 + indent_horizontal, SIZE * 200], [SIZE * 200 + indent_horizontal, SIZE * 200]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 205 + indent_horizontal, SIZE * 105], [SIZE * 295 + indent_horizontal, SIZE * 105], [SIZE * 295 + indent_horizontal, SIZE * 195], [SIZE * 205 + indent_horizontal, SIZE * 195]], 3)
    elif right == "bullets":
        pygame.draw.polygon(sc, LIGHTYELLOW, [[SIZE * 235 + indent_horizontal, SIZE * 135], [SIZE * 240 + indent_horizontal, SIZE * 130], [SIZE * 245 + indent_horizontal, SIZE * 135], [SIZE * 245 + indent_horizontal, SIZE * 160], [SIZE * 235 + indent_horizontal, SIZE * 160]])
        pygame.draw.polygon(sc, LIGHTYELLOW, [[SIZE * 255 + indent_horizontal, SIZE * 135], [SIZE * 260 + indent_horizontal, SIZE * 130], [SIZE * 265 + indent_horizontal, SIZE * 135], [SIZE * 265 + indent_horizontal, SIZE * 160], [SIZE * 255 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, YELLOW, True, [[SIZE * 235 + indent_horizontal, SIZE * 137], [SIZE * 245 + indent_horizontal, SIZE * 137]], 5)
        pygame.draw.lines(sc, YELLOW, True, [[SIZE * 255 + indent_horizontal, SIZE * 137], [SIZE * 265 + indent_horizontal, SIZE * 137]], 5)

    elif right == "medkit":
        pygame.draw.polygon(sc, MEDKIT, [[SIZE * 210 + indent_horizontal, SIZE * 110], [SIZE * 290 + indent_horizontal, SIZE * 110], [SIZE * 290 + indent_horizontal, SIZE * 190], [SIZE * 210 + indent_horizontal, SIZE * 190]])
        pygame.draw.rect(sc, WHITE, (SIZE * 211 + indent_horizontal, SIZE * 110, SIZE * 78, SIZE * 15), 8)
        pygame.draw.polygon(sc, RED, [[SIZE * 220 + indent_horizontal, SIZE * 145], [SIZE * 245 + indent_horizontal, SIZE * 145], [SIZE * 245 + indent_horizontal, SIZE * 120], [SIZE * 255 + indent_horizontal, SIZE * 120], [SIZE * 255 + indent_horizontal, SIZE * 145], [SIZE * 280 + indent_horizontal, SIZE * 145], [SIZE * 280 + indent_horizontal, SIZE * 155], [SIZE * 280 + indent_horizontal, SIZE * 155], [SIZE * 255 + indent_horizontal, SIZE * 155], [SIZE * 255 + indent_horizontal, SIZE * 180], [SIZE * 245 + indent_horizontal, SIZE * 180], [SIZE * 245 + indent_horizontal, SIZE * 155], [SIZE * 220 + indent_horizontal, SIZE * 155]])
    elif right == "enemy1":
        pygame.draw.polygon(sc, WHITE, [[SIZE * 205 + indent_horizontal, 5], [SIZE * 295 + indent_horizontal, 5], [SIZE * 295 + indent_horizontal, SIZE * 95], [SIZE * 205 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 215 + indent_horizontal, SIZE * 15], [SIZE * 285 + indent_horizontal, SIZE * 15], [SIZE * 285 + indent_horizontal, SIZE * 85], [SIZE * 215 + indent_horizontal, SIZE * 85]])
        pygame.draw.rect(sc, GREEN, (SIZE * 230 + indent_horizontal, SIZE * 30, SIZE * 10, SIZE * 20))
        pygame.draw.rect(sc, GREEN, (SIZE * 260 + indent_horizontal, SIZE * 30, SIZE * 10, SIZE * 20))
        pygame.draw.polygon(sc, DARK_GREEN, [[SIZE * 225 + indent_horizontal, SIZE * 25], [SIZE * 245 + indent_horizontal, SIZE * 30], [SIZE * 245 + indent_horizontal, SIZE * 40], [SIZE * 225 + indent_horizontal, SIZE * 35]])
        pygame.draw.polygon(sc, DARK_GREEN, [[SIZE * 255 + indent_horizontal, SIZE * 40], [SIZE * 275 + indent_horizontal, SIZE * 35], [SIZE * 275 + indent_horizontal, SIZE * 25], [SIZE * 255 + indent_horizontal, SIZE * 30]])
        pygame.draw.polygon(sc, GREEN, [[SIZE * 235 + indent_horizontal, SIZE * 70], [SIZE * 245 + indent_horizontal, SIZE * 65], [SIZE * 255 + indent_horizontal, SIZE * 65], [SIZE * 265 + indent_horizontal, SIZE * 70], [SIZE * 265 + indent_horizontal, SIZE * 80], [SIZE * 255 + indent_horizontal, SIZE * 75], [SIZE * 245 + indent_horizontal, SIZE * 75], [SIZE * 235 + indent_horizontal, SIZE * 80]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 260 + indent_horizontal, SIZE * 95], [SIZE * 260 + indent_horizontal, SIZE * 115], [SIZE * 275 + indent_horizontal, SIZE * 125], [SIZE * 275 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 125], [SIZE * 240 + indent_horizontal, SIZE * 115], [SIZE * 240 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 225 + indent_horizontal, SIZE * 200], [SIZE * 275 + indent_horizontal, SIZE * 200], [SIZE * 275 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 240 + indent_horizontal, SIZE * 200], [SIZE * 240 + indent_horizontal, SIZE * 280], [SIZE * 230 + indent_horizontal, SIZE * 280], [SIZE * 230 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 260 + indent_horizontal, SIZE * 200], [SIZE * 260 + indent_horizontal, SIZE * 280], [SIZE * 270 + indent_horizontal, SIZE * 280], [SIZE * 270 + indent_horizontal, SIZE * 200]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 270 + indent_horizontal, SIZE * 125], [SIZE * 280 + indent_horizontal, SIZE * 125], [SIZE * 290 + indent_horizontal, SIZE * 160], [SIZE * 280 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 270 + indent_horizontal, SIZE * 125], [SIZE * 280 + indent_horizontal, SIZE * 125], [SIZE * 290, SIZE * 160], [SIZE * 280, SIZE * 160]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 280 + indent_horizontal, SIZE * 145], [SIZE * 290 + indent_horizontal, SIZE * 145], [SIZE * 290 + indent_horizontal, SIZE * 165], [SIZE * 280 + indent_horizontal, SIZE * 165]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 282 + indent_horizontal, SIZE * 147], [SIZE * 288 + indent_horizontal, SIZE * 147], [SIZE * 288 + indent_horizontal, SIZE * 153], [SIZE * 282 + indent_horizontal, SIZE * 153]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 220, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 180], [SIZE * 220 + indent_horizontal, SIZE * 180]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 220 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 180], [SIZE * 220 + indent_horizontal, SIZE * 180]], 2)
    elif right == "enemy1_corpse_0":
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 205 + indent_horizontal, SIZE * 5], [SIZE * 295 + indent_horizontal, SIZE * 5], [SIZE * 295 + indent_horizontal, SIZE * 95], [SIZE * 205 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLUE, [[SIZE * 215 + indent_horizontal, SIZE * 15], [SIZE * 285 + indent_horizontal, SIZE * 15], [SIZE * 285 + indent_horizontal, SIZE * 85], [SIZE * 215 + indent_horizontal, SIZE * 85]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 235 + indent_horizontal, SIZE * 25], [SIZE * 265 + indent_horizontal, SIZE * 25]], 15)
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 220 + indent_horizontal, SIZE * 35], [SIZE * 280 + indent_horizontal, SIZE * 35]], 10)
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 220 + indent_horizontal, SIZE * 45], [SIZE * 280 + indent_horizontal, SIZE * 45]], 10)
        pygame.draw.polygon(sc, WHITE, [[SIZE * 260 + indent_horizontal, SIZE * 95], [SIZE * 260 + indent_horizontal, SIZE * 115], [SIZE * 275 + indent_horizontal, SIZE * 125], [SIZE * 275 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 125], [SIZE * 240 + indent_horizontal, SIZE * 115], [SIZE * 240 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 225 + indent_horizontal, SIZE * 200], [SIZE * 275 + indent_horizontal, SIZE * 200], [SIZE * 275 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 240 + indent_horizontal, SIZE * 200], [SIZE * 240 + indent_horizontal, SIZE * 280], [SIZE * 230 + indent_horizontal, SIZE * 280], [SIZE * 230 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 260 + indent_horizontal, SIZE * 200], [SIZE * 260 + indent_horizontal, SIZE * 280], [SIZE * 270 + indent_horizontal, SIZE * 280], [SIZE * 270 + indent_horizontal, SIZE * 200]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 270 + indent_horizontal, SIZE * 125], [SIZE * 280 + indent_horizontal, SIZE * 125], [SIZE * 290 + indent_horizontal, SIZE * 160], [SIZE * 280 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 270 + indent_horizontal, SIZE * 125], [SIZE * 280 + indent_horizontal, SIZE * 125], [SIZE * 290 + indent_horizontal, SIZE * 160], [SIZE * 280 + indent_horizontal, SIZE * 160]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 280 + indent_horizontal, SIZE * 145], [SIZE * 290 + indent_horizontal, SIZE * 145], [SIZE * 290 + indent_horizontal, SIZE * 165], [SIZE * 280 + indent_horizontal, SIZE * 165]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 282 + indent_horizontal, SIZE * 147], [SIZE * 288 + indent_horizontal, SIZE * 147], [SIZE * 288 + indent_horizontal, SIZE * 153], [SIZE * 282 + indent_horizontal, SIZE * 153]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 220 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 180], [SIZE * 220 + indent_horizontal, SIZE * 180]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 220 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 180], [SIZE * 220 + indent_horizontal, SIZE * 180]], 2)
    elif right == "enemy1_corpse_1":
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 205 + indent_horizontal, SIZE * 5], [SIZE * 295 + indent_horizontal, SIZE * 5], [SIZE * 295 + indent_horizontal, SIZE * 95], [SIZE * 205 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 215 + indent_horizontal, SIZE * 15], [SIZE * 285 + indent_horizontal, SIZE * 15], [SIZE * 285 + indent_horizontal, SIZE * 85], [SIZE * 215 + indent_horizontal, SIZE * 85]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 220 + indent_horizontal, SIZE * 30], [SIZE * 243 + indent_horizontal, SIZE * 18], [SIZE * 269 + indent_horizontal, SIZE * 45], [SIZE * 260 + indent_horizontal, SIZE * 50], [SIZE * 280 + indent_horizontal, SIZE * 65], [SIZE * 276 + indent_horizontal, SIZE * 72], [SIZE * 54 + indent_horizontal, SIZE * 80], [SIZE * 260 + indent_horizontal, SIZE * 62], [SIZE * 250 + indent_horizontal, SIZE * 80], [SIZE * 220 + indent_horizontal, SIZE * 49]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 260 + indent_horizontal, SIZE * 95], [SIZE * 260 + indent_horizontal, SIZE * 115], [SIZE * 275 + indent_horizontal, SIZE * 125], [SIZE * 275 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 125], [SIZE * 240 + indent_horizontal, SIZE * 115], [SIZE * 240 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 225 + indent_horizontal, SIZE * 200], [SIZE * 275 + indent_horizontal, SIZE * 200], [SIZE * 275 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 240 + indent_horizontal, SIZE * 200], [SIZE * 240 + indent_horizontal, SIZE * 280], [SIZE * 230 + indent_horizontal, SIZE * 280], [SIZE * 230 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 260 + indent_horizontal, SIZE * 200], [SIZE * 260 + indent_horizontal, SIZE * 280], [SIZE * 270 + indent_horizontal, SIZE * 280], [SIZE * 270 + indent_horizontal, SIZE * 200]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 270 + indent_horizontal, SIZE * 125], [SIZE * 280 + indent_horizontal, SIZE * 125], [SIZE * 290 + indent_horizontal, SIZE * 160], [SIZE * 280 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 270 + indent_horizontal, SIZE * 125], [SIZE * 280 + indent_horizontal, SIZE * 125], [SIZE * 290 + indent_horizontal, SIZE * 160], [SIZE * 280 + indent_horizontal, SIZE * 160]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 280 + indent_horizontal, SIZE * 145], [SIZE * 290 + indent_horizontal, SIZE * 145], [SIZE * 290 + indent_horizontal, SIZE * 165], [SIZE * 280 + indent_horizontal, SIZE * 165]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 282 + indent_horizontal, SIZE * 147], [SIZE * 288 + indent_horizontal, SIZE * 147], [SIZE * 288 + indent_horizontal, SIZE * 153], [SIZE * 282 + indent_horizontal, SIZE * 153]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 220 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 180], [SIZE * 220 + indent_horizontal, SIZE * 180]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 220 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 180], [SIZE * 220 + indent_horizontal, SIZE * 180]], 2)
    elif right == "enemy1_corpse_2":
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 205 + indent_horizontal, SIZE * 105], [SIZE * 295 + indent_horizontal, SIZE * 105], [SIZE * 295 + indent_horizontal, SIZE * 195], [SIZE * 205 + indent_horizontal, SIZE * 195]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 215 + indent_horizontal, SIZE * 115], [SIZE * 285 + indent_horizontal, SIZE * 115], [SIZE * 285 + indent_horizontal, SIZE * 185], [SIZE * 215 + indent_horizontal, SIZE * 185]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 220 + indent_horizontal, SIZE * 130], [SIZE * 243 + indent_horizontal, SIZE * 118], [SIZE * 269 + indent_horizontal, SIZE * 145], [SIZE * 260 + indent_horizontal, SIZE * 150], [SIZE * 280 + indent_horizontal, SIZE * 165], [SIZE * 276 + indent_horizontal, SIZE * 172], [SIZE * 254 + indent_horizontal, SIZE * 180], [SIZE * 260 + indent_horizontal, SIZE * 162], [SIZE * 250 + indent_horizontal, SIZE * 180], [SIZE * 220 + indent_horizontal, SIZE * 149]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 260 + indent_horizontal, SIZE * 195], [SIZE * 260 + indent_horizontal, SIZE * 215], [SIZE * 275 + indent_horizontal, SIZE * 225], [SIZE * 275 + indent_horizontal, SIZE * 320], [SIZE * 225 + indent_horizontal, SIZE * 320], [SIZE * 225 + indent_horizontal, SIZE * 225], [SIZE * 240 + indent_horizontal, SIZE * 215], [SIZE * 240 + indent_horizontal, SIZE * 195]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 270 + indent_horizontal, SIZE * 225], [SIZE * 280 + indent_horizontal, SIZE * 225], [SIZE * 290 + indent_horizontal, SIZE * 260], [SIZE * 80 + indent_horizontal, SIZE * 260]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 270 + indent_horizontal, SIZE * 225], [SIZE * 280 + indent_horizontal, SIZE * 225], [SIZE * 290 + indent_horizontal, SIZE * 260], [SIZE * 280 + indent_horizontal, SIZE * 260]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 280 + indent_horizontal, SIZE * 245], [SIZE * 290 + indent_horizontal, SIZE * 245], [SIZE * 290 + indent_horizontal, SIZE * 265], [SIZE * 280 + indent_horizontal, SIZE * 265]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 282 + indent_horizontal, SIZE * 247], [SIZE * 288 + indent_horizontal, SIZE * 247], [SIZE * 288 + indent_horizontal, SIZE * 253], [SIZE * 282 + indent_horizontal, SIZE * 253]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 220 + indent_horizontal, SIZE * 225], [SIZE * 230 + indent_horizontal, SIZE * 225], [SIZE * 230 + indent_horizontal, SIZE * 280], [SIZE * 220 + indent_horizontal, SIZE * 280]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 220 + indent_horizontal, SIZE * 225], [SIZE * 230 + indent_horizontal, SIZE * 225], [SIZE * 230 + indent_horizontal, SIZE * 280], [SIZE * 220 + indent_horizontal, SIZE * 280]], 2)
    elif right == "enemy1_corpse_3":
        pygame.draw.polygon(sc, WHITE, [[SIZE * 205 + indent_horizontal, SIZE * 205], [SIZE * 295 + indent_horizontal, SIZE * 205], [SIZE * 295 + indent_horizontal, SIZE * 295], [SIZE * 205 + indent_horizontal, SIZE * 295]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 215 + indent_horizontal, SIZE * 215], [SIZE * 285 + indent_horizontal, SIZE * 215], [SIZE * 285 + indent_horizontal, SIZE * 285], [SIZE * 215 + indent_horizontal, SIZE * 285]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 220 + indent_horizontal, SIZE * 230], [SIZE * 243 + indent_horizontal, SIZE * 218], [SIZE * 269 + indent_horizontal, SIZE * 245], [SIZE * 260 + indent_horizontal, SIZE * 250], [SIZE * 280 + indent_horizontal, SIZE * 265], [SIZE * 276 + indent_horizontal, SIZE * 272], [SIZE * 254 + indent_horizontal, SIZE * 280], [SIZE * 260 + indent_horizontal, SIZE * 262], [SIZE * 250 + indent_horizontal, SIZE * 280], [SIZE * 220 + indent_horizontal, SIZE * 249]])
        pygame.draw.polygon(sc, MAGENTA, [[SIZE * 269 + indent_horizontal, SIZE * 245], [SIZE * 269 + indent_horizontal, SIZE * 300], [SIZE * 220 + indent_horizontal, SIZE * 300], [SIZE * 220 + indent_horizontal, SIZE * 249]])
    elif right == "enemy2":
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 205 + indent_horizontal, 5], [SIZE * 295 + indent_horizontal, 5], [SIZE * 295 + indent_horizontal, SIZE * 95], [SIZE * 205 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 215 + indent_horizontal, SIZE * 15], [SIZE * 285 + indent_horizontal, SIZE * 15], [SIZE * 285 + indent_horizontal, SIZE * 85], [SIZE * 215 + indent_horizontal, SIZE * 85]])
        pygame.draw.rect(sc, GREEN, (SIZE * 230 + indent_horizontal, SIZE * 30, SIZE * 10, SIZE * 20))
        pygame.draw.rect(sc, GREEN, (SIZE * 260 + indent_horizontal, SIZE * 30, SIZE * 10, SIZE * 20))
        pygame.draw.polygon(sc, DARK_GREEN, [[SIZE * 225 + indent_horizontal, SIZE * 25], [SIZE * 245 + indent_horizontal, SIZE * 30], [SIZE * 245 + indent_horizontal, SIZE * 40], [SIZE * 225 + indent_horizontal, SIZE * 35]])
        pygame.draw.polygon(sc, DARK_GREEN, [[SIZE * 255 + indent_horizontal, SIZE * 40], [SIZE * 275 + indent_horizontal, SIZE * 35], [SIZE * 275 + indent_horizontal, SIZE * 25], [SIZE * 255 + indent_horizontal, SIZE * 30]])
        pygame.draw.polygon(sc, GREEN, [[SIZE * 235 + indent_horizontal, SIZE * 70], [SIZE * 245 + indent_horizontal, SIZE * 65], [SIZE * 255 + indent_horizontal, SIZE * 65], [SIZE * 265 + indent_horizontal, SIZE * 70], [SIZE * 265 + indent_horizontal, SIZE * 80], [SIZE * 255 + indent_horizontal, SIZE * 75], [SIZE * 245 + indent_horizontal, SIZE * 75], [SIZE * 235 + indent_horizontal, SIZE * 80]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 260 + indent_horizontal, SIZE * 95], [SIZE * 260 + indent_horizontal, SIZE * 115], [SIZE * 275 + indent_horizontal, SIZE * 125], [SIZE * 275 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 125], [SIZE * 240 + indent_horizontal, SIZE * 115], [SIZE * 240 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 225 + indent_horizontal, SIZE * 200], [SIZE * 275 + indent_horizontal, SIZE * 200], [SIZE * 275 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 240 + indent_horizontal, SIZE * 200], [SIZE * 240 + indent_horizontal, SIZE * 280], [SIZE * 230 + indent_horizontal, SIZE * 280], [SIZE * 230 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 260 + indent_horizontal, SIZE * 200], [SIZE * 260 + indent_horizontal, SIZE * 280], [SIZE * 270 + indent_horizontal, SIZE * 280], [SIZE * 270 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 220 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 160], [SIZE * 270 + indent_horizontal, SIZE * 160], [SIZE * 270 + indent_horizontal, SIZE * 170], [SIZE * 230 + indent_horizontal, SIZE * 170], [SIZE * 220 + indent_horizontal, SIZE * 170]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 220 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 160], [SIZE * 270 + indent_horizontal, SIZE * 160], [SIZE * 270 + indent_horizontal, SIZE * 170], [SIZE * 230 + indent_horizontal, SIZE * 170], [SIZE * 220 + indent_horizontal, SIZE * 170]], 2)
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 270 + indent_horizontal, SIZE * 125], [SIZE * 280 + indent_horizontal, SIZE * 125], [SIZE * 280 + indent_horizontal, SIZE * 160], [SIZE * 270 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 270 + indent_horizontal, SIZE * 125], [SIZE * 280 + indent_horizontal, SIZE * 125], [SIZE * 280 + indent_horizontal, SIZE * 160], [SIZE * 270 + indent_horizontal, SIZE * 160]], 2)
        pygame.draw.polygon(sc, BROWN, [[SIZE * 270 + indent_horizontal, SIZE * 145], [SIZE * 280 + indent_horizontal, SIZE * 145], [SIZE * 280 + indent_horizontal, SIZE * 165], [SIZE * 270 + indent_horizontal, SIZE * 165]])
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 272 + indent_horizontal, SIZE * 147], [SIZE * 278 + indent_horizontal, SIZE * 147], [SIZE * 278 + indent_horizontal, SIZE * 153], [SIZE * 272 + indent_horizontal, SIZE * 153]])
    elif right == "enemy2_corpse_0":
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 205 + indent_horizontal, SIZE * 5], [SIZE * 295 + indent_horizontal, SIZE * 5], [SIZE * 295 + indent_horizontal, SIZE * 95], [SIZE * 205 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLUE, [[SIZE * 215 + indent_horizontal, SIZE * 15], [SIZE * 285 + indent_horizontal, SIZE * 15], [SIZE * 285 + indent_horizontal, SIZE * 85], [SIZE * 215 + indent_horizontal, SIZE * 85]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 235 + indent_horizontal, SIZE * 25], [SIZE * 265 + indent_horizontal, SIZE * 25]], 15)
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 220 + indent_horizontal, SIZE * 35], [SIZE * 280 + indent_horizontal, SIZE * 35]], 10)
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 220 + indent_horizontal, SIZE * 45], [SIZE * 280 + indent_horizontal, SIZE * 45]], 10)
        pygame.draw.polygon(sc, WHITE, [[SIZE * 260 + indent_horizontal, SIZE * 95], [SIZE * 260 + indent_horizontal, SIZE * 115], [SIZE * 275 + indent_horizontal, SIZE * 125], [SIZE * 275 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 125], [SIZE * 240 + indent_horizontal, SIZE * 115], [SIZE * 240 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 225 + indent_horizontal, SIZE * 200], [SIZE * 275 + indent_horizontal, SIZE * 200], [SIZE * 275 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 240 + indent_horizontal, SIZE * 200], [SIZE * 240 + indent_horizontal, SIZE * 280], [SIZE * 230 + indent_horizontal, SIZE * 280], [SIZE * 230 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 260 + indent_horizontal, SIZE * 200], [SIZE * 260 + indent_horizontal, SIZE * 280], [SIZE * 270 + indent_horizontal, SIZE * 280], [SIZE * 270 + indent_horizontal, SIZE * 200]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 270 + indent_horizontal, SIZE * 125], [SIZE * 280 + indent_horizontal, SIZE * 125], [SIZE * 290 + indent_horizontal, SIZE * 160], [SIZE * 280 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 270 + indent_horizontal, SIZE * 125], [SIZE * 280 + indent_horizontal, SIZE * 125], [SIZE * 290 + indent_horizontal, SIZE * 160], [SIZE * 280 + indent_horizontal, SIZE * 160]], 2)
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 220 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 180], [SIZE * 220 + indent_horizontal, SIZE * 180]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 220 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 180], [SIZE * 220 + indent_horizontal, SIZE * 180]], 2)
    elif right == "enemy2_corpse_1":
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 205 + indent_horizontal, SIZE * 5], [SIZE * 295 + indent_horizontal, SIZE * 5], [SIZE * 295 + indent_horizontal, SIZE * 95], [SIZE * 205 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 215 + indent_horizontal, SIZE * 15], [SIZE * 285 + indent_horizontal, SIZE * 15], [SIZE * 285 + indent_horizontal, SIZE * 85], [SIZE * 215 + indent_horizontal, SIZE * 85]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 220 + indent_horizontal, SIZE * 30], [SIZE * 243 + indent_horizontal, SIZE * 18], [SIZE * 269 + indent_horizontal, SIZE * 45], [SIZE * 260 + indent_horizontal, SIZE * 50], [SIZE * 280 + indent_horizontal, SIZE * 65], [SIZE * 276 + indent_horizontal, SIZE * 72], [SIZE * 254 + indent_horizontal, SIZE * 80], [SIZE * 260 + indent_horizontal, SIZE * 62], [SIZE * 250 + indent_horizontal, SIZE * 80], [SIZE * 220 + indent_horizontal, SIZE * 49]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 260 + indent_horizontal, SIZE * 95], [SIZE * 260 + indent_horizontal, SIZE * 115], [SIZE * 275 + indent_horizontal, SIZE * 125], [SIZE * 275 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 125], [SIZE * 240 + indent_horizontal, SIZE * 115], [SIZE * 240 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 225 + indent_horizontal, SIZE * 200], [SIZE * 275 + indent_horizontal, SIZE * 200], [SIZE * 275 + indent_horizontal, SIZE * 220], [SIZE * 225 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 240 + indent_horizontal, SIZE * 200], [SIZE * 240 + indent_horizontal, SIZE * 280], [SIZE * 230 + indent_horizontal, SIZE * 280], [SIZE * 230 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 260 + indent_horizontal, SIZE * 200], [SIZE * 260 + indent_horizontal, SIZE * 280], [SIZE * 270 + indent_horizontal, SIZE * 280], [SIZE * 270 + indent_horizontal, SIZE * 200]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 270 + indent_horizontal, SIZE * 125], [SIZE * 280 + indent_horizontal, SIZE * 125], [SIZE * 290 + indent_horizontal, SIZE * 160], [SIZE * 280 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 270 + indent_horizontal, SIZE * 125], [SIZE * 280 + indent_horizontal, SIZE * 125], [SIZE * 290 + indent_horizontal, SIZE * 160], [SIZE * 280 + indent_horizontal, SIZE * 160]], 2)
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 220 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 180], [SIZE * 220 + indent_horizontal, SIZE * 180]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 220 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 125], [SIZE * 230 + indent_horizontal, SIZE * 180], [SIZE * 220 + indent_horizontal, SIZE * 180]], 2)
    elif right == "enemy2_corpse_2":
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 205 + indent_horizontal, SIZE * 105], [SIZE * 295 + indent_horizontal, SIZE * 105], [SIZE * 295 + indent_horizontal, SIZE * 195], [SIZE * 205 + indent_horizontal, SIZE * 195]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 215 + indent_horizontal, SIZE * 115], [SIZE * 285 + indent_horizontal, SIZE * 115], [SIZE * 285 + indent_horizontal, SIZE * 185], [SIZE * 215 + indent_horizontal, SIZE * 185]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 220 + indent_horizontal, SIZE * 130], [SIZE * 243 + indent_horizontal, SIZE * 118], [SIZE * 269 + indent_horizontal, SIZE * 145], [SIZE * 260 + indent_horizontal, SIZE * 150], [SIZE * 280 + indent_horizontal, SIZE * 165], [SIZE * 276 + indent_horizontal, SIZE * 172], [SIZE * 254 + indent_horizontal, SIZE * 180], [SIZE * 260 + indent_horizontal, SIZE * 162], [SIZE * 250 + indent_horizontal, SIZE * 180], [SIZE * 220 + indent_horizontal, SIZE * 149]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 260 + indent_horizontal, SIZE * 195], [SIZE * 260 + indent_horizontal, SIZE * 215], [SIZE * 275 + indent_horizontal, SIZE * 225], [SIZE * 275 + indent_horizontal, SIZE * 320], [SIZE * 225 + indent_horizontal, SIZE * 320], [SIZE * 225 + indent_horizontal, SIZE * 225], [SIZE * 240 + indent_horizontal, SIZE * 215], [SIZE * 240 + indent_horizontal, SIZE * 195]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 270 + indent_horizontal, SIZE * 225], [SIZE * 280 + indent_horizontal, SIZE * 225], [SIZE * 290 + indent_horizontal, SIZE * 260], [SIZE * 280 + indent_horizontal, SIZE * 260]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 270 + indent_horizontal, SIZE * 225], [SIZE * 280 + indent_horizontal, SIZE * 225], [SIZE * 290 + indent_horizontal, SIZE * 260], [SIZE * 280 + indent_horizontal, SIZE * 260]], 2)
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 220 + indent_horizontal, SIZE * 225], [SIZE * 230 + indent_horizontal, SIZE * 225], [SIZE * 230 + indent_horizontal, SIZE * 280], [SIZE * 220 + indent_horizontal, SIZE * 280]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 220 + indent_horizontal, SIZE * 225], [SIZE * 230 + indent_horizontal, SIZE * 225], [SIZE * 230 + indent_horizontal, SIZE * 280], [SIZE * 220 + indent_horizontal, SIZE * 280]], 2)
    elif right == "enemy2_corpse_3":
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 205 + indent_horizontal, SIZE * 205], [SIZE * 295 + indent_horizontal, SIZE * 205], [SIZE * 295 + indent_horizontal, SIZE * 295], [SIZE * 205 + indent_horizontal, SIZE * 295]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 215 + indent_horizontal, SIZE * 215], [SIZE * 285 + indent_horizontal, SIZE * 215], [SIZE * 285 + indent_horizontal, SIZE * 285], [SIZE * 215 + indent_horizontal, SIZE * 285]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 220 + indent_horizontal, SIZE * 230], [SIZE * 243 + indent_horizontal, SIZE * 218], [SIZE * 269 + indent_horizontal, SIZE * 245], [SIZE * 260 + indent_horizontal, SIZE * 250], [SIZE * 280 + indent_horizontal, SIZE * 265], [SIZE * 276 + indent_horizontal, SIZE * 272], [SIZE * 254 + indent_horizontal, SIZE * 280], [SIZE * 260 + indent_horizontal, SIZE * 262], [SIZE * 250 + indent_horizontal, SIZE * 280], [SIZE * 220 + indent_horizontal, SIZE * 249]])
        pygame.draw.polygon(sc, MAGENTA, [[SIZE * 269 + indent_horizontal, SIZE * 245], [SIZE * 269 + indent_horizontal, SIZE * 300], [SIZE * 220 + indent_horizontal, SIZE * 300], [SIZE * 220 + indent_horizontal, SIZE * 249]])
    if middle == "wall2" or middle == "wall":
        pygame.draw.polygon(sc, NAVY, [[SIZE * 100 + indent_horizontal, SIZE * 100], [SIZE * 200 + indent_horizontal, SIZE * 100], [SIZE * 200 + indent_horizontal, SIZE * 200], [SIZE * 100 + indent_horizontal, SIZE * 200]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 105 + indent_horizontal, SIZE * 105], [SIZE * 195 + indent_horizontal, SIZE * 105], [SIZE * 195 + indent_horizontal, SIZE * 195], [SIZE * 105 + indent_horizontal, SIZE * 195]], 3)
    elif middle == "medkit":
        pygame.draw.polygon(sc, MEDKIT, [[SIZE * 110 + indent_horizontal, SIZE * 110], [SIZE * 190 + indent_horizontal, SIZE * 110], [SIZE * 190 + indent_horizontal, SIZE * 190], [SIZE * 110 + indent_horizontal, SIZE * 190]])
        pygame.draw.rect(sc, WHITE, (SIZE * 111 + indent_horizontal, SIZE * 110, SIZE * 78, SIZE * 26), 8)
        pygame.draw.polygon(sc, RED, [[SIZE * 120 + indent_horizontal, SIZE * 145], [SIZE * 145 + indent_horizontal, SIZE * 145], [SIZE * 145 + indent_horizontal, SIZE * 120], [SIZE * 155 + indent_horizontal, SIZE * 120], [SIZE * 155 + indent_horizontal, SIZE * 145], [SIZE * 180 + indent_horizontal, SIZE * 145], [SIZE * 180 + indent_horizontal, SIZE * 155], [SIZE * 180 + indent_horizontal, SIZE * 155], [SIZE * 155 + indent_horizontal, SIZE * 155], [SIZE * 155 + indent_horizontal, SIZE * 180], [SIZE * 145 + indent_horizontal, SIZE * 180], [SIZE * 145 + indent_horizontal, SIZE * 155], [SIZE * 120 + indent_horizontal, SIZE * 155]])
    elif middle == "bullets":
        pygame.draw.polygon(sc, LIGHTYELLOW, [[SIZE * 135 + indent_horizontal, SIZE * 135], [SIZE * 140 + indent_horizontal, SIZE * 130], [SIZE * 145 + indent_horizontal, SIZE * 135], [SIZE * 145 + indent_horizontal, SIZE * 160], [SIZE * 135 + indent_horizontal, SIZE * 160]])
        pygame.draw.polygon(sc, LIGHTYELLOW, [[SIZE * 155 + indent_horizontal, SIZE * 135], [SIZE * 160 + indent_horizontal, SIZE * 130], [SIZE * 165 + indent_horizontal, SIZE * 135], [SIZE * 165 + indent_horizontal, SIZE * 160], [SIZE * 155 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, YELLOW, True, [[SIZE * 135 + indent_horizontal, SIZE * 137], [SIZE * 145 + indent_horizontal, SIZE * 137]], 5)
        pygame.draw.lines(sc, YELLOW, True, [[SIZE * 155 + indent_horizontal, SIZE * 137], [SIZE * 165 + indent_horizontal, SIZE * 137]], 5)
    elif middle == "enemy1":
        pygame.draw.polygon(sc, WHITE, [[SIZE * 105 + indent_horizontal, 5], [SIZE * 195 + indent_horizontal, 5], [SIZE * 195 + indent_horizontal, SIZE * 95], [SIZE * 105 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 115 + indent_horizontal, SIZE * 15], [SIZE * 185 + indent_horizontal, SIZE * 15], [SIZE * 185 + indent_horizontal, SIZE * 85], [SIZE * 115 + indent_horizontal, SIZE * 85]])
        pygame.draw.rect(sc, GREEN, (SIZE * 130 + indent_horizontal, SIZE * 30, SIZE * 10, SIZE * 20))
        pygame.draw.rect(sc, GREEN, (SIZE * 160 + indent_horizontal, SIZE * 30, SIZE * 10, SIZE * 20))
        pygame.draw.polygon(sc, DARK_GREEN, [[SIZE * 125 + indent_horizontal, SIZE * 25], [SIZE * 145 + indent_horizontal, SIZE * 30], [SIZE * 145 + indent_horizontal, SIZE * 40], [SIZE * 125 + indent_horizontal, SIZE * 35]])
        pygame.draw.polygon(sc, DARK_GREEN, [[SIZE * 155 + indent_horizontal, SIZE * 40], [SIZE * 175 + indent_horizontal, SIZE * 35], [SIZE * 175 + indent_horizontal, SIZE * 25], [SIZE * 155 + indent_horizontal, SIZE * 30]])
        pygame.draw.polygon(sc, GREEN, [[SIZE * 135 + indent_horizontal, SIZE * 70], [SIZE * 145 + indent_horizontal, SIZE * 65], [SIZE * 155 + indent_horizontal, SIZE * 65], [SIZE * 165 + indent_horizontal, SIZE * 70], [SIZE * 165 + indent_horizontal, SIZE * 80], [SIZE * 155 + indent_horizontal, SIZE * 75], [SIZE * 145 + indent_horizontal, SIZE * 75], [SIZE * 135 + indent_horizontal, SIZE * 80]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 160 + indent_horizontal, SIZE * 95], [SIZE * 160 + indent_horizontal, SIZE * 115], [SIZE * 175 + indent_horizontal, SIZE * 125], [SIZE * 175 + indent_horizontal, SIZE * 220], [SIZE * 125 + indent_horizontal, SIZE * 220], [SIZE * 125 + indent_horizontal, SIZE * 125], [SIZE * 140 + indent_horizontal, SIZE * 115], [SIZE * 140 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 125 + indent_horizontal, SIZE * 200], [SIZE * 175 + indent_horizontal, SIZE * 200], [SIZE * 175 + indent_horizontal, SIZE * 220], [SIZE * 125 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 140 + indent_horizontal, SIZE * 200], [SIZE * 140 + indent_horizontal, SIZE * 280], [SIZE * 130 + indent_horizontal, SIZE * 280], [SIZE * 130 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 160 + indent_horizontal, SIZE * 200], [SIZE * 160 + indent_horizontal, SIZE * 280], [SIZE * 170 + indent_horizontal, SIZE * 280], [SIZE * 170 + indent_horizontal, SIZE * 200]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 170 + indent_horizontal, SIZE * 125], [SIZE * 180 + indent_horizontal, SIZE * 125], [SIZE * 190 + indent_horizontal, SIZE * 160], [SIZE * 180 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 170 + indent_horizontal, SIZE * 125], [SIZE * 180 + indent_horizontal, SIZE * 125], [SIZE * 190 + indent_horizontal, SIZE * 160], [SIZE * 180 + indent_horizontal, SIZE * 160]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 180 + indent_horizontal, SIZE * 145], [SIZE * 190 + indent_horizontal, SIZE * 145], [SIZE * 190 + indent_horizontal, SIZE * 165], [SIZE * 180 + indent_horizontal, SIZE * 165]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 182 + indent_horizontal, SIZE * 147], [SIZE * 188 + indent_horizontal, SIZE * 147], [SIZE * 188 + indent_horizontal, SIZE * 153], [SIZE * 182 + indent_horizontal, SIZE * 153]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 120 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 180], [SIZE * 120 + indent_horizontal, SIZE * 180]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 120 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 180], [SIZE * 120 + indent_horizontal, SIZE * 180]], 2)
    elif middle == "enemy1_corpse_0":
        pygame.draw.polygon(sc, WHITE, [[SIZE * 105 + indent_horizontal, SIZE * 5], [SIZE * 195 + indent_horizontal, SIZE * 5], [SIZE * 195 + indent_horizontal, SIZE * 95], [SIZE * 105 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLUE, [[SIZE * 115 + indent_horizontal, SIZE * 15], [SIZE * 185 + indent_horizontal, SIZE * 15], [SIZE * 185 + indent_horizontal, SIZE * 85], [SIZE * 115 + indent_horizontal, SIZE * 85]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 135 + indent_horizontal, SIZE * 25], [SIZE * 165 + indent_horizontal, SIZE * 25]], 15)
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 120 + indent_horizontal, SIZE * 35], [SIZE * 180 + indent_horizontal, SIZE * 35]], 10)
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 120 + indent_horizontal, SIZE * 45], [SIZE * 180 + indent_horizontal, SIZE * 45]], 10)
        pygame.draw.polygon(sc, WHITE, [[SIZE * 160 + indent_horizontal, SIZE * 95], [SIZE * 160 + indent_horizontal, SIZE * 115], [SIZE * 175 + indent_horizontal, SIZE * 125], [SIZE * 175 + indent_horizontal, SIZE * 220], [SIZE * 125 + indent_horizontal, SIZE * 220], [SIZE * 125 + indent_horizontal, SIZE * 125], [SIZE * 140 + indent_horizontal, SIZE * 115], [SIZE * 140 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 125 + indent_horizontal, SIZE * 200], [SIZE * 175 + indent_horizontal, SIZE * 200], [SIZE * 175 + indent_horizontal, SIZE * 220], [SIZE * 125 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 140 + indent_horizontal, SIZE * 200], [SIZE * 140 + indent_horizontal, SIZE * 280], [SIZE * 130 + indent_horizontal, SIZE * 280], [SIZE * 130 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 160 + indent_horizontal, SIZE * 200], [SIZE * 160 + indent_horizontal, SIZE * 280], [SIZE * 170 + indent_horizontal, SIZE * 280], [SIZE * 170 + indent_horizontal, SIZE * 200]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 170 + indent_horizontal, SIZE * 125], [SIZE * 180 + indent_horizontal, SIZE * 125], [SIZE * 190 + indent_horizontal, SIZE * 160], [SIZE * 180 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 170 + indent_horizontal, SIZE * 125], [SIZE * 180 + indent_horizontal, SIZE * 125], [SIZE * 190 + indent_horizontal, SIZE * 160], [SIZE * 180 + indent_horizontal, SIZE * 160]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 180 + indent_horizontal, SIZE * 145], [SIZE * 190 + indent_horizontal, SIZE * 145], [SIZE * 190 + indent_horizontal, SIZE * 165], [SIZE * 180 + indent_horizontal, SIZE * 165]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 182 + indent_horizontal, SIZE * 147], [SIZE * 188 + indent_horizontal, SIZE * 147], [SIZE * 188 + indent_horizontal, SIZE * 153], [SIZE * 182 + indent_horizontal, SIZE * 153]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 120 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 180], [SIZE * 120 + indent_horizontal, SIZE * 180]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 120 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 180], [SIZE * 120 + indent_horizontal, SIZE * 180]], 2)
    elif middle == "enemy1_corpse_1":
        pygame.draw.polygon(sc, WHITE, [[SIZE * 105 + indent_horizontal, SIZE * 5], [SIZE * 195 + indent_horizontal, SIZE * 5], [SIZE * 195 + indent_horizontal, SIZE * 95], [SIZE * 105 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 115 + indent_horizontal, SIZE * 15], [SIZE * 185 + indent_horizontal, SIZE * 15], [SIZE * 185 + indent_horizontal, SIZE * 85], [SIZE * 115 + indent_horizontal, SIZE * 85]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 120 + indent_horizontal, SIZE * 30], [SIZE * 143 + indent_horizontal, SIZE * 18], [SIZE * 169 + indent_horizontal, SIZE * 45], [SIZE * 160 + indent_horizontal, SIZE * 50], [SIZE * 180 + indent_horizontal, SIZE * 65], [SIZE * 176 + indent_horizontal, SIZE * 72], [SIZE * 154 + indent_horizontal, SIZE * 80], [SIZE * 160 + indent_horizontal, SIZE * 62], [SIZE * 150 + indent_horizontal, SIZE * 80], [SIZE * 120 + indent_horizontal, SIZE * 49]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 160 + indent_horizontal, SIZE * 95], [SIZE * 160 + indent_horizontal, SIZE * 115], [SIZE * 175 + indent_horizontal, SIZE * 125], [SIZE * 175 + indent_horizontal, SIZE * 220], [SIZE * 125 + indent_horizontal, SIZE * 220], [SIZE * 125 + indent_horizontal, SIZE * 125], [SIZE * 140 + indent_horizontal, SIZE * 115], [SIZE * 140 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 125 + indent_horizontal, SIZE * 200], [SIZE * 175 + indent_horizontal, SIZE * 200], [SIZE * 175 + indent_horizontal, SIZE * 220], [SIZE * 125 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 140 + indent_horizontal, SIZE * 200], [SIZE * 140 + indent_horizontal, SIZE * 280], [SIZE * 130 + indent_horizontal, SIZE * 280], [SIZE * 130 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 160 + indent_horizontal, SIZE * 200], [SIZE * 160 + indent_horizontal, SIZE * 280], [SIZE * 170 + indent_horizontal, SIZE * 280], [SIZE * 170 + indent_horizontal, SIZE * 200]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 170 + indent_horizontal, SIZE * 125], [SIZE * 180 + indent_horizontal, SIZE * 125], [SIZE * 190 + indent_horizontal, SIZE * 160], [SIZE * 180 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 170 + indent_horizontal, SIZE * 125], [SIZE * 180 + indent_horizontal, SIZE * 125], [SIZE * 190 + indent_horizontal, SIZE * 160], [SIZE * 180 + indent_horizontal, SIZE * 160]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 180 + indent_horizontal, SIZE * 145], [SIZE * 190 + indent_horizontal, SIZE * 145], [SIZE * 190 + indent_horizontal, SIZE * 165], [SIZE * 180 + indent_horizontal, SIZE * 165]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 182 + indent_horizontal, SIZE * 147], [SIZE * 188 + indent_horizontal, SIZE * 147], [SIZE * 188 + indent_horizontal, SIZE * 153], [SIZE * 182 + indent_horizontal, SIZE * 153]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 120 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 180], [SIZE * 120 + indent_horizontal, SIZE * 180]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 120 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 180], [SIZE * 120 + indent_horizontal, SIZE * 180]], 2)
    elif middle == "enemy1_corpse_2":
        pygame.draw.polygon(sc, WHITE, [[SIZE * 105 + indent_horizontal, SIZE * 105], [SIZE * 195 + indent_horizontal, SIZE * 105], [SIZE * 195 + indent_horizontal, SIZE * 195], [SIZE * 105 + indent_horizontal, SIZE * 195]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 115 + indent_horizontal, SIZE * 115], [SIZE * 185 + indent_horizontal, SIZE * 115], [SIZE * 185 + indent_horizontal, SIZE * 185], [SIZE * 115 + indent_horizontal, SIZE * 185]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 120 + indent_horizontal, SIZE * 130], [SIZE * 143 + indent_horizontal, SIZE * 118], [SIZE * 169 + indent_horizontal, SIZE * 145], [SIZE * 160 + indent_horizontal, SIZE * 150], [SIZE * 180 + indent_horizontal, SIZE * 165], [SIZE * 176 + indent_horizontal, SIZE * 172], [SIZE * 154 + indent_horizontal, SIZE * 180], [SIZE * 160 + indent_horizontal, SIZE * 162], [SIZE * 150 + indent_horizontal, SIZE * 180], [SIZE * 120 + indent_horizontal, SIZE * 149]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 160 + indent_horizontal, SIZE * 195], [SIZE * 160 + indent_horizontal, SIZE * 215], [SIZE * 175 + indent_horizontal, SIZE * 225], [SIZE * 175 + indent_horizontal, SIZE * 320], [SIZE * 125 + indent_horizontal, SIZE * 320], [SIZE * 125 + indent_horizontal, SIZE * 225], [SIZE * 140 + indent_horizontal, SIZE * 215], [SIZE * 140 + indent_horizontal, SIZE * 195]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 125 + indent_horizontal, SIZE * 300], [SIZE * 175 + indent_horizontal, SIZE * 300], [SIZE * 175 + indent_horizontal, SIZE * 320], [SIZE * 125 + indent_horizontal, SIZE * 320]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 140 + indent_horizontal, SIZE * 300], [SIZE * 140 + indent_horizontal, SIZE * 380], [SIZE * 130 + indent_horizontal, SIZE * 380], [SIZE * 130 + indent_horizontal, SIZE * 300]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 160 + indent_horizontal, SIZE * 300], [SIZE * 160 + indent_horizontal, SIZE * 380], [SIZE * 170 + indent_horizontal, SIZE * 380], [SIZE * 170 + indent_horizontal, SIZE * 300]])
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 170 + indent_horizontal, SIZE * 225], [SIZE * 180 + indent_horizontal, SIZE * 225], [SIZE * 190 + indent_horizontal, SIZE * 260], [SIZE * 180 + indent_horizontal, SIZE * 260]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 170 + indent_horizontal, SIZE * 225], [SIZE * 180 + indent_horizontal, SIZE * 225], [SIZE * 190 + indent_horizontal, SIZE * 260], [SIZE * 180 + indent_horizontal, SIZE * 260]], 2)
        pygame.draw.polygon(sc, RED, [[SIZE * 180 + indent_horizontal, SIZE * 245], [SIZE * 190 + indent_horizontal, SIZE * 245], [SIZE * 190 + indent_horizontal, SIZE * 265], [SIZE * 180 + indent_horizontal, SIZE * 265]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 182 + indent_horizontal, SIZE * 247], [SIZE * 188 + indent_horizontal, SIZE * 247], [SIZE * 188 + indent_horizontal, SIZE * 253], [SIZE * 182 + indent_horizontal, SIZE * 253]])
        # hand right(empty) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 120 + indent_horizontal, SIZE * 225], [SIZE * 130 + indent_horizontal, SIZE * 225], [SIZE * 130 + indent_horizontal, SIZE * 280], [SIZE * 120 + indent_horizontal, SIZE * 280]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 120 + indent_horizontal, SIZE * 225], [SIZE * 130 + indent_horizontal, SIZE * 225], [SIZE * 130 + indent_horizontal, SIZE * 280], [SIZE * 120 + indent_horizontal, SIZE * 280]], 2)
    elif middle == "enemy1_corpse_3":
        pygame.draw.polygon(sc, WHITE, [[SIZE * 105 + indent_horizontal, SIZE * 205], [SIZE * 195 + indent_horizontal, SIZE * 205], [SIZE * 195 + indent_horizontal, SIZE * 295], [SIZE * 105 + indent_horizontal, SIZE * 295]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 115 + indent_horizontal, SIZE * 215], [SIZE * 185 + indent_horizontal, SIZE * 215], [SIZE * 185 + indent_horizontal, SIZE * 285], [SIZE * 115 + indent_horizontal, SIZE * 285]])
        pygame.draw.polygon(sc, GRAY, [[SIZE * 120 + indent_horizontal, SIZE * 230], [SIZE * 143 + indent_horizontal, SIZE * 218], [SIZE * 169 + indent_horizontal, SIZE * 245], [SIZE * 160 + indent_horizontal, SIZE * 250], [SIZE * 180 + indent_horizontal, SIZE * 265], [SIZE * 176 + indent_horizontal, SIZE * 272], [SIZE * 154 + indent_horizontal, SIZE * 280], [SIZE * 160 + indent_horizontal, SIZE * 262], [SIZE * 150 + indent_horizontal, SIZE * 280], [SIZE * 120 + indent_horizontal, SIZE * 249]])
        pygame.draw.polygon(sc, MAGENTA, [[SIZE * 169 + indent_horizontal, SIZE * 245], [SIZE * 169 + indent_horizontal, SIZE * 300], [SIZE * 120 + indent_horizontal, SIZE * 300], [SIZE * 120 + indent_horizontal, SIZE * 249]])
    elif middle == "enemy2":
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 105 + indent_horizontal, 5], [SIZE * 195 + indent_horizontal, 5], [SIZE * 195 + indent_horizontal, SIZE * 95], [SIZE * 105 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 115 + indent_horizontal, SIZE * 15], [SIZE * 185 + indent_horizontal, SIZE * 15], [SIZE * 185 + indent_horizontal, SIZE * 85], [SIZE * 115 + indent_horizontal, SIZE * 85]])
        pygame.draw.rect(sc, GREEN, (SIZE * 130 + indent_horizontal, SIZE * 30, SIZE * 10, SIZE * 20))
        pygame.draw.rect(sc, GREEN, (SIZE * 160 + indent_horizontal, SIZE * 30, SIZE * 10, SIZE * 20))
        pygame.draw.polygon(sc, DARK_GREEN, [[SIZE * 125 + indent_horizontal, SIZE * 25], [SIZE * 145 + indent_horizontal, SIZE * 30], [SIZE * 145 + indent_horizontal, SIZE * 40], [SIZE * 125 + indent_horizontal, SIZE * 35]])
        pygame.draw.polygon(sc, DARK_GREEN, [[SIZE * 155 + indent_horizontal, SIZE * 40], [SIZE * 175 + indent_horizontal, SIZE * 35], [SIZE * 175 + indent_horizontal, SIZE * 25], [SIZE * 155 + indent_horizontal, SIZE * 30]])
        pygame.draw.polygon(sc, GREEN, [[SIZE * 135 + indent_horizontal, SIZE * 70], [SIZE * 145 + indent_horizontal, SIZE * 65], [SIZE * 155 + indent_horizontal, SIZE * 65], [SIZE * 165 + indent_horizontal, SIZE * 70], [SIZE * 165 + indent_horizontal, SIZE * 80], [SIZE * 155 + indent_horizontal, SIZE * 75], [SIZE * 145 + indent_horizontal, SIZE * 75], [SIZE * 135 + indent_horizontal, SIZE * 80]])
        pygame.draw.polygon(sc, WHITE, [[SIZE * 160 + indent_horizontal, SIZE * 95], [SIZE * 160 + indent_horizontal, SIZE * 115], [SIZE * 175 + indent_horizontal, SIZE * 125], [SIZE * 175 + indent_horizontal, SIZE * 220], [SIZE * 125 + indent_horizontal, SIZE * 220], [SIZE * 125 + indent_horizontal, SIZE * 125], [SIZE * 140 + indent_horizontal, SIZE * 115], [SIZE * 140 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 125 + indent_horizontal, SIZE * 200], [SIZE * 175 + indent_horizontal, SIZE * 200], [SIZE * 175 + indent_horizontal, SIZE * 220], [SIZE * 125 + indent_horizontal, SIZE * 220]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 140 + indent_horizontal, SIZE * 200], [SIZE * 140 + indent_horizontal, SIZE * 280], [SIZE * 130 + indent_horizontal, SIZE * 280], [SIZE * 130 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, JEANS, [[SIZE * 160 + indent_horizontal, SIZE * 200], [SIZE * 160 + indent_horizontal, SIZE * 280], [SIZE * 170 + indent_horizontal, SIZE * 280], [SIZE * 170 + indent_horizontal, SIZE * 200]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 120 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 160], [SIZE * 170 + indent_horizontal, SIZE * 160], [SIZE * 170 + indent_horizontal, SIZE * 170], [SIZE * 130 + indent_horizontal, SIZE * 170], [SIZE * 120 + indent_horizontal, SIZE * 170]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 120 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 125], [SIZE * 130 + indent_horizontal, SIZE * 160], [SIZE * 170 + indent_horizontal, SIZE * 160], [SIZE * 170 + indent_horizontal, SIZE * 170], [SIZE * 130 + indent_horizontal, SIZE * 170], [SIZE * 120 + indent_horizontal, SIZE * 170]], 2)
        # hand left(gun) v
        pygame.draw.polygon(sc, BLACK, [[SIZE * 170 + indent_horizontal, SIZE * 125], [SIZE * 180 + indent_horizontal, SIZE * 125], [SIZE * 180 + indent_horizontal, SIZE * 160], [SIZE * 170 + indent_horizontal, SIZE * 160]])
        pygame.draw.lines(sc, WHITE, True, [[SIZE * 170 + indent_horizontal, SIZE * 125], [SIZE * 180 + indent_horizontal, SIZE * 125], [SIZE * 180 + indent_horizontal, SIZE * 160], [SIZE * 170 + indent_horizontal, SIZE * 160]], 2)
        pygame.draw.polygon(sc, BROWN, [[SIZE * 170 + indent_horizontal, SIZE * 145], [SIZE * 180 + indent_horizontal, SIZE * 145], [SIZE * 180 + indent_horizontal, SIZE * 165], [SIZE * 170 + indent_horizontal, SIZE * 165]])
        pygame.draw.polygon(sc, YELLOW, [[SIZE * 172 + indent_horizontal, SIZE * 147], [SIZE * 178 + indent_horizontal, SIZE * 147], [SIZE * 178 + indent_horizontal, SIZE * 153], [SIZE * 172 + indent_horizontal, SIZE * 153]])


def drawWeapon(state, weapon):
    if weapon == "fist":
        if state == "idle":
            pygame.draw.polygon(sc, WHITE, [[SIZE * 185 + indent_horizontal, SIZE * 210], [SIZE * 280 + indent_horizontal, SIZE * 290], [SIZE * 250 + indent_horizontal, SIZE * 290], [SIZE * 175 + indent_horizontal, SIZE * 230]])
            pygame.draw.lines(sc, BLACK, False, [[SIZE * 185 + indent_horizontal, SIZE * 210], [SIZE * 280 + indent_horizontal, SIZE * 290], [SIZE * 250 + indent_horizontal, SIZE * 290], [SIZE * 175 + indent_horizontal, SIZE * 230]], 5)
            pygame.draw.polygon(sc, MAGENTA, [[SIZE * 170 + indent_horizontal, SIZE * 210], [SIZE * 190 + indent_horizontal, SIZE * 210], [SIZE * 190 + indent_horizontal, SIZE * 230], [SIZE * 170 + indent_horizontal, SIZE * 230]])
        elif state == "attack":
            pygame.draw.polygon(sc, WHITE, [[SIZE * 155 + indent_horizontal, SIZE * 180], [SIZE * 280 + indent_horizontal, SIZE * 290], [SIZE * 250 + indent_horizontal, SIZE * 290], [SIZE * 145 + indent_horizontal, SIZE * 200]])
            pygame.draw.lines(sc, BLACK, False, [[SIZE * 155 + indent_horizontal, SIZE * 180], [SIZE * 280 + indent_horizontal, SIZE * 290], [SIZE * 250 + indent_horizontal, SIZE * 290], [SIZE * 145 + indent_horizontal, SIZE * 200]], 5)
            pygame.draw.polygon(sc, MAGENTA, [[SIZE * 140 + indent_horizontal, SIZE * 180], [SIZE * 160 + indent_horizontal, SIZE * 180], [SIZE * 160 + indent_horizontal, SIZE * 200], [SIZE * 140 + indent_horizontal, SIZE * 200]])
    elif weapon == "pistol":
        if state == "idle":
            pygame.draw.polygon(sc, WHITE, [[SIZE * 150 + indent_horizontal, SIZE * 150], [SIZE * 170 + indent_horizontal, SIZE * 150], [SIZE * 270 + indent_horizontal, SIZE * 190], [SIZE * 270 + indent_horizontal, SIZE * 270], [SIZE * 260 + indent_horizontal, SIZE * 270]])
            pygame.draw.polygon(sc, GRAY, [[SIZE * 150 + indent_horizontal, SIZE * 150], [SIZE * 250 + indent_horizontal, SIZE * 200], [SIZE * 250 + indent_horizontal, SIZE * 280], [SIZE * 190 + indent_horizontal, SIZE * 200], [SIZE * 150 + indent_horizontal, SIZE * 180]])
            pygame.draw.polygon(sc, WHITE, [[SIZE * 245 + indent_horizontal, SIZE * 250], [SIZE * 300 + indent_horizontal, SIZE * 290], [SIZE * 270 + indent_horizontal, SIZE * 290], [SIZE * 235 + indent_horizontal, SIZE * 270]])
            pygame.draw.lines(sc, BLACK, False, [[SIZE * 245 + indent_horizontal, SIZE * 250], [SIZE * 300 + indent_horizontal, SIZE * 290], [SIZE * 270 + indent_horizontal, SIZE * 290], [SIZE * 235 + indent_horizontal, SIZE * 270]], 5)
            pygame.draw.polygon(sc, MAGENTA, [[SIZE * 230 + indent_horizontal, SIZE * 250], [SIZE * 250 + indent_horizontal, SIZE * 250], [SIZE * 250 + indent_horizontal, SIZE * 270], [SIZE * 230 + indent_horizontal, SIZE * 270]])
        elif state == "attack":
            pygame.draw.polygon(sc, YELLOW, [[SIZE * 145 + indent_horizontal, SIZE * 145], [SIZE * 175 + indent_horizontal, SIZE * 145], [SIZE * 175 + indent_horizontal, SIZE * 190], [SIZE * 145 + indent_horizontal, SIZE * 190]])
            pygame.draw.polygon(sc, WHITE, [[SIZE * 150 + indent_horizontal, SIZE * 150], [SIZE * 170 + indent_horizontal, SIZE * 150], [SIZE * 270 + indent_horizontal, SIZE * 190], [SIZE * 270 + indent_horizontal, SIZE * 270], [SIZE * 260 + indent_horizontal, SIZE * 270]])
            pygame.draw.polygon(sc, GRAY, [[SIZE * 150 + indent_horizontal, SIZE * 150], [SIZE * 250 + indent_horizontal, SIZE * 200], [SIZE * 250 + indent_horizontal, SIZE * 280], [SIZE * 190 + indent_horizontal, SIZE * 200], [SIZE * 150 + indent_horizontal, SIZE * 180]])
            pygame.draw.polygon(sc, WHITE, [[SIZE * 245 + indent_horizontal, SIZE * 250], [SIZE * 300 + indent_horizontal, SIZE * 290], [SIZE * 270 + indent_horizontal, SIZE * 290], [SIZE * 235 + indent_horizontal, SIZE * 270]])
            pygame.draw.lines(sc, BLACK, False, [[SIZE * 245 + indent_horizontal, SIZE * 250], [SIZE * 300 + indent_horizontal, SIZE * 290], [SIZE * 270 + indent_horizontal, SIZE * 290], [SIZE * 235 + indent_horizontal, SIZE * 270]], 5)
            pygame.draw.polygon(sc, MAGENTA, [[SIZE * 230 + indent_horizontal, SIZE * 250], [SIZE * 250 + indent_horizontal, SIZE * 250], [SIZE * 250 + indent_horizontal, SIZE * 270], [SIZE * 230 + indent_horizontal, SIZE * 270]])


def drawHUD(hp, ammo, lastact):
    pygame.draw.polygon(sc, GRAY, [[SIZE * 0 + indent_horizontal, SIZE * 270], [SIZE * 300 + indent_horizontal, SIZE * 270], [SIZE * 300 + indent_horizontal, SIZE * 300], [SIZE * 0 + indent_horizontal, SIZE * 300]])
    pygame.draw.lines(sc, LIGHTGRAY, False, [[SIZE * 125 + indent_horizontal, SIZE * 270], [SIZE * 125 + indent_horizontal, SIZE * 300]], 5)
    pygame.draw.lines(sc, LIGHTGRAY, False, [[SIZE * 175 + indent_horizontal, SIZE * 270], [SIZE * 175 + indent_horizontal, SIZE * 300]], 5)
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
            if disp_middle == "" or disp_middle == "enemy1_corpse_3" or disp_middle == "enemy2_corpse_3" or disp_middle == "bullets" or disp_middle == "medkit":
                if disp_middle == "bullets":
                    if direction == 0:
                        coords = str(y) + "-" + str(x - 1)
                        leveldict[coords] = ""
                    elif direction == 1:
                        coords = str(y + 1) + "-" + str(x)
                        leveldict[coords] = ""
                    elif direction == 2:
                        coords = str(y) + "-" + str(x + 1)
                        leveldict[coords] = ""
                    elif direction == 3:
                        coords = str(y - 1) + "-" + str(x)
                        leveldict[coords] = ""
                    ammo += 2
                if disp_middle == "medkit":
                    if direction == 0:
                        coords = str(y) + "-" + str(x - 1)
                        leveldict[coords] = ""
                    elif direction == 1:
                        coords = str(y + 1) + "-" + str(x)
                        leveldict[coords] = ""
                    elif direction == 2:
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
                        leveldict = leveldict_new.copy()
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
                screen = 1
            else:
                screen -= 1
            option = 0
    if last_key == "down":
                    if mode == "game":
                        turn = "enemy"
                        if y - 1 != 0:
                            disp_left, disp_middle, disp_right = look(x, y - 1, direction, leveldict)
                            if disp_middle == "" or disp_middle == "enemy1_corpse_3" or disp_middle == "enemy2_corpse_3" or disp_middle == "bullets" or disp_middle == "medkit":
                                if disp_middle == "bullets":
                                    if direction == 2:
                                        coords = str(y) + "-" + str(x - 1)
                                        leveldict[coords] = ""
                                    elif direction == 3:
                                        coords = str(y + 1) + "-" + str(x)
                                        leveldict[coords] = ""
                                    elif direction == 0:
                                        coords = str(y) + "-" + str(x + 1)
                                        leveldict[coords] = ""
                                    elif direction == 1:
                                        coords = str(y - 1) + "-" + str(x)
                                        leveldict[coords] = ""
                                    ammo += 2
                                if disp_middle == "medkit":
                                    if direction == 2:
                                        coords = str(y) + "-" + str(x - 1)
                                        leveldict[coords] = ""
                                    elif direction == 3:
                                        coords = str(y + 1) + "-" + str(x)
                                        leveldict[coords] = ""
                                    elif direction == 0:
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
                                        leveldict = leveldict_new.copy()
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
                        if screen == 1:
                            screen = 0

                        else:
                            screen += 1
                        option = 0
    elif last_key == "left":
        if mode == "game":
            turn = "enemy"
            if direction != 3:
                direction += 1
            else:
                direction = 0
        elif mode == "debug":
            if screen == 0:
                if option == 0:
                    option = 2
                else:
                    option -= 1
            else:
                if option == 0:
                    option = 1
                else:
                    option -= 1
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
                if option == 2:
                    option = 0
                else:
                    option += 1
            else:
                if option == 1:
                    option = 0
                else:
                    option += 1
    elif last_key == "space":
        if mode == "game":
            turn = "enemy"
            right, middle, left = look(x, y, direction, leveldict)
            if current_weapon == "fist":
                damage = randint(4, 11)
                weapon_action = "attack"
            elif current_weapon == "pistol":
                if ammo != 0:
                    weapon_action = "attack"
                    damage = randint(6, 15)
                    ammo -= 1
    
            if direction == 0:
                coords = str(y) + "-" + str(x + 1)
            elif direction == 1:
                coords = str(y + 1) + "-" + str(x)
            elif direction == 2:
                coords = str(y) + "-" + str(x - 1)
            elif direction == 3:
                coords = str(y - 1) + "-" + str(x)
            if middle == "enemy1" or middle == "enemy2":
                leveldict["health_enemy"] = leveldict["health_enemy"] - damage
                if leveldict["health_enemy"] <= 0:
                    leveldict[coords] = leveldict[coords] + "_corpse_3"
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
    if mode == "game":
        disp_left, disp_middle, disp_right = look(x, y, direction, leveldict)
        print(disp_left, disp_middle, disp_right)
        refresh(disp_left, disp_middle, disp_right, health, ammo, weapon_action, current_weapon)
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
        pygame.draw.polygon(sc, WHITE, [[SIZE * 105 + indent_horizontal, 5], [SIZE * 195 + indent_horizontal, 5], [SIZE * 195 + indent_horizontal, SIZE * 95], [SIZE * 105 + indent_horizontal, SIZE * 95]])
        pygame.draw.polygon(sc, BLACK, [[SIZE * 115 + indent_horizontal, SIZE * 15], [SIZE * 185 + indent_horizontal, SIZE * 15], [SIZE * 185 + indent_horizontal, SIZE * 85], [SIZE * 115 + indent_horizontal, SIZE * 85]])
        pygame.draw.rect(sc, GREEN, (SIZE * 130 + indent_horizontal, SIZE * 30, SIZE * 10, SIZE * 20))
        pygame.draw.rect(sc, GREEN, (SIZE * 160 + indent_horizontal, SIZE * 30, SIZE * 10, SIZE * 20))
        pygame.draw.polygon(sc, DARK_GREEN, [[SIZE * 125 + indent_horizontal, SIZE * 25], [SIZE * 145 + indent_horizontal, SIZE * 30], [SIZE * 145 + indent_horizontal, SIZE * 40], [SIZE * 125 + indent_horizontal, SIZE * 35]])
        pygame.draw.polygon(sc, DARK_GREEN, [[SIZE * 155 + indent_horizontal, SIZE * 40], [SIZE * 175 + indent_horizontal, SIZE * 35], [SIZE * 175 + indent_horizontal, SIZE * 25], [SIZE * 155 + indent_horizontal, SIZE * 30]])
        text = font.render("Compystein 3-D Beta 1", 1, GREEN)
        sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 55])
        text = font.render("Press [Enter] to start!", 1, GREEN)
        sc.blit(text, [indent_horizontal + SIZE * 10, SIZE * 135])
    elif mode == "help":
        sc.fill(GRAY)
        text = font.render("Compystein 3-D Beta 1 Help", 1, GREEN)
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
        sc.blit(text, [indent_horizontal + SIZE * 20, SIZE * 125])        
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
            elif option == 1:
                text = font.render("Close game", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 80])
                text = font.render(">Set HP to 100", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 100])
                text = font.render("Give 10 bullets", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 120])
            elif option == 2:
                text = font.render("Close game", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 80])
                text = font.render("Set HP to 100", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 100])
                text = font.render(">Give 10 bullets", 1, WHITE)
                sc.blit(text, [indent_horizontal + SIZE * 5, SIZE * 120])
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
    pygame.display.update()
    pygame.time.delay(500)
    last_key = ""
    if turn != "player":
        turn = "player"
        b = 0
        for tile in leveldict:
            if b != 1:
                if leveldict[tile] == "enemy1" or leveldict[tile] == "enemy2":
                    if leveldict[tile] == "enemy1":
                        a = 0
                    else:
                        a = 1
                    enemy_X = int(tile[2:3])
                    enemy_Y = int(tile[:1])
                    if enemy_X + 1 == x and enemy_Y == y or enemy_X - 1 == x and enemy_Y == y or enemy_X + 1 == x and enemy_Y + 1 == y or enemy_X + 1 == x and enemy_Y - 1 == y or enemy_X - 1 == x and enemy_Y + 1 == y or enemy_X + 1 == x and enemy_Y - 1 == y or enemy_X == x and enemy_Y + 1 == y or enemy_X == x and enemy_Y - 1 == y:
                        damage += 5
                        health = health - damage
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
                    leveldict[tile] = ""
                    if a == 0:
                        leveldict[coords] = "enemy1"
                    else:
                        leveldict[coords] = "enemy2"
                        

    if weapon_action == "attack":
        weapon_action = "idle"
    turn = "player"
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
