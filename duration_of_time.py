"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.

"""
SECONDS = 60
SECS_IN_MIN = 60 * 60
SECS_IN_DAY = SECS_IN_MIN * 24

duration = [53, 120, 153, 2475, 4153, 400153, 634126]

for sec in duration:
    if sec < SECONDS:
        print(sec, 'сек')
    elif sec < SECS_IN_MIN:
        print(f'{sec // SECONDS} мин {sec % SECONDS} сек')
    elif sec < SECS_IN_DAY:
        print(f'{sec // SECS_IN_MIN} час {sec % SECS_IN_MIN // SECONDS} мин {sec % SECS_IN_MIN % SECONDS} сек')
    else:
        day = sec // SECS_IN_DAY
        temp = sec % SECS_IN_DAY
        print(f'{day} дн {temp // SECS_IN_MIN} час {temp % SECS_IN_MIN // SECONDS} мин {temp % SECS_IN_MIN % SECONDS} сек')
