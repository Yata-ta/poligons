import main
import PyQt5
from PyQt5 import QtWidgets
import sys
import pygame


class Window(PyQt5.QtWidgets.QMainWindow):

    posicaoX = 200
    posicaoY = 200
    largura = 500
    altura = 700
    titulo = "Poligons"


    def __init__(self):
        super(Window,self).__init__()
        
        self.setGeometry(self.posicaoX, self.posicaoY, self.largura, self.altura)
        self.setWindowTitle(self.titulo)

        self.layout = PyQt5.QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.initUI()


    def initUI (self):
        
        menuBar = PyQt5.QtWidgets.QMenuBar(self)
        self.setMenuBar(menuBar)

        fileMenu = menuBar.addMenu("&File")
        editMenu = menuBar.addMenu("&Edit")
        helpMenu = menuBar.addMenu("&Help")


        newSubMenu = fileMenu.addAction("&New")
        openSubMenu = fileMenu.addAction("&Open")
        saveSubMenu = fileMenu.addMenu("&Save As")
        exitSubMenu = fileMenu.addAction("Exit")





    def open(self):
        self.show()





app = PyQt5.QtWidgets.QApplication(sys.argv)


pygame.init()
s=pygame.Surface((640,480))
s.fill((64,128,192,224))
pygame.draw.circle(s,(255,255,255,255),(100,100),50)


win = Window(s)
win.open()
      
sys.exit(app.exec_())
    
