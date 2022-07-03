import pygame

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

