import os
import signal
import threading

from pynput.keyboard import Key, Listener

from .utils import *


class Key_listener:
    """
    Key listener class for our game

    Bascially this class will start a new thread and begin the Listener process from ``pynput.keyboard`` package.
    Once it recive a valid keyboard signal, it will write the key to a list named `operation` with length only 1
    and raise a signal to inform the main thread

    Args: 
         operation(list[Key]) : The operation list given by the main thread, once there is a valid operation, 
                                it will be writen on the first element of the list
    """
    def __init__(self, operation):
        # the actual listener thread
        self.listener_thread = threading.Thread(target=self.listen, daemon=True)
        # we only accept 4 direction key
        # the reason for using `set` instead of list is that 
        # set can use O(1) time to check whether the item is in itself or not
        self.valid_keys = set([Key.left, Key.right, Key.up, Key.down])
        # hard code some rule for operation
        # Ex: once you let the snake go left, you cannot directly let the snake go right
        #     or it will eat itself
        self.opposite_direction = {Key.left : Key.right, 
                                   Key.up : Key.down,
                                   Key.right : Key.left,
                                   Key.down : Key.up}
        self.operation = operation


    def on_press(self, key):
        """
        The call back function for key pressed event

        Once there is a key pressed event detected by the listener, it will call this function
        """

        # if the pressed key is one of four direction key 
        # and it is different that the previous valid key
        if key in self.valid_keys and key != self.operation[0]:
            # and if the pressed direction key is not the opposite direction of previous pressed direction 
            if not self.operation[0] or key != self.opposite_direction[self.operation[0]]:
                # we will consider this direction as valid
                # update the operation list
                self.operation[0] = key
                # raise signal to notify the main thread
                os.kill(os.getpid(), signal.SIGUSR1)

        # if the `ESC` key pressed
        if key == Key.esc:
            # raise another signal to notify the main thread to shut down the game
            os.kill(os.getpid(), signal.SIGUSR2)


    def on_release(self, key):
        """
        The call back function for key released event

        do nothing
        """
        pass


    def listen(self):
        """
        The function that the thread will exectue
        Basically it follow the Listener api
        no worry for detailed implementation
        """
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()


    def start(self):
        """
        Start the thread
        """
        self.listener_thread.start()
    
    
    def join(self):
        """
        let the thread join the main thread
        """
        self.listener_thread.join()

if __name__ == "__main__":
    Key_listener = Key_listener([None])
    Key_listener.start()
    Key_listener.join()
