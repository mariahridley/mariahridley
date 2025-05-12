import random
class LSystem:
    def __init__(self, axiom, rules, angle, step):
        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.step = step

    def generate(self, iterations):
        state = self.axiom
        for _ in range(iterations):
            new_state = ""
            for symbol in state:
                if symbol in self.rules:
                    choices = self.rules[symbol]
                    probabilities = [choice[0] for choice in choices]
                    chosen_rule = random.choices(choices, probabilities)[0]
                    new_state += chosen_rule[1]
                else:
                    new_state += symbol
            state = new_state
        return state

# Example usage
random.seed(42)
nd_ls_1 = LSystem(axiom="F",
rules={"F": [(.33, "F[+F]F[-F]F"), (.33, "F[+F]F"), (.33, "F[-F]F")]},
angle=25.7, 
step=10,
iterations = 2,
)
print(nd_ls_1.generate(4))
nd_ls_1.plot()

# F[-F]F[+F[+F]F]F[+F]F[-F]F[-F[+F]F[-F]F]F[+F]F[-F[+F]F[-F]F[-F[+F]F]F[-F]F]F[+F]F[-F[+F]F[-F]F]F[-F]F[+F[+F]F[+F[+F]F[-F]F]F[+F]F[-F]F[-F[+F]F[-F]F[+F[+F]F]F[-F]F[-F[+F]F]F[+F]F[-F]F]F[+F]F[-F[-F]F]F[+F]F]F[-F]F[+F[-F]F]F[+F]F[-F]F[-F[-F]F[+F[-F]F]F[+F]F[-F[+F]F[-F]F]F[+F]F]F[+F]F[-F]F[+F[+F]F]F[+F]F[-F[-F]F]F[-F]F[-F[+F]F[-F]F[-F[+F]F]F[+F]F[-F]F[+F[-F]F[+F[-F]F]F[+F]F[-F]F]F[+F]F[-F[+F]F]F[+F]F[-F]F[-F[-F]F[-F[+F]F]F[-F]F]F[+F]F[+F[+F]F[-F]F]F[+F]F[-F]F]F[+F]F[-F]F[-F[-F]F]F[-F]F[+F[-F]F[+F[+F]F[-F]F]F[+F]F[-F]F]F[-F]F[+F[-F]F]F[+F]F[-F]F[+F[+F]F[-F[+F]F[-F]F]F[-F]F[+F[-F]F[+F[+F]F[-F]F]F[+F]F]F[+F]F[-F[+F]F[-F]F]F[-F]F[-F[+F]F[+F[+F]F[-F]F]F[+F]F]F[-F]F[-F[+F]F[-F]F]F[+F]F[-F]F[+F[-F]F[+F[+F]F]F[+F]F[-F[+F]F]F[+F]F[-F]F[+F[+F]F[-F]F[+F[+F]F]F[+F]F[-F[+F]F[-F]F]F[+F]F[-F]F]F[+F]F[-F]F[+F[+F]F]F[+F]F[-F]F[-F[-F]F]F[-F]F[-F[+F]F[-F]F[+F[+F]F[-F]F]F[-F]F[-F[+F]F[-F]F]F[+F]F[-F]F]F[-F]F[+F[+F]F]F[+F]F[-F[-F]F]F[-F]F]F[+F]F[-F]F[+F[+F]F[-F]F]F[+F]F[-F[+F]F]F[+F]F[+F[-F]F[+F[-F]F]F[-F]F[-F[+F]F[-F]F]F[+F]F]F[+F]F[+F[-F]F]F[+F]F[-F]F[-F[+F]F[-F]F[+F[+F]F]F[+F]F[+F[+F]F[-F]F[+F[+F]F[-F]F]F[-F]F]F[+F]F[+F[-F]F]F[+F]F[-F[+F]F[-F]F]F[-F]F[-F[-F]F[+F[-F]F]F[-F]F[-F[-F]F]F[+F]F[-F]F]F[+F]F[-F[+F]F[-F]F]F[+F]F]F[+F]F[-F]F[+F[+F]F]F[-F]F[+F[+F]F[-F]F[+F[-F]F]F[+F]F]F[+F]F[+F[-F]F]F[-F]F[-F[+F]F]F[-F]F[-F[+F]F[-F]F[-F[+F]F[-F]F]F[-F]F]F[+F]F[+F[+F]F]F[-F]F[-F[+F]F[-F]F]F[+F]F]F[+F]F[+F[-F]F]F[+F]F[-F]F[+F[-F]F[-F[+F]F[-F]F]F[+F]F[-F]F]F[+F]F[+F[-F]F]F[+F]F[-F]F[+F[+F]F[-F]F[+F[-F]F]F[+F]F[-F]F[+F[+F]F[-F[+F]F]F[+F]F]F[+F]F[-F[+F]F]F[-F]F]F[+F]F[-F]F[-F[-F]F]F[+F]F[-F]F[+F[+F]F[+F[-F]F]F[+F]F[-F]F[-F[+F]F[-F]F]F[-F]F]F[+F]F[-F]F[+F[+F]F]F[-F]F[-F[-F]F]F[+F]F[-F]F[-F[+F]F[-F]F[+F[+F]F[-F]F]F[-F]F[-F[-F]F]F[-F]F]F[+F]F[+F[+F]F[-F]F]F[-F]F[-F[-F]F]F[+F]F[-F[-F]F[+F[+F]F]F[+F]F[-F]F[-F[-F]F]F[+F]F[-F]F[+F[+F]F[-F[-F]F]F[+F]F[-F]F]F[+F]F[-F]F[-F[+F]F[-F]F]F[+F]F]F[+F]F[-F]F[+F[+F]F]F[-F]F[-F[+F]F[-F]F]F[+F]F[-F[+F]F[-F]F[+F[+F]F]F[-F]F]F[-F]F[+F[+F]F[-F]F]F[+F]F
# test_nd (coding_rooms_unit_tests.TestLS) ... ERROR

# ======================================================================
# ERROR: test_nd (coding_rooms_unit_tests.TestLS)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/usercode/coding_rooms_unit_tests.py", line 8, in test_nd
#     nd_ls_1 = LSystem(axiom="[F]", rules={"F": [(0.33, "F[+F]F[-F]F"), (0.33, "F[+F]F"), (0.33, "F[-F]F")]}, angle=25.7, step=10, n=2,)
# TypeError: LSystem.__init__() got an unexpected keyword argument 'n'

# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# FAILED (errors=1)


