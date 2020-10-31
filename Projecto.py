from graphics import *
from random import randint

class DieView:
    """ DieView is a widget that displays a graphical
    representation of a standard six-sided die."""

    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
           d1 = GDie(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides
        of length 20."""

        # first define some standard values
        self.win = win
        self.background = "white"  # color of die face
        self.foreground = "black"  # color of the pips
        self.psize = 0.1 * size  # radius of each pip
        hsize = size / 2.0  # half of size
        offset = 0.6 * hsize  # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx - hsize, cy - hsize)
        p2 = Point(cx + hsize, cy + hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        # Create 7 circles for standard pip locations
        self.pips = [self.__makePip(cx - offset, cy - offset),
                     self.__makePip(cx - offset, cy),
                     self.__makePip(cx - offset, cy + offset),
                     self.__makePip(cx, cy),
                     self.__makePip(cx + offset, cy - offset),
                     self.__makePip(cx + offset, cy),
                     self.__makePip(cx + offset, cy + offset)]

        # Create a table for which pips are on for each value
        self.onTable = [[], [3], [2, 4], [2, 3, 4],
                        [0, 2, 4, 6], [0, 2, 3, 4, 6], [0, 1, 2, 4, 5, 6]]

        self.setValue(1)

    def __makePip(self, x, y):
        """Internal helper method to draw a pip at (x,y)"""
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        """ Set this die to display value."""
        # Turn all the pips off
        for pip in self.pips:
            pip.setFill(self.background)

        # Turn the appropriate pips back on
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)


class Piece:

    def __init__(self, win, color, x, y):
        self.color = color
        self.win = win
        self.shape = Circle(Point(x, y), 15)
        self.shape.setFill(color)
        self.shape.draw(win)
        self.x = self.shape.getCenter().getX()
        self.y = self.shape.getCenter().getY()
        self.startX = x
        self.startY = y
        self.isSafe = True
        self.isStart = True
        self.times_moved = 0

    def get_position(self):
        return self.shape.getCenter()

    def get_color(self):
        return self.color

    def return_home(self):
        self.x = 0
        self.y = 0

    def move(self, times):
        # See parcheesi.jpg for E (Edges) 1 - 8 and P (Points) 1 - 4 References
        for x in range(times):
            if self.times_moved == 63:  # Move to get to home, when the piece has traveled all around.
                if self.shape.getCenter().getY() == 29:
                    self.shape.move(0, 41.5)  # Movement for blue Pieces to End
                elif self.shape.getCenter().getY() == 994.5:
                    self.shape.move(0, -41.5)  # Movement for Green Pieces to End
                elif self.shape.getCenter().getX() == 28.5:
                    self.shape.move(41.5, 0)  # Movement for Yellow Pieces to End
                else:
                    self.shape.move(-41.5, 0)  # Movement for Red Pieces to End

            elif self.shape.getCenter().getX() == 400 and self.shape.getCenter().getY() == 319.5:  # When the piece is in C1
                self.shape.move(-80, 81.5)

            elif self.shape.getCenter().getX() == 320 and self.shape.getCenter().getY() == 617:  # When the piece is in C2
                self.shape.move(81, 87)

            elif self.shape.getCenter().getX() == 617 and self.shape.getCenter().getY() == 704:  # When the piece is in C3
                self.shape.move(81, -87)

            elif self.shape.getCenter().getX() == 698 and self.shape.getCenter().getY() == 401:  # When the piece is in C4
                self.shape.move(-80, -81.5)

            elif self.shape.getCenter().getX() == 29.5 and self.shape.getCenter().getY() == 401:  # E1
                self.shape.move(0, -108)

            elif self.shape.getCenter().getX() == 29.5 and self.shape.getCenter().getY() == 617:  # E2
                self.shape.move(41.5, 0)

            elif self.shape.getCenter().getX() == 400 and self.shape.getCenter().getY() == 994.5:  # E3
                self.shape.move(108.5, 0)

            elif self.shape.getCenter().getX() == 617 and self.shape.getCenter().getY() == 994.5:  # E4
                self.shape.move(0, -41.5)

            elif self.shape.getCenter().getX() == 988.5 and self.shape.getCenter().getY() == 617:  # E5
                self.shape.move(0, -108)

            elif self.shape.getCenter().getX() == 988.5 and self.shape.getCenter().getY() == 401:  # E6
                self.shape.move(-41.5, 0)

            elif self.shape.getCenter().getX() == 618 and self.shape.getCenter().getY() == 29:  # E7
                self.shape.move(0, -109)

            elif self.shape.getCenter().getX() == 400 and self.shape.getCenter().getY() == 29:  # E8
                self.shape.move(0, 41.5)

            elif self.shape.getCenter().getX() == 29.5 and self.shape.getCenter().getY() == 509:  # P1
                self.shape.move(0, -108)

            elif self.shape.getCenter().getX() == 508.5 and self.shape.getCenter().getY() == 994.5:  # P2
                self.shape.move(0, -108)

            elif self.shape.getCenter().getX() == 998.5 and self.shape.getCenter().getY() == 509:  # P3
                self.shape.move(0, -108)

            elif self.shape.getCenter().getX() == 509 and self.shape.getCenter().getY() == 29.5:  # P4
                self.shape.move(0, -108)

            elif self.shape.getCenter().getX() == 400:
                self.shape.move(0, 41.5)

            elif self.shape.getCenter().getY() == 401:
                self.shape.move(-41.5, 0)

            elif self.shape.getCenter().getY() == 617:
                self.shape.move(41.5, 0)

            elif self.shape.getCenter().getX() == 617:
                self.shape.move(0, -41.5)

            self.times_moved += 1


    def moveToStart(self):
        while self.shape.getCenter().getX() != self.startX:
            if self.shape.getCenter().getX() > self.startX:
                self.shape.move(-0.5, 0)
            else:
                self.shape.move(0.5, 0)

        while self.shape.getCenter().getY() != self.startY:
            if self.shape.getCenter().getY() > self.startY:
                self.shape.move(0, -0.5)
            else:
                self.shape.move(0, 0.5)


    def nextcoords(self, i, times):
        #  Determines the coordinates of the next move for a piece
        nextX = self.shape.getCenter().getX()
        nextY = self.shape.getCenter().getY()
        tmoved = self.times_moved
        for x in range(times):
            if tmoved == 63:  # Move to get to home, when the piece has traveled all around.
                if nextY == 29:
                    nextY += 41.5  # Movement for blue Pieces
                elif nextY == 994.5:
                    nextY -= 41.5 # Movement for Green Pieces
                elif nextX == 28.5:
                    nextX += 41.5  # Movement for Yellow Pieces
                else:
                    nextX -= 41.5  # Movement for Red Pieces

            elif nextX == 400 and nextY == 319.5:  # When the piece is in C1(Corner 1)
                nextX -= 80
                nextY += 80

            elif nextX == 28.9 and nextY == 509:  # When the piece is in C1(Corner 2)
                nextX += 82
                nextY += 87

            elif nextX == 617 and nextY == 745.5:  # When the piece is in C3(Corner 3)
                nextX += 84
                nextY -= 85

            elif nextX == 701 and nextY == 401:  # When the piece is in C3(Corner 3)
                nextX -= 80
                nextY -= 40

            elif nextX == 400:
                nextY += 41.5

            elif nextY == 401:
                nextX -= 41.5

            elif nextY == 617:
                nextX += 41.5

            elif nextX == 617:
                nextY -= 41.5

            self.times_moved += 1

        return Point(nextX, nextY)

class Player:

    def __init__(self, win, color, x, y):
        self.color = color
        self.win = win
        self.pieces = [Piece(win, color, x, y), Piece(win, color, x+40, y),
                       Piece(win, color, x, y+40), Piece(win, color, x+40, y+40)]
        self.color = color
        self.start = 4
        self.path = 0
        self.end = 0
        self.safe_spots = [Point(400, 195), Point(195.5, 401), Point(29.5, 509), Point(195, 617),
                           Point(400, 828.5), Point(508.5, 994.5), Point(617, 828.5), Point(822.5, 617),
                           Point(988.5, 509), Point(822.5, 401), Point(618, 195), Point(509, 29)]

    def spawn(self):
        for i in range(len(self.pieces)):
            if self.pieces[i].isStart is True:
                self.add_path()
                if self.color == 'blue':
                    self.moveTo(i, 400, 195)
                    self.pieces[i].isStart = False
                    break
                elif self.color == 'yellow':
                    self.moveTo(i, 195.5, 617)
                    self.pieces[i].isStart = False
                    break
                elif self.color == 'green':
                    self.moveTo(i, 617, 828.5)
                    self.pieces[i].isStart = False
                    break
                else:
                    self.moveTo(i, 822.5, 401)
                    self.pieces[i].isStart = False
                    break

    def moveTo(self, i, x, y):
        # Move the Piece to an exact Desired Coordinates (Ex. Spawn, Start)
        while self.pieces[i].shape.getCenter().getX() != x:
            if self.pieces[i].x > x:
                self.pieces[i].shape.move(-0.5, 0)
            else:
                self.pieces[i].shape.move(0.5, 0)

        while self.pieces[i].shape.getCenter().getY() != y:
            if self.pieces[i].y > y:
                self.pieces[i].shape.move(0, -0.5)
            else:
                self.pieces[i].shape.move(0, 0.5)


    def add_start(self):
        self.path -= 1
        self.start += 1

    def add_path(self):
        self.start -= 1
        self.path += 1

    def add_end(self):
        self.path -= 1
        self.end += 1

    def get_start(self):
        return self.start

    def get_path(self):
        return self.path

    def get_end(self):
        return self.end


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