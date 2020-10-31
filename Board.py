# Board.py
from graphics import *
from Player import *
from random import randint
from DieView import *

class Board:

    def __init__(self, win):
        i = Image(Point(512, 512), "parcheesi-board.gif")
        i.draw(win)
        self.win = win
        self.box_num = self.drawall(win)
        self.players = [Player(win, "blue", 150, 150), Player(win, "yellow", 150, 830),
                        Player(win, "green", 830, 830), Player(win, "red", 820, 150)]
        self.safe_spots = [Point(0, 1), Point(0, 1), Point(0, 1), Point(0, 1), Point(0, 1), Point(0, 1),
                           Point(0, 1), Point(0, 1), Point(0, 1), Point(0, 1), Point(0, 1), Point(0, 1)]
        self.end_spots = [Point(500, 500), Point(500, 550), Point(450, 525), Point(450, 525)]

    def cicle(self, player):
        #  Manages the order of the players
        if player == 3:
            player = 0
        else:
            player += 1
        return player

    def turn(self, win, i, dices):
        count = 0
        for d in dices:
            if dices[0] + dices[1] == 5 and self.players[i].start == 4: #if both dices add up to five
                self.players[i].spawn()
                self.players[i].add_path()
                break

            elif dices[0] + dices[1] == 5:
                choice = self.spawnorMove()  # The Player chooses to Spawn a Piece or Move a Piece
                if choice == 1:  # Choice for Spawn
                    self.players[i].spawn()
                    break
                else:
                    for dice in dices:
                        movedaPiece = False
                        while movedaPiece is False:
                            piece_num = self.boxToPiece(i)  # The player clicks a box to choose which Piece to move
                            nextcoord = self.players[i].pieces[piece_num].nextcoords(i, dice)

                            if self.isSafeSpot(nextcoord) and self.isOccupied(nextcoord):
                                pass  # Cant move the Piece if next coord is a safe space and is occupied:
                            elif self.isSafeSpot(nextcoord):
                                self.players[i].pieces[piece_num].move(dice)
                                self.isEndCoord(nextcoord, i)
                                movedaPiece = True
                            elif self.isOccupied(nextcoord):
                                self.eat(nextcoord)
                                self.players[i].pieces[piece_num].move(dice)
                                self.isEndCoord(nextcoord, i)
                                movedaPiece = True
                            else:
                                self.players[i].pieces[piece_num].move(dice)
                                self.isEndCoord(nextcoord, i)
                                movedaPiece = True

                            if movedaPiece is False:
                                print("Piece cant be moved")
                    break

            elif dices[1] == 5 and dices[0] != 5:
                for dice in reversed(dices):
                    if self.players[i].start == 4:  # If all pieces are on start
                        self.players[i].spawn()

                    elif 0 < self.players[i].start < 4 and dice == 5:  # if one or more pieces are in the Path
                        choice = self.spawnorMove()  # The Player chooses to Spawn a Piece or Move a Piece

                        if choice == 1:  # Choice for Spawn
                            self.players[i].spawn()

                        else:  # Choice for Move
                            movedaPiece = False  # Variable to continue
                            while movedaPiece is False:
                                piece_num = self.boxToPiece(i)  # The player clicks a box to choose which Piece to move
                                nextcoord = self.players[i].pieces[piece_num].nextcoords(i, dice)

                                if self.isSafeSpot(nextcoord) and self.isOccupied(nextcoord):
                                    pass  # Cant move the Piece if next coord is a safe space and is occupied:
                                elif self.isSafeSpot(nextcoord):
                                    self.players[i].pieces[piece_num].move(dice)
                                    self.isEndCoord(nextcoord, i)
                                    movedaPiece = True
                                elif self.isOccupied(nextcoord):
                                    self.eat(nextcoord)
                                    self.players[i].pieces[piece_num].move(dice)
                                    self.isEndCoord(nextcoord, i)
                                    movedaPiece = True
                                else:
                                    self.players[i].pieces[piece_num].move(dice)
                                    self.isEndCoord(nextcoord, i)
                                    movedaPiece = True

                                if movedaPiece is False:
                                    print("Piece cant be moved")

                    else:
                        movedaPiece = False  # Variable to continue
                        while movedaPiece is False:
                            piece_num = self.boxToPiece(i)  # The player clicks a box to choose which Piece to move
                            nextcoord = self.players[i].pieces[piece_num].nextcoords(i, dice)

                            if self.isSafeSpot(nextcoord) and self.isOccupied(nextcoord, i):
                                pass  # Cant move the Piece if next coord is a safe space and is occupied:
                            elif self.isSafeSpot(nextcoord):
                                self.players[i].pieces[piece_num].move(dice)
                                self.isEndCoord(nextcoord, i)
                                movedaPiece = True
                            elif self.isOccupied(nextcoord, i):
                                self.eat(nextcoord)
                                self.players[i].pieces[piece_num].move(dice)
                                self.isEndCoord(nextcoord, i)
                                movedaPiece = True
                            else:
                                self.players[i].pieces[piece_num].move(dice)
                                self.isEndCoord(nextcoord, i)
                                movedaPiece = True

                            if movedaPiece is False:
                                print("Piece cant be moved")


                break



            elif d == 5:  # If the dice is five(5)
                    if self.players[i].start == 4:  # If all pieces are on start
                        self.players[i].spawn()


                    elif 0 < self.players[i].start < 4:  # if one or more pieces are in the Path

                        choice = self.spawnorMove() # The Player chooses to Spawn a Piece or Move a Piece

                        if choice == 1: # Choice for Spawn
                            self.players[i].spawn()

                        else:  # Choice for Move

                            movedaPiece = False # Variable to continue
                            while movedaPiece is False:
                                piece_num = self.boxToPiece(i) # The player clicks a box to choose which Piece to move
                                nextcoord = self.players[i].pieces[piece_num].nextcoords(i, d)

                                if self.isSafeSpot(nextcoord) and self.isOccupied(nextcoord, i):
                                    pass  # Cant move the Piece if next coord is a safe space and is occupied:
                                elif self.isSafeSpot(nextcoord):
                                    self.players[i].pieces[piece_num].move(d)
                                    self.isEndCoord(nextcoord, i)
                                    movedaPiece = True
                                elif self.isOccupied(nextcoord, i):
                                    self.eat(nextcoord)
                                    self.players[i].pieces[piece_num].move(d)
                                    self.isEndCoord(nextcoord,i)
                                    movedaPiece = True
                                else:
                                    self.players[i].pieces[piece_num].move(d)
                                    self.isEndCoord(nextcoord, i)
                                    movedaPiece = True

                                if movedaPiece is False:
                                    print("Piece cant be moved")


            else:
                if 0 < self.players[i].path < 4:
                    movedaPiece = False  # Variable to continue
                    while movedaPiece is False:
                        piece_num = self.boxToPiece(i)  # The player clicks a box to choose which Piece to move
                        nextcoord = self.players[i].pieces[piece_num].nextcoords(i, d)

                        if self.isSafeSpot(nextcoord) and self.isOccupied(nextcoord, i):
                            pass  # Cant move the Piece if next coord is a safe space and is occupied:
                        elif self.isSafeSpot(nextcoord):
                            self.players[i].pieces[piece_num].move(d)
                            self.isEndCoord(nextcoord, i)
                            movedaPiece = True
                        elif self.isOccupied(nextcoord, i):
                            self.eat(nextcoord)
                            self.players[i].pieces[piece_num].move(d)
                            self.isEndCoord(nextcoord, i)
                            movedaPiece = True
                        else:
                            self.players[i].pieces[piece_num].move(d)
                            self.isEndCoord(nextcoord, i)
                            movedaPiece = True

                        if movedaPiece is False:
                            print("Piece cant be moved")

    def boxToPiece(self, i):
        clickedaBox = False
        while clickedaBox is False:
            click = self.win.getMouse()
            if self.box_num[0].getP2().getX() >= click.getX() >= self.box_num[0].getP1().getX() and self.box_num[0].getP2().getY() >= click.getY() >= self.box_num[0].getP1().getY():
                if self.players[i].pieces[0].isStart is False:
                    return 0
            elif self.box_num[1].getP2().getX() >= click.getX() >= self.box_num[1].getP1().getX() and self.box_num[1].getP2().getY() >= click.getY() >= self.box_num[1].getP1().getY():
                if self.players[i].pieces[1].isStart is False:
                    return 1
            elif self.box_num[2].getP2().getX() >= click.getX() >= self.box_num[2].getP1().getX() and self.box_num[2].getP2().getY() >= click.getY() >= self.box_num[2].getP1().getY():
                if self.players[i].pieces[2].isStart is False:
                    return 2
            elif self.box_num[3].getP2().getX() >= click.getX() >= self.box_num[3].getP1().getX() and self.box_num[3].getP2().getY() >= click.getY() >= self.box_num[3].getP1().getY():
                if self.players[i].pieces[3].isStart is False:
                    return 3

    def isEndCoord(self, nextcoord, i): # Adds one to the End Counter
        nextX = nextcoord.getX()
        nextY = nextcoord.getY()
        for s in self.end_spots:
            if nextX == s.getX() and nextY == s.getY():
                self.players[i].path -= 1
                self.players[i].end += 1

    def isSafeSpot(self, nextcoord):
        nextX = nextcoord.getX()
        nextY = nextcoord.getY()
        for s in self.safe_spots:
            if nextX == s.getX() and nextY == s.getY():
                print("Its Safe")
                return True
        print("NOT Safe")
        return False

    def isOccupied(self, nextcoord,i):
        nextX = nextcoord.getX()
        nextY = nextcoord.getY()
        for pl in self.players:
            for pi in pl.pieces:
                if self.players == pl:
                    pass
                elif nextX == pi.shape.getCenter().getX() and nextY == pi.shape.getCenter().getY():
                    print("Its Occupied")
                    return True
        print("Its not Occupied")
        return False

    def eat(self,nextcoord):
        nextX = nextcoord.getX()
        nextY = nextcoord.getY()
        for player in self.players:
            for piece in player.pieces:
                if nextX == piece.shape.getCenter().getX() and nextY == piece.shape.getCenter().getY():
                    player.add_start()
                    piece.moveToStart()
                    break

    def hasEnded(self):
        for p in range(len(self.players)):
            if self.players[p].end == 4:
                return True
        return False

    def spawnorMove(self):
        clickedaBox = False
        box = [Rectangle(Point(1200, 200), (Point(1250, 240))),
               Rectangle(Point(1270, 200), (Point(1320, 240)))]
        for x in box:
            x.setFill("black")
            x.draw(self.win)
        txt = [Text(Point(1225, 220), "Spawn"), Text(Point(1295, 220), "Move")]
        for x in txt:
            x.setOutline("white")
            x.draw(self.win)
        while clickedaBox is False:
            click = self.win.getMouse()
            print("Recieved Click for Spawn or Move")
            print(f"CLick is ({click.getX()}, {click.getY()}")
            print(f"X: {box[0].getP2().getX()} <= {click.getX()} <= {box[0].getP1().getX()}")
            print(box[0].getP2().getX() <= click.getX() <= box[0].getP1().getX())
            print(f"Y: {box[0].getP2().getY()} <= {click.getY()} <= {box[0].getP1().getY()}")
            print(box[0].getP2().getY() <= click.getY() <= box[0].getP1().getY())
            if box[0].getP2().getX() >= click.getX() >= box[0].getP1().getX() and box[0].getP2().getY() >= click.getY() >= box[0].getP1().getY():
                for x in txt:
                    x.undraw()
                for x in box:
                    x.undraw()
                return 1

            elif box[1].getP2().getX() >= click.getX() >= box[1].getP1().getX() and box[1].getP2().getY() >= click.getY() >= box[1].getP1().getY():
                for x in txt:
                    x.undraw()
                for x in box:
                    x.undraw()
                return 2

    def drawall(self, win):
        t1 = Text(Point(1250, 830), "What Piece do you want to move?")
        t1.setSize(22)
        t1.draw(win)
        numboxes = [Rectangle(Point(1150, 850), Point(1180, 880)), Rectangle(Point(1200, 850), Point(1230, 880)),
                 Rectangle(Point(1150, 900), Point(1180, 930)), Rectangle(Point(1200, 900), Point(1230, 930))]

        numtxt = [Text(Point(1165, 865), '1'), Text(Point(1215, 865), '2'),
               Text(Point(1165, 915), '3'), Text(Point(1215, 915), '4')]
        box2 = Rectangle(Point(1250, 600), Point(1330, 650))
        box2.setFill("black")
        box2.draw(win)
        txt2 =  Text(Point(1290, 625), 'Roll Dices')
        txt2.setOutline("white")
        txt2.draw(win)
        for x in numboxes:
            x.setFill("black")
            x.draw(win)
        for x in numtxt:
            x.setOutline("white")
            x.draw(win)
        return numboxes

def parcheesi():
    win = GraphWin("Parcheesi Game", 1500, 1024)
    theBoard = Board(win)
    dices2 = [DieView(win, Point(1200, 500), 100), DieView(win, Point(1400, 500), 100)]

    player = 0
    while theBoard.hasEnded() is False:
        t1 = Text(Point(1250, 80), f"Player {player+1}'s turn.")
        t1.setSize(22)
        t1.draw(win)
        moved = False
        win.getMouse()
        dices = rollDice(dices2)
        win.getMouse()
        theBoard.turn(win, player, dices)
        if dices[0] != dices[1]:
            player = theBoard.cicle(player)

        t1.undraw()

    win.getMouse()


def rollDice(dices2):
    dicevalue1 = randint(1, 6)
    dicevalue2 = randint(1, 6)
    dices2[0].setValue(dicevalue1)
    dices2[1].setValue(dicevalue2)
    return dicevalue1, dicevalue2


def main():
    parcheesi()


main()