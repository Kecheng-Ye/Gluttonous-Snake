from block import *
from random import choice

Direction_dict = dict(left     = (0, -1),
                      up       = (-1, 0),
                      right    = (0, 1),
                      down     = (1, 0))

class GameEnd(Exception):
    pass

class GameBoardIndexError(GameEnd):
    pass

class board:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.game_board = []
        self.empty_spot = set()
        self.Snake = None
        self.Fruit_lst = set()

        for i in range(self.height):
            self.game_board.append([])
            for j in range(self.width):
                self.game_board[i].append(Empty_Spot(i, j))
                self.empty_spot.add((i, j))

        self.game_initialize()
    

    def Snake_initialize(self):
        # add snake
        # snake_init_h, snake_init_w = choice(tuple(self.empty_spot))
        snake_init_h, snake_init_w = 0, 0
        Snake_head = Snake_Node(snake_init_h, snake_init_w)
        self.empty_spot.remove((snake_init_h, snake_init_w))
        self.Snake = Snake(head = Snake_head, end = None)


    def Fruit_random_generate(self):
        # add fruit
        fruit_init_h, fruit_init_w = choice(tuple(self.empty_spot))
        self.Fruit_lst.add((fruit_init_h, fruit_init_w))
        self.empty_spot.remove((fruit_init_h, fruit_init_w))


    def game_initialize(self):
        self.Snake_initialize()
        self.Fruit_random_generate()
        self.Update_board()


    def Update_board(self):
        new_board = [[Empty_Spot(i, j) for j in range(self.width)] for i in range(self.width)]

        for snake_node in self.Snake:
            h, w = snake_node.get_coordinates()
            self.Check_coordinate(h, w)
            new_board[h][w] = snake_node
        
        for fruit in self.Fruit_lst:
            h, w = fruit
            self.Check_coordinate(h, w)
            new_board[h][w] = Fruit_Spot(h, w)
        
        self.game_board = new_board


    def Snake_grow(self,
                   Direction : str):
        self.Snake.grow(Direction, self.empty_spot)


    def Snake_move(self, Direction : str):
        if self.Snake.move(Direction, self.empty_spot, self.Fruit_lst):
            self.Fruit_random_generate()


    def Check_coordinate(self, h, w):
        if h >= 0 and h < self.height:
            if w >= 0 and w < self.width:
                return
        
        raise GameBoardIndexError("index [{} {}] is invalid in Board ({}x{})".format(h, w, self.width, self.height))


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


    def __str__(self):
        result = ""
        for node in self:
            result += node.__str__()
            result += "\n"
        
        return result


    def __repr__(self):
        return self.__str__()


    def grow(self,
             direction : str,
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
            if direction in Direction_dict:
                h_movement, w_movement = Direction_dict[direction]
                new_tail = Snake_Node(head_h - h_movement, head_w - w_movement)
            else:
                raise NotImplementedError

        self.end.connect(new_tail)
        self.end = new_tail
        self.length += 1
        if empty_spot:
            empty_spot.remove(self.end.get_coordinates())

    def move(self, 
             direction : str,
             empty_spot : set = None,
             Fruit_lst : set = None):
        
        Eat_fruit = False
        end_h, end_w = self.end.get_coordinates()
        
        node = self.end
        while node != self.head:
            node.set(*node.prev.get_coordinates())
            node = node.prev

        if direction in Direction_dict:
            h_movement, w_movement = Direction_dict[direction]
            head_h, head_w = self.head.get_coordinates()
            self.head.set(head_h + h_movement, head_w + w_movement)

        else:
            raise NotImplementedError

        if empty_spot:
            empty_spot.add((end_h, end_w))

            if Fruit_lst and self.head.get_coordinates() in Fruit_lst:
                Fruit_lst.remove(self.head.get_coordinates())
                self.grow(direction, empty_spot)
                Eat_fruit = True

            else:
                empty_spot.remove(self.head.get_coordinates())
        
        return Eat_fruit


if __name__ == "__main__":
    # board = board(2, 2)
    # test_sanke1 = Snake_Node(1,1)
    # test_sanke2 = Snake_Node(1,2)
    # test_sanke3 = Snake_Node(1,3)

    # test_sanke1.connect(test_sanke2)
    # test_sanke2.connect(test_sanke3)

    # Snake = Snake(test_sanke1, test_sanke3)

    # test_sanke1 = Snake_Node(5, 5)
    # Snake = Snake(test_sanke1)

    # Snake.grow(Direction.right)
    # print(Snake)

    # print("************")

    # Snake.grow(Direction.right)
    # print(Snake)
    # for node in Snake:
    #     print(node)
    pass
