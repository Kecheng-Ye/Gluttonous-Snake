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