class GameEnd(Exception):
    pass

class GameBoardIndexError(GameEnd):
    pass

class Bounds_checker:

    def __init__(self, w_limit, h_limit):
        self.width = w_limit
        self.height = h_limit

    def Check_coordinate(self, h, w, raise_warning=True, error_message = None):
        if h >= 0 and h < self.height:
            if w >= 0 and w < self.width:
                return True
        
        if raise_warning:
            error_message = error_message if error_message else "index [{} {}] is invalid in Board ({}x{})".format(h, w, self.width, self.height)
            raise GameBoardIndexError(error_message)
        else:
            return False

Direction_dict = dict(left     = (0, -1),
                      up       = (-1, 0),
                      right    = (0, 1),
                      down     = (1, 0))
