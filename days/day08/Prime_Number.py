def prime_checker(number):
    divisor = 0
    for i in range(2, number):
        if number % i == 0:
            divisor += 1
    if divisor == 0:
        print('It\'s a prime number.')
    else:
        print('It\'s not a prime number.')
        
n = int(input("Check this number: "))
prime_checker(number=n)

