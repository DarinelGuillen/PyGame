# server_tab.py
import pygame as pg

def draw_server_window(window, WIDTH, HEIGHT, DARK, GREEN):
    window.fill(DARK)
    font = pg.font.Font(None, 50)
    text_surface = font.render("Esperando datos del cliente...", True, GREEN)
    window.blit(text_surface, (50, HEIGHT / 2 - 25))
    pg.display.update()
