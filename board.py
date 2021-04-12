from block import *
from random import choice, randrange
import enum

class Direction(enum.Enum):
   left     = 1
   up       = 2
   right    = 3
   down     = 4

class board:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.game_board = []
        self.empty_spot = set()
        self.Snake = None
        self.Fruit_lst = []

        for i in range(self.height):
            self.game_board.append([])
            for j in range(self.width):
                self.game_board[i].append(Empty_Spot(i, j))
                self.empty_spot.add((i, j))

        self.game_initialize()
    

    def Snake_initialize(self):
        # add snake
        # snake_init_h, snake_init_y = choice(tuple(self.empty_spot))
        snake_init_h, snake_init_w = (0, 1)
        Snake_head = Snake_Node(snake_init_h, snake_init_w)
        self.empty_spot.remove((snake_init_h, snake_init_w))
        self.Snake = Snake(head = Snake_head, end = None)


    def Fruit_intialize(self):
        # add fruit
        fruit_init_h, fruit_init_w = choice(tuple(self.empty_spot))
        self.Fruit_lst.append((fruit_init_h, fruit_init_w))
        self.empty_spot.remove((fruit_init_h, fruit_init_w))


    def game_initialize(self):
        self.Snake_initialize()
        self.Fruit_intialize()
        self.Update_board()


    def Update_board(self):
        new_board = [[Empty_Spot(i, j) for j in range(self.width)] for i in range(self.width)]

        for snake_node in self.Snake:
            h, w = snake_node.get_coordinates()
            new_board[h][w] = snake_node
        
        for fruit in self.Fruit_lst:
            h, w = fruit
            new_board[h][w] = Fruit_Spot(h, w)
        
        self.game_board = new_board


    def Snake_grow(self,
                   Direction : Direction):
        
        self.Snake.grow(Direction, self.empty_spot)
class Snake:

    def __init__(self,
                 head, 
                 end = None,
                 length = 1):

        self.head = head
        self.end = end if end else self.head
        self.iter_temp = self.head
        self.length = length

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_temp:
            ret = self.iter_temp
            self.iter_temp = self.iter_temp.next
            return ret

        else:
            self.iter_temp = self.head
            raise StopIteration

    def __len__(self):
        return self.length

    def grow(self,
             direction: Direction,
             empty_spot : set = None):

        if self.head != self.end:
            end = self.end
            end_prev = self.end.prev

            end_h, end_w = end.get_coordinates()
            end_prev_h, end_prev_w = end_prev.get_coordinates()

            assert abs(end_h - end_prev_h) + abs(end_w - end_prev_w) == 1, \
                  (f'Malformed Snake: [{end_prev_h}, {end_prev_w}] connect to [{end_h}, {end_w}].')

            if end_h == end_prev_h:
                new_tail = Snake_Node(end_h, end_w + (end_w - end_prev_w))
            else:
                new_tail = Snake_Node(end_h + (end_h - end_prev_h), end_w)

        else:
            head_h, head_w = self.head.get_coordinates()
            if direction == Direction.left:
                new_tail = Snake_Node(head_h, head_w + 1)
            elif direction == Direction.right:
                new_tail = Snake_Node(head_h, head_w - 1)
            elif direction == Direction.up:
                new_tail = Snake_Node(head_h + 1, head_w)
            elif direction == Direction.up:
                new_tail = Snake_Node(head_h - 1, head_w)
            else:
                raise NotImplementedError
        
        self.end.connect(new_tail)
        self.end = new_tail
        self.length += 1
        if empty_spot:
            empty_spot.remove(self.end.get_coordinates())

    def __str__(self):
        result = ""
        for node in self:
            result += node.__str__()
            result += "\n"
        
        return result

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    # board = board(2, 2)
    # test_sanke1 = Snake_Node(1,1)
    # test_sanke2 = Snake_Node(1,2)
    # test_sanke3 = Snake_Node(1,3)

    # test_sanke1.connect(test_sanke2)
    # test_sanke2.connect(test_sanke3)

    # Snake = Snake(test_sanke1, test_sanke3)

    test_sanke1 = Snake_Node(5, 5)
    Snake = Snake(test_sanke1)

    Snake.grow(Direction.right)
    # print(Snake)

    # print("************")

    # Snake.grow(Direction.right)
    # print(Snake)
    # for node in Snake:
    #     print(node)

