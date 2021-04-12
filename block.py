from abc import ABC, abstractmethod

class Base_Block(ABC):

    def __init__(self, 
                 x : int, 
                 y : int):

        self.x = x
        self.y = y

    def __str__(self):
        return "This is a based object block with coordinate [{}, {}]".format(self.x, self.y)


    def __repr__(self):
        return self.__str__()


    def get_coordinates(self):
        return self.x, self.y


    def set(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def render_terminal(self):
        return NotImplementedError


class Empty_Spot(Base_Block):

    def __init__(self, 
                 x : int, 
                 y : int):

        super(Empty_Spot, self).__init__(x, y)

    def __str__(self):
        return "This is a empty spot with coordinate [{}, {}]".format(self.x, self.y)

    def render_terminal(self):
        return "*"

class Snake_Node(Base_Block):

    def __init__(self, 
                 x : int, 
                 y : int,
                 prev = None,
                 next = None):

        super(Snake_Node, self).__init__(x, y)
        self.prev = prev
        self.next = next

    def __str__(self):
        prev_x, prev_y, next_x, next_y = [None] * 4

        if self.prev:
            prev_x, prev_y = self.prev.get_coordinates() 
        
        if self.next:
            next_x, next_y = self.next.get_coordinates()


        result = "This is a snake node with coordinate [{}, {}]\n".format(self.x, self.y)
        result += "With its prev snake of [{}, {}]\n".format(prev_x, prev_y)
        result += "And its next snake of [{}, {}]".format(next_x, next_y)

        return result

    def connect(self, another_node):
        self.next = another_node
        another_node.prev = self
        pass

    def render_terminal(self):
        return "S"

class Fruit_Spot(Base_Block):

    def __init__(self, 
                 x : int, 
                 y : int):

        super(Fruit_Spot, self).__init__(x, y)

    def __str__(self):
        return "This is a fruit spot with coordinate [{}, {}]".format(self.x, self.y)

    def render_terminal(self):
        return "X"

if __name__ == "__main__":
    test_block = Snake_Node(1,1)
    test_sanke = Snake_Node(1,2)
    test_block.next = test_sanke
    print(test_block)






