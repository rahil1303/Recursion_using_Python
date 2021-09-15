def factorial(num):
  if num == 0:
    return 1
  else:
    return num * factorial(num - 1)

a = (factorial(4))
x = "%.2f" % a 
print(x)
