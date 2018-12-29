### Seven Segment Display

### WIP ####

vals = [None,None,None,None,None,None,None]

def display():
    '''
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


    # the list of 7 segment stuff
    temp = [" ","_"," ","\n","|","_","|","\n","|"," ","|","\n"," ","‾"," ","\n"]

    key = [1,6,10,13,8,4,5] # ABCDEFG

    
