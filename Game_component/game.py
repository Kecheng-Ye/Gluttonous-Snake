import time
from datetime import datetime
from pysigset import suspended_signals

from .board import *
from .Keyboard_control import *
from .render import *


class Glutonous_Snake:

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
    opr = ""
    listener = Key_listener(opr)
    listener.start()
    for i in range(10):
        print(i)
    listener.join()

    game = Glutonous_Snake(20, 20)
    game.start()
