from tkinter import *
from random import *
from ships import  Ship

class GamePlayer:
    def gameTableInit(self,pixels):
        fields = {}
        for i in range(100+pixels, 600+pixels,50):
            for j in range(100, 600, 50):
                fields[(i, j)] = 0
        return fields

