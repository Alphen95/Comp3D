import pygame, platform, time, sys, linecache, json
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
NEON_GREEN = (57,255,20)
SIZE = 2
health = 0
ready_to_refresh = True
quitted = False
last_key = ""
arguments = sys.argv
screen = 0
option = 0
tick = 0
name_level = ""
tile = ""
path_folder = str(Path().absolute())
kernel = platform.system()
run = True
useLocalization = False
current_section = 1
highlited = -1
selected = ""
mode = "edit"

leveldict = {
    "1-1": "", "1-2": "", "1-3": "", "1-4": "", "1-5": "",
    "2-1": "", "2-2": "", "2-3": "", "2-4": "", "2-5": "",
    "3-1": "", "3-2": "", "3-3": "", "3-4": "", "3-5": "",
    "4-1": "", "4-2": "", "4-3": "", "4-4": "", "4-5": "",
    "5-1": "", "5-2": "", "5-3": "", "5-4": " ", "5-5": ""
}

if kernel == "Windows":
    path_menu = path_folder + "\\res\\editor\\menu_bar.png"
    path_wall = path_folder + "\\res\\editor\\wall.png"
    path_bullets = path_folder + "\\res\\editor\\bullets.png"
    path_medkit = path_folder + "\\res\\editor\\medkit.png"
    path_enemy1 = path_folder + "\\res\\editor\\enemy1.png"
    path_enemy2 = path_folder + "\\res\\editor\\enemy2.png"
    path_boss = path_folder + "\\res\\editor\\boss.png"
    path_localization = path_folder + "\\localization\\translated_editor.json"
    path_saveicon = path_folder + "\\res\\editor\\save.png"
    path_loadicon = path_folder + "\\res\\editor\\load.png"
else:
    path_menu = path_folder + "/res/editor/menu_bar.png"
    path_wall = path_folder + "/res/editor/wall.png"
    path_bullets = path_folder + "/res/editor/bullets.png"
    path_medkit = path_folder + "/res/editor/medkit.png"
    path_enemy1 = path_folder + "/res/editor/enemy1.png"
    path_enemy2 = path_folder + "/res/editor/enemy2.png"
    path_boss = path_folder + "/res/editor/boss.png"
    path_localization = path_folder + "/localization/translated_editor.json"
    path_saveicon = path_folder + "/res/editor/save.png"
    path_loadicon = path_folder + "/res/editor/load.png"    
    
image_menubar = pygame.image.load(path_menu)
image_wall = pygame.image.load(path_wall)
image_bullets = pygame.image.load(path_bullets)
image_medkit = pygame.image.load(path_medkit)
image_enemy1 = pygame.image.load(path_enemy1)
image_enemy2 = pygame.image.load(path_enemy2)
image_boss = pygame.image.load(path_boss)
image_save = pygame.image.load(path_saveicon)
image_load = pygame.image.load(path_loadicon)

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
pygame.display.set_caption('Compystein 3-D Level Editor')
sc = pygame.display.set_mode((SIZE * 300, SIZE * 300))
font = pygame.font.Font("pixel_font.ttf", 72)
normal_font = pygame.font.Font("pixel_font.ttf", 32)
small_font = pygame.font.Font("pixel_font.ttf", 16)
if useLocalization:
    pygame.display.set_caption(text_localization[0])
else:
    pygame.display.set_caption("Compystein 3-D Level Editor")

def draw_menubar(highlited):
    sc.blit(pygame.transform.scale(image_menubar, (300 * SIZE, 10 * SIZE)), (0 * SIZE, 0* SIZE))
    if useLocalization:
        text_menu_add_sect = small_font.render(text_localization[1], 1, NEON_GREEN)
        text_menu_rmv_sect = small_font.render(text_localization[2], 1, NEON_GREEN)
        text_menu_tile_sel = small_font.render(text_localization[3], 1, NEON_GREEN)
    else:
        text_menu_add_sect = small_font.render("Add section", 1, NEON_GREEN)
        text_menu_rmv_sect = small_font.render("Remove section", 1, NEON_GREEN)
        text_menu_tile_sel = small_font.render("+ Tiles", 1, NEON_GREEN)
    sc.blit(text_menu_add_sect, [SIZE * 5, SIZE * 2])
    sc.blit(text_menu_rmv_sect, [SIZE * 65, SIZE * 2])
    sc.blit(text_menu_tile_sel, [SIZE * 135, SIZE * 2])
    sc.blit(pygame.transform.scale(image_save, (10 * SIZE, 10 * SIZE)), (200*SIZE,0*SIZE))
    sc.blit(pygame.transform.scale(image_load, (10 * SIZE, 10 * SIZE)), (210*SIZE,0*SIZE))
    if highlited == 2:
        sc.blit(pygame.transform.scale(image_menubar, (38 * SIZE, 72 * SIZE)), (135 * SIZE, 10* SIZE))
        if useLocalization:
            text_submenu_0_erase = small_font.render(str(text_localization[4]), 1, NEON_GREEN)
            text_submenu_0_bullets = small_font.render(str(text_localization[5]), 1, NEON_GREEN)
            text_submenu_0_medkit = small_font.render(str(text_localization[6]), 1, NEON_GREEN)
            text_submenu_0_wall = small_font.render(str(text_localization[7]), 1, NEON_GREEN)
            text_submenu_0_enemy1 = small_font.render(str(text_localization[8]), 1, NEON_GREEN)
            text_submenu_0_enemy2 = small_font.render(str(text_localization[9]), 1, NEON_GREEN)
            text_submenu_0_boss = small_font.render(str(text_localization[10]), 1, NEON_GREEN)
        else:
            text_submenu_0_erase = small_font.render("Erase", 1, NEON_GREEN)
            text_submenu_0_bullets = small_font.render("Bullets", 1, NEON_GREEN)
            text_submenu_0_medkit = small_font.render("Medkit", 1, NEON_GREEN)
            text_submenu_0_wall = small_font.render("Wall", 1, NEON_GREEN)
            text_submenu_0_enemy1 = small_font.render("Oknoser", 1, NEON_GREEN)
            text_submenu_0_enemy2 = small_font.render("Binixoid", 1, NEON_GREEN)
            text_submenu_0_boss = small_font.render("Glitchy", 1, NEON_GREEN)
        sc.blit(text_submenu_0_erase, [SIZE * 137, SIZE * 12])
        sc.blit(text_submenu_0_bullets, [SIZE * 137, SIZE * 22])
        sc.blit(text_submenu_0_medkit, [SIZE * 137, SIZE * 32])
        sc.blit(text_submenu_0_wall, [SIZE * 137, SIZE * 42])
        sc.blit(text_submenu_0_enemy1, [SIZE * 137, SIZE * 52])
        sc.blit(text_submenu_0_enemy2, [SIZE * 137, SIZE * 62])
        sc.blit(text_submenu_0_boss, [SIZE * 137, SIZE * 72])

def draw_section(section,leveldict):
    iteration = 0
    section = section *5
    for i in range(1+section,6+section):
        for i1 in range(5,0,-1):
            #print("coords",((i1*60-60)*SIZE), int((((i-section)*60)-60)*SIZE))
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
            #print("tile",tile)
            tile_contents = leveldict[tile]
            if tile_contents == "wall":
                sc.blit(pygame.transform.scale(image_wall, (60 * SIZE, 60 * SIZE)), (((i1*60-60)*SIZE), int((((i-section)*60)-60)*SIZE)))
            elif tile_contents == "bullets":
                sc.blit(pygame.transform.scale(image_bullets, (60 * SIZE, 60 * SIZE)), (((i1*60-60)*SIZE), int((((i-section)*60)-60)*SIZE)))
            elif tile_contents == "medkit":
                sc.blit(pygame.transform.scale(image_medkit, (60 * SIZE, 60 * SIZE)), (((i1*60-60)*SIZE), int((((i-section)*60)-60)*SIZE)))
            elif "enemy1" in tile_contents:
                sc.blit(pygame.transform.scale(image_enemy1, (60 * SIZE, 60 * SIZE)), (((i1*60-60)*SIZE), int((((i-section)*60)-60)*SIZE)))
            elif "enemy2" in tile_contents:
                sc.blit(pygame.transform.scale(image_enemy2, (60 * SIZE, 60 * SIZE)), (((i1*60-60)*SIZE), int((((i-section)*60)-60)*SIZE)))
            elif "boss" in tile_contents:
                sc.blit(pygame.transform.scale(image_boss, (60 * SIZE, 60 * SIZE)), (((i1*60-60)*SIZE), int((((i-section)*60)-60)*SIZE)))
            iteration +=1
        i_str = str(i)
        text_editor_x = small_font.render(i_str, 1, WHITE)
        sc.blit(text_editor_x, [SIZE * 1, SIZE * (25 + ((60*i)-60))])
    
while run:
    sc.fill(BLACK)
    if mode == "edit":
        draw_section(current_section - 1,leveldict)
        draw_menubar(highlited)
    elif mode == "save":
        if useLocalization:
            text_save_0 = normal_font.render(str(text_localization[12]), 1, NEON_GREEN)
            text_save_1 = normal_font.render(str(text_localization[13]), 1, NEON_GREEN)
        else:
            text_save_0 = normal_font.render("Save level", 1, NEON_GREEN)
            text_save_1 = normal_font.render("Enter filename...", 1, NEON_GREEN)
        sc.blit(text_save_0, [SIZE * 10, SIZE * 12])
        sc.blit(text_save_1, [SIZE * 10, SIZE * 32])
        text_filename = normal_font.render(str(name_level),1,NEON_GREEN)
        sc.blit(text_filename, [SIZE * 5, SIZE * 50])
    elif mode == "load":
        if useLocalization:
            text_save_0 = normal_font.render(str(text_localization[11]), 1, NEON_GREEN)
            text_save_1 = normal_font.render(str(text_localization[13]), 1, NEON_GREEN)
        else:
            text_save_0 = normal_font.render("Load level", 1, NEON_GREEN)
            text_save_1 = normal_font.render("Enter filename...", 1, NEON_GREEN)
        sc.blit(text_save_0, [SIZE * 10, SIZE * 12])
        sc.blit(text_save_1, [SIZE * 10, SIZE * 32])
        text_filename = normal_font.render(str(name_level),1,NEON_GREEN)
        sc.blit(text_filename, [SIZE * 5, SIZE * 50])    
        
    pygame.display.update()    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and mode == "edit":
            if event.button == 1:
                if mode == "edit":
                    mouse_pos = event.pos
                    if mouse_pos[0] <= 60*SIZE and mouse_pos[1] <= 10.5*SIZE:
                        for tile in leveldict:
                            last_tile = tile
                        last_tile_len = len(last_tile)
                        last_tile_len = last_tile_len-2
                        last_tile_x = int(last_tile[0:last_tile_len])
                        for i in range(1+last_tile_x,6+last_tile_x):
                            for i1 in range(1,6):
                                name_cell = str(i) + "-" + str(i1)
                                leveldict.update({name_cell:""}) 
                    elif mouse_pos[0] <= 210*SIZE and mouse_pos[0] >= 200*SIZE and mouse_pos[1] <= 10.5*SIZE:
                        mode="save"
                    elif mouse_pos[0] <= 220*SIZE and mouse_pos[0] >= 210*SIZE and mouse_pos[1] <= 10.5*SIZE:
                        mode="load"                        
                    elif mouse_pos[0] <= 130*SIZE and mouse_pos[0] >= 60*SIZE and mouse_pos[1] <= 10.5*SIZE:
                        for tile in leveldict:
                            last_tile = tile
                        last_tile_len = len(last_tile)
                        last_tile_len = last_tile_len-2
                        last_tile_x = int(last_tile[0:last_tile_len]) - 5
                        if last_tile_x != 0:
                            for i in range(1+last_tile_x,6+last_tile_x):
                                for i1 in range(1,6):
                                    name_cell = str(i) + "-" + str(i1)
                                    leveldict.pop(name_cell)
                        else:
                    elif mouse_pos[0] >= 130*SIZE and mouse_pos[0] <= 175*SIZE:
                        if mouse_pos[1] <= 10.5*SIZE:
                            highlited = 2
                        elif mouse_pos[1] >= 10.5*SIZE and mouse_pos[1] <= 10*SIZE*2 and highlited == 2:
                            highlited = -2
                            selected = ""
                        elif mouse_pos[1] >= 10.5*SIZE*2 and mouse_pos[1] <= 10*SIZE*3 and highlited == 2:
                            highlited = -2
                            selected = "bullets"
                        elif mouse_pos[1] >= 10.5*SIZE*3 and mouse_pos[1] <= 10*SIZE*4 and highlited == 2:
                            highlited = -2
                            selected = "medkit"
                        elif mouse_pos[1] >= 10.5*SIZE*4 and mouse_pos[1] <= 10*SIZE*5 and highlited == 2:
                            highlited = -2
                            selected = "wall"
                        elif mouse_pos[1] >= 10.5*SIZE*5 and mouse_pos[1] <= 10*SIZE*6 and highlited == 2:
                            highlited = -2
                            selected = "enemy1_10"
                        elif mouse_pos[1] >= 10.5*SIZE*6 and mouse_pos[1] <= 10*SIZE*7 and highlited == 2:
                            highlited = -2
                            selected = "enemy2_15"
                        elif mouse_pos[1] >= 10.5*SIZE*7 and mouse_pos[1] <= 10*SIZE*8 and highlited == 2:
                            highlited = -2
                            selected = "boss_25"                    
                    if mouse_pos[0] <= 60*SIZE:
                        y = 5 
                    elif mouse_pos[0] <= 120*SIZE:
                        y = 4
                    elif mouse_pos[0] <= 180*SIZE:
                        y = 3
                    elif mouse_pos[0] <= 240*SIZE:
                        y = 2
                    elif mouse_pos[0] <= 300*SIZE:
                        y = 1
                    if mouse_pos[1] <= 60*SIZE and mouse_pos[1] >= 10.5*SIZE:
                        x = 1 + (5* (current_section-1))
                    elif mouse_pos[1] <= 120*SIZE and mouse_pos[1] >= 10.5*SIZE:
                        x = 2 +(5* (current_section-1))
                    elif mouse_pos[1] <= 180*SIZE and mouse_pos[1] >= 10.5*SIZE:
                        x = 3 + (5* (current_section-1))
                    elif mouse_pos[1] <= 240*SIZE and mouse_pos[1] >= 10.5*SIZE:
                        x = 4 + (5* (current_section-1))
                    elif mouse_pos[1] <= 300*SIZE and mouse_pos[1] >= 10.5*SIZE:
                        x = 5 + (5* (current_section-1))
                    if y != 0 and x != 0 and highlited == -1:
                        tile = str(x)+"-"+str(y)  
                        leveldict[tile] = selected
                        
                    if highlited == -2:
                        highlited = -1                    
                        
                        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and mode == "edit":
                run = False
                exit()
            elif event.key == pygame.K_DOWN and mode == "edit":
                try:
                    section_temp = current_section * 5+1
                    coords = str(section_temp)+"-"+str(1)
                    tile = leveldict[coords]
                    current_section += 1
                except:
                    pass
            elif event.key == pygame.K_UP and mode == "edit":
                try:
                    section_temp = current_section * 5-5
                    coords = str(section_temp)+"-"+str(1)
                    tile = leveldict[coords]
                    current_section -= 1
                except:
                    pass
            elif event.key == pygame.K_RETURN and mode == "save" or event.key == pygame.K_RETURN and mode == "load":
                try:
                    if mode == "save":
                        json_level = json.dumps(leveldict)
                        name_level = name_level+".json"
                        with open(name_level,mode="w") as level:
                            level.write(json_level)
                    elif mode == "load":
                        name_level = name_level+".json"
                        with open(name_level,mode="r") as level:
                            json_level = level.read()
                        leveldict = json.loads(json_level)
                    mode = "edit"
                except:
                    mode = "edit"
                name_level = ""
            elif event.key == pygame.K_BACKSPACE and mode == "save" or event.key == pygame.K_BACKSPACE and mode == "load" or event.key == pygame.K_DELETE and mode == "save" or event.key == pygame.K_DELETE and mode == "load":
                name_level = name_level[:-1]
            elif event.key == 27:
                mode = "edit"
            elif mode == "save" or mode == "load":
                name_level += event.unicode
    x = 0
    y = 0
    