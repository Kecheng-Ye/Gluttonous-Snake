from board import *
from render import *
from Keyboard_control import *
import time


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

        except GameBoardIndexError:
            print("Snake crash, end")

        except GameEnd:
            print("Game end")
    
    def update(self, num = None, stack = None):
        if self.cur_operation[0]:
            move_direction = self.direction_dict[self.cur_operation[0]]
            self.game_board.Snake_move(move_direction)
        
        self.game_board.Update_board()
        self.render_engine.render_terminal(self.game_board)
        time.sleep(0.5)

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