from pysmt.shortcuts import Symbol, And, GE, LT, Plus, Equals, Int, get_model
from pysmt.typing import INT
from algorithm import *
from graph_class import *
from heap import *
from problem_set import *

hello = [Symbol(s, INT) for s in "hello"]
world = [Symbol(s, INT) for s in "world"]

letters = set(hello+world)

domains = And([And(GE(l, Int(1)),
                   LT(l, Int(10))) for l in letters])
#print(domains)
                   
                   
sum_hello = Plus(hello) # n-ary operators can take lists
print(sum_hello)
sum_world = Plus(world) # as arguments
print(sum_world)

problem = And(Equals(sum_world, Int(25)),
              Equals(sum_hello, Int(25)))
formula = And(domains, problem)

#print("Serialization of the formula:")
print(formula)

model = get_model(formula)
if model:
  print(model)
else:
  print("No solution found")