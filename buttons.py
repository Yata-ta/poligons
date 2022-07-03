import pygame

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

        