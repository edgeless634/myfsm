# MyFSM

一个简单的状态机

## 功能

- 基本的状态机 功能
- 自动画图
  - 需要安装graphviz模块

## 演示代码

```python
from myfsm import FSM

fsm = FSM()

fsm.add_status("status 1")
fsm.add_status("status 2")

fsm.add_moves("status 1", "status 2", lambda:print("from one to two"))
fsm.add_moves("status 2", "status 1", lambda:print("from two to one"))

fsm.teleport_to("status 1")
fsm.to("status 2")
fsm.to("status 1")

print(fsm.graph())
```