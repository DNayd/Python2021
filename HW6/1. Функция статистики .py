def Stat(GG):
  A = alphabet
  for n in GG:
    keys = A.keys()
    if n in keys:
      A[n] += 1
    else:
      A[n] = 1
  return 
print(Stat('sequence'))
