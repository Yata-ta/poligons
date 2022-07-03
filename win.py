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
        
        for x in range(self.posX, self.width+self.posX, blockSize):
            for y in range(self.posY, self.height+self.posY, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(window, (0,0,0), rect, 1)
        



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
    framesPerSecond = 24


    def __init__(self):

        pygame.init()
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.UImanager = pygame_gui.UIManager((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.initGUI()

    def initGUI(self):
        
        #button_layout_rect = pygame.Rect(30, 20, 100, 20)
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon)

        self.win.blit(self.gui.background, (0,0))
        self.win.blit(self.game.background, (self.game.posX,self.game.posY))
        self.game.drawGrid(self.win)

        pygame.draw.circle(self.win, (0,0,0), (450+70, 300+50), 5)
        #UIButton(relative_rect=button_layout_rect,
        #    text='Hello',
        #  container=self.win)

        rect = pygame.Rect(300, 200, 50, 20)
        pygame_gui.elements.ui_button.UIButton(relative_rect=rect,text='Hello', manager = self.UImanager, container=self.win())

    def run(self):

        while(self.running == True):
            dt = self.clock.tick(self.framesPerSecond)
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
        
            print(self.clock.get_fps())
            pygame.display.update()
        pygame.quit()

w = Window()
w.run()