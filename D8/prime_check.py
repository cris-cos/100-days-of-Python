def prime_checker(number):
    occurence = 0
    for i in range(1, number):
        if number%i == 0:
            occurence += 1
    if occurence > 2:
        print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)