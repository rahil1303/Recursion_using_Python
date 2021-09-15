def recursiverange(n):
  if n == 0:
    return 0
  else:
    return n + recursiverange(n - 1)
