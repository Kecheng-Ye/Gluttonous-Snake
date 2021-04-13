class GameEnd(Exception):
    pass

class GameBoardIndexError(GameEnd):
    pass

class Bounds_checker:

    def __init__(self, w_limit, h_limit):
        self.width = w_limit
        self.height = h_limit

    def Check_coordinate(self, h, w, raise_warning=True):
        if h >= 0 and h < self.height:
            if w >= 0 and w < self.width:
                return True
        
        if raise_warning:
            raise GameBoardIndexError("index [{} {}] is invalid in Board ({}x{})".format(h, w, self.width, self.height))
        else:
            return False

# TODO: implement a generic version of direction
