from pysmt.shortcuts import *

varA = Symbol("A") 
varB = Symbol("B") 



f = Implies(varA, varB)
print(f)
print(get_model(f))