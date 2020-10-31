from graphics import *

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
            print(f"Current X: {self.shape.getCenter().getX()}")
            print(f"Current Y: {self.shape.getCenter().getY()}\n")
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

        print(f"Current X: {self.shape.getCenter().getX()}")
        print(f"Current Y: {self.shape.getCenter().getY()}\n")

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