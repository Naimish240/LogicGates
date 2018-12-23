# --- Implementing logic gates with only NAND gate ---

# --- WIP ---

def Input(ch=0):
    if ch:
        return[int(input("Enter the value of pin A: ")),int(input("Enter the value of pin A: "))]
    return [int(input("Enter the input: "))]


class NAND(object):
    def __init__(self):
        self.Input = [None,None]
        self.Output = None
        self.Model = "NAND Gate"

    def __repr__(self):
        print(self.Model)
        print("Input : ",self.Input)
        print("Output : ",self.Output)
        return ''

    def getInput(self,a,b):
        self.Input = [a,b]
        self.calOutput()

    def calOutput(self):
        if self.Input[0] == 1 and self.Input[1] == 1:
            self.Output = 0
        else:
            self.Output = 1
    
class AND():
    def __init__(self,In=None):
        ob1 = NAND()
        ob2 = NAND()

        if not In:
            self.Input = Input(1)
        else:
            self.Input = In

        self.Model = "AND Gate"

        # Calculate the value of first NAND gate 
        ob1.getInput(self.Input[0],self.Input[1])

        # Calculates the value of the second NAND gate
        ob2.getInput(ob1.Output,ob1.Output)
        self.Output = ob2.Output 
    
class NOT():
    def __init__(self,In = None):
        self.ob1 = NAND()

        self.Model = "NOT Gate"
        if not In:
            self.Input = Input()
        else:
            self.Input = In

        self.ob1.getInput(self.Input[0],self.Input[0])
        self.Output = self.ob1.Output

class OR():
    def __init__(self,In=None):
        # three gates, since there are three nand gates involved in making an or gate
        ob1 = NAND()
        ob2 = NAND()
        ob3 = NAND()

        self.Model = "OR Gate"
        if not In:
            self.Input = Input(1)
        else:
            self.Input = In
        # Evaluating the nand gates to get the equivalent or gate
        ob1.getInput(self.Input[0],self.Input[0])
        ob2.getInput(self.Input[1],self.Input[1])

        ob3.getInput(ob1.Output,ob2.Output)

        # saving the output with the or gate
        self.Output = ob3.Output

class NOR():
    def __init__(self,In=None):
        if not In:
            self.Input = Input(1)
        else:
            self.Input = In

        ob1 = OR(In)
        ob2 = NOT(ob1.Output)

        self.Model = "NOR Gate"

        self.Output = ob2.Output

class XOR():
    def __init__(self,In=None):
        if not In:
            self.Input = Input(1)
        else:
            self.Input = In
        self.Model = "XOR Gate"
        
        ob1 = NAND()
        ob2 = NAND()
        ob3 = NAND()
        ob4 = NAND()

        ob1.getInput(self.Input[0],self.Input[1])
        ob2.getInput(self.Input[0],ob1.Output)
        ob3.getInput(ob1.Output,self.Input[1])
        ob4.getInput(ob2.Output,ob3.Output)

        self.Output = ob4.Output

class XNOR():
    def __init__(self,In=None):
        if not In:
            self.Input = Input(1)
        else:
            self.Input = In
        self.Model = "XNOR Gate"

        ob1 = XOR(In)
        ob2 = NOT([ob1.Output])

        self.Output = ob2.Output

class HalfAdder():
    def __init__(self,In=None):
        if not In:
            self.Input = Input(1)
        else:
            self.Input = In
        self.Model = "Half Adder"

        ob1 = XOR(self.Input)
        ob2 = AND(self.Input)

        self.Output = [ob1.Output,ob2.Output]    # S,C        

class HalfSubtractor():
    def __init__(self,In=None):
        if not In:
            self.Input = Input(1)
        else:
            self.Input = In
        self.Model = "Half Subtractor"

        ob1 = XOR(self.Input)
        ob2 = NOT(self.Input[0])
        ob3 = AND([ob2.Output,self.Input[2]])

        self.Output = [ob1.Output,ob3.Output]

