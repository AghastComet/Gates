gates = []
debug=True

#decorator to record what gates are loaded, maybe useful later
def addGate(clas):
    global gates
    gates+=[clas]
    if debug: print(clas.__name__,'gate loaded successfully')
    return clas

#start of gates' codes, more can be added easily
@addGate
class And:
    def __init__(self, gateA, gateB):
        self.gateA = gateA
        self.gateB = gateB

    @property #runs value funciton when value variable is read
    def value(self):
        return self.gateA.value and self.gateB.value

@addGate
class In:
    def __init__(self, value):
        self.value = value

#example code
iGate1 = In(True)
iGate2 = In(False)
aGate  = And(iGate1, iGate2)
print(aGate.value)
iGate2.value = True
print(aGate.value)
