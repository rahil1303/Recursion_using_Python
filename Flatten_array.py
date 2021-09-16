def flatten(arr):
  resultarr = []
  for custItem in arr:
    if type(custItem) is list:
      resultarr.extend(flatten(custItem))
     else:
      resultarr.append(custItem)
 return resultarr
