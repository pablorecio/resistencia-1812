
# -*- coding: utf-8 -*-

import pygame
import pygame.font
import board

import sys
sys.path.append("./libguadalete")
import libguadalete
import game

#-------- Sizes declarations -----------------
screen_size = (760,560)
board_ub = (10,10)
frame_A = (10,500)
piece_frame_A = (17,506)
text_frame_A = (57,506)
frame_B = (251,500)
piece_frame_B = (258,506)
text_frame_B = (298,206)
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
path_font_names = 'fonts/zektonbi.ttf'
#----------------------------------------------

def generate_background_surface(surfaces):
    surface = pygame.Surface(screen_size)
    
    surface.blit(surfaces['background'],(0,0))
    surface.blit(surfaces['frame'], frame_A)
    surface.blit(surfaces['frame'], frame_B)
    surface.blit(surfaces['piece_A'], piece_frame_A)
    surface.blit(surfaces['piece_B'], piece_frame_B)
    surface.blit(surfaces['name_team_A'], text_frame_A)
    surface.blit(surfaces['name_team_B'], text_frame_B)

    return surface

def extract_name(team):
    i = team[1].find("/equipo")
    j = team[1].find(".clp")

    return (team[1])[i+7:j]

def run(teamA, teamB):
    lib = libguadalete.LibGuadalete(teamA,teamB)
    out_file = lib.run_game()

    entire_game = lib.parseFile(out_file)
    
    pygame.init()

    surfaces = {}
    name_team_A = extract_name(teamA)
    name_team_B = extract_name(teamB)

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Resistencia en Cadiz: 1812 (Tablero)')
    favicon = pygame.image.load(path_favicon).convert()
    pygame.display.set_icon(favicon)

    res_game = game.Game(entire_game, path_piece_A,
                         path_piece_B, path_piece_default)

    surfaces['background'] = pygame.image.load(path_background).convert()
    surfaces['frame'] = pygame.image.load(path_frame).convert()
    piece_surf_frame_A = pygame.image.load(path_piece_A).convert()
    surfaces['piece_A'] = pygame.transform.scale(piece_surf_frame_A,(35,35))
    piece_surf_frame_B = pygame.image.load(path_piece_B).convert()
    surfaces['piece_B'] = pygame.transform.scale(piece_surf_frame_B,(35,35))

    name_font = pygame.font.Font(path_font_names, 22)
    surfaces['name_team_A'] = name_font.render(name_team_A, 1, font_name_color)
    surfaces['name_team_B'] = name_font.render(name_team_B, 1, font_name_color)

    background = generate_background_surface(surfaces)
    img_board = res_game.draw_board().convert()

    screen.blit(background,(0,0))
    screen.blit(img_board,board_ub)
    pygame.display.flip()

    clock = pygame.time.Clock()
    while True:
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return 
            if event.type == pygame.KEYDOWN:
                if event.key == 275:
                    res_game.next_turn()
                    surface = res_game.draw_board()
                    surface.convert()
                    screen.blit(background,(0,0))
                    screen.blit(surface,board_ub)
                    pygame.display.flip()
                if event.key == 276:
                    res_game.previous_turn()
                    surface = res_game.draw_board()
                    surface.convert()
                    screen.blit(background,(0,0))
                    screen.blit(surface,board_ub)
                    pygame.display.flip()
