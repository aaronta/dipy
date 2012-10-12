from dipy.core.ndindex import ndindex

import numpy as np
from numpy.testing import assert_array_equal

def test_ndindex():
    x = list(ndindex(1, 2, 3))
    expected = [ix for ix, e in np.ndenumerate(np.zeros((1, 2, 3)))]
    assert_array_equal(x, expected)
