class GameEnd(Exception):
    """
    A encapsulation of python Exception
    
    Aims to raise a specific exception to notify that the game ends 
    """
    pass

class GameBoardIndexError(Exception):
    """
    A encapsulation of python Exception
    
    Aims to raise a specific exception to notify that one round of game fails  
    """
    pass

class Bounds_checker:
    """
    The class for checking if some coordinate is not valid in the given board setting

    Args: 
          w_limit(int): the width of the game board
          h_limit(int): the height of the game board
    """
    def __init__(self, w_limit, h_limit):
        self.width = w_limit
        self.height = h_limit

    def Check_coordinate(self, h, w, raise_warning=True, error_message = None):
        """
        The actual check function
        Take in a `h` and `w` coordinate and decide whether this coordinate is out of bound of the game board

        Args: 
             h(int):                the input h coordinate
             w(int):                the input w coordinate
             raise_warning(bool):   the flag decide whether this function will raise exception or not
             error_message(str):    the error message for the raised warning
        """
        # check h is in [0 - self.height] bound
        if h >= 0 and h < self.height:
            # check w is in [0 - self.height] bound
            if w >= 0 and w < self.width:
                return True
        
        # raise warning if needed
        if raise_warning:
            error_message = error_message if error_message else "index [{} {}] is invalid in Board ({}x{})".format(h, w, self.width, self.height)
            raise GameBoardIndexError(error_message)
        else:
            return False

# the movement dict for each direction
# Ex: if a snake node with coordinate (h, w) is moved to the left with one unit
#     then result node coordinate will be (h, w - 1)
Direction_dict = dict(left     = (0, -1),
                      up       = (-1, 0),
                      right    = (0, 1),
                      down     = (1, 0))
