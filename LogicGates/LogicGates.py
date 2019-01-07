# --- Python implementation of logic gates ---

class LogicGate(object):
    def __init__(self, name,model):
        self.name = name 
        self.model = model
    
    def display(self):
        pass
    
    def getInput(self):
        pass
    
    def findOutput(self):
        pass

def connector(ob_from,ob_to):
    for i in range(len(ob_to.pins)):
        if ob_to.pins[i] == None:
            ob_to.pins[i] = ob_from.out()
            return
    print("NO FREE PINS!!!")

class UnaryGate(LogicGate):
    def __init__(self,name,model):
        LogicGate.__init__(self,name,model)

        self.Input = [None]
        self.Output = [None]
        self.InPins = 1
        self.OutPins = 1

    

class BinaryGate(LogicGate):
    def __init__(self,name,model):
        LogicGate.__init__(self,name,model)

        self.Input = [None,None]
        self.Output = [None]
        self.InPins = 2
        self.OutPins = 1

class NotGate(UnaryGate):
    def __init__(self,name):
        UnaryGate.__init__(self,name,"NOT Gate")
    
    def getInput(self):
        if self.Input[0] == None:
            self.Input[0] = int(input("Enter the value of the NOT gate: "))
        

    def findOutput(self):
        if self.Input[0] == 0:
            self.Output[0] = 1
        else:
            self.Output[0] = 0

    def __str__(self):
        print("Gate ",self.name)
        print("NOT Gate Input: ", self.Input[0])
        print("NOT Gate Output: ", self.Output[0])
    
class AndGate(BinaryGate):
    def __init__(self):
        BinaryGate.__init__(self,name,"AND Gate")

    def getInput(self):
        print


    

