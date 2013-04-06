import unittest
import matplotlib.pyplot as plt

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.fig1 = plt.figure(figsize=(4,5))
        self.fig2 = plt.figure(figsize=(6,7))

    def test_figure1(self):
        h = self.fig1.get_figheight()
        w = self.fig1.get_figwidth()
        self.assertEqual((w, h),(4.,5.))

    def test_figure2(self):
        h = self.fig2.get_figheight()
        w = self.fig2.get_figwidth()
        self.assertEqual((w, h),(6.,7.))

   
if __name__ == '__main__':
    unittest.main()
