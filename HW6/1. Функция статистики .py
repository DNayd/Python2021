# В идеале:
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

# Вероятнее всего так будет работать, но не факт :)
def alph():
  A = input('Введите алфавит: ').split()
  seq = input('Введите последовательность: ')
  for i in range(len(seq)):
      G = seq.count(A[i])
      print(A[i], G)
