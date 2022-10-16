def factorial(n):

    a = 1
    for i in range(n):
        a = a * (i + 1)
    return a

def report():
    for i in range(101):
        digits = len(str(factorial(i)))
        print(f"{i : >3}! is {digits : >3} digits long")
