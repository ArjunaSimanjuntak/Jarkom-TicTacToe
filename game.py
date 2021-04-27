import pygame
"""#Peletakan GUI saat running
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '400,100'
"""
from grid import Grid

#tampilan display 
surface = pygame.display.set_mode((600,600))
#Title
pygame.display.set_caption('Tic-tac-toe')
#Grid objek
grid = Grid()

#Proses aplikasi tereksekusi
running = True
#Inisiasi player
player = "X"

while running:
    for event in pygame.event.get():
        #Ketika klik X maka running akan false
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Untuk tombol kiri mouse
            if pygame.mouse.get_pressed()[0]:
                #Koordinat saat klik tombol kiri mouse
                pos = pygame.mouse.get_pos()
                #Membagi nilai koordinat menjadi cell koordinat
                print(pos[0] // 200, pos[1] // 200)
                #Mengambil posisi mouse dan memberi nilai X atau O bergantian
                grid.get_mouse(pos[0] // 200, pos[1] // 200, player)
                if grid.switch_player: 
                    if player == "X":
                        player = "O"
                    else:
                        player="X"

                grid.print_grid()

    #Tampilan warna hitam
    surface.fill((0,0,0))

    #Tampilan garis dari grid
    grid.draw(surface)

    pygame.display.flip()