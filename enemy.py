from gameplayer import *
from player import *
import random

class Enemy(GamePlayer):

    def __init__(self,root,player:Player): # to rozwianie z playerem mi sie nie podoba
        #self.ship = 0
        self.player = player
        self.root = root
        self.fourMast = Ship(4, 1)
        self.threeMast = Ship(3, 2)
        self.twoMast = Ship(2, 3)
        self.oneMast = Ship(1, 4)
        self.enemyGameTable = self.gameTableInit(550)
        self.enemyAllShips = 20
        self.enemyButtons = self.enemyButtonsCreate()
        self.notPlaced = True
        self.shipSize = 0
        self.alreadyShootingHere = []

    def enemyButtonsCreate(self):
        buttons = {}
        for i in range(650, 1150, 50):
            for j in range(100, 600, 50):
                button = Button(self.root, bg="yellow")
                button.place(x=i, y=j, height=50, width=50)
                button.bind('<Button-1>', lambda event, b=button: self.shot(b))
                buttons[(i, j)] = button
        return buttons

    def setEnemyShips(self,ship): #zobaczymy czy przekazanie tej zmiennej tu wystarczy
        self.notPlaced = True
        while self.notPlaced:
            x = random.randrange(650, 1150, 50)
            y = random.randrange(100, 550, 50)
            o = random.randint(0, 1)
            self.shipSize = ship * 50
            if (o == 0):  # poziomo
                if (x <= 1150 - self.shipSize):
                    col = self.enemyColissionChecker(x, y, o)
                    for i in range(0, self.shipSize, 50):
                        if (not col):
                            self.enemyGameTable[(x + i, y)] = 1
                            self.enemyFieldBlocker(x, y, o)
                            self.notPlaced = False
            else:
                if (y <= 600 - self.shipSize and x <= 1150):
                    col = self.enemyColissionChecker(x, y, o)
                    for i in range(0, self.shipSize, 50):
                        if (not col):
                            self.enemyGameTable[(x, y + i)] = 1
                            self.enemyFieldBlocker(x, y, o)
                            self.notPlaced = False

    def enemyColissionChecker(self, x, y, o):
        colission = False
        if (o == 0):
            for i in range(0, self.shipSize, 50):
                if (self.enemyGameTable[(x + i, y)] != 0):
                    colission = True
            return colission
        else:
            for i in range(0, self.shipSize, 50):
                if (self.enemyGameTable[(x, y + i)] != 0):
                    colission = True
            return colission

    def enemyFieldBlocker(self, x, y, o):
        if (o == 0):
            for i in range(x - 50, x + self.shipSize + 50, 50):  # poziomo
                for j in range(y - 50, y + 100, 50):
                    if (i >= 650 and j >= 100 and i <= 1100 and j <= 550):
                        if (self.enemyGameTable[(i, j)] == 0):
                            self.enemyGameTable[(i, j)] = "X"
        else:
            for i in range(x - 50, x + 100, 50):  # pionowo
                for j in range(y - 50, y + self.shipSize + 50, 50):
                    if (i >= 650 and j >= 100 and i <= 1100 and j <= 550):
                        if (self.enemyGameTable[(i, j)] != 1 and (i, j) in self.enemyGameTable.keys()):
                            self.enemyGameTable[(i, j)] = "X"


    def shot(self,button:Button):
        x = button.winfo_x()
        y = button.winfo_y()
        if self.enemyGameTable[(x, y)] == 1:
            button.configure(bg="blue")
            self.enemyAllShips -= 1
        else:
            button.configure(bg="red")
        self.enemyShot()

    def enemyShot(self):
        while True:  # komputer bedzie losowal miejsce do strzalu dopoki nie trafi na takie co nie strzelal
            x = random.randrange(100, 600, 50)
            y = random.randrange(100, 600, 50)
            if (x, y) not in self.alreadyShootingHere:
                if self.player.playerGameTable[(x, y)] == 1:  # jezeli trafi
                    self.player.playerButtons[(x, y)].configure(bg="yellow")
                    self.player.playerAllShips -= 1
                else:
                    self.player.playerButtons[(x, y)].configure(bg="red")
                    self.alreadyShootingHere.append((x, y))
                break
            else:
                continue

