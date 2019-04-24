import common
import unittest
import illuminator

class TestFluorescence(unittest.TestCase):
    illum = illuminator.Illuminator()

    def flash(self):
        illum.flash_fluorescence()


if __name__ == '__main__':
    unittest.main()
