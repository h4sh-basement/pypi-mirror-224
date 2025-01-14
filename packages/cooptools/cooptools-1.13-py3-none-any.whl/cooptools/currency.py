import dataclasses
import math
from dataclasses import dataclass

@dataclass(frozen=True)
class USD:
    dollars: int
    cents: int

    @classmethod
    def from_val(cls, val: float|str|int):
        if type(val) == str:
            val = float(val)

        if type(val) not in (float, int):
            raise TypeError(f'{val} [{type(val)}] not supported to be converted to CurrencySchema')

        dollars = int(val)
        cents = int(val * 100 - dollars * 100) # Weird multiplcation to avoid float issues

        return USD(dollars=dollars, cents=cents)

    @property
    def AmountFloated(self) -> float:
        return self.dollars + round(self.cents / 100, 2)

    @classmethod
    def verify_val(cls, val):
        if type(val) in [float, int, str]:
            val = USD.from_val(val)

        if type(val) != USD:
            raise NotImplementedError(f"{val} is not of type [{USD}]")

        return val

    def __add__(self, other):
        other = self.verify_val(other)

        dollars = self.dollars + other.dollars
        cents = self.cents + other.cents

        if cents >= 100:
            cent_dols = math.floor(cents / 100)
            cents = cents % 100
            dollars += cent_dols

        if cents < 0:
            factor = math.ceil(- cents / 100)
            dollars -= 1 * factor
            cents += 100 * factor

        return USD(dollars=dollars, cents=cents)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other = self.verify_val(other)

        dollars = self.dollars - other.dollars
        cents = self.cents - other.cents

        if cents > -100:
            cent_dols = math.floor(cents / 100)
            cents = cents % 100
            dollars += cent_dols
        return USD(dollars=dollars, cents=cents)

    def __gt__(self, other):
        return (self - other).AmountFloated > 0

    def __lt__(self, other):
        return (other - self).AmountFloated > 0

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return not self.__gt__(other)

    def __str__(self):
        return "${:,.2f}".format(self.AmountFloated)

    def __neg__(self):
        return USD(dollars=-self.dollars, cents=-self.cents)

    def __float__(self):
        return self.AmountFloated

    def to_dict(self):
        return vars(self)


if __name__ == "__main__":
    a = USD.from_val(1.5)
    b = USD.from_val(3.5)
    d = USD(1, 250)
    c = a + b
    print(c)
    print(d)
    print(d.dollars, d.cents)
    e = d + c
    print(e, e.dollars, e.cents)
    print(e.to_dict())
    print(dataclasses.asdict(e))