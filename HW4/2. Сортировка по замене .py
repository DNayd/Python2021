Reference = input('Введите референсе: ')
num = int(input('Сколько последовательностей необходимо сверить? '))
x = []
for i in range (num):
  x.append(input('Введите последовательность: '))
def sortchange(x):
  z = []
  for i in range(0, num):
    y = 0
    for j in range(0,len(x[i])):
      if x[i][j]!=ref[j]:
        y+=1
    z.append(y)
    for i in range(1,len(z)):
        key=z[i]
        j=x[i]
        n=i-1
        while n>=0 and key<z[n]:
            z[n+1]=z[n]
            x[n + 1] = x[n]
            n-=1
        x[n + 1] = j
        z[n+1]=key
    print(x)
sortchange(x)  
