def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    
    i = 2
    
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
        

quant = int(input())

for i in range(quant):
    number = int(input())
    if isPrime(number):
        print('Prime')
    else:
        print('Not prime')
