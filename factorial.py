def fact(n):
    """
    5 * 4 * 3 * 2 * 1
    """
    if n == 0:
        return 1

    result = n * fact(n-1)
    return result


def div(n):
    return 100/n


if __name__ == "__main__":
    print(fact(5))
