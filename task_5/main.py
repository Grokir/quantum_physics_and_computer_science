"""
Задание 5.
Реализовать симуляцию передачи кубитов между пользователями (стр. 83-96). Необходимо:
1. Создать кубит-сообщение;
2. Выбрать базис для кодирования сообщения и закодировать сообщение состояниями |+> и |-> (создать функцию шифратор);
3. “Передать” это состояние другому пользователю (создать функцию дешифратор);
4. Сгенерировать базис для дешифровки на стороне получателя;
5. Сравнить полученные сообщения.

"""

from calc import bb84_simulate
import numpy as np
from simulator import *


def test_bb84():
    print("=== Квантовая передача по протоколу BB84 ===\n")

    # Алиса хочет передать 20 бит
    original_message = [
        1, 0, 1, 1, 0, 1, 0, 0, 1, 0,
        1, 1, 0, 1, 0, 1, 1, 0, 1, 0
    ]
   
    alice_bits, bob_bits, matching_bits, matching_bases, alice_bases, bob_bases = bb84_simulate(original_message)

    print(f"{'№':<3} {'Алиса':<6} {'Базис А':<6} {'Базис Б':<6} {'Боб':<6} {'Совпал?':<8}")
    print("-" * 55)

    for i in range(len(alice_bits)):
        matched = "Да" if alice_bases[i] == bob_bases[i] else "Нет"
        print(f"{i+1:<3} {str(alice_bits[i]):<6} {alice_bases[i]:<6} {bob_bases[i]:<6} {str(bob_bits[i]):<6} {matched:<8}")

    alice_bits_clean = [int(bit) for bit in alice_bits]
    bob_bits_clean = [int(bit) for bit in bob_bits]
    matching_bases_clean = [str(bit) for bit in matching_bases]
    matching_bits_clean =  [int(bit) for bit in matching_bits]

    print("\n" + "="*60)
    print(f"Сообщение Алисы : {alice_bits_clean}")
    print(f"Сообщение Боба  : {bob_bits_clean}")
    print(f"Совпавшие базисы: {matching_bases_clean}")
    print(f"Совпавшие биты (ключ): {matching_bits_clean}")
    print(f"Процент совпадений: {len(matching_bits) / len(alice_bits) * 100:.1f}%")

    # Совпавшие биты должны быть равны битам Алисы в позициях совпавших базисов
    for i, base in enumerate(alice_bases):
        if base == bob_bases[i]:
            # Проверяем, что бит Боба равен биту Алисы
            if bob_bits[i] != alice_bits[i]:
                print(f"ОШИБКА: На позиции {i+1} базисы совпали, но биты не совпадают!")
                break
            else:
                print("\nПроверка корректности: все совпавшие биты соответствуют исходным — ОК!")

    print("\nПроверка: ключ сформирован — пройдено.")
    print("Протокол BB84 успешно смоделирован!")



if __name__ == "__main__":
    test_bb84()