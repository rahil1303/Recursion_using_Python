def isOdd(num):
    if type(num) not in [int, long]:
        return False
    if str(num)[-1] in "13579":
        return True
    return False
  
  
 
def isEven(n):
    isEven = True;
    for i in range(1, n+1):
        if isEven == True:
            isEven = False;
        else:
            isEven = True;
 
    return isEven;
 
# Driver code   
n = 101;
if isEven(n) == True:
    print ("Even");
else:
    print ("Odd");
