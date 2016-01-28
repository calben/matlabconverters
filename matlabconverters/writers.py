import numpy as np
import pandas as pd
import os

from matlabconverters.loaders import load_mat, strip_mat_metadata


def flat_mat_to_dir(mat : str, out_prefix = "", show_debug = False, fmt="%.2f") -> bool:
    data = load_mat(mat, show_debug)
    if out_prefix[-1] == "/":
        if not os.path.exists(out_prefix):
            os.makedirs(out_prefix)
    for k, v in data.items():
        if "__" not in k:
            np.savetxt(out_prefix + k + ".csv", v, delimiter=",", fmt=fmt)

def hierarchical_mat_to_dir(mat: str, out_prefix = "", show_debug = False, fmt="%.2f") -> bool:
    data = strip_mat_metadata(load_mat(mat, show_debug))
    if not out_prefix == "":
        if out_prefix[-1] == "/":
            if not os.path.exists(out_prefix):
                os.makedirs(out_prefix)
    for k, v in data.items():
        df = pd.DataFrame(v)
        df.to_csv(out_prefix + k + ".csv")
