from random import choice

from .block import *
from .utils import *

class board:
    """
    The class to main the game board

    Args:
         width(int):                            the width of the board
         height(int):                           the height of the board
         snake_init_coordinates(list[int]):     optional arguments to manually initialize the sanke coordinate for debug use
         fruit_init_coordinates(list[int]):     optional arguments to manually initialize the fruit coordinate for debug use

    Class member:
         game_board([[empty_spot]]):             A two-dimensional array of basic `Base_Block` object, which is the true board of our game
                                                 so each element of our game_board will either be an `Empty_Spot` or `Snake_Node` or `Fruit_Node`
         
         Snake(Snake):                           The whole Snake object that present the snake in the game

         empty_spot(set[tuple[int]]):            The set contains the all of board's current empty spot coordinates, this is particularly convenient
                                                 when we want to generate a random choice for our fruit coordinate
        
         Fruit_lst(set[tuple[int]]):             The set that contains all the fruit coordinates on the current board

         boundary_checker(Bounds_checker):       The bounds checker for checking invalid index for the game board   
    """
    def __init__(self, width, height, snake_init_coordinates = None, fruit_init_coordinates = None):
        self.width = width
        self.height = height
        self.game_board = []
        self.Snake = None
        self.empty_spot = set()
        self.Fruit_lst = set()
        self.boundary_checker = Bounds_checker(self.width, self.height)

        # initialize the game board array and empty spot
        # # implement your code below
        # pass 
        for i in range(self.height):
            self.game_board.append([])
            for j in range(self.width):
                # initially every spot will be a empty spot
                self.game_board[i].append(Empty_Spot(i, j))
                # so every coodinate will be in the `empty_spot` set
                self.empty_spot.add((i, j))

        self.game_initialize(snake_init_coordinates, fruit_init_coordinates)
    

    def restart(self):
        """
        Reintialization of the board

        Useful when restarting the whole game
        """
        self.__init__(self.width, self.height)


    def Snake_initialize(self, snake_init_coordinates=None):
        """
        Initialization function for the Snake

        Args: 
             snake_init_coordinates(tuple[int]):    optional arguments to manually initialize the sanke coordinate instead of random choice from the `empty_spot`   
        """
        # # implement your code below
        # pass
        # if there has no given snake initialization coordinates
        if not snake_init_coordinates:
            # we will get the coordinate from a random choice from `empty_spot`
            snake_init_h, snake_init_w = choice(tuple(self.empty_spot))
        else:
            # otherwise we will strickly initialize the snake with given coordinates
            snake_init_h, snake_init_w = snake_init_coordinates

        # initialized the snake object 
        Snake_head = Snake_Node(snake_init_h, snake_init_w)
        self.Snake = Snake(head = Snake_head, end = None)
        # remeber to maintain the validity of the `empty_spot`
        self.empty_spot.remove((snake_init_h, snake_init_w))


    def Fruit_random_generate(self, fruit_init_coordinates=None):
        """
        Random generate a fruit based on current board state

        Args: 
             fruit_init_coordinates(tuple[int]):    optional arguments to manually initialize the fruit coordinate instead of random choice from the `empty_spot`   
        """
        # # implement your code below
        # pass
        # check function `Snake_initialize` for comments
        if not fruit_init_coordinates:
            fruit_init_h, fruit_init_w = choice(tuple(self.empty_spot))
        else:
            fruit_init_h, fruit_init_w = fruit_init_coordinates

        self.Fruit_lst.add((fruit_init_h, fruit_init_w))
        self.empty_spot.remove((fruit_init_h, fruit_init_w))


    def game_initialize(self, snake_init_coordinates, fruit_init_coordinates):
        """
        Initialization function for the whole game board

        Args: 
             snake_init_coordinates(tuple[int]):    optional arguments to manually initialize the sanke coordinate instead of random choice from the `empty_spot`
             fruit_init_coordinates(tuple[int]):    optional arguments to manually initialize the fruit coordinate instead of random choice from the `empty_spot`
        """

        self.Snake_initialize(snake_init_coordinates)
        self.Fruit_random_generate(fruit_init_coordinates)
        # because the previous two function only changes the content of `Snake` or `Fruit_lst` or `empty_spot`
        # we still have to apply the changes to the actual board board
        self.Update_board()


    def Update_board(self):
        """
        The function for updating all the changes on `Snake` or `Fruit_lst` to the `game_board`
        """
        # initialize a new board
        new_board = [[Empty_Spot(i, j) for j in range(self.width)] for i in range(self.width)]

        # # implement your code below
        # pass
        # iterate the `Snake` object 
        for snake_node in self.Snake:
            # get every snake node coordinate
            h, w = snake_node.get_coordinates()
            # check if one coordiante is valid or not
            self.boundary_checker.Check_coordinate(h, w)
            # finally add the valid snake node to the board
            new_board[h][w] = snake_node
        
        # same logic as the previous loop
        for fruit in self.Fruit_lst:
            h, w = fruit
            self.boundary_checker.Check_coordinate(h, w)
            new_board[h][w] = Fruit_Spot(h, w)
        
        ## stop here
        # assign the new board to the `game_board`
        self.game_board = new_board


    def Snake_grow(self, Direction : str):
        """
        The function to make the snake grow from a certain direction operation

        Args:
             Direction(str):        The current direction operation("left", "right", "up", "down")
        """
        self.Snake.grow(Direction, self.empty_spot, self.boundary_checker)


    def Snake_move(self, Direction : str):
        """
        The function to make the snake move from a certain direction operation 

        Args:
             Direction(str):        The current direction operation("left", "right", "up", "down")
        """
        # if the snake has eaten any fruit during this single move
        if self.Snake.move(Direction, self.empty_spot, self.Fruit_lst, self.boundary_checker):
            # generate a new fruit
            self.Fruit_random_generate()


    def Snake_init_from_lst(self, node_list : list):
        """
        The function to directly initialize a snake based on the input node list

        Args:
             node_list(list[list[int]]):       A two dimensional array, each element of the outter array is the coordinate of a snake node (from head to tail)

        Ex: 
             Input->    NodeList = [[0, 0], [0, 1], [0, 2]]
             Output->   Initialize a new Snake object with its head as [0, 0] sequentially connect to node [0, 1], [0, 2]  
        """
        self.Snake.init_from_lst(node_list, self.empty_spot)


class Snake:
    """
    The Snake class

    Essentially one Snake is a linkedlist of several `Snake_Node`
    The specific Snake move or Snake grow function will be implemented in this class

    Args: 
         head(Snake_Node):          The head node of the snake
         end(Snake_Node):           The tail node of the snake
         length(int):               The length of the snake      
    """
    def __init__(self,
                 head, 
                 end = None,
                 length = 1):
        # # implement your code below
        # pass
        self.head = head
        self.end = end if end else self.head
        self.iter_temp = self.head
        self.length = length


    def __iter__(self):
        """
        To make the whole Snake object iterable

        By iterable, it means that we can 
        ```
        for i in Snake:
            pass
        ```

        One object can be iterable if it has implmented '__next__' function
        """
        return self


    def __next__(self):
        """
        The function to access the next node of `iter_temp` node
        if it reach end, then the iteration will end
        """
        # # implement your code below
        # pass        
        # as long as the `iter_temp` is not None
        if self.iter_temp:
            # there is a valid next element
            ret = self.iter_temp
            # update the `iter_temp` to next node
            self.iter_temp = self.iter_temp.next
            return ret

        # if the `iter_temp` reachs end
        else:
            # reset the `iter_temp` to enable next iteration
            self.iter_temp = self.head
            raise StopIteration


    def __len__(self):
        """
        Enable the ```len()``` function for the Snake object
        """
        # # implement your code below
        # pass
        return self.length


    def __str__(self):
        # # implement your code below
        # pass
        result = "This is a Snake object of length {}\nWith its children in the following order:\n\n".format(self.length)
        for node in self:
            result += node.__str__()
            result += "\n"
        
        return result


    def __repr__(self):
        return self.__str__()


    def grow(self,
             direction : str,
             empty_spot : set = None,
             Bounds_checker : Bounds_checker = None):
        """
        The core function for Snake to grow one unit with certain direction key

        Args: 
             direction(str):                    The moving direction of the Snake
             empty_spot(set[tuple[int]]):       The empty spot of current game board
             Bounds_checker(Bounds_checker):    The bounds checker for checking any invalid index


        After a Snake eat a fruit, one more `Snake_Node` will add directly to the tail node of the Snake
        But there is four way for one node to connect with another node
        We split all grow scenarios into two

        1. The Snake has length longer than 1:

        So the information of the previous node of tail node should also be included

        Ex: 
        Initially the board is

          0 1 2 3 4 
         -----------
       0 |  X S    |
       1 |  S S    |
       2 |         |
       3 |         |
       4 |         |
         -----------

        when the head node `[0, 2]` eat the fruit `[0, 1]`, the board will change to 

          0 1 2 3 4 
         -----------
       0 |  S S    |
       1 |    S    |
       2 |         |
       3 |         |
       4 |         |
         -----------

        Then the new added node will directly add to the negative projection between tail node `[1, 2]` and the prev of tail node `[0, 2]`
        the distance of this two node is `[1, 0]`, so the new tail node's coodinate will be `[1, 2] + [1 , 0] = [2, 2]`, the result board will be 

          0 1 2 3 4 
         -----------
       0 |  S S    |
       1 |    S    |
       2 |    S    |
       3 |         |
       4 |         |
         -----------

        2. The Snake has length = 1:

        If the snake has only one node, the newly-added node will depend on the moving direction of the snake

        Ex: 
        Initially the board is

          0 1 2 3 4 
         -----------
       0 |         |
       1 |  S X    |
       2 |         |
       3 |         |
       4 |         |
         -----------

        when the head node `[1, 1]` eat the fruit `[1, 2]` with a `right` operation, the new node will
        only add to the opposite side of the operation which is `left`

         0 1 2 3 4 
         -----------
       0 |         |
       1 |  S S    |
       2 |         |
       3 |         |
       4 |         |
         -----------
        """
        # # implement your code below
        # pass
        # The length > 1 condition
        if self.head != self.end:
            end = self.end
            end_prev = self.end.prev

            end_h, end_w = end.get_coordinates()
            end_prev_h, end_prev_w = end_prev.get_coordinates()

            assert abs(end_h - end_prev_h) + abs(end_w - end_prev_w) == 1, \
                  (f'Malformed Snake: [{end_prev_h}, {end_prev_w}] connect to [{end_h}, {end_w}].')

            # calculate the coordinate difference between two node
            coordinate_diff = [end_h - end_prev_h, end_w - end_prev_w]
            # get the result new node coordinates
            grow_node_h, grow_node_w = end_h + coordinate_diff[0], end_w + coordinate_diff[1]
            # check if the new node's coordinate validity
            if not Bounds_checker.Check_coordinate(grow_node_h, grow_node_w, raise_warning=False):
                # meet edge case
                grow_node_h, grow_node_w = self.random_grow([end_h, end_w], coordinate_diff, Bounds_checker)

            new_tail = Snake_Node(grow_node_h, grow_node_w)
        
        # if node length == 1
        else:
            head_h, head_w = self.head.get_coordinates()
            if direction in Direction_dict:
                h_movement, w_movement = Direction_dict[direction]
                new_tail = Snake_Node(head_h - h_movement, head_w - w_movement)
            else:
                raise NotImplementedError

        # connect the new node to the tail of the snake
        self.end.connect(new_tail)
        self.end = new_tail
        self.length += 1

        # update the `empty_spot`
        if empty_spot:
            empty_spot.remove(self.end.get_coordinates())


    def random_grow(self, coordinate : list, coordinate_diff : list, boundary_checker : Bounds_checker):
        """
        Function try to resolve such edge case

        Args:
             coordinate(list[int]):             The current end node coordinate
             coordinate_diff(list[int]):        The coordinate difference between the end node and end prev node
             boundary_checker(Bounds_checker):  The boundary checker

        Ex:
        Initially the board is like the following with Snake head `[1, 2]` and the fruit node `[0, 2]`

          0 1 2 3 4 
         -----------
       0 |    X    |
       1 |    S    |
       2 |    S    |
       3 |    S    |
       4 |  S S    |
         -----------

        After the snake move upwards, the Snake eats the fruit, it suppose to grow, while according to the afroementioned logic the 
        new added snake node will be `[5, 2]` which is out of bound

          0 1 2 3 4 
         -----------
       0 |    S    |
       1 |    S    |
       2 |    S    |
       3 |    S    |
       4 |    S    |
         -----------
              S

        So our snake will have two choices for this grow

            0 1 2 3 4                        0 1 2 3 4                      
          -----------                      -----------                     
        0 |    S    |                    0 |    S    |
        1 |    S    |                    1 |    S    |
        2 |    S    |                    2 |    S    |
        3 |    S    |                    3 |    S    |
        4 |  S S    |                    4 |    S S  |
          -----------                      -----------

       Then the function will return one of the possible valid choice for this random grow
                                             
        """
        # determine which coordinate should be changed
        for idx, val in enumerate(coordinate_diff):
            if val == 0:
                add_idx = idx

        result = []

        # random choice of that 
        for i in [-1, 1]:
            temp = coordinate.copy()
            temp[add_idx] += i
            # check if the potential choice is invalid or not
            if boundary_checker.Check_coordinate(*temp, raise_warning=False):
                result.append(temp)
        
        return choice(result)

    def move(self, 
             direction : str,
             empty_spot : set = None,
             Fruit_lst : set = None,
             Bounds_checker : Bounds_checker = None):
        """
        The function that let snake move one unit by certain direction

        Conceptually, a snake's move is really just the head move forward a unit and all the node got to its previous node's position
        Since our Snake is essentially a linkedlist, this move implmentation will be very first

        Args:
             direction(str):                    The current end node coordinate
             empty_spot(set(list[int])):        The empty spot of current game board
             Fruit_lst(set(list[int])):         The fruit list of current game board
             boundary_checker(Bounds_checker):  The boundary checker

        Return:
               Eat_fruit(bool):                 Whether this move action make the snake eat any fruit
        """
        
        assert direction in ['left', 'right', 'up', 'down']

        Eat_fruit = False
        # # implement your code below
        # pass
        end_h, end_w = self.end.get_coordinates()
        
        # reversely traverse the snake linkedlist
        # because if we firstly change the head node then every rest of the node will be same as the head one
        node = self.end
        while node != self.head:
            node.set(*node.prev.get_coordinates())
            node = node.prev

        # do the actual moving for the head node
        if direction in Direction_dict:
            h_movement, w_movement = Direction_dict[direction]
            head_h, head_w = self.head.get_coordinates()

            # check if the head node coordinate is valid or not
            if Bounds_checker:
                # if out of bound, then we know the snake hits on the boundary
                Bounds_checker.Check_coordinate(head_h + h_movement, head_w + w_movement, error_message = "Snake crash on boundary")

            self.head.set(head_h + h_movement, head_w + w_movement)
        else:
            raise NotImplementedError

        # update the `empty_spot`
        if empty_spot:
            
            # first add back the end node 
            empty_spot.add((end_h, end_w))

            # check if the head node of the snake hit any fruit
            if Fruit_lst and self.head.get_coordinates() in Fruit_lst:
                Fruit_lst.remove(self.head.get_coordinates())
                self.grow(direction, empty_spot, Bounds_checker)
                Eat_fruit = True
            else:
                # if our head node hits some point which is not in the empty list
                # then we know the snake have already eat itself
                if self.head.get_coordinates() not in empty_spot:
                    raise GameBoardIndexError("Snake eat itself")
                
                # remove the head node position from the `empty_spot`
                empty_spot.remove(self.head.get_coordinates())
        
        return Eat_fruit

    def init_from_lst(self, node_list, empty_spot=None):
        """
        The function to directly initialize a snake based on the input node list for debug use

        Args:
             node_list(list[list[int]]):       A two dimensional array, each element of the outter array is the coordinate of a snake node (from head to tail)

        Ex: 
             Input->    NodeList = [[0, 0], [0, 1], [0, 2]]
             Output->   Initialize a new Snake object with its head as [0, 0] sequentially connect to node [0, 1], [0, 2]  
        """
        # # implement your code below
        # pass
        self.head = None
        self.end = None
        self.length = len(node_list)
        self.iter_temp = None

        prev = None
        for i, item in enumerate(node_list):
            temp_node = Snake_Node(*item)
            if i == 0:
                self.head = temp_node
            else:
                prev.connect(temp_node)

            if empty_spot and temp_node.get_coordinates() in empty_spot:
                empty_spot.remove(temp_node.get_coordinates())
            prev = temp_node
        
        self.end = prev
        self.iter_temp = self.head
        
    
         

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
