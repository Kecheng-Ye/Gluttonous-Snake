import time
from datetime import datetime
from pysigset import suspended_signals

from .board import *
from .Keyboard_control import *
from .render import *


class Glutonous_Snake:

    def __init__(self, width, height):
        self.game_board     = board(width, height)
        self.render_engine  = Render_engine()
        self.cur_operation  = [None]
        self.key_listener   = Key_listener(self.cur_operation)
        self.direction_dict = {Key.left : "left", 
                              Key.right : "right", 
                              Key.up    : "up", 
                              Key.down  : "down"}
        self.keyboard_signal = signal.signal(signal.SIGUSR1, self.update)
        self.exit_signal     = signal.signal(signal.SIGUSR2, self.game_end)

    def start(self):
        try:
            self.key_listener.start()
            while(True):
                self.update()

        except GameBoardIndexError as error:
            print("Snake crash because", str(error))

        except GameEnd:
            print("Game end because player press 'ESC'")
    
    def update(self, num = None, stack = None):
        # now = datetime.now()
        # print("now =", now)
        # with suspended_signals(signal.SIGUSR1):
        
        if self.cur_operation[0]:
            # print("Snake head {} with operation {}".format(self.game_board.Snake.head.get_coordinates(), self.cur_operation))
            move_direction = self.direction_dict[self.cur_operation[0]]
            self.game_board.Snake_move(move_direction)
        
        self.game_board.Update_board()

        with suspended_signals(signal.SIGUSR1):
            self.render_engine.render_terminal(self.game_board)
        
        time.sleep(0.1)

    def game_end(self, num = None, stack = None):
        raise GameEnd


if __name__ == "__main__":
    # opr = ""
    # listener = Key_listener(opr)
    # listener.start()
    # for i in range(10):
    #     print(i)
    # listener.join()

    game = Glutonous_Snake(20, 20)
    game.start()
