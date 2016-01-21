import numpy as np

from scipy.io import loadmat


def load_mat(mat : str, show_debug = True) -> {}:
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




