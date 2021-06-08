def val_checker(verbosity=False):
    def get_num(func):
        def validator(*args):
            num = func(*args)
            if verbosity(num):
                return num
            else:
                raise ValueError(f'wrong val {args}')
            return num
        return validator
    return get_num


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

res = calc_cube(4)
print(res)
