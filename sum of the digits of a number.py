def sum_of_the_digits(n, sum):
    if n % 10 == 0:
        return
    sum = sum + n % 10
    n = n//10

    sum_of_the_digits(n, sum)
    print(sum)


n = int(input("enter a number: "))
sum_of_the_digits(n, sum=0)
