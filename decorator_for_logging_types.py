def type_logger(func):
    print(func.__name__, end=' (')

    def logger(*args):
        s = ''
        for _ in args:
            s += f'{_}: {type(_)}, '
        s = s[:-2] + f' func_type: {type(func(*args))} func_result: {func(*args)})'
        return s

    return logger


@type_logger
def calc_cube(x, y):
    return x ** int(y)


res = calc_cube(2, '8')
print(res)
