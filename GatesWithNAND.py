# --- Implementing logic gates with only NAND gate ---

# --- WIP ---

class NAND(object):
    def __init__(self,Model = "NAND Gate"):
        self.Input = [None,None]
        self.Output = None
        self.Model = Model

    def __str__(self):
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
    
class AND(NAND):
    def __init__(self):
        self.ob1 = NAND("AND Gate")
        self.ob2 = NAND("AND Gate")

        self.Model = "AND Gate"

        # Calculate the value of first NAND gate 
        self.ob1.getInput(int(input("Enter the value of pin A: ")),int(input("Enter the value of pin B: ")))
        self.Input = self.ob1.Input
        # Calculates the value of the second NAND gate
        self.ob2.getInput(self.ob1.Output,self.ob1.Output)
        self.Output = self.ob2.Output 
    
class NOT(NAND):
    def __init__(self):
        self.ob1 = NAND("NOT Gate")

        self.Model = "NOT Gate"

        self.Input = int(input("Enter the input: "))
        self.ob1.getInput(self.Input,self.Input)
        self.Output = self.ob1.Output


