import turtle
# Remove unused imports

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
        turtle.clearscreen()
        turtle.speed(0)
        turtle.penup()
        turtle.setpos(self.starting_pos)
        turtle.setheading(90)
        turtle.pendown()
        turtle.color(self.color)

        stack = []
        for command in self.commands:
            if command == "F":
                turtle.forward(self.step)
            elif command == "+":
                turtle.right(self.angle)
            elif command == "-":
                turtle.left(self.angle)
            elif command == '[':
                pos = turtle.position()
                heading = turtle.heading()
                stack.append((pos, heading))
            elif command == ']':
                pos, heading = stack.pop()
                turtle.penup()
                turtle.setpos(pos)
                turtle.setheading(heading)
                turtle.pendown()

        turtle.exitonclick()

    def plot(self):
        self.iterate()
        self.draw()


ls1 = LSystem(
    axiom="F",
    rules={"F": "F[+F]F[-F][F]"},
    angle=22,
    step = 7,
    n = 4,
)
ls1.plot()

# ls1 = LSystem(axiom="-L",
# rules={"L": "LF+RFR+FL-F-LFLFL-FRFR+", "R": "-LFLF+RFRFR+F+RF-LFL-FR"},
# angle=25.7, step=10,
# )
# ls1.plot()