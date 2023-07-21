def f(i):
    
    if i == 0:
      return 1  
    else:
       return  i * f(i - 1)
n = int(input('n: '))
spisok = [f(n - i) for i in range(n)]
                                  
print(spisok)
