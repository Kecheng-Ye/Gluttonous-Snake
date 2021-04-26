from Game_componentboard import *
import threading
import time

class Render_engine:
    """
    The render engine class for our game
    Bascially this class will open a new thread and continously render the game board on different platform (now only support terminal render)

    Args: 
         render_platform(str) : the platform that our render engine will render the game board on
         game_board(board)    : the actual game board
         refresh_rate(float)  : How long will the engine refresh rendering, the less the time is,
                                Then the engine will render the game board more often
    """
    def __init__(self, render_platform, game_board, refresh_rate = 0.01):
        assert render_platform in ['terminal']
        
        self.render_platform = render_platform
        self.game_board = game_board
        # the logical flag that stop or start the rendering 
        self.show = False
        # the actual render thread which will execute the `self.render` function
        self.render_thread = threading.Thread(target=self.render, daemon=True)
        self.refresh_rate = refresh_rate


    def render(self):
        # determine the render function based on the 
        if self.render_platform == 'terminal':
            render_function = self.render_terminal
        # Let the thread run forever in this function
        while True:
            # if the render engine is start
            if self.show:
                # then the engine will render the board into specific platform
                # in every 0.01 sec
                render_function(self.game_board)
                time.sleep(self.refresh_rate)


    def render_terminal(self, board):
        """
        Specific render function for terminal
        It will basically print the cuurent state of game board 
        on the terminal 

        Args: 
              board(board) : the game board of our game

        The example output of a game board(5 x 5):
        ```
        -----------
        |         |
        |         |
        |         |
        |      X  |
        |        S|
        -----------
        ```
        The `Snake` is denoted with letter `S`
        and the `Fruit` is shown as `X`
        """
        # implement your code below
        result = ""

        for i in range(board.height):
            
            for j in range(board.width):
                # invoke each block's render teriminal function
                pass

        print(result)
        pass 

    def start(self):
        """
        Set the show flag to ``TRUE``
        and start the render_thread
        """
        self.show = True
        self.render_thread.start()


    def pause(self):
        """
        Set the show flag to ``FALSE``
        This can let the render engine to stop rendering without close this thread
        """
        self.show = False


    def restart(self):
        """
        Set the show flag back to ``TRUE``
        and the render engine will continue to render the game board
        """
        self.show = True


    def is_running(self):
        """
        Return the status of render engine
        """
        return self.show


if __name__ == "__main__":
    engine = Render_engine()
    board = board(5, 5, snake_init_coordinates = [3, 1], fruit_init_coordinates = [3, 2])
    # board.Fruit_lst = [(1, 2)]
    # board.Update_board()
    # engine.render_terminal(board)

    # board.Snake_grow("up")
    # board.Snake_grow("left")
    # # board.Snake_grow("left")
    # # board.Snake_grow("left")
    # board.Update_board()
    # engine.render_terminal(board)
    # print(len(board.empty_spot))

    # board.Snake_grow("right")
    # board.Update_board()
    # engine.render_terminal(board)
    # print(len(board.empty_spot))

    # board.Snake_move("right")
    # board.Update_board()
    # engine.render_terminal(board)
    # print(len(board.empty_spot))

    # board.Snake_move("up")
    # board.Update_board()
    # engine.render_terminal(board)
    # print(len(board.empty_spot))

    board.Snake_init_from_lst([[3, 1], [4, 1], [4, 2], [4, 3], [4, 4], [3, 4], [2, 4], [1, 4], [0, 4], [0, 3]])
    board.Update_board()
    engine.render_terminal(board)
    board.Snake_move("right")
    board.Update_board()
    engine.render_terminal(board)