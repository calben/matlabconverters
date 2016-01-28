import numpy as np
import pandas as pd

from scipy.io import loadmat


def load_mat(mat : str, show_debug = False) -> {}:
    data = loadmat(mat)
    if(show_debug):
        print("Mat has " + str(len(data.keys())) + " keys.")
        if verify_flat_mat(data):
            print("Mat is flat.")
        else:
            print("Mat is not flat.")
    return data


def verify_flat_mat(data : {}, show_debug = False) -> bool:
    try:
        for k, v in data.items():
            if "__" not in k:
                if not (isinstance(v, (np.ndarray, np.generic))):
                    return False
        return True
    except Exception as e:
        print(e)
        return False


def strip_mat_metadata(mat : {}, show_debug = False) -> {}:
    result = {}
    for k, v in mat.items():
        if "__" not in k:
            if (isinstance(v, (np.ndarray, np.generic))):
                result[k] = v
    if(show_debug):
        print("Keys := " + str(result.keys()))
    return result

def load_mat_to_pandas(mat : str, show_debug = False) -> pd.DataFrame :
    return pd.DataFrame(strip_mat_metadata(load_mat(mat, show_debug)))


