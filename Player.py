from graphics import *
from Piece import *

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
