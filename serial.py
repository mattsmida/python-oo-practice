class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 100):
        """ Creates a serial number generator with a start value,
        maintaining the current value. """
        self.start = start
        self.current_serial = start
        # self.start = self.current_serial = start   # <--- pythonic!

    def generate(self):
        """ Takes in the current serial number and increments it by one.
        Returns that value. """
        self.current_serial = self.current_serial + 1   # use += instead!
        return self.current_serial - 1


    def reset(self):
        """ Resets the generator to the initial value. """
        self.current_serial = self.start

    # Need some kind of storage for the current number
    # Need two methods: generate() and reset()
    # generate(): returns next in sequence
    # reset(): puts the number back to original