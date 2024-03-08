# ui_components.py
import pygame as pg

def draw_button(window, text, center_x, center_y, width, height, color, text_color):
    font = pg.font.Font(None, 50)
    button = pg.Rect(center_x - width / 2, center_y - height / 2, width, height)
    pg.draw.rect(window, color, button)
    text_surface = font.render(text, True, text_color)
    window.blit(text_surface, text_surface.get_rect(center=button.center))
    return button
