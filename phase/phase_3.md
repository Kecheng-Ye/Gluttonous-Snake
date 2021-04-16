### 阶段三任务
* 阅读`Game_component/board.py`代码中`Snake`这个类的相关注释
* 实现`Snake`类，其本质是一个**doublely-linkedlist**
  * 其中，自己实现一个python的迭代器，[参考网址]([Game_component/board.py](https://www.runoob.com/python3/python3-iterator-generator.html))
  * 暂时不需要实现`Snake`中`grow`,`random_grow`以及`move`这三个函数
* 运行阶段三任务
```{bash}
python main.py --phase 3

# expect output
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