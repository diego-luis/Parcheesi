class Piece:

    x = 0
    y = 0

    def __init__(self, color, win):
        self.color = color
        self.win = win

    def move(self, x, y):
        self.y = self.y + y
        self.x = self.x + x

    def get_position(self):
        return self.x, self.y

    def get_color(self):
        return self.color

    def return_home(self):
        self.x = 0
        self.y = 0
