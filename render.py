from board import *

class Render_engine:

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