import pygame

class Mouse():

    def __init__(self) -> None:
        pass
    
    def getPosition(self):
        return pygame.mouse.get_pos()
    def getClickLeft(self):
        return pygame.mouse.get_pressed()[0]


class Keyboard():

    def __init__(self) -> None:
        pass


class Interface ():
    
    mouse = Mouse()
    keyboard = Keyboard()

    def __init__(self) -> None:
        pass

