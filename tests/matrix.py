import common
import unittest
import illuminator

class TestMatrix(unittest.TestCase):

    def __init__(self):
       self.illum = illuminator.Illuminator()

    def iterate(self):
        self.illum.iterate_matrix()

    def pattern(self):
        pass

    def phase_contrast(self):
        self.illum.flash_phase_contrast()


if __name__ == '__main__':
    unittest.main()
