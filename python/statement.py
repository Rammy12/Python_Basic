
"""
problem link:-
https://practice.geeksforgeeks.org/batch/fork-python/track/python-module-2-ControlStatementsandLoops/problem/if-loop-python
"""

def friends_in_trouble(j_angry, s_angry):
    if (j_angry == s_angry):

       return True

    elif(j_angry != s_angry):

        return False

"""
problem link:-
https://practice.geeksforgeeks.org/batch/fork-python/track/python-module-2-ControlStatementsandLoops/problem/mark-even-and-odd
"""

def checkOddEven(x):
    if(x % 2 == 0):
      # Complete the statement below
      return True
    else:
        # Complete the statement below
        return False

"""
problem link:-
https://practice.geeksforgeeks.org/batch/fork-python/track/python-module-2-ControlStatementsandLoops/problem/check-the-status
"""
def check_status(a, b, flag):
    ##Your code here
    ##Either True or False is returned
    if( a<0 or b<0):
        if(a<0 and b<0):
            if(flag):
                return True
            else:
                return  False
        elif(not flag):
            return True
        else:
            return False
    else:
        return False

"""
problem link:-
https://practice.geeksforgeeks.org/batch/fork-python/track/python-module-2-ControlStatementsandLoops/problem/for-loop-python
"""

def multiplicationTable(N):## in is a membership operator that is true if something is a member of sequence
    for i in range(1,11): ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i * N, end=" ") ## Separating by spaces using end =" "

"""
problem link:-
https://practice.geeksforgeeks.org/batch/fork-python/track/python-module-2-ControlStatementsandLoops/problem/for-loop-2-python
"""


def stringJumper(str):
    for i in range(0,len(str),2): ## from 0 to length of str and skip 2
        print(str[i], end="") ##printing character and separating characters by nothing

"""
problem link:-
https://practice.geeksforgeeks.org/batch/fork-python/track/python-module-2-ControlStatementsandLoops/problem/while-loop-in-python
"""

def printInDecreasing(x):
    # Complete the code below
    while(x >= 0):
        
        # your statement below to print the number
        # in decreasing order
        # Note: use end=" " parameter with print to seperate numbers by space.
        ##Output for testcases will automatically separated by a new line by the print() in driver code
        print(x,end=" ")
        
        
        x -= 1
"""
problem link:-
https://practice.geeksforgeeks.org/batch/fork-python/track/python-module-2-ControlStatementsandLoops/problem/jumping-through-while-python
"""

def printIncreasingPower(x):
    ##Your code here
    
    # Loop to jump in powers of 2
    y,z=1,1
    while(z<=x):
        ##Your code here
        
        print (z , end = " ")
        
        ##Your code here
        y+=1
        z=y**2

"""
problem link:-
https://practice.geeksforgeeks.org/batch/fork-python/track/python-module-2-ControlStatementsandLoops/problem/zero-converter-python
"""
def pos(n):
    ## Write the code
    while(n):
        print(n-1,end=" ")
        n-=1
        
        
    
def neg(n):
    ##Write the code
    while(n<=0):
        print(n,end=" ")
        n+=1

"""
problem link:-
https://practice.geeksforgeeks.org/batch/fork-python/track/python-module-2-ControlStatementsandLoops/problem/cat-and-hat-python
"""

def cat_hat(str):
    str1=str.count("cat")
    str2=str.count("hat")
    if str1==str2:
        return True
    else:
        return False
  ##your code here##
  ##You need to write complete code this time 