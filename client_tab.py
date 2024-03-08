import pygame as pg

def draw_client_window(window, WIDTH, HEIGHT, DARK, BLUE, PURPLE):
    # Ajustar las dimensiones de las áreas
    upper_half_height = HEIGHT // 4  # Ahora la "mitad superior" es solo un cuarto de la altura total
    lower_half_height = HEIGHT - upper_half_height  # La "mitad inferior" es el resto

    # Fondo morado para la nueva área superior
    upper_half = pg.Rect(0, 0, WIDTH, upper_half_height)
    window.fill(PURPLE, upper_half)

    # Dibujar botón "Give Off" en la nueva área inferior más grande
    give_off_button = pg.Rect(WIDTH / 2 - 100, HEIGHT - lower_half_height // 2, 200, 50)
    pg.draw.rect(window, BLUE, give_off_button)
    font = pg.font.Font(None, 50)
    text_surface = font.render("Give Off", True, DARK)
    window.blit(text_surface, (WIDTH / 2 - 100 + 25, HEIGHT - lower_half_height // 2 + 10))

    pg.display.update()

    return give_off_button
