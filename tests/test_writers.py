from unittest import TestCase

from matlabconverters.writers import *

class TestLoaders(TestCase):

    def test_mat_to_dir(self):
        flat_mat_to_dir("example_data/simple_mat.mat", out_prefix="example_writes/", show_debug=True, fmt="%.0f")
        assert(False)