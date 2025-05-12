from turtle import RawTurtle

class State:
    def __init__(self, x=0, y=0, angle=0):
        self.x = x
        self.y = y
        self.angle = angle
    
    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.angle:.2f})"
    
    def __repr__(self):
        return f"State({self.x:.2f}, {self.y:.2f}, {self.angle:.2f})"
    
    def set_state(self, t):
        self.x = float(t[0])
        self.y = float(t[1])
        self.angle = float(t[2])
def set_state(self, t):
    if isinstance(t, RawTurtle):
        t = (t.xcor(), t.ycor(), t.heading())
    self.x = float(t[0])
    self.y = float(t[1])
    self.angle = float(t[2])


class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0