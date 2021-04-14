import time
from datetime import datetime
from pysigset import suspended_signals

from .board import *
from .Keyboard_control import *
from .render import *


class Glutonous_Snake:
    """
    The main game class

    The game will be exectuted along with ``3`` threads
    1. The `main thread` which is the game thread mainly concerned with our game board
    2. The `keyboard listener thread` which will catch any keyboard signal and write the valid keyboard opeartion onto the ``cur_operation`` list,
       then the main thread will change the game board state based on this operation
    3. The `render engine thread` which will continuously render our game board on certain platform to inform the user what is going on of the game board

    Args: 
         width(int):    The width of the game board
         height(int):   The height of the game board

    Class member:
         game_board(board):                 The actual game board

         render_engine(Render_engine):      The render engine

         key_listener(Key_listener):        The Key listener

         cur_operation(list[Key]):          The list that contains the valid keyboard opeartion updated by `key_listener`

         direction_dict(dict[Key : str]):   The dictionary that maps a certain direction key to its string representation

         keyboard_signal(signal):           The signal that will be activated when `key_listener` detect a valid direction key
                                            once this signal has been detected, the `self.update` function will automatically executed
                                            
         exit_signal(signal):               The signal that will be activated when `key_listener` detect a `ESC` key
                                            once this signal has been detected, the `self.game_end` function will automatically executed
    """
    def __init__(self, width, height):
        self.game_board     = board(width, width)
        self.render_engine  = Render_engine("terminal", self.game_board)
        self.cur_operation  = [None]
        self.key_listener   = Key_listener(self.cur_operation)
        self.direction_dict = {Key.left : "left", 
                              Key.right : "right", 
                              Key.up    : "up", 
                              Key.down  : "down"}
        self.keyboard_signal = signal.signal(signal.SIGUSR1, self.update)
        self.exit_signal     = signal.signal(signal.SIGUSR2, self.game_end)

        # start the two working threads
        self.key_listener.start()
        self.render_engine.start()

    def start(self):
        try:
            while(True):
                try:
                    self.update()
                except GameBoardIndexError as error:
                    print("Snake crash because", str(error))
                    print("Press Any 'direction key' to restart or 'ESC' to quit the game")
                    self.render_engine.pause()
                    self.restart()

        except GameEnd:
            print("Game end")
    
    def update(self, num = None, stack = None):
        if self.cur_operation[0]:
            if not self.render_engine.is_running():
                self.render_engine.restart()
            move_direction = self.direction_dict[self.cur_operation[0]]
            self.game_board.Snake_move(move_direction)
        
        self.game_board.Update_board()
        time.sleep(0.2)

    def restart(self):
        self.game_board.restart()
        self.cur_operation[0] = None

    def game_end(self, num = None, stack = None):
        raise GameEnd


if __name__ == "__main__":
    game = Glutonous_Snake(20, 20)
    game.start()
