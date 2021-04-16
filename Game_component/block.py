from abc import ABC, abstractmethod

class Base_Block(ABC):
    """
    Base class for each block of our game board.

    Note: This is a class with abstractmethod ``render_terminal``,
          cannot directly instantiate this class

    Args: 
          x(int): the height coordinate of this block 
          y(int): the width coordinate of this block
    """
    def __init__(self, 
                 x : int, 
                 y : int):

        self.x = x
        self.y = y


    def __str__(self):
        return "This is a based object block with coordinate [{}, {}]".format(self.x, self.y)


    def __repr__(self):
        """
        Once we call `print` function on this object, the terminal will print whatever this function returns
        """
        return self.__str__()


    def get_coordinates(self):
        """
        Return the x, y coordinate of this block
        """
        return self.x, self.y


    def set(self, x, y):
        self.x = x
        self.y = y


    @abstractmethod
    def render_terminal(self):
        """
        Abstract method for rendering this object in the terminal,
        should be implemented in the child class
        """
        raise NotImplementedError


class Empty_Spot(Base_Block):
    """
    Class of empty block(a block that is neither a part of snake nor a fruit) of our game board.

    Args: 
          x(int): the height coordinate of this block
          y(int): the width coordinate of this block
    """
    def __init__(self, 
                 x : int, 
                 y : int):

        # implement your code below
        pass



    def __str__(self):
        # implement your code below
        pass


    def render_terminal(self):
        """
        Specific render method for empty spot
        """
        # implement your code below
        pass


class Snake_Node(Base_Block):
    """
    Class of sanke block of our game board.

    Basically it is a doube-linked linkedlist node 

    Args: 
          x(int):            the height coordinate of this block
          y(int):            the width coordinate of this block
          prev(Snake_Node):  the previous node that link to this node
          next(Snake_Node):  the next node that link to this node
    """
    def __init__(self, 
                 x : int, 
                 y : int,
                 prev = None,
                 next = None):
        # implement your code below
        pass        


    def __str__(self):
        # implement your code below
        pass


    def connect(self, another_node):
        """
        Function to make another node connect to the tail of current node
        Useful when we want to grow the snake

        Args: 
              another_node(Snake_Node): the node that will be connected to the tail of this node
        """
        # implement your code below
        pass


    def render_terminal(self):
        """
        Specific render method for snake spot
        """
        # implement your code below
        pass

class Fruit_Spot(Base_Block):
    """
    Class of fruit block of our game board.

    Args: 
          x(int): the height coordinate of this block
          y(int): the width coordinate of this block
    """
    def __init__(self, 
                 x : int, 
                 y : int):
        # implement your code below
        pass


    def __str__(self):
        # implement your code below
        pass


    def render_terminal(self):
        """
        Specific render method for snake spot
        """
        # implement your code below
        pass

if __name__ == "__main__":
    test_block = Snake_Node(1,1)
    test_sanke = Snake_Node(1,2)
    print(test_block)






