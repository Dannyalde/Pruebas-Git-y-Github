num = int(input("ingrese un numero positivo diferente de cero:"))

def factorial(num):
    factorial = 1
    for iter in range(num,1,-1):
        factorial = factorial *iter
    
    return factorial

num_factorial = factorial(num)

if num%2 == 0:
    print(f"{num} es un numero par y su factorial es {num_factorial}")
else:
    print(f"{num} es un numero impar y su factorial es {num_factorial}")

