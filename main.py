from Game_component import *

def main():
    game = Glutonous_Snake(5, 5)
    game.start()


if __name__ == '__main__':
    # main()
    engine = Render_engine('terminal', None)
    board = board(5, 5, snake_init_coordinates = [3, 1], fruit_init_coordinates = [0, 2])
    board.Snake_init_from_lst([[1, 2], [2, 2], [3, 2], [4, 2], [4, 1]])
    board.Update_board()
    engine.render_terminal(board)
    board.Snake_move("up")
    board.Update_board()
    engine.render_terminal(board)