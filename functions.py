def is_even(x):
    if x == 0:
        return True
    else:
        return not is_odd(x)


def is_odd(x):
    return is_even(x - 1)
