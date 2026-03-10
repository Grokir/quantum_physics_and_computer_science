import  numpy   as np
from    numpy   import ndarray
from    math    import sqrt


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


def Kronecker(lhs_matr: ndarray, rhs_matr: ndarray) -> ndarray:
    """Тензорное произведение (произведение Кронекера)"""
    return np.kron(lhs_matr, rhs_matr)


def Test1() -> bool:
    # Из-за того, что в теории к Лабораторной работе №2 
    # часть первой координаты на рисунке срезано, то
    # пришлось округлять до двух знаков
    
    np_ref:      ndarray = np.array([[-0.60], [0.80]])
    np_base_ket: ndarray = np.array([[0.989],[0.145]])
    np_res = np_X(np_Z(np_H(np_base_ket)))
    npf = (round(np_res[0][0], 2) == np_ref[0][0]) and (round(np_res[1][0], 2) == np_ref[1][0])

    return npf


def Test2() -> bool:
    # Из-за того, что в теории к Лабораторной работе №2 
    # часть первой координаты на рисунке срезано, то
    # пришлось округлять до двух знаков
    x: ndarray = np.array(
        [
            [0.0, 1.0], 
            [1.0, 0.0]
        ]
    )

    z: ndarray = np.array(
        [
            [1.0,  0.0], 
            [0.0, -1.0]
        ]
    )

    h: ndarray = np.array(
        [
            [1.0,  1.0], 
            [1.0, -1.0]
        ]
    )
    h *= pow(base=sqrt(2), exp=-1)

    U = x@z@h

    np_ref:      ndarray = np.array([[-0.60], [0.80]])
    np_base_ket: ndarray = np.array([[0.989],[0.145]])
    # np_res = np_X(np_Z(np_H(np_base_ket)))
    np_res = U@np_base_ket
    npf = (round(np_res[0][0], 2) == np_ref[0][0]) and (round(np_res[1][0], 2) == np_ref[1][0])

    return npf




def main():

    # res: bool = Test1()
    # print(f"\n\nNP TEST №1: round(XZH[[0.989],[0.145]])  == [[-0.60], [0.80]] : {res}\n\n")
    # res: bool = Test2()
    # print(f"\n\nNP TEST №2: round(XZH*[[0.989],[0.145]]) == [[-0.60], [0.80]] : {res}\n\n")
    # return

    # Матрица оператора NOT
    x: ndarray = np.array(
        [
            [0.0, 1.0], 
            [1.0, 0.0]
        ]
    )

    # Матрица оператора Z
    z: ndarray = np.array(
        [
            [1.0,  0.0], 
            [0.0, -1.0]
        ]
    )

    # Матрица оператора H
    h: ndarray = np.array(
        [
            [1.0,  1.0], 
            [1.0, -1.0]
        ]
    )
    h *= pow(base=sqrt(2), exp=-1)


    print("Задание 3")
    print("Часть 1: U1 = U2 = U")
    
    bz_ket_0: ndarray = np.array([[1.],[0.]])
    bz_ket_1: ndarray = np.array([[0.],[1.]])

    bz_ket_00: ndarray = Kronecker(bz_ket_0, bz_ket_0)
    bz_ket_01: ndarray = Kronecker(bz_ket_0, bz_ket_1)
    bz_ket_10: ndarray = Kronecker(bz_ket_1, bz_ket_0)
    bz_ket_11: ndarray = Kronecker(bz_ket_1, bz_ket_1)


    print("\n1. XZH = U")


    # Способ 1-й: "Влоб" или "почленно"
    # xzh_0: ndarray = np_X(np_Z(np_H(bz_ket_0)))
    # xzh_1: ndarray = np_X(np_Z(np_H(bz_ket_1)))
    # print(f"   XZH|00> :\n{Kronecker(xzh_0, xzh_0)}\n")
    # print(f"   XZH|01> :\n{Kronecker(xzh_0, xzh_1)}\n")
    # print(f"   XZH|10> :\n{Kronecker(xzh_1, xzh_0)}\n")
    # print(f"   XZH|11> :\n{Kronecker(xzh_1, xzh_1)}\n")

    # Способ 2-й: через матричное произв-ие Кронекера 
    U1 = x@z@h
    print(f"   (U1 ⊗ U2)|00> :\n{Kronecker(U1, U1)@bz_ket_00}\n")
    print(f"   (U1 ⊗ U2)|01> :\n{Kronecker(U1, U1)@bz_ket_01}\n")
    print(f"   (U1 ⊗ U2)|10> :\n{Kronecker(U1, U1)@bz_ket_10}\n")
    print(f"   (U1 ⊗ U2)|11> :\n{Kronecker(U1, U1)@bz_ket_11}\n")
    
    # добавим разделитель
    print(("-" * 35 + '\n'))


    print("\n2. HXZ = U")

    # Способ 1-й: "Влоб" или "почленно"
    # hxz_0: ndarray = np_H(np_X(np_Z(bz_ket_0)))
    # hxz_1: ndarray = np_H(np_X(np_Z(bz_ket_1)))
    # print(f"   HXZ|00> :\n{Kronecker(hxz_0, hxz_0)}\n")
    # print(f"   HXZ|01> :\n{Kronecker(hxz_0, hxz_1)}\n")
    # print(f"   HXZ|10> :\n{Kronecker(hxz_1, hxz_0)}\n")
    # print(f"   HXZ|11> :\n{Kronecker(hxz_1, hxz_1)}\n")

    # Способ 2-й: через матричное произв-ие Кронекера
    U2 = h@x@z
    print(f"   (U1 ⊗ U2)|00> :\n{Kronecker(U2, U2)@bz_ket_00}\n")
    print(f"   (U1 ⊗ U2)|01> :\n{Kronecker(U2, U2)@bz_ket_01}\n")
    print(f"   (U1 ⊗ U2)|10> :\n{Kronecker(U2, U2)@bz_ket_10}\n")
    print(f"   (U1 ⊗ U2)|11> :\n{Kronecker(U2, U2)@bz_ket_11}\n")


    print('\n', ('<' + "#" * 35 + '>'), '\n\n')

    print("Часть 2: U1 ≠ U2")
    print("   1. XZH = U1")
    print("   2. HXZ = U2\n")
    print(f"   (U1 ⊗ U2)|00> :\n{Kronecker(U2, U1)@bz_ket_00}\n")
    print(f"   (U1 ⊗ U2)|01> :\n{Kronecker(U2, U1)@bz_ket_01}\n")
    print(f"   (U1 ⊗ U2)|10> :\n{Kronecker(U2, U1)@bz_ket_10}\n")
    print(f"   (U1 ⊗ U2)|11> :\n{Kronecker(U2, U1)@bz_ket_11}\n")
    
    # добавим разделитель
    print(("-" * 35 + '\n'))
    
    print("   1. XZH = U2")
    print("   2. HXZ = U1\n")
    print(f"   (U1 ⊗ U2)|00> :\n{Kronecker(U2, U1)@bz_ket_00}\n")
    print(f"   (U1 ⊗ U2)|01> :\n{Kronecker(U2, U1)@bz_ket_01}\n")
    print(f"   (U1 ⊗ U2)|10> :\n{Kronecker(U2, U1)@bz_ket_10}\n")
    print(f"   (U1 ⊗ U2)|11> :\n{Kronecker(U2, U1)@bz_ket_11}\n")

if __name__ == "__main__":
    main()