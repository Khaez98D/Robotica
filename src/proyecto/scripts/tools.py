import pygame

# esta clase sera la encargada de manejar la visualizacion del gridmap y de las
# celdas exploradas por el algormitmo de busqueda. Igualmente, permitira mostrar
# la trayectoria planeada.
class Tools:
    def __init__(self, height, width, size_win_x, size_win_y, prob_free, prob_occ):
        # height: altura (en px) del gridmap
        # width: ancho (en px) del gridmap
        # size_win_x: ancho del canvas
        # size_win_y: altura del canvas
        # prob_free: probabilidad con la que se asume celda libre
        # prob_occ: probabilidad con la que se asume celda ocupada
        self.height = height
        self.width = width
        self.size_win_x = size_win_x
        self.size_win_y = size_win_y
        self.block_size_x = size_win_x / width
        self.block_size_y = size_win_y / height
        self.screen = []
        self.myfont = []
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)
        self.darkBlue = (0,0,128)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.pink = (255,200,200)
        self.orange = (253, 106, 2)
        self.gray = (192,192,192)
        self.prob_free = prob_free
        self.prob_occ = prob_occ


    def init_canvas(self, gridmap, start, goal):
        # este metodo permite inicializar el canvas con el gridmap
        # gridmap: gridmap del entorno mapeado
        # start: pose inicial (se marca la celda correspondiente en rojo)
        # goal: pose objetivo (se marca la celda correspondiente en verde)
        # es posible que por la alta resolucion del gridmap, las celdas start y goal se
        # vean solo como un punto pequeno en el dibujo
        pygame.init()
        self.screen = pygame.display.set_mode((self.size_win_x, self.size_win_y))
        self.screen.fill(self.white)
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 20)
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x*self.block_size_x, y*self.block_size_y, 
                                    self.block_size_x, self.block_size_y)
                if gridmap[y][x] > (1-self.prob_free):
                    pygame.draw.rect(self.screen, self.white, rect, 0)
                elif gridmap[y][x] < (1-self.prob_occ):
                    pygame.draw.rect(self.screen, self.black, rect, 0)
                else:
                    pygame.draw.rect(self.screen, self.gray, rect, 0)
                if start == (y,x):
                    pygame.draw.rect(self.screen, self.red, rect, 0)
                if goal == (y,x):
                    pygame.draw.rect(self.screen, self.green, rect, 0)            
        pygame.display.update()

    def draw_visited(self, current, start):
        # este metodo permite pintar de azul una celda visitada
        # current: coordenadas (x,y) de la celda visitada en el gridmap
        # start: pose inicial (se marca la celda correspondiente en rojo)
        rect = pygame.Rect(current[1]*self.block_size_x, current[0]*self.block_size_y, 
                            self.block_size_x, self.block_size_y)
        pygame.draw.rect(self.screen, self.blue, rect, 0)
        if start == current:
            pygame.draw.rect(self.screen, self.red, rect, 0)
        pygame.display.update()

    def draw_path(self, path, start, goal):
        # este metodo permite de naranja todas las celdas que conforman la trayectoria
        # path: lista con las acciones (N,S,W,E) que deben aplicarse para aplicar la ruta planeada
        # start: pose inicial (se marca la celda correspondiente en rojo)
        # goal: pose objetivo (se marca la celda correspondiente en verde) 
        current = list(start)        
        for i in path:
            if i == 'N':
                current[0] -= 1
            elif i == 'S':
                current[0] += 1
            elif i == 'E':
                current[1] += 1
            elif i == 'W':
                current[1] -= 1
            rect = pygame.Rect(current[1]*self.block_size_x, current[0]*self.block_size_y, 
                                self.block_size_x, self.block_size_y)
            pygame.display.update()
            # time.sleep(0.1)
            if tuple(current) == goal:
                continue
            pygame.draw.rect(self.screen, self.orange, rect, 0)            
        pygame.display.update()