def productsofArray(n):
  if len(arr) == 0:
    return 1
  else:
    return arr[0] * productsofArray(arr[1::])
  
 print(productsofArray([1,2,3))
