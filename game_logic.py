# game_logic.py

import pygame as pg
import sys
from network import iniciar_servidor, conectar_a_servidor, enviar_mensaje, recibir_mensaje
from server_tab import draw_server_window
from client_tab import draw_client_window
from ui_components import draw_button

# Nuevas constantes para estados de juego
ESTADO_ESPERANDO_SELECCION = 0
ESTADO_MODO_SERVIDOR = 1
ESTADO_MODO_CLIENTE = 2

def manejar_eventos_servidor(conn, window, WIDTH, HEIGHT, DARK, GREEN):
    try:
        data = recibir_mensaje(conn)
        if data:
            print(f"Dato recibido: {data}")
            draw_server_window(window, WIDTH, HEIGHT, DARK, GREEN)
    except BlockingIOError:
        pass

def manejar_eventos_cliente(conn, event, window, WIDTH, HEIGHT, DARK, BLUE, PURPLE, give_off_button):
    mouse_pos = pg.mouse.get_pos()
    upper_half_height = HEIGHT // 4
    if mouse_pos[1] < upper_half_height:
        mensaje = f"Click en {mouse_pos}"
        enviar_mensaje(conn, mensaje)
        print(f"Enviando posición {mensaje}")
    elif give_off_button and give_off_button.collidepoint(mouse_pos):
        print("Terminando conexión y cerrando el juego.")
        if conn:
            conn.close()
        return False  # Para detener el bucle
    return True  # Continuar ejecución

def seleccionar_rol(mouse_pos, window, WIDTH, HEIGHT, DARK, GREEN, BLUE, PURPLE, server_button, client_button):
    if server_button.collidepoint(mouse_pos):
        print("Iniciando como servidor...")
        conn = iniciar_servidor()
        draw_server_window(window, WIDTH, HEIGHT, DARK, GREEN)
        return ESTADO_MODO_SERVIDOR, conn, None
    elif client_button.collidepoint(mouse_pos):
        print("Conectando como cliente...")
        conn = conectar_a_servidor()
        window.fill(DARK)
        give_off_button = draw_client_window(window, WIDTH, HEIGHT, DARK, BLUE, PURPLE)
        return ESTADO_MODO_CLIENTE, conn, give_off_button
    return ESTADO_ESPERANDO_SELECCION, None, None

def main_logic(WIDTH, HEIGHT, window):
    DARK, GREEN, BLUE, PURPLE = (0, 0, 0), (0, 255, 0), (0, 0, 255), (128, 0, 128)
    window.fill(DARK)
    server_button = draw_button(window, "Servidor", WIDTH / 2, HEIGHT / 2 - 75, 300, 100, GREEN, DARK)
    client_button = draw_button(window, "Cliente", WIDTH / 2, HEIGHT / 2 + 75, 300, 100, BLUE, DARK)
    pg.display.update()

    running, estado = True, ESTADO_ESPERANDO_SELECCION
    conn, give_off_button = None, None

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN and estado == ESTADO_ESPERANDO_SELECCION:
                estado, conn, give_off_button = seleccionar_rol(pg.mouse.get_pos(), window, WIDTH, HEIGHT, DARK, GREEN, BLUE, PURPLE, server_button, client_button)
            elif event.type == pg.MOUSEBUTTONDOWN and estado == ESTADO_MODO_CLIENTE:
                running = manejar_eventos_cliente(conn, event, window, WIDTH, HEIGHT, DARK, BLUE, PURPLE, give_off_button)

        if estado == ESTADO_MODO_SERVIDOR and conn:
            manejar_eventos_servidor(conn, window, WIDTH, HEIGHT, DARK, GREEN)

    pg.quit()
    sys.exit()