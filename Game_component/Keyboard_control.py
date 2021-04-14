import os
import signal
import threading

from pynput.keyboard import Key, Listener

from .utils import *


class Key_listener:

    def __init__(self, operation):
        self.listener_thread = threading.Thread(target=self.listen, daemon=True)
        self.valid_keys = set([Key.left, Key.right, Key.up, Key.down])
        self.opposite_direction = {Key.left : Key.right, 
                                   Key.up : Key.down,
                                   Key.right : Key.left,
                                   Key.down : Key.up}
        self.operation = operation

    def on_press(self, key):
        if key in self.valid_keys and key != self.operation[0]:
            if not self.operation[0] or key != self.opposite_direction[self.operation[0]]:
                self.operation[0] = key
                os.kill(os.getpid(), signal.SIGUSR1)


    def on_release(self, key):
        if key == Key.esc:
            os.kill(os.getpid(), signal.SIGUSR2)

    def listen(self):
        # Collect events until released
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def start(self):
        self.listener_thread.start()
    
    def join(self):
        self.listener_thread.join()

if __name__ == "__main__":
    Key_listener = Key_listener([None])
    Key_listener.start()
    Key_listener.join()
