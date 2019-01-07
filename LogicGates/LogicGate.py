# --- Python program to implement logic gates ---

# -----------------------------------------------------------------------------------------------------

#########################################################################################
#                                                                                       #
#           Things Implemented:                                                         #
#               1. An error class for pin inputs                                        #
#               2. Classes for Unary and Binary Gates                                   #
#               3. NOT, AND, OR, XOR gates                                              #
#               4. Connector                                                            #        
#                                                                                       #
#########################################################################################

#########################################################################################
#                                                                                       #
#                              WORK IN PROGRESS                                         #
#                                                                                       #
#########################################################################################

# -----------------------------------------------------------------------------------------------------

# Error defining classes: 
class Error(Exception):
    # Base class for raising all errors
    pass
class PinValueError(Error):
    # Raised when the pin is not a valid input
    pass

# -----------------------------------------------------------------------------------------------------

# The base class, where it all begins
class LogicGate(object):
    def __init__(self, name, model):
        self.name = name            # Stores the name of the logic gate (gate1, gate2, etc)
        self.model = model          # Stores the model of the logic gate (and, or, etc)
        self.output = None          # Stores the output of the gate

    def getName(self):
        return self.name
    
    def getModel(self):
        return self.model
    
    def getOutput(self):
        self.performLogic()         # Will be defined in sub classes
        return self.output

# -----------------------------------------------------------------------------------------------------

# The class for all unary gates
class UnaryGate(LogicGate):
    def __init__(self, name, model):
        LogicGate.__init__(self,name,model)

        self.pin = None
    
    def getInput(self):
        val = None
        # Checks for connector
        # replace with try-except from below later
        if self.pin == None:
            while True:
                ##val = int(input("Enter the value of pin for gate %s : "%(self.getModel())))
                print("Enter the value of pin for gate %s : "%(self.getModel()),end = '')
                val = int(input())

                if val not in [0,1]:
                    print("Invalid value for pin! Can give value of only '0' or '1'!")
                    continue
                else:
                    break
            self.pin = val
        else:
            return self.pin.getFrom().getOutput()
    
    def setNextPin(self, src):
        if self.pin == None:
            self.pin = src
        else:
            print("Cannot connect! NO FREE PINS ON GATE!!!")

# -----------------------------------------------------------------------------------------------------

# The class for all binary gates
class BinaryGate(LogicGate):
    def __init__(self, name, model):
        LogicGate.__init__(self,name,model)

        self.pinA = None
        self.pinB = None
    
    def getInput(self):
        ### NOT WORKING ###
        val = None
        while True:
            ##val = int(input("Enter the value of pin for gate %s : "%(self.getModel())))
            val = int(input("Enter the value of pin for gate : ",end = ''))

            if val not in [0,1]:
                print("Invalid value for pin! Can give value of only '0' or '1'!")
                continue
            else:
                break
        return val
    
    def getPinA(self):
        if self.pinA == None:
            return self.getInput()
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return self.getInput()
        else:
            return self.pinB.getFrom().getOutput()
        
    def setNextPin(self, src):
        if self.pinA == None:
            self.pinA = src
        else:
            if self.pinB == None:
                self.pinB = src
            else:
                print("Cannot connect! NO FREE PINS ON GATE!!!")
# -----------------------------------------------------------------------------------------------------    

# Class Implementing NOT Gate
class NotGate(UnaryGate):
    def __init__(self, name, model = "NOT GATE" ):
        UnaryGate.__init__(self, name, model)
    
    # Function to do what a not gate does
    def performLogic(self):
        a = self.getInput()
        if a == 1:
            return 0
        return 1

# -----------------------------------------------------------------------------------------------------    

# Class Implementing AND Gate
class AndGate(BinaryGate):
    def __init__(self, name, model="AND Gate" ):
        BinaryGate.__init__(self, name, model)

    def performLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 1 and b == 1:
            return 1
        return 0
# -----------------------------------------------------------------------------------------------------    

# Class to implement OR Gate
class OrGate(BinaryGate):
    def __init__(self, name, model = "OR Gate" ):
        BinaryGate.__init__(self, name, model)

    def performLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        return 0

# -----------------------------------------------------------------------------------------------------

# Class to implement XOR Gate
class XorGate(BinaryGate):
    def __init__(self, name, model = "XOR Gate"):
        BinaryGate.__init__(self, name, model)
    
    def performLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if (a == 0 and b == 0) or (a == 1 and b == 1):
            return 1
        return 0

# -----------------------------------------------------------------------------------------------------

# Class to implement Connectors
class Connectors(object):
    def __init__(self, From, To):
        self.From = From
        self.To = To
    
        To.setNextPin(self)
    
    def getFrom(self):
        return self.From
    
    def getTo(self):
        return self.To

# -----------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    print("This is a simple implementation of logic gates in python")

# -----------------------------------------------------------------------------------------------------
