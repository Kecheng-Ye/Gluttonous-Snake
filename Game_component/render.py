from .board import *
import threading
import time

class Render_engine:
    def __init__(self, render_platform, game_board):
        assert render_platform in ['terminal']
        
        self.render_platform = render_platform
        self.game_board = game_board
        self.show = False
        self.render_thread = threading.Thread(target=self.render, daemon=True)


    def render(self):
        if self.render_platform == 'terminal':
            render_function = self.render_terminal

        while True:
            if self.show:
                render_function(self.game_board)
                time.sleep(0.01)


    def render_terminal(self, board):
        result = "-" * (board.width * 2 + 1) + "\n"

        for i in range(board.height):
            result += "|"
            for j in range(board.width):
                result += board.game_board[i][j].render_terminal()
                if j < board.width - 1:
                    result += " "
            
            result += "|\n"
        
        result += "-" * (board.width * 2 + 1)

        print(result)
    
    def start(self):
        self.show = True
        self.render_thread.start()

    def pause(self):
        self.show = False

    def restart(self):
        self.show = True

    def is_running(self):
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