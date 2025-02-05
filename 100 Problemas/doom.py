import pygame
import random
 
# Inicializar el juego
pygame.init()
 
# Definir dimensiones de la pantalla
width = 800
height = 600
 
# Crear la pantalla del juego
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Los Simpsons Doom")
 
# Cargar imágenes de los personajes
background = pygame.image.load("background.png")
player = pygame.image.load("homer.png")
enemy = pygame.image.load("burns.png")
 
# Dimensiones de los personajes
player_width = 64
player_height = 64
enemy_width = 64
enemy_height = 64
 
# Posición inicial del jugador
player_x = 350
player_y = 500
 
# Velocidad del jugador
player_speed = 5
 
# Crear enemigos
enemy_x = random.randint(0, width - enemy_width)
enemy_y = random.randint(50, 150)
enemy_speed = 3
 
# Función para dibujar al jugador
def draw_player(x, y):
    screen.blit(player, (x, y))
 
# Función para dibujar a los enemigos
def draw_enemy(x, y):
    screen.blit(enemy, (x, y))
 
# Bucle principal del juego
running = True
while running:
    # Capturar eventos del teclado y del mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # Obtener teclas presionadas
    keys = pygame.key.get_pressed()
 
    # Mover al jugador
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed
 
    # Actualizar la posición de los enemigos
    enemy_y += enemy_speed
 
    # Detectar colisiones entre el jugador y el enemigo
    if (
        player_x < enemy_x + enemy_width
        and player_x + player_width > enemy_x
        and player_y < enemy_y + enemy_height
        and player_y + player_height > enemy_y
    ):
        print("¡Colisión!")
        # Aquí podrías implementar una acción cuando haya colisión, como finalizar el juego o restar vidas
 
    # Actualizar la lógica del juego
 
    # Dibujar elementos en la pantalla
    screen.blit(background, (0, 0))
    draw_player(player_x, player_y)
    draw_enemy(enemy_x, enemy_y)
 
    # Actualizar la pantalla
    pygame.display.flip()
 
# Finalizar el juego
pygame.quit()
 