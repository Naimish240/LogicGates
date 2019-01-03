### Seven Segment Display

### WIP ####
from copy import deepcopy
from GatesWithNAND import NOT,AND,AND3,MultiOR

'''
    Note: 0 ---> on
          1 ---> off

    Numbers:
    
    Display: ABCDEFG
    Key    : 1001111
    1                       
    2      |
    3      |
    4       
    
    Display: ABCDEFG
    Key    : 0010010
    1     _ 
    2     _|
    3    |  
    4     ‾ 

    Display: ABCDEFG
    Key    : 0000110
    1     _ 
    2     _|
    3      |
    4     ‾ 

    Display: ABCDEFG
    Key    : 1001100
    1       
    2    |_|
    3      |
    4       

    Display: ABCDEFG
    Key    : 0100100
    1     _ 
    2    |_
    3      |
    4     ‾ 

    Display: ABCDEFG
    Key    : 0100000
    1     _
    2    |_
    3    | |
    4     ‾ 

    Display: ABCDEFG
    Key    : 0001111
    1     _ 
    2      |
    3      |
    4     

    Display: ABCDEFG
    Key    : 0000000
    1     _ 
    2    |_|
    3    | |
    4     ‾ 

    Display: ABCDEFG
    Key    : 0000100
    1     _ 
    2    |_|
    3      |
    4     ‾ 

    Display: ABCDEFG
    Key    : 0000001
    1     _ 
    2    | |
    3    | |
    4     ‾

    Letters: 

    Display: ABCDEFG
    Key    : 0001000
    1     _ 
    2    |_|
    3    | |
    4      
    
    Display: ABCDEFG
    Key    : 1100000
    1     
    2    |_
    3    | |
    4     ‾ 

    Display: ABCDEFG
    Key    : 0110001
    1     _ 
    2    |
    3    | 
    4     ‾ 

    Display: ABCDEFG
    Key    : 1000010
    1      
    2     _|
    3    | |
    4     ‾ 

    Display: ABCDEFG
    Key    : 0110000
    1     _ 
    2    |_
    3    | 
    4     ‾ 

    Display: ABCDEFG
    Key    : 0111000
    1     _ 
    2    |_
    3    | 
    4      

'''

class Display(object):
# The list of 7 segment stuff
    temp = [        
            # Add '\n' at end of each line when adding two numbers
                                   #        0   1   2   3
                                    
            [" ","_"," "," "],     #   0    0   1   2   3
            ["|","_","|"," "],     #   1    4   5   6   7
            ["|"," ","|"," "],     #   2    8   9   10  11
            [" ","‾"," "," "]      #   3    12  13  14  15
        ]

# Co-ord is temp[i//4][i%4]

key = {
    'A' : 1,
    'B' : 6,
    'C' : 10,
    'D' : 13,
    'E' : 8,
    'F' : 4,
    'G' : 5
    
}
def isA(n):
    # Stores the values
    # [A,B,C,D]
    A,B,C,D = n[0], n[1], n[2], n[3]
    notA = NOT([A]).Output
    notB = NOT([B]).Output
    notC = NOT([C]).Output
    notD = NOT([D]).Output

    ob1 = AND([notB,notD])
    ob2 = AND([notA,C])
    ob3 = AND([B,C])
    ob4 = AND([C,notD])
    ob5 = AND3([notA,B,D])
    ob6 = AND3([A,notC,notD])
    ob7 = AND3([A,notB,notC])

    obj = MultiOR([ob1.Output,ob2.Output,ob3.Output,ob4.Output,ob5.Output,ob6.Output,ob7.Output])

    return obj.Output

def isB(n):
    # Stores the values
    # [A,B,C,D]
    A,B,C,D = n[0], n[1], n[2], n[3]
    notA = NOT([A]).Output
    notB = NOT([B]).Output
    notC = NOT([C]).Output
    notD = NOT([D]).Output

    ob1 = AND([notB,notD])
    ob2 = AND3([notA,notC,notD])
    ob3 = AND3([A,notC,D])
    ob4 = AND3([notA,C,D])
    ob5 = AND3([notA,notB,C])

    obj = MultiOR([ob1.Output,ob2.Output,ob3.Output,ob4.Output,ob5.Output])

    return obj.Output

def isC(n):
    # Stores the values
    # [A,B,C,D]
    A,B,C,D = n[0], n[1], n[2], n[3]
    notA = NOT([A]).Output
    notB = NOT([B]).Output
    notC = NOT([C]).Output

    ob1 = AND([notA,notC])
    ob2 = AND([notA,D])
    ob3 = AND([notA,B])
    ob4 = AND([notC,D])
    ob5 = AND([A,notB])

    obj = MultiOR([ob1.Output,ob2.Output,ob3.Output,ob4.Output,ob5.Output])

    return obj.Output

def isD(n):
    # Stores the values
    # [A,B,C,D]
    A,B,C,D = n[0], n[1], n[2], n[3]
    notA = NOT([A]).Output
    notB = NOT([B]).Output
    notC = NOT([C]).Output
    notD = NOT([D]).Output

    ob1 = AND([notB,notD])
    ob2 = AND([C,notD])
    ob3 = AND3([notA,notB,C])
    ob4 = AND3([A,notB,notC])
    ob5 = AND3([B,notC,D])

    obj = MultiOR([ob1.Output,ob2.Output,ob3.Output,ob4.Output,ob5.Output])

    return obj.Output

def isE(n):
    # Stores the values
    # [A,B,C,D]
    A,B,C,D = n[0], n[1], n[2], n[3]
    notB = NOT([B]).Output
    notD = NOT([D]).Output

    ob1 = AND([notB,notD])
    ob2 = AND([C,notD])
    ob3 = AND([A,B])
    ob4 = AND([A,C])

    obj = MultiOR([ob1.Output,ob2.Output,ob3.Output,ob4.Output])

    return obj.Output

def isF(n):
    # Stores the values
    # [A,B,C,D]
    A,B,C,D = n[0], n[1], n[2], n[3]
    notA = NOT([A]).Output
    notB = NOT([B]).Output
    notC = NOT([C]).Output
    notD = NOT([D]).Output

    ob1 = AND([notC,notD])
    ob2 = AND([A,notB])
    ob3 = AND([A,C])
    ob4 = AND3([B,C,notD])
    ob5 = AND3([notA,B,notC])

    obj = MultiOR([ob1.Output,ob2.Output,ob3.Output,ob4.Output,ob5.Output])

    return obj.Output    

def isG(n):
    # Stores the values
    # [A,B,C,D]
    A,B,C,D = n[0], n[1], n[2], n[3]
    notA = NOT([A]).Output
    notB = NOT([B]).Output
    notC = NOT([C]).Output
    notD = NOT([D]).Output

    ob1 = AND([A,notB])
    ob2 = AND([C,notD])
    ob3 = AND([A,C])
    ob4 = AND([A,D])
    ob5 = AND([notB,C])
    ob6 = AND3([notA,B,notC])

    obj = MultiOR([ob1.Output,ob2.Output,ob3.Output,ob4.Output,ob5.Output,ob6.Output])

    return obj.Output

def SingleDisplay(n):

    temp_disp = deepcopy(Display.temp)

    if isA(n) == 0:
        temp_disp[key['A']//4][key['A']%4] = " "

    if isB(n) == 0:
        temp_disp[key['B']//4][key['B']%4] = " "

    if isC(n) == 0:
        temp_disp[key['C']//4][key['C']%4] = " "

    if isD(n) == 0:
        temp_disp[key['D']//4][key['D']%4] = " "

    if isE(n) == 0:
        temp_disp[key['E']//4][key['E']%4] = " "

    if isF(n) == 0:
        temp_disp[key['F']//4][key['F']%4] = " "

    if isG(n) == 0:
        temp_disp[key['G']//4][key['G']%4] = " "

    for i in temp_disp:
        for j in i:
            print(j,end = '')
        print()

if __name__ == '__main__':
    SingleDisplay([1,0,0,0])
    SingleDisplay([0,1,0,0])
    SingleDisplay([0,0,0,1])
    SingleDisplay([0,0,1,1])
       