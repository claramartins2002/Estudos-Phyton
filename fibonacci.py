# Construa o λ-termo correspondente a série de Fibonacci, que é definida da seguinte forma: Fb(0) = 0,Fib(1) = 1, Fib(n+2) = Fib(n) + Fib(n+1). 

def fibo(n): 

  f0 = 0 

  f1 = 1 

  for k in range(1,n+1): 

    f2 = f0 + f1 

    f0 = f1 

    f1 = f2 

  return f0 

 

print(fibo(6)) 