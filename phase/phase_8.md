### 阶段八任务
* 实现`Game_component/board.py`的`Snake`类中`move`这个函数
  * 注意阅读`Game_component/utils.py`,里面有些有用的工具可以在这个函数使用
  * 仔细阅读函数注释，实现所有函数的功能
  * 阶段八有多个问题，每个问题由`xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`隔开
  * `problem_2`的`Fruit`位置可以与下面输出不一致，但是`Snake`的形状**必须一致**
* 运行阶段八任务
```{bash}
python main.py --phase 8

# expect output
Before move
*******************************
-----------
|    X    |
|         |
|         |
|         |
|    S    |
-----------


after move right
*******************************
-----------
|    X    |
|         |
|         |
|         |
|      S  |
-----------


after move up
*******************************
-----------
|    X    |
|         |
|         |
|      S  |
|         |
-----------


after move right
*******************************
-----------
|    X    |
|         |
|         |
|        S|
|         |
-----------
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


Before move
*******************************
-----------
|      S S|
|        S|
|        S|
|  S X   S|
|  S S S S|
-----------


After move right
*******************************
-----------
|      S S|
|    X   S|
|        S|
|  S S   S|
|  S S S S|
-----------
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


Before move
*******************************
-----------
|         |
|    X    |
|         |
|      S S|
|         |
-----------


After move right
*******************************
Snake crash because Snake crash on boundary
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


Before move
*******************************
-----------
|      S S|
|    X   S|
|        S|
|  S S S S|
|  S S S S|
-----------


After move right
*******************************
Snake crash because Snake eat itself
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```