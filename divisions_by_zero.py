class DivisionsByZeroError(Exception):
    def __str__(self):
        return 'division by zero is not possible'


def division(x, y):
    try:
        if y == 0:
            raise DivisionsByZeroError
    except DivisionsByZeroError as err:
        return err
    else:
        return x / y


print(division(5, 0))
print(division(5, 2))
