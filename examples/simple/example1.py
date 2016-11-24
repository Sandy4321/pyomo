# Example adapted from PuLP file test1.py


# Import PuLP modeler functions
from pyomo.simple import *

# A new problem
prob = SimpleModel()

# Variables
# 0 <= x <= 4
x = prob.var("x", bounds=(0,4))
# -1 <= y <= 1
y = prob.var("y", bounds=(-1,1))
# 0 <= z
z = prob.var("z", bounds=(0,None))

# Objective
prob += x + 4*y + 9*z
# (the name at the end is facultative)

# Constraints
prob += x+y <= 5
prob += x+z >= 10
prob += -y+z == 7

# Optimize
status = prob.solve("glpk")

# Print the status of the solved LP
print("Status: %s" % status['Solver'][0]['termination condition'])

# Print the value of the variables at the optimum
print("x = %f" % value(x))
print("y = %f" % value(y))
print("z = %f" % value(z))

# Print the value of the objective
print("objective = %f" % value(prob.objective()))

