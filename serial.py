"""Python serial number generator."""

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
    def __init__(self,start):
        """ sets the ascending number and holds the starter number """
        self.numb = start
        self.starter = start
    def __repr__(self):
        return f"Current Serial is {self.numb}, next serial is {self.numb + 1} and the starter value is {self.starter}"
    def generate(self):
        """ prints the current value of SerialNum and adds 1  """
        print(self.numb)
        self.numb += 1
    def reset(self):
        """ resets serial number to start number """
        self.numb = self.starter