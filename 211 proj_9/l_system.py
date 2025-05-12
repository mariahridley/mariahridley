import turtle
import matplotlib.pyplot as plt
import numpy as np

class LSystem:
    """Represnets an L-system with its axiom, rules, rewriting, and drawing methods."""
    def __init__(self, axiom, rules, angle, step, n=3, starting_pos=(-200,0), starting_angle=0, color="blue"):
        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.step = step
        self.n = n
        self.starting_pos = starting_pos
        self.starting_angle = starting_angle
        self.color = color
        self.commands = None

    def iterate(self):
        """Iterates the L-system n times."""
        current_string = self.axiom
        for _ in range(self.n):
            new_string = ""
            for char in current_string:
                new_string += self.rules.get(char, char)
            current_string = new_string
        self.commands = current_string

    def draw(self):
        """Draws the L-system using turtle graphics."""
        t = turtle.Turtle()
        screen = turtle.Screen()
        t.reset()
        t.goto(self.starting_pos)
        t.setheading(self.starting_angle)
        t.setheading(90)

        t.speed(0)
        t.color(self.color)
        state = turtle.Turtle().stack()
        mstack = state.Stack()

        print(self.commands)
        for command in self.commands:
            if command == "F":
                turtle.forward(self.step)
            elif command == "+":
                turtle.right(self.angle)
            elif command == "-":
                turtle.left(self.angle)
            elif command == '[':
                branch_start_state = state.State()
                branch_start_state.set_state(t)
                mstack.push(branch_start_state)
            elif command == ']':
                my_s = mstack.pop()

                t.penup()
                t.goto(my_s.x, my_s.y)
                t.pendown()
                t.setheading(my_s.angle)
                
        screen.exitonclick()
    def plot(self):
        """Plots the L-system using matplotlib."""
        self.iterate()
        self.draw()
    




#  [10 pts] The LSystem class constructor
# • [15 pts] The iterate method
# • [15 pts] The iterate method for branching structures
# • [20 pts] The draw method
# • [20 pts] The plot method
# • [20 pts] Extra credit (optional) – nd_l_system.py, and ss.png

# ls1 = LSystem(
#     axiom="F",
#     rules={"F": "F[+F]F[-F][F]"},
#     angle=22,
#     step = 7,
#     n = 4,
# )
# ls1.plot()

ls1 = LSystem(
    axiom="-L",
    rules={"L": "LF+RFR+FL-F-LFLFL-FRFR+", 
                "R": "- LFLF+RFRFR+F+RF-LFL-FR"},

    angle=90,

    step=10,

    n=3,

    )

ls1.plot(n=3)

