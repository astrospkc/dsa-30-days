# n = 5
# sum of first n numbers
# sum  = 1+2+3+4+5

def Sum_of_first_n_numbers(i, n, sum):
    if i > n:
        return
    print(sum)
    sum = sum+i
    # print(sum)
    Sum_of_first_n_numbers(i+1, n, sum)


Sum_of_first_n_numbers(i=1, n=int(input("enter a number: ")), sum=0)
