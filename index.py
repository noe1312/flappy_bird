import pygame, sys, random

#Se crea una funcion para que se ejecute el floor picture
def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,600))
    screen.blit(floor_surface,(floor_x_pos + 266,600))

#Se crea la función para que aparezcan las tuberias
def create_pipe():
    #Se crean los tuberias en diferentes alturas aleatorias
    random_pipe_pos = random.choice(pipe_height)
    #Se crean las tuberias top y bottom
    bottom_pipe = pipe_surface.get_rect(midtop = (600,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (600,random_pipe_pos - 150))
    return bottom_pipe, top_pipe

#Funcion para realizar el movimiento de las tuberias
def move_pipes(pipes):
    for pipe in pipes:
        #Itera a travez de la lista y las va a ir desplazando hacia la izquierda
        pipe.centerx -= 2
    return pipes

#Se dibujan las tuberias
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_surface, pipe)
        else:
            #Rota la imagen de la tuberia para que este en la parte superior
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

#Definir la funcion para la colision con el bird
def check_collision(pipes):
    global can_score
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            can_score =True
            return False
    if bird_rect.top <= 0 or bird_rect.bottom >= 600:
        can_score = True
        return False
    
    return True

#Crear la funcion para rotar/transicionar la imagen del bird
def rotate_bird(bird):
    #Toma tres parametros que son la imagen, el angulo de rotacion en sentido horario y la escala en 1
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird

#Crear la secuencia y posicion del bird
def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (266,bird_rect.centery))
    return new_bird, new_bird_rect

#Crear el score para el juego
def score_display(game_state):
    if game_state == 'main_game':
        #Crear el texto la claridad y el color del score
        score_sourface = game_font.render('Score: '+ str(int(score)), True, (255,255,255))
        #La posicion
        score_rect = score_sourface.get_rect(center = (266, 100))
        #Se agrega al juego
        screen.blit(score_sourface, score_rect)

    if game_state == 'game_over':
        score_sourface = game_font.render(f'High Score: {int(score)}', True, (255,255,255))
        score_rect = score_sourface.get_rect(center = (266, 120))
        screen.blit(score_sourface, score_rect)

        # #High Score
        # high_score_sourface = game_font.render(f'High Score: {int(score)}', True, (255,255,255))
        # high_score_rect = high_score_sourface.get_rect(center = (266,100))
        # screen.blit(high_score_sourface, high_score_rect)

#Funcion para actualizar el score 
def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

pygame.init()

screen = pygame.display.set_mode((510,740))
clock = pygame.time.Clock()
#Establecer el tipo de fuente (letra y el tamaño) para el juego
game_font = pygame.font.SysFont('04B_19.ttf',40)

#Variables del juego
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0
can_score = True

#Se importa la imagen de fondo de la app, lo convierte para ser mas facil de trabajar
bg_surface = pygame.transform.scale(pygame.image.load('assets/background-day.png').convert(), (510,740))

#Se carga la imagen para el piso
floor_surface = pygame.transform.scale(pygame.image.load('assets/base.png').convert(),(510,152))

#Se fija la posicion inicial para el movimiento de la imagen
floor_x_pos = 0

bird_downflap = pygame.image.load('assets/bluebird-downflap.png').convert_alpha()
bird_midflap = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_upflap = pygame.image.load('assets/bluebird-upflap.png').convert_alpha()

#Almacena todas las imagenes en una lista para generar una secuencia de movimiento
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
#Se establece la imagen inicial
bird_surface = bird_frames[bird_index]
#Fijar la posicion del bird
bird_rect = bird_surface.get_rect(center = (266,288))

#Se establece el evento para el cambio de imagen y su secuencia
BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 100)

#Se cargan las imagenes de las tuberias
pipe_surface =  pygame.transform.scale(pygame.image.load('assets/pipe-green.png').convert(),(78,500))
#Se crea una lista para almacenar las tuberias
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [300, 350, 400, 450, 500]

#imagen game over
game_over_surface = pygame.image.load('assets/message.png').convert_alpha()
game_over_rect = game_over_surface.get_rect(center = (266,288))

#Se agregan los sonidos del juego
flap_sound = pygame.mixer.Sound('sound/sfx-whoosh.mp3')
death_sound = pygame.mixer.Sound('sound/sfx_metal-beaten.mp3')
score_sound = pygame.mixer.Sound('sound/sfx_coin-recieved.mp3')
score_sound_countdown = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            #Se realiza la funcionalidad de salto para la tecla space
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 5
                flap_sound.play()
            #Se establece la funcionalidad para reactivar el juego
            if event.key == pygame.K_SPACE and game_active==False:
                game_active = True
                #Se reinicia la tuberia y se centra el bird
                pipe_list.clear()
                bird_rect.center = (266,288)
                bird_movement = 0
                score = 0
        if event.type == SPAWNPIPE:
            #Cuando surja el evento se crea una nueva tuberia y se almacena en la lista
            pipe_list.extend(create_pipe())
        
        #Se establece el evento para realizar la secuencia de movimiento
        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            #Cuando llega a la ultima imagen se reiniciaria la secuencia
            else:
                bird_index = 0

            bird_surface, bird_rect = bird_animation()

    #Se fija la imagen de fondo del juego
    screen.blit(bg_surface, (0,0))
    if game_active:

        bird_movement += gravity
        #Se fija la imagen del bird con la funcion rotate_bird
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery

        #Se fija el bird
        screen.blit(rotated_bird, bird_rect)
        bird_rect.centery += bird_movement
        game_active = check_collision(pipe_list)

        #Las Tuberias
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        #Aumenta el score
        score += 0.01
        #pipe_score_check()
        score_display('main_game')
        #Se establece la reproduccion del score_sound y se reinicia la reproduccion cuado se llega a 0 o menos
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display('game_over')
    
    #Se itera imagen del suelo
    floor_x_pos -= 2
    #Se establece el suelo
    draw_floor()

    #Se realiza la continuidad de la imagen con un if
    if floor_x_pos <= -266:
        floor_x_pos = 0
    
    pygame.display.update()
    clock.tick(90)