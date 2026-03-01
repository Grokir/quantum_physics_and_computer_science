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


def Test() -> tuple[bool, bool]:
    # Из-за того, что в теории к Лабораторной работе №2 
    # часть первой координаты на рисунке срезано, то
    # пришлось округлять до двух знаков
    
    np_ref: ndarray = np.array([[-0.60], [0.80]])
    qt_ref: Qobj    = Qobj([[-0.60], [0.80]])

    np_base_ket:    ndarray = np.array([[0.989],[0.145]])
    qt_base_ket:    Qobj    = Qobj([[0.989],[0.145]]) # ket-vector{0, 1}

    np_res = np_X(np_Z(np_H(np_base_ket)))
    qt_res = qt_X(qt_Z(qt_H(qt_base_ket)))

    qtf = (round(float(qt_res[0][0]), 2) == qt_ref[0][0]) and (round(float(qt_res[1][0]), 2) == qt_ref[1][0])
    npf = (round(np_res[0][0], 2) == np_ref[0][0]) and (round(np_res[1][0], 2) == np_ref[1][0])

    return npf, qtf

    


def main():

    # res: tuple[bool, bool] = Test()
    # print(f"\n\nNP res: {res[0]} | QT res: {res[1]}\n\n")
    # return


    print("Задание 2\n")
    print("[Часть 1] : numpy")
    np_base_ket:      ndarray = np.array([[0.],[1.]])
    np_res1:        ndarray = np_Z(np_X(np_base_ket))
    np_res2:        ndarray = np_H(np_X(np_base_ket))
    np_res3:        ndarray = np_X(np_Z(np_H(np_base_ket)))
    np_res4:        ndarray = np_H(np_Z(np_Z(np_X(np_base_ket))))
    np_res5:        ndarray = np_Z(np_Z(np_H(np_H(np_base_ket))))
    np_res6:        ndarray = np_X(np_X(np_X(np_base_ket)))
    print(f"[0] base_ket:  \n{np_base_ket}\n")
    print(f"[1] |ψ'> = Z*X*|ψ>:  \n{np_res1}\n")
    print(f"[2] |ψ'> = H*X*|ψ>:\n{np_res2}\n")
    print(f"[3] |ψ'> = X*Z*H*|ψ>:\n{np_res3}\n")
    print(f"[4] |ψ'> = H*Z*Z*X|ψ>:\n{np_res4}\n")
    print(f"[5] |ψ'> = Z*Z*H*H|ψ>:\n{np_res5}\n")
    print(f"[6] |ψ'> = X*X*X|ψ>:\n{np_res6}\n")

    # добавим разделитель
    print(("=" * 70 + '\n'))

    print("[Часть 2] : qutip")
    qt_base_ket:    Qobj = qt.ket('1') # ket-vector{0, 1}
    qt_res1:        Qobj = qt_Z(qt_X(qt_base_ket))
    qt_res2:        Qobj = qt_H(qt_X(qt_base_ket))
    qt_res3:        Qobj = qt_X(qt_Z(qt_H(qt_base_ket)))
    qt_res4:        Qobj = qt_H(qt_Z(qt_Z(qt_X(qt_base_ket))))
    qt_res5:        Qobj = qt_Z(qt_Z(qt_H(qt_H(qt_base_ket))))
    qt_res6:        Qobj = qt_X(qt_X(qt_X(qt_base_ket)))
    print(f"[0] base_ket:  \n{qt_base_ket}\n")
    print(f"[1] |ψ'> = Z*X*|ψ>:  \n{qt_res1}\n")
    print(f"[2] |ψ'> = H*X*|ψ>:\n{qt_res2}\n")
    print(f"[3] |ψ'> = X*Z*H*|ψ>:\n{qt_res3}\n")
    print(f"[4] |ψ'> = H*Z*Z*X|ψ>:\n{qt_res4}\n")
    print(f"[5] |ψ'> = Z*Z*H*H|ψ>:\n{qt_res5}\n")
    print(f"[6] |ψ'> = X*X*X|ψ>:\n{qt_res6}\n")


if __name__ == "__main__":
    main()