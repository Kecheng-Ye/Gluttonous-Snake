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