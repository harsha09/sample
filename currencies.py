class Currency:

    __currencies = {'EUR': 1.19, 'GBP': 1.34, 'USD': 1, 'INR': 0.016}

    def __init__(self, value, unit="USD"):
        """Initialization. """
        if type(value) == int or type(value) == float:
            self.value = value
        else:
            raise ValueError('Invalid value, should be of int or float type.')
        if type(unit) == str:
            self.unit = unit
        else:
            raise ValueError('Invalid Unit, should be of string type.')

    def convert_to_dollar(self):
        """Converts any currency to dollar. """
        return self.value * Currency.__currencies[self.unit]

    def __str__(self):
        return "{} {}".format(self.value, self.unit)

    def __add(self, other):
        """Converts any currency to USD, then add both the currencies.
        Then converts it to currency of LHS object."""
        if type(other) == int or type(other) == float:
            summed_value = self.value + other
        else:
            summed_value = Currency.convert_to_dollar(self) + Currency.convert_to_dollar(
                other)
        return Currency(summed_value/Currency.__currencies[self.unit], self.unit)

    def __add__(self, other):
        return Currency.__add(self, other)

    def __radd__(self, other):
        return Currency.__add(other, self)

    def __iadd__(self, other):
        """Implementing Incrementing functionality. """
        self.value = Currency.__add(self, other)
        return self

    def __sub(self, other):
        """Converts any currency to USD, then subtracts both the currencies.
        Then converts it to currency of LHS object."""
        if type(other) == int or type(other) == float:
            summed_value = self.value - other
        else:
            summed_value = Currency.convert_to_dollar(self) - Currency.convert_to_dollar(
                other)
        return Currency(summed_value/Currency.__currencies[self.unit], self.unit)

    def __sub__(self, other):
        return Currency.__sub(self, other)

    def __rsub__(self, other):
        return Currency.__sub(other, self)

    def __isub__(self, other):
        """Implementing Incrementing functionality. """
        self.value = Currency.__sub(self, other)
        return self
