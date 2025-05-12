import turtle
import random

class LSystem:
    """
    Represents an L-system with its axiom, rules, rewriting, and drawing methods.
    """
    def __init__(self, axiom, rules, angle, step, n=3, starting_pos=(-200, 0), starting_angle=0, color="blue"):
        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.step = step
        self.n = n
        self.starting_pos = starting_pos
        self.starting_angle = starting_angle
        self.color = color
        self.commands = None
        random.seed(42)  # Set the seed for reproducibility

    def iterate(self):
        """Iterates the L-system n times."""
        current_string = self.axiom
        for _ in range(self.n):
            new_string = ""
            for char in current_string:
                if char in self.rules:
                    rule = self.rules[char]
                    if isinstance(rule, list):
                        # Select a rule based on probabilities
                        probabilities = [r[0] for r in rule]
                        choices = [r[1] for r in rule]
                        new_string += random.choices(choices, probabilities)[0]
                    else:
                        new_string += rule
                else:
                    new_string += char
            current_string = new_string
        self.commands = current_string

    def draw(self):
        """Draws the L-system using the turtle module."""
        if self.commands is None:
            return

        turtle.clearscreen()
        turtle.speed(0)
        turtle.penup()
        turtle.setpos(self.starting_pos)
        turtle.setheading(self.starting_angle)
        turtle.pendown()
        turtle.color(self.color)

        stack = []
        for command in self.commands:
            if command == 'F':
                turtle.forward(self.step)
            elif command == '+':
                turtle.right(self.angle)
            elif command == '-':
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

        turtle.done()

    def plot(self):
        """Iterates and then draws the L-system."""
        self.iterate()
        self.draw()

# Example usage:
nd_ls_1 = LSystem(
    axiom="F",
    rules={"F": [(.33, "F[+F]F[-F]F"), (.33, "F[+F]F"), (.33, "F[-F]F")]},
    angle=25.7,
    step=10
)
nd_ls_1.plot()





