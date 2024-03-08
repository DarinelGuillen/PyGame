# game_logic.py
import pygame as pg
import sys
from network import iniciar_servidor, conectar_a_servidor, enviar_mensaje, recibir_mensaje
from server_tab import draw_server_window
from client_tab import draw_client_window
from ui_components import draw_button

def main_logic(WIDTH, HEIGHT, window):
    DARK = (0, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    PURPLE = (128, 0, 128)

    window.fill(DARK)
    server_button = draw_button(window, "Servidor", WIDTH / 2, HEIGHT / 2 - 75, 300, 100, GREEN, DARK)
    client_button = draw_button(window, "Cliente", WIDTH / 2, HEIGHT / 2 + 75, 300, 100, BLUE, DARK)
    pg.display.update()

    running = True
    role_selected = False
    server_mode = False
    client_mode = False
    conn = None
    give_off_button = None

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN and not role_selected:
                mouse_pos = pg.mouse.get_pos()
                if server_button.collidepoint(mouse_pos):
                    print("Iniciando como servidor...")
                    conn = iniciar_servidor()
                    server_mode = True
                    role_selected = True
                    draw_server_window(window, WIDTH, HEIGHT, DARK, GREEN)
                elif client_button.collidepoint(mouse_pos):
                    print("Conectando como cliente...")
                    conn = conectar_a_servidor()
                    client_mode = True
                    role_selected = True
                    window.fill(DARK)
                    give_off_button = draw_client_window(window, WIDTH, HEIGHT, DARK, BLUE, PURPLE)

            elif event.type == pg.MOUSEBUTTONDOWN and client_mode:
                mouse_pos = pg.mouse.get_pos()
                if give_off_button and give_off_button.collidepoint(mouse_pos):
                    print("Terminando conexión y cerrando el juego.")
                    running = False
                    if conn:
                        conn.close()

        if server_mode and conn:
            try:
                data = recibir_mensaje(conn)
                if data:
                    print(f"Dato recibido: {data}")
                    draw_server_window(window, WIDTH, HEIGHT, DARK, GREEN)
            except BlockingIOError:
                pass

    pg.quit()
    sys.exit()
