from board import *

class Render_engine:

    def render_terminal(self, board):
        result = "-------------------------------\n"

        for i in range(board.height):
            for j in range(board.width):
                result += board.game_board[i][j].render_terminal() + " "
            
            result += "\n"
        
        result += "-------------------------------"

        print(result)

    
if __name__ == "__main__":
    engine = Render_engine()
    board = board(3, 3)
    engine.render_terminal(board)
