import pygame
import pygame_gui


WIDTH = 900
HEIGHT = 400

class Game():

    width = 450
    height = 300
    posX = 70
    posY = 50

    
    def __init__(self) -> None:
        self.background = pygame.Surface((self.width, self.height))
        self.background.fill((255, 255, 255))

        #window.blit(self.background, (0,0))

    def drawGrid(self, window) -> None:
        blockSize = 20 #Set the size of the grid block
        print(max(range(self.posX, self.width, blockSize)))
        for x in range(self.posX, self.width, blockSize):
            for y in range(self.posY, self.height, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(window, (0,0,0), rect,1)
        print(x)



class GUI():

    def __init__(self) -> None:
        self.background = pygame.Surface((WIDTH, HEIGHT))
        self.background.fill((247, 231, 208))

class Window():

    running = True
    game = Game()
    gui = GUI()
    title = "Poligons"
    icon = pygame.image.load('icon.jpg')


    def __init__(self):

        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        
        self.initGUI()

    def initGUI(self):
        
        #button_layout_rect = pygame.Rect(30, 20, 100, 20)
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon)

        self.win.blit(self.gui.background, (0,0))
        self.win.blit(self.game.background, (self.game.posX,self.game.posY))
        self.game.drawGrid(self.win)

        #UIButton(relative_rect=button_layout_rect,
        #    text='Hello',
        #  container=self.win)

    def run(self):

        while(self.running == True):
            
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
        
            pygame.display.update()
        pygame.quit()

w = Window()
w.run()