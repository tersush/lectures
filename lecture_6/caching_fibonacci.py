number = int(input())

def fibonacci(number):
    if number <=  0:
        return []
    
    elif number == 1:
        return [0]
    
    elif number == 2:
        return [0,1]
    
    list_fibonacci = [0,1]
    fib_1 = 0
    fib_2 = 1
    
    for i in range(2,number):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
            list_fibonacci.append(fib_2)
    return list_fibonacci

print(fibonacci(number))