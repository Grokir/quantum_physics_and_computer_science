import  numpy       as np
from    numpy       import ndarray
from    interface   import Qubit, QuantumDevice

KET_0: ndarray = np.array([
    [1],
    [0]
], dtype=complex)

H: ndarray = np.array(
    [
        [1,  1],
        [1, -1]
    ],
    dtype=complex) / np.sqrt(2)


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

