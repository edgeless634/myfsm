

class FSM:
    def __init__(self):
        self.__slots__ = ("status_now", "statuses", "status_moves")
        self.status_now = "init"
        self.statuses = ["init", ]
        self.status_moves = {}
    
    def _is_status_exist(self, status):
        return self.statuses.index(status)

    def add_status(self,status_add):
        self.statuses.append(status_add)

    def teleport_to(self, status_to):
        if not self._is_status_exist(status_to):
            raise TypeError(f"Status {status_to} does not exist.")
        self.status_now = status_to
    
    def add_moves(self, status_from, status_to, func):
        if not self.status_moves.get(status_from):
            self.status_moves[status_from] = {}
        self.status_moves[status_from][status_to] = func

    def to(self, status_to, *args):
        if not self._is_status_exist(status_to):
            raise TypeError(f"Status {status_to} does not exist.")
        self.status_moves[self.status_now][status_to](*args)
        self.status_now = status_to

    def graph(self):
        import graphviz
        dot = graphviz.Digraph(comment='The Round Table')
        for status in self.statuses:
            dot.node(status, status)
        for status_from in self.status_moves:
            for status_to in self.status_moves[status_from]:
                dot.edge(status_from, status_to)
        return dot.source


if __name__ == "__main__":
    fsm = FSM()

    fsm.add_status("status 1")
    fsm.add_status("status 2")

    fsm.add_moves("status 1", "status 2", lambda:print("from one to two"))
    fsm.add_moves("status 2", "status 1", lambda:print("from two to one"))

    fsm.teleport_to("status 1")
    fsm.to("status 2")
    fsm.to("status 1")

    print(fsm.graph())