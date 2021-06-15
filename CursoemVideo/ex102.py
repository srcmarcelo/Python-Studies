def factorial(n, show=False):
    """
    --Factorial of a number
    param n: number to see its factorial.
    param show: (optional) to see the calculus.
    return: the factorial of n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end=' x ' if c != 1 else ' = ')
        f *= c
    return f


print(factorial(int(input('Enter here a number: ')), show=True))
