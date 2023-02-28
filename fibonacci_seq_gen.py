

# Fibonacci Sequence Generator
# Have the user enter a number and
# generate a fibonacci sequence
# which size is equivalent to that number


def fib_seq(n):
    '''
    Generates a fibonacci sequence
    with size of n
    :param: n
    :return: fibonacci sequence
    '''

    assert n > 0

    fibonacci = [1]

    while len(fibonacci) < n:
        if len(fibonacci) == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])

    # convert the numbers to strings

    for i in range(len(fibonacci)):
        fibonacci[i] = str(fibonacci[i])

    return (', '.join(fibonacci))

def main():
    print(fib_seq(int(input('How many numbers do you need in the sequence?'))))


if __name__ == '__main__':
    main()

