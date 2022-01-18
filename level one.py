import sys
import numpy as np
from matplotlib import pyplot as plt
import keyboard

mapa = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]
#definindo mapa do jogo sendo 1 as paredes

posx, posy = (1,1)
exitx, exity = (3,3)
rot = np.pi/4
#posição inicial do jogador e eixos x e y

#Loop para Perspectiva do jogador
for i in range(60):
    #60 interações
    rot_i = rot + np.deg2rad(i - 30)
    x, y = (posx, posy)
    sin, cos = (0.02 * np.sin(rot_i), 0.02*np.cos(rot_i))
    n = 0
    while True:
        #calculando a distancia com um contador
        x, y =(x + cos, y + sin)
        n = n+1
        #certificando-se de que foi encontrado paredes
        if mapa[int(x)] [int(y)] != 0:
           h = 1/(0.02 * n) #calculando a altura da parede
           break
    plt.vlines(i, -h, h, lw = 8)

plt.axis('off'); plt.tight_layout(); plt.axis([0, 60, -1, 1])
plt.draw(); plt.pause(0.0001); plt.clf()

key = keyboard.read_key()
x, y = (posx, posy)

if key == 'w':
    x, y = (x + 0.3*np.cos(rot), y + 0.3*np.sin(rot))
elif key == 's':
    x, y = (x - 0.3 * np.cos(rot), y - 0.3 * np.sin(rot))
elif key == 'd':
    rot = rot - np.pi/8
elif key == 'a':
    rot = rot + np.pi/8
elif key == 'esc':
    sys.exit()

if mapa[int(x)] [int(y)] == 0:
   if int(posx) == exitx and int(posy) == exity:
      sys.exit()
   posx, posy = (x, y)

plt.close()