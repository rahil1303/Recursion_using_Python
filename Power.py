####Method 1
def power(base,exp):
  if exp == 0:
    return 1
   if exp == 1:
    return base
   else:
    return base * power(base,exp-1)
    
d = power(base,exp)
x = "%.2f" % d
print(x)

#### Method 2
def power(base,exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * power(base,exp-1)
 

f = (power(2,4))
x = "%.4f" % f
print(x)

### Method in built function
d = (math.pow(2,4))
print(abs(d))
