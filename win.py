import pygame
import pygame_gui
import buttons
import interface



WIDTH = 900
HEIGHT = 400

class Game():

    width = 450
    height = 300
    posX = 70
    posY = 50
    color = (255, 255, 255)
    
    def __init__(self) -> None:
        self.background = pygame.Surface((self.width, self.height))
        self.background.fill(self.color)

        #window.blit(self.background, (0,0))

    def drawGrid(self, window) -> None:
        blockSize = 15 #Set the size of the grid block
        
        for x in range(self.posX, self.width+self.posX, blockSize):
            for y in range(self.posY, self.height+self.posY, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(window, (230,230,230), rect, 1)
        

class GUI():

    color = (247, 231, 208)

    def __init__(self) -> None:
        self.background = pygame.Surface((WIDTH, HEIGHT))
        self.background.fill(self.color)



def changeLabelText():
    print("Click")
    pass



class Window():

    running = True
    game = Game()
    gui = GUI()
    interface = interface.Interface()


    title = "Poligons"
    logo = pygame.image.load('Design/logo.jpg')
    framesPerSecond = 24
    

    def __init__(self):

        pygame.init()
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.UImanager = pygame_gui.UIManager((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(self.framesPerSecond)

        self.buttonPointIncrease = buttons.ButtonIcon(800, 100, 30, 30, self.win, self.gui.color, (214,200,178), function = changeLabelText, img = pygame.image.load("Design/buttonIncrease.png"))
        self.buttonPointDecrease = buttons.ButtonIcon(850, 100, 30, 30, self.win, self.gui.color, (214,200,178), function = changeLabelText,  img = pygame.image.load("Design/buttonDecrease.png"))

        self.initGUI()

    def initGUI(self) -> None:
        
        #button_layout_rect = pygame.Rect(30, 20, 100, 20)
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.logo)

        self.win.blit(self.gui.background, (0,0))
        self.win.blit(self.game.background, (self.game.posX,self.game.posY))
        self.game.drawGrid(self.win)

        pygame.draw.circle(self.win, (0,0,0), (450+70, 300+50), 5)



        self.buttonPointIncrease.renderButton()
        self.buttonPointDecrease.renderButton()


    def updateWidgets(self):

        self.dt = self.clock.tick(self.framesPerSecond)

        self.buttonPointIncrease.updateButton(self.interface.mouse)
        self.buttonPointDecrease.updateButton(self.interface.mouse)      

    def run(self):

        while(self.running == True):

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
        
            #print(self.clock.get_fps())
            self.updateWidgets()
            pygame.display.update()
        pygame.quit()

w = Window()
w.run()