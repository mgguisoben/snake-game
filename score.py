from pygame import draw

BORDER_WD = 3


class ScoreBoard:

    def __init__(self, window, window_lt):
        self.window = window
        self.lt = window_lt - 17

        self.border_pts = [(17, 37), (self.lt, 37), (self.lt, self.lt), (17, self.lt)]

    def create_border(self):
        border = draw.lines(self.window, "black", True, self.border_pts, BORDER_WD)
        return border
