from Core import *

inp = In()
inp2= In()

aGate=And(inp, inp2)

print(aGate.value)
inp.value = True
print(aGate.value)
inp2.value = True
print(aGate.value)

