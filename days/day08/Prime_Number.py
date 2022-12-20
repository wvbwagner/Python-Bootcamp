def prime_checker(number):
    divisor = 0
    for i in range(1, number + 1):
        if number % i == 0:
            divisor += 1
    if divisor == 2:
        print(f'It\'s a prime number.')
    else:
        print(f'It\'s not a prime number.')
        
n = int(input("Check this number: "))
prime_checker(number=n)

