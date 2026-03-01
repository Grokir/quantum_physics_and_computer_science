import numpy as np
import qutip as qt
from qutip  import Qobj
from numpy  import ndarray
from math   import sqrt


# Оператор NOT
def np_X(vec: ndarray = np.array([])) -> ndarray:
    x: ndarray = np.array(
        [
            [0.0, 1.0], 
            [1.0, 0.0]
        ]
    )

    if len(vec) == 0:
        return x@x
    
    return x@vec

# Оператор Z
def np_Z(vec: ndarray = np.array([])) -> ndarray:
    z: ndarray = np.array(
        [
            [1.0,  0.0], 
            [0.0, -1.0]
        ]
    )

    if len(vec) == 0:
        return z@z
    
    return z@vec

# Оператор Адамара (H)
def np_H(vec: ndarray = np.array([])) -> ndarray:
    h: ndarray = np.array(
        [
            [1.0,  1.0], 
            [1.0, -1.0]
        ]
    )
    h *= pow(base=sqrt(2), exp=-1)
    if len(vec) == 0:
        return h@h
    
    return h@vec


###########################################

# Оператор NOT
def qt_X(vec: Qobj = Qobj(), square: bool = False) -> Qobj:

    x: Qobj = qt.sigmax()

    if square:
        return x*x
    
    return x*vec

# Оператор Z
def qt_Z(vec: Qobj = Qobj(), square: bool = False) -> Qobj:
    z: Qobj = qt.sigmaz()

    if square:
        return z*z
    
    return z*vec

# Оператор Адамара (H)
def qt_H(vec: Qobj = Qobj(), square: bool = False) -> Qobj:
    h: Qobj = Qobj(
        [
            [1.0,  1.0], 
            [1.0, -1.0]
        ]
    )
    h *= pow(base=sqrt(2), exp=-1)
    if square:
        return h*h
    
    return h*vec


def main():
    print("Задание 1\n")
    print("[Часть 1] : numpy")
    np_base_ket:      ndarray = np.array([[0.],[1.]])
    np_res1:   ndarray = np_X(np_base_ket)
    np_res2:   ndarray = np_Z(np_base_ket)
    np_res3:   ndarray = np_H(np_base_ket)
    print(f"base_ket:  \n{np_base_ket}\n")
    print(f"X*base_ket:\n{np_res1}\n")
    print(f"Z*base_ket:\n{np_res2}\n")
    print(f"H*base_ket:\n{np_res3}\n")

    # добавим разделитель
    print(("=" * 70 + '\n'))

    print("[Часть 2] : qutip")
    qt_base_ket: Qobj = qt.ket('1') # ket-vector{0, 1}
    qt_res1 = qt_X(qt_base_ket)
    qt_res2 = qt_Z(qt_base_ket)
    qt_res3 = qt_H(qt_base_ket)
    print(f"base_ket:  \n{qt_base_ket}\n")
    print(f"X*base_ket:\n{qt_res1}\n")
    print(f"Z*base_ket:\n{qt_res2}\n")
    print(f"H*base_ket:\n{qt_res3}\n")

if __name__ == "__main__":
    main()