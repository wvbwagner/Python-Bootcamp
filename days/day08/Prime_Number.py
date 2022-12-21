def prime_checker(number):
    divisor = 0
    for i in range(2, number):
        if number % i == 0:
            divisor += 1
            print('It\'s not a prime number.')
            exit(0)
    print('It\'s a prime number.')
     
n = int(input("Check this number: "))
prime_checker(number=n)

