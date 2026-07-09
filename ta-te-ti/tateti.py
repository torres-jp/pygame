# pyrefly: ignore [missing-import]
import pygame

pygame.init()
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("TA TE TI")

fondo = pygame.image.load("static/tictactoe_background.png")
circulo = pygame.image.load("static/circle.png")
cruz = pygame.image.load("static/x.png")

fondo = pygame.transform.scale(fondo, (450, 450))
circulo = pygame.transform.scale(circulo, (120, 120))
cruz = pygame.transform.scale(cruz, (120, 120))


coor = [
    [(40, 50), (165, 50), (290, 50)],
    [(40, 175), (165, 175), (290, 175)],
    [(40, 300), (165, 300), (290, 300)],
]
board = [["", "", ""], ["", "", ""], ["", "", ""]]


turno = "X"
game_over = False
clock = pygame.time.Clock()


def draw_board():
    screen.blit(fondo, (0, 0))


while not game_over:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    screen.blit(fondo, (0, 0))
    screen.blit(circulo, (40, 50))
    screen.blit(cruz, (160, 165))

    pygame.display.update()


pygame.quit()
