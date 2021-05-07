from random import randint

class Die:
    """class representing a die"""
    def __init__(self, num_sides=6):
        """6 sides die"""
        self.num_sides=num_sides

    def roll(self):
        """retrun random number between 1 and number of sides"""
        return randint(1,self.num_sides)