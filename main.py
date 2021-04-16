import argparse
from Game_component import *

class Problem:

    def phase_1(self):
        """
        Expect Output:

        ```{bash}
        This is a empty spot with coordinate [0, 0]
        This is a fruit spot with coordinate [0, 0]
        ```

        """
        test_block_1 = Empty_Spot(0, 0)
        print(test_block_1)

        test_block_2 = Fruit_Spot(0, 0)
        print(test_block_2)


    def phase_2(self):
        """
        Expect Output:

        ```{bash}
        Two seperate Snake node
        *******************************
        This is a snake node with coordinate [1, 1]
        With its prev snake of [None, None]
        And its next snake of [None, None]
        *******************************
        This is a snake node with coordinate [1, 2]
        With its prev snake of [None, None]
        And its next snake of [None, None]


        Now connect them together
        *******************************
        This is a snake node with coordinate [1, 1]
        With its prev snake of [None, None]
        And its next snake of [1, 2]
        *******************************
        This is a snake node with coordinate [1, 2]
        With its prev snake of [1, 1]
        And its next snake of [None, None]
        ```
        
        """
        print("Two seperate Snake node")
        test_snake_node_1 = Snake_Node(1,1)
        print("*******************************")
        print(test_snake_node_1)

        test_snake_node_2 = Snake_Node(1,2)
        print("*******************************")
        print(test_snake_node_2)
        
        print("\n\nNow connect them together")
        test_snake_node_1.connect(test_snake_node_2)

        print("*******************************")
        print(test_snake_node_1)
        print("*******************************")
        print(test_snake_node_2)


    def phase_3(self):
        """
        Expected Output
        ```{bash}
        *******************************
        This is a snake node with coordinate [1, 1]
        With its prev snake of [None, None]
        And its next snake of [1, 2]
        *******************************
        This is a snake node with coordinate [1, 2]
        With its prev snake of [1, 1]
        And its next snake of [1, 3]
        *******************************
        This is a snake node with coordinate [1, 3]
        With its prev snake of [1, 2]
        And its next snake of [None, None]


        One Snake object with above three nodes
        *******************************
        This is a Snake object of length 3
        With its children in the following order:

        This is a snake node with coordinate [1, 1]
        With its prev snake of [None, None]
        And its next snake of [1, 2]
        This is a snake node with coordinate [1, 2]
        With its prev snake of [1, 1]
        And its next snake of [1, 3]
        This is a snake node with coordinate [1, 3]
        With its prev snake of [1, 2]
        And its next snake of [None, None]

        We can also iterate the Snake object
        *******************************
        Node 1:
        This is a snake node with coordinate [1, 1]
        With its prev snake of [None, None]
        And its next snake of [1, 2]
        Node 2:
        This is a snake node with coordinate [1, 2]
        With its prev snake of [1, 1]
        And its next snake of [1, 3]
        Node 3:
        This is a snake node with coordinate [1, 3]
        With its prev snake of [1, 2]
        And its next snake of [None, None]
        ```
        """
        test_snake_node_1 = Snake_Node(1,1)
        test_snake_node_2 = Snake_Node(1,2)
        test_snake_node_3 = Snake_Node(1,3)
        test_snake_node_1.connect(test_snake_node_2)
        test_snake_node_2.connect(test_snake_node_3) 

        print("Three connected Snake node")
        print("*******************************")
        print(test_snake_node_1)
        print("*******************************")
        print(test_snake_node_2)
        print("*******************************")
        print(test_snake_node_3)

        print("\n\nOne Snake object with above three nodes")
        test_snake = Snake(test_snake_node_1, test_snake_node_3, 3)
        print("*******************************")
        print(test_snake)

        print("We can also iterate the Snake object")
        print("*******************************")
        for i, node in enumerate(test_snake):
            print("Node {}:".format(i + 1))
            print(node)


    def phase_4(self):
        """
        Expected Output

        Note: The given coordinates part should be exactly the same as the standard output
              while the two random choice part can be different than the output as long as the 
              two board you generate shows some form of randomness

        ```
        Testing with given coordinate
        *******************************
        Detect None Empty Spot on the game_board
        This is a fruit spot with coordinate [0, 0]
        Detect None Empty Spot on the game_board
        This is a snake node with coordinate [1, 1]
        With its prev snake of [None, None]
        And its next snake of [None, None]
        length of the empty spot: 23


        Testing with random coordinate
        *******************************
        Detect None Empty Spot on the game_board
        This is a snake node with coordinate [0, 0]
        With its prev snake of [None, None]
        And its next snake of [None, None]
        Detect None Empty Spot on the game_board
        This is a fruit spot with coordinate [0, 3]
        length of the empty spot: 23
        *******************************
        Detect None Empty Spot on the game_board
        This is a snake node with coordinate [2, 3]
        With its prev snake of [None, None]
        And its next snake of [None, None]
        Detect None Empty Spot on the game_board
        This is a fruit spot with coordinate [3, 0]
        length of the empty spot: 23
        ```
        """

        def phase_4_checker(board):
            game_board =board.game_board
            for i in range(board.height):
                for j in range(board.width):
                    if not isinstance(game_board[i][j], Empty_Spot):
                        print("Detect None Empty Spot on the game_board")
                        print(game_board[i][j])

                        if (i, j) in board.empty_spot:
                            print("Error!!!!")
                            print("Detect this Node[{} {}] still in the empty spot".format(i, j))

            print("length of the empty spot: {}".format(len(board.empty_spot)))


        test_board_1 = board(5, 5, [1, 1], [0, 0])
        print("Testing with given coordinate")
        print("*******************************")
        phase_4_checker(test_board_1)

        print("\n\nTesting with random coordinate")
        print("*******************************")
        test_board_2 = board(5, 5)
        phase_4_checker(test_board_2)
        print("*******************************")
        test_board_3 = board(5, 5)
        phase_4_checker(test_board_3)


    def phase_5(self):
        """
        Expect Output

        ```{shell}
        -----------
        |X        |
        |  S      |
        |         |
        |         |
        |         |
        -----------
        ```
        """
        test_board_1 = board(5, 5, [1, 1], [0, 0])
        render = Render_engine('terminal', test_board_1)

        render.render_terminal(test_board_1)


    def phase_6(self):
        """
        Expect Output
        
        ```{shell}
        -----------
        |      S S|
        |        S|
        |        S|
        |  S X   S|
        |  S S S S|
        -----------


        Specific Information of this snake
        *******************************
        This is a Snake object of length 10
        With its children in the following order:

        This is a snake node with coordinate [3, 1]
        With its prev snake of [None, None]
        And its next snake of [4, 1]
        This is a snake node with coordinate [4, 1]
        With its prev snake of [3, 1]
        And its next snake of [4, 2]
        This is a snake node with coordinate [4, 2]
        With its prev snake of [4, 1]
        And its next snake of [4, 3]
        This is a snake node with coordinate [4, 3]
        With its prev snake of [4, 2]
        And its next snake of [4, 4]
        This is a snake node with coordinate [4, 4]
        With its prev snake of [4, 3]
        And its next snake of [3, 4]
        This is a snake node with coordinate [3, 4]
        With its prev snake of [4, 4]
        And its next snake of [2, 4]
        This is a snake node with coordinate [2, 4]
        With its prev snake of [3, 4]
        And its next snake of [1, 4]
        This is a snake node with coordinate [1, 4]
        With its prev snake of [2, 4]
        And its next snake of [0, 4]
        This is a snake node with coordinate [0, 4]
        With its prev snake of [1, 4]
        And its next snake of [0, 3]
        This is a snake node with coordinate [0, 3]
        With its prev snake of [0, 4]
        And its next snake of [None, None]
        ```
        """
        test_board_1 = board(5, 5, snake_init_coordinates = [3, 1], fruit_init_coordinates = [3, 2])
        test_board_1.Snake_init_from_lst([[3, 1], [4, 1], [4, 2], [4, 3], [4, 4], [3, 4], [2, 4], [1, 4], [0, 4], [0, 3]])
        test_board_1.Update_board()
        render = Render_engine('terminal', test_board_1)
        render.render_terminal(test_board_1)

        print("\n\nSpecific Information of this snake")
        print("*******************************")
        print(test_board_1.Snake)

    
    def phase_7(self):
        
        test_board_1 = board(5, 5, snake_init_coordinates = [4, 2], fruit_init_coordinates = [0, 2])
        render = Render_engine('terminal', test_board_1)
        print("Before grow")
        print("*******************************")
        render.render_terminal(test_board_1)
        print("\n\nafter grow once")
        print("*******************************")
        test_board_1.Snake_grow("right")
        test_board_1.Update_board()
        render.render_terminal(test_board_1)
        print("\n\nafter grow twice")
        print("*******************************")
        test_board_1.Snake_grow("right")
        test_board_1.Update_board()
        render.render_terminal(test_board_1)
        print("\n\nafter grow three times")
        print("*******************************")
        test_board_1.Snake_grow("right")
        test_board_1.Update_board()
        render.render_terminal(test_board_1)




def parse_args():
    parser = argparse.ArgumentParser(description='Make your own Glutonous_Snake')
    parser.add_argument('--phase',type=int, default=1, help='What phase you are solving')
    args = parser.parse_args()
    return args



def main():
    args = parse_args()
    problem = Problem()

    problem_func = getattr(Problem, "phase_{}".format(args.phase))
    problem_func(problem)




if __name__ == '__main__':
    main()