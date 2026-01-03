def odd_or_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(odd_or_even(num))
