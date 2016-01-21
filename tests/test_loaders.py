from unittest import TestCase

from matlabconverters.loaders import *

class TestLoaders(TestCase):

    def test_verify_flat_mat(self):
        assert(verify_flat_mat("example_data/simple_mat.mat", show_debug=True) == True)

