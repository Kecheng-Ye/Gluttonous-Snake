# Glutonous Snake

### Python 环境设置
```{bash}
pip install -r requirements.txt
```

### 整个项目的流程
![](resources/flow_chart.png)


### 阶段一任务
* 阅读`Game_component/block.py`代码
* 在现有的`Base_Block`作为基类，分别implement`Empty_Spot`以及`Fruit_Spot` class(暂时不需要implement两个类中`render_terminal`函数)
* 运行阶段一任务
```{bash}
python main.py --phase 1

# expect output
This is a empty spot with coordinate [0, 0]
This is a fruit spot with coordinate [0, 0]
```



### 阶段二任务
* 依旧在`Game_component/block.py`中实现`Snake_Node` class(暂时不需要implement类中`render_terminal`函数)
* 运行阶段二任务
```{bash}
python main.py --phase 2

# expect output
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


### 阶段四任务
* 阅读`Game_component/board.py`代码中`board`这个类的相关注释
* 根据注释的提示实现`board`这个类的`__init__`函数
  * 注意`__init__`中附带的函数需要一并实现
* 运行阶段四任务
  * 注意阶段四有两个部分
    * 第一个部分的输出应该与目标输出完全一致
    * 第二部分的输出可以与目标输出不一致，只要两次生成的board是有随机性的即可
```{bash}
python main.py --phase 4

# expect output
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

### 阶段五任务
* 阅读`Game_component/render.py`代码
* 实现`Render_engine`这个类中`render_terminal`这个函数
  * 注意阅读函数中的注释，实现另外的一些必要函数
* 运行阶段五任务
```{bash}
python main.py --phase 5

# expect output
-----------
|X        |
|  S      |
|         |
|         |
|         |
-----------
```

### 阶段六任务
* 实现`Game_component/board.py`中`init_from_lst`这个函数
  * 注意阅读函数中的注释, 了解此函数需求
  * 这个函数是为了后续debug的便利
* 运行阶段六任务
```{bash}
python main.py --phase 5

# expect output
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