from simulator  import *
from qrng       import *


def generate_random_bits(n: int, device: QuantumDevice) -> list[int]:
    """Генерирует n случайных битов."""
    return [int(qrng(device)) for _ in range(n)]


def main():
    print("[QRNG - Квантовый Генератор Случайных Чисел]")
    
    device = SimulatedQuantumDevice()
    
    num_bits = int(input("\nВведите число битов для генерации > "))
    random_bits = generate_random_bits(num_bits, device)
    
    print(f"\n[Сгенерированные биты]")
    print(''.join(map(str, random_bits)))
    
    # Статистика
    zeros = random_bits.count(0)
    ones = random_bits.count(1)
    
    print(f"\n[Статистика]")
    print(f"  Нулей  (|0⟩): {zeros} ({zeros/num_bits*100:.1f}%)")
    print(f"  Единиц (|1⟩): {ones} ({ones/num_bits*100:.1f}%)")
    
    # Проверка качества генератора
    print(f"\n[Проверка работы генератора]")
    print(f"  Баланс 0/1: {"GOOD" if 40 <= zeros/num_bits*100 <= 60 else "BAD"}")



if __name__ == "__main__":
    main()
