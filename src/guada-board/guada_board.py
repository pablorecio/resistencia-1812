
# -*- coding: utf-8 -*-

import pygame
import pygame.font
import board

import sys
sys.path.append("./libguadalete")
import libguadalete
import game
import button

#-------- Sizes and positions declarations ---
button_start = 120

screen_size = (760,560)
frame_size = (230,47)
buttom_size = (50,50)

board_ub = (10,10)
frame_A_pos = (510,255)
frame_B_pos = (510,198)
piece_frame = (6,6)
text_frame = (45,6)
left_arrow_2_pos = (button_start, 500)
left_arrow_1_pos = (button_start + 70, 500)
right_arrow_1_pos = (button_start + 140,500)
right_arrow_2_pos = (button_start + 210, 500)
exit_pos = (650, 500)
#----------------------------------------------
# ------ Colors -------------------------------
font_name_color = (0,0,0)
#----------------------------------------------
#------- Files and variables ------------------
path_favicon = 'images/favicon.png'
path_piece_A = 'images/piece-orange.png'
path_piece_B = 'images/piece-violete.png'
path_piece_default = 'images/piece-default.png'
path_background = 'images/fondo.png'
path_frame = 'images/marco.png'
path_right_arrow_1 = './images/flecha_derecha1.png'
path_right_arrow_2 = './images/flecha_derecha2.png'
path_left_arrow_1 = './images/flecha_izquierda1.png'
path_left_arrow_2 = './images/flecha_izquierda2.png'
path_exit = './images/salir.png'
path_font_names = 'fonts/zektonbi.ttf'
#----------------------------------------------

def generate_buttons_list():
    buttons = []

    button_left_arrow_2 = button.Button((path_left_arrow_2,)*3)
    button_left_arrow_1 = button.Button((path_left_arrow_1,)*3)
    button_right_arrow_1 = button.Button((path_right_arrow_1,)*3)
    button_right_arrow_2 = button.Button((path_right_arrow_2,)*3)

    button_exit = button.Button((path_exit,)*3)

    buttons.append((button_left_arrow_2, 0, left_arrow_2_pos))
    buttons.append((button_left_arrow_1, 0, left_arrow_1_pos))
    buttons.append((button_right_arrow_1, 0, right_arrow_1_pos))
    buttons.append((button_right_arrow_2, 0, right_arrow_2_pos))
    buttons.append((button_exit, 0, exit_pos))

    return buttons;

def generate_background_surface(surfaces):
    surface = pygame.Surface(screen_size)
    srfc_frame_A = pygame.Surface(frame_size)
    srfc_frame_B = pygame.Surface(frame_size)

    srfc_frame_A.blit(surfaces['frame'],(0,0))
    srfc_frame_A.blit(surfaces['piece_A'], piece_frame)
    srfc_frame_A.blit(surfaces['name_team_A'], text_frame)

    srfc_frame_B.blit(surfaces['frame'],(0,0))
    srfc_frame_B.blit(surfaces['piece_B'], piece_frame)
    srfc_frame_B.blit(surfaces['name_team_B'], text_frame)
    
    surface.blit(surfaces['background'],(0,0))
    surface.blit(srfc_frame_A, frame_A_pos)
    surface.blit(srfc_frame_B, frame_B_pos)

    return surface

#buttons_list is a list of tuples (Button, state, position)
def draw_buttons(background, buttons_list):
    rects = []
    for button in buttons_list:
        aux_state = button[1]
        aux_surface = button[0].get_surface(aux_state)
        aux_pos = button[2]
        rects.append(background.blit(aux_surface, aux_pos))

    return background, rects

def extract_name(team):
    i = team[0].find("/reglas")
    j = team[0].find(".clp")

    return (team[0])[i+7:j]

def run(teamA, teamB):
    lib = libguadalete.LibGuadalete(teamA,teamB)
    out_file = lib.run_game()

    entire_game = lib.parseFile(out_file)
    
    pygame.init()

    background_surfaces = {}
    name_team_A = extract_name(teamA)
    name_team_B = extract_name(teamB)

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Resistencia en Cadiz: 1812 (Tablero)')
    favicon = pygame.image.load(path_favicon).convert()
    pygame.display.set_icon(favicon)

    res_game = game.Game(entire_game, path_piece_A,
                         path_piece_B, path_piece_default)

    background_surfaces['background'] = pygame.image.load(path_background).convert()
    background_surfaces['frame'] = pygame.image.load(path_frame).convert()
    piece_surf_frame_A = pygame.image.load(path_piece_A).convert()
    background_surfaces['piece_A'] = pygame.transform.scale(piece_surf_frame_A,(35,35))
    piece_surf_frame_B = pygame.image.load(path_piece_B).convert()
    background_surfaces['piece_B'] = pygame.transform.scale(piece_surf_frame_B,(35,35))

    name_font = pygame.font.Font(path_font_names, 22)
    background_surfaces['name_team_A'] = name_font.render(name_team_A, 1, font_name_color)
    background_surfaces['name_team_B'] = name_font.render(name_team_B, 1, font_name_color)

    buttons_list = generate_buttons_list()
    
    background = generate_background_surface(background_surfaces)
    back_buttons, buttons_rect = draw_buttons(background, buttons_list)
    img_board = res_game.draw_board().convert()

    screen.blit(back_buttons,(0,0))
    screen.blit(img_board,board_ub)
    pygame.display.flip()

    clock = pygame.time.Clock()
    while True:
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return 
            elif event.type == pygame.KEYDOWN:
                if event.key == 275:
                    res_game.next_turn()
                    surface = res_game.draw_board()
                    surface.convert()
                    back_buttons, buttons_rect = draw_buttons(background, buttons_list)
                    screen.blit(back_buttons,(0,0))
                    screen.blit(surface,board_ub)
                    pygame.display.flip()
                if event.key == 276:
                    res_game.previous_turn()
                    surface = res_game.draw_board()
                    surface.convert()
                    back_buttons, buttons_rect = draw_buttons(background, buttons_list)
                    screen.blit(back_buttons,(0,0))
                    screen.blit(surface,board_ub)
                    pygame.display.flip()
            elif event.type == pygame.MOUSEMOTION:
                print event.pos
