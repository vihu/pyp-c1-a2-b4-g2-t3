import unittest


class Insertion(object):
    def __init__(self, sample):
        ''' sample is the list to sort
        '''
        self.sample = sample

    @property
    def sorter(self):
        ''' implement insertion sort here
        '''
        inp = self.sample
        for i in range(1, len(inp)):
            x = inp[i]
            j = i
            while j > 0 and inp[j-1] > x:
                inp[j] = inp[j-1]
                j -= 1
            inp[j] = x
        return inp

    def __repr__(self):
        return 'Insertion({})'.format(self.sample)


class InsertionTestCases(unittest.TestCase):

    def test_simple(self):
        x1 = [1, 2, 3, 4, 5]
        b = Insertion(x1)
        self.assertEquals(b.sorter, sorted(b.sample))

    def test_negatives(self):
        x2 = [4, 5, 23, 5, 6, 1, 6, -1, 0.3]
        b = Insertion(x2)
        self.assertEquals(b.sorter, sorted(b.sample))

    def test_all_negatives(self):
        x3 = [-1, -4, -3, -2, -5]
        b = Insertion(x3)
        self.assertEquals(b.sorter, sorted(b.sample))

    def test_decimals(self):
        x4 = [0.3, 0.2, 0.1, 0.4, -0.5, -0.3]
        b = Insertion(x4)
        self.assertEquals(b.sorter, sorted(b.sample))


if __name__ == '__main__':
    unittest.main()
