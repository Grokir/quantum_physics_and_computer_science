import  numpy       as np
from    numpy       import ndarray

from qrng      import *
from interface import *
from simulator import *

KET_0: ndarray = np.array([
    [1],
    [0]
], dtype=complex)

KET_1: ndarray = np.array([
    [0],
    [1]
], dtype=complex)

KET_PLUS:  ndarray = (KET_0 + KET_1) / np.sqrt(2)   # |+⟩
KET_MINUS: ndarray = (KET_0 - KET_1) / np.sqrt(2)  # |−⟩

H: ndarray = np.array(
    [
        [1,  1],
        [1, -1]
    ],
    dtype=complex) / np.sqrt(2)

X: ndarray = np.array(
        [
            [0.0, 1.0], 
            [1.0, 0.0]
        ],
    dtype=complex)

Z: ndarray = np.array(
        [
            [1.0,  0.0], 
            [0.0, -1.0]
        ],
    dtype=complex)


class SimulatedQubit(Qubit):
    def __init__(self):
        self.reset()

    def h(self):
        self.state = H @ self.state

    def measure(self) -> bool:
        # Вероятность получить |0⟩
        pr0 = np.abs(self.state[0, 0]) ** 2
        # Генерируем случайное число и сравниваем с вероятностью
        sample = np.random.random() <= pr0
        return bool(0 if sample else 1)

    def reset(self):
        self.state = KET_0.copy()

    
    def encode_bit(self, bit: bool, basis: str):
        """
        Кодирует бит в заданном базисе.
        basis: 'Z' → использует |0⟩/|1⟩
               'X' → использует |+⟩/|−⟩
        """
        self.reset()  # начинаем с |0⟩
        if bit:
            # Если бит = 1, нужно получить |1⟩ или |−⟩
            if basis == 'Z':
                self.state = KET_1.copy()
            elif basis == 'X':
                self.h()  # |0⟩ → |+⟩
                self.state = KET_MINUS.copy()
                self.state = KET_1.copy()
                self.h()
            else:
                raise ValueError("Basis must be 'Z' or 'X'")
        else:
            # bit = 0
            if basis == 'Z':
                pass  # уже |0⟩
            elif basis == 'X':
                self.h()  # |0⟩ → |+⟩
            else:
                raise ValueError("Basis must be 'Z' or 'X'")
            
    def decode_bit(self, basis: str) -> bool:
        """
        <measure_in_basis>
        Измеряет в заданном базисе.
        Если basis='X', то сначала применяем H, потом измеряем в Z-базисе.
        """
        if basis == 'Z':
            return self.measure()
        elif basis == 'X':
            self.h()  # переводим в Z-базис
            result = self.measure()
            self.h()  # возвращаем обратно (для корректности состояния, хотя в симуляции не обязательно)
            return result
        else:
            raise ValueError("Basis must be 'Z' or 'X'")


class SimulatedQuantumDevice(QuantumDevice):
    def __init__(self):
        self._qubits: list[SimulatedQubit] = []

    def allocate_qubit(self) -> SimulatedQubit:
        qubit = SimulatedQubit()
        self._qubits.append(qubit)
        return qubit

    def deallocate_qubit(self, qubit: SimulatedQubit):
        if qubit in self._qubits:
            self._qubits.remove(qubit)

