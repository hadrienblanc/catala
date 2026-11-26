from catala_runtime import *


def round_to_decimal(variable: Money, n_decimal: Integer) -> Money:
    if n_decimal >= Integer(2):
        return variable
    elif n_decimal == Integer(1):
        return Money(Integer(Money(variable * Integer(10)).round()) / Integer(10))
    else:
        pow_10 = Integer(pow(10, -int(n_decimal)))
        cents = int(variable)
        truncated = Money(abs(cents) // int(pow_10) * (-1 if cents < 0 else 1))
        r: Money = Money(Integer(truncated)).round()
        return Money(r * pow_10)
