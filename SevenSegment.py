### Seven Segment Display

### WIP ####

from GatesWithNAND import *



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
key = [1,6,10,13,8,4,5] # ABCDEFG

    
