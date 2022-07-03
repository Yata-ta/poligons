import pygame
import pygame_gui


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


class ButtonIcon():

    def __init__(self, x, y, width, height, window, backgroundColor, hoverColor, function, img = None) -> None:
        
        self.posX = x
        self.posY = y
        self.width = width
        self.height = height

        self.pressed = False

        self.rect = pygame.Rect(x, y, width, height)
        self.window = window
        if(img != None):
            self.img = pygame.transform.scale(img, (width,height)).convert_alpha()
        else:
            #TODO  button image withoun icon
            pass

        self.backgroundColor = backgroundColor
        self.hoverColor = hoverColor

        if(callable(function) == True):
            self.function = function
            #self.function = staticmethod(function)
        else:
            #TODO error function button
            print("No Function")
            pass
        
    def renderButton(self) -> None:

        pygame.draw.rect(self.window, self.backgroundColor, self.rect)
        self.window.blit(self.img, self.img.get_rect(center = self.rect.center))

    def collisionDetection(self, mouse) -> bool:
        return bool(self.rect.collidepoint(mouse.getPosition()))

    def hoverUpdate(self, mouse)->None:

        if (self.collisionDetection(mouse) == True):
            pygame.draw.rect(self.window, self.hoverColor, self.rect)
            self.window.blit(self.img, self.img.get_rect(center = self.rect.center))
        else:
            pygame.draw.rect(self.window, self.backgroundColor, self.rect)
            self.window.blit(self.img, self.img.get_rect(center = self.rect.center))

    def updateButton(self, mouse) -> None:

        self.hoverUpdate(mouse)
        self.checkClicked(mouse)

    def checkClicked(self, mouse) -> bool:

        if (mouse.getClickLeft() == False):
            self.pressed = False

        mouseX, mouseY = mouse.getPosition()
        if ((self.posX <= mouseX <= self.posX + self.width) and (self.posY <= mouseY <= self.posY + self.height) and (mouse.getClickLeft()) and (self.pressed == False)):
            self.pressed = True
            self.function()
            return True
        else:
            False

        



class Mouse():

    def __init__(self) -> None:
        pass
    
    def getPosition(self):
        return pygame.mouse.get_pos()
    def getClickLeft(self):
        return pygame.mouse.get_pressed()[0]


class Interface ():
    
    mouse = Mouse()

    def __init__(self) -> None:
        pass



def changeLabelText():
    print("Click")
    pass



class Window():

    running = True
    game = Game()
    gui = GUI()
    interface = Interface()


    title = "Poligons"
    logo = pygame.image.load('Design/logo.jpg')
    framesPerSecond = 24
    

    def __init__(self):

        pygame.init()
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.UImanager = pygame_gui.UIManager((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(self.framesPerSecond)

        self.buttonPointIncrease = ButtonIcon(800, 100, 30, 30, self.win, self.gui.color, (214,200,178), function = changeLabelText, img = pygame.image.load("Design/buttonIncrease.png"))
        self.buttonPointDecrease = ButtonIcon(850, 100, 30, 30, self.win, self.gui.color, (214,200,178), function = changeLabelText,  img = pygame.image.load("Design/buttonDecrease.png"))

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