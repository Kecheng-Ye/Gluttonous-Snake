from board import *
from render import *
from pynput.keyboard import Key, Listener
import threading
import time

class Key_listener:

    def __init__(self, operation):
        self.listener_thread = threading.Thread(target=self.listen, daemon=True)
        self.valid_keys = set([Key.left, Key.right, Key.up, Key.down])
        self.operation = operation

    def on_press(self, key):
        if key in self.valid_keys:
            # print('{0} pressed'.format(key))
            self.operation[0] = key

    def on_release(self, key):
        if key in self.valid_keys:
            # print('{0} release'.format(key))
            self.operation[0] = key

        if key == Key.esc:
            raise GameEnd

    def listen(self):
        # Collect events until released
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def start(self):
        self.listener_thread.start()
    
    def join(self):
        self.listener_thread.join()


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

    def start(self):
        try:
            self.key_listener.start()
            while(True):

                if self.cur_operation[0]:
                    move_direction = self.direction_dict[self.cur_operation[0]]
                    self.game_board.Snake_move(move_direction)
                
                self.game_board.Update_board()
                self.render_engine.render_terminal(self.game_board)
                time.sleep(0.5)

        except GameBoardIndexError:
            print("Snake crash, end")

        except GameEnd:
            print("Game end")
    


if __name__ == "__main__":
    # opr = ""
    # listener = Key_listener(opr)
    # listener.start()
    # for i in range(10):
    #     print(i)
    # listener.join()

    game = Glutonous_Snake(5, 5)
    game.start()