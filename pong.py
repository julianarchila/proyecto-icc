def main():
    import pygame

    pygame.init()

    # Colores
    black = (0, 0, 0)
    white = (255, 255, 255)
    screen_size = (800, 600)
    player_width = 15
    player_height = 90

    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    # coordenadas y velocidad de jugador1
    player1_x_coord = 50
    player1_y_coord = 300 - 45
    player1_y_speed = 0

    # coordenadas y velocidad de jugador2
    player2_x_coord = 750 - player_width
    player2_y_coord = 300 - 45
    player2_y_speed = 0

    # Coordenadas de la pelota
    pelota_x = 400
    pelota_y = 300
    pelota_speed_x = 4
    pelota_speed_y = 4

    # Marcadores
    score1 = 0
    score2 = 0

    game_over = False


    def draw_text(surface, text, size, x, y):
        font = pygame.font.SysFont("serif", size)
        text_surface = font.render(text, True, white)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)


    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_over = True

            if event.type == pygame.KEYDOWN:
                # Jugador 1
                if event.key == pygame.K_w:
                    player1_y_speed = -4
                if event.key == pygame.K_s:
                    player1_y_speed = 4

                # Jugador 2
                if event.key == pygame.K_UP:
                    player2_y_speed = -4
                if event.key == pygame.K_DOWN:
                    player2_y_speed = 4

            if event.type == pygame.KEYUP:
                # Jugador 1
                if event.key == pygame.K_w:
                    player1_y_speed = 0
                if event.key == pygame.K_s:
                    player1_y_speed = 0

                # Jugador 2
                if event.key == pygame.K_UP:
                    player2_y_speed = 0
                if event.key == pygame.K_DOWN:
                    player2_y_speed = 0

        # Modificar coordenadas para dar movimiento
        player1_y_coord += player1_y_speed

        if player1_y_coord <= 0:
            player1_y_coord = 0

        if player1_y_coord >= 600 - 90:
            player1_y_coord = 600 - 90

        player2_y_coord += player2_y_speed

        if player2_y_coord <= 0:
            player2_y_coord = 0

        if player2_y_coord >= 600 - 90:
            player2_y_coord = 600 - 90

        # Movimiento pelota
        if pelota_y > 590 or pelota_y < 10:
            pelota_speed_y *= -1

        # Revisa si la pelota sale del lado derecho
        if pelota_x > 800:
            pelota_x = 400
            pelota_y = 300
            # invierte direccióm
            pelota_speed_x *= -1
            pelota_speed_y += -1
            # Marcador jugador 1
            score1 += 1

        # Revisa si la pelota sale del lado izquierdo
        if pelota_x < 0:
            pelota_x = 400
            pelota_y = 300
            # invierte direccióm
            pelota_speed_x *= -1
            pelota_speed_y += -1
            # Marcador jugador 1

            score2 += 1

        pelota_x += pelota_speed_x
        pelota_y += pelota_speed_y

        screen.fill(black)
        # Zona de dibujo
        jugador1 = pygame.draw.rect(
            screen, white, (player1_x_coord, player1_y_coord, player_width, player_height)
        )
        jugador2 = pygame.draw.rect(
            screen, white, (player2_x_coord, player2_y_coord, player_width, player_height)
        )
        pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)
        # imprimir marcador
        draw_text(screen, str(score1), 25, 350, 10)
        draw_text(screen, str(score2), 25, 450, 10)

        # Colisiones
        if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
            pelota_speed_x *= -1

        if score1 == 5 or score2 == 5:
            game_over = True
            draw_text(screen, "GAME OVER", 100, 220, 150)


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
