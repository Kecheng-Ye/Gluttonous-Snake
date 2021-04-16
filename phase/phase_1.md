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