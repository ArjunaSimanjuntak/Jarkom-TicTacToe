import pygame
import os

#Load gambar X dan O dari file res
letterX = pygame.image.load(os.path.join('res', 'x.png'))
letterO = pygame.image.load(os.path.join('res', 'o.png'))

class Grid:
    def __init__(self):
        #List of tuples of tuples
        self.grid_lines =  [((0,200),(600,200)), # Horizontal line pertama
                            ((0,400),(600,400)), # Horizontal line kedua
                            ((200,0),(200,600)), # Vertikal line pertama
                            ((400,0),(400,600))] # Vertikal line Kedua
        
        #Membuat matrix
        #Tiap y, membentuk 3 x dan set nilai menjadi 0
        self.grid =[[0 for x in range(3)] for y in range(3)]
        self.switch_player = True


    def draw(self, surface):
        #Menggambar garis untuk grid
        for line in self.grid_lines:
            pygame.draw.line(surface, (200,200,200), line[0], line[1], 5)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell_value(x, y) == "X":
                    surface.blit(letterX, (x*200, y*200))
                elif self.get_cell_value(x, y ) == "O":
                    surface.blit(letterO, (x*200, y*200))

    #Getter
    def get_cell_value(self, x, y):
        return self.grid[y][x]

    #Setter
    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value

    #Set nilai dari klik mouse menjadi X dan O secara bergantian
    def get_mouse(self, x, y, player):
        if self.get_cell_value(x, y) == 0:
            self.switch_player = True
            if player == "X":
                self.set_cell_value(x, y, "X")
            elif player == "O":
                self.set_cell_value(x, y, "O")
        else:
            self.switch_player = False

    #Untuk debugging
    def print_grid(self):
        for row in self.grid:
            print(row)