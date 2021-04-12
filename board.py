from block import *
from random import choice, randrange

class board:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.game_board = []
        self.empty_spot = []
        self.Snake = None

        for i in range(self.height):
            self.game_board.append([])
            for j in range(self.width):
                self.game_board[i].append(Empty_Spot(i, j))
                self.empty_spot.append((i, j))

        self.game_initialize()
    
    def game_initialize(self):
        # add snake
        snake_init_idx = randrange(len(self.empty_spot))
        snake_init_x, snake_init_y = self.empty_spot[snake_init_idx]
        self.game_board[snake_init_x][snake_init_y] = Snake_Node(snake_init_x, snake_init_y)
        self.empty_spot.pop(snake_init_idx)
        self.Snake = Snake(head = self.game_board[snake_init_x][snake_init_y], end = None)

        # add fruit
        fruit_init_idx = randrange(len(self.empty_spot))
        fruit_init_x, fruit_init_y = self.empty_spot[fruit_init_idx]
        self.game_board[fruit_init_x][fruit_init_y] = Fruit_Spot(fruit_init_x, fruit_init_y)
        self.empty_spot.pop(fruit_init_idx)


class Snake:

    def __init__(self,
                 head, 
                 end = None):

        self.head = head
        self.end = end
        self.iter_temp = self.head

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_temp:
            ret = self.iter_temp
            self.iter_temp = self.iter_temp.next
            return ret
            
        else:
            raise StopIteration



if __name__ == "__main__":
    # board = board(2, 2)
    test_sanke1 = Snake_Node(1,1)
    test_sanke2 = Snake_Node(1,2)
    test_sanke3 = Snake_Node(1,3)

    test_sanke1.connect(test_sanke2)
    test_sanke2.connect(test_sanke3)

    Snake = Snake(test_sanke1, test_sanke3)

    for node in Snake:
        print(node)

