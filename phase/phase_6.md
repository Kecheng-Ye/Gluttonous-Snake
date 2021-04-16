### 阶段六任务
* 实现`Game_component/board.py`中`init_from_lst`这个函数
  * 注意阅读函数中的注释, 了解此函数需求
  * 这个函数是为了后续debug的便利
* 运行阶段六任务
```{bash}
python main.py --phase 6

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