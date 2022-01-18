# 1 - Saber gerenciar as Janelas do computador
# 2 - Saber fazer a interação dos inputs entre jogo e usuário
# 3 - Saber desenhar qualquer coisa na tela
# 4 - Saber trabalhar com sons
# 5 - Saber usar a lógica no programa

import pygame

pygame.init()
#display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #definindo full screen
display = pygame.display.set_mode([840, 420])
pygame.display.set_caption("Folks") #Título da janela

PressingW = False #variavel definida como false

gameLoop = True               #Linha de codigos
while gameLoop:               #Para definir a
                      #Persistência da janela
    pygame.display.update()
    # Draw:
    display.fill([19, 173, 235])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                print('Soltou W')
                PressingW = True
                #Sempre que pressionado w variavel se torna True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('Apertou W')
                PressingW = False
                #Sempre que soltar W variavel se torna false



        #Metodo mais simples e facil de se reconhecer os inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            print('Pressionando W')