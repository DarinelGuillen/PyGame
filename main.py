# main.py
import pygame as pg
from game_logic import main_logic

def main():
    pg.init()
    WIDTH, HEIGHT = 800, 600
    window = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Atrapando Frutas - Modo Red")
    main_logic(WIDTH, HEIGHT, window)

if __name__ == "__main__":
    main()
