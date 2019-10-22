gates = []
if __name__=='__main__':
    debug=True
else:
    debug=False
    
def addGate(clas):
    global gates
    gates+=[clas]
    if debug: print(clas.__name__,'gate loaded successfully')
    return clas

#parent class to initialize most gates whit one or two inputs
class _Gate():
    def __init__(self, gateA, gateB=None):
        self.gateA = gateA
        self.gateB = gateB

    @property
    def value(self):
        pass
        
@addGate
class And(_Gate):
    @property
    def value(self):
        return self.gateA.value and self.gateB.value
    
@addGate
class Or(_Gate):
    @property
    def value(self):
        return self.gateA.value or self.gateB.value
    
@addGate
class In:
    def __init__(self, value=False):
        self.value = value

        
if __name__ == '__main__':
    iGate1 = In(True)
    iGate2 = In(False)
    oGate  = Or(iGate1, iGate2)
    print(oGate.value)
    iGate1.value = False
    print(oGate.value)

