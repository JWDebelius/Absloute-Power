from __future__ import division

from unittest import TestCase, main

import numpy as np
import numpy.testing as npt

from absloute_power.distance import (convert_to_mirror)


class DistanceTest(TestCase):

    def setUp(self):
        self.length = 3
        self.dm = np.array([[0, 1, 2],
                            [1, 0, 3],
                            [2, 3, 0]])

    def test_convert_to_mirror(self):
        vec = np.arange(0, ((self.length) * (self.length - 1))/2) + 1
        test_dm = convert_to_mirror(self.length, vec)
        npt.assert_array_equal(test_dm, self.dm)

if __name__ == '__main__':
    main()

