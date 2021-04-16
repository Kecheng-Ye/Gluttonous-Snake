### 阶段七任务
* 实现`Game_component/board.py`的`Snake`类中`grow`这个函数
  * 函数实现了`Snake`在吃掉`Fruit`之后生长一个单位的过程
  * 注意阅读函数中的注释，实现另外的一些必要函数
  * 注意考虑一些边界情况，详情可以参考`phase_7`中的一些例子
* 运行阶段七任务
```{bash}
python main.py --phase 7

# expect output
Before grow
*******************************
-----------
|    X    |
|         |
|         |
|         |
|    S    |
-----------
Now, Snake's length is 1


after grow once
*******************************
-----------
|    X    |
|         |
|         |
|         |
|  S S    |
-----------
Now, Snake's length is 2


after grow twice
*******************************
-----------
|    X    |
|         |
|         |
|         |
|S S S    |
-----------
Now, Snake's length is 3


after grow three times
*******************************
-----------
|    X    |
|         |
|         |
|S        |
|S S S    |
-----------
Now, Snake's length is 4
```