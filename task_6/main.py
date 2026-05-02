from calc import bb84_simulate
import random


def apply_one_time_pad(message_bits: list, key_bits: list) -> list:
    """Побитовое XOR сообщения и ключа (шифрование/дешифрование)."""
    return [m ^ k for m, k in zip(message_bits, key_bits)]

def message_to_bits(text: str) -> list:
    """Преобразует строку в список битов (8-битная кодировка utf-8)."""
    result = []
    for byte in text.encode('utf-8'):
        for i in range(8):
            result.append(bool((byte >> (7 - i)) & 1))
    return result

def bits_to_message(bits: list) -> str:
    """Восстанавливает строку из списка битов (8 бит на символ)."""
    bytes_list = []
    for i in range(0, len(bits), 8):
        byte_val = 0
        for bit in bits[i:i+8]:
            byte_val = (byte_val << 1) | int(bit)
        bytes_list.append(byte_val)
    return bytes(bytes_list).decode('utf-8')

def main():
    # 1. Генерация ключа (BB84)
    alice_message = "Hello, world! This is lab. work No.6!"
    alice_message_bits = message_to_bits(alice_message)
    required_key_len = len(alice_message_bits)

     # Вероятность совпадения базисов ~0.5, поэтому передаём вдвое больше битов.
    initial_key_len = required_key_len * 3
    alice_initial_key = [random.randint(0, 1) for _ in range(initial_key_len)]

    # 2. Симуляция BB84 – передача начального ключа от Алисы к Бобу.
    (alice_bits, bob_bits, matching_bits, 
     matching_bases, alice_bases, bob_bases) = bb84_simulate(alice_initial_key)

    # 3. Общий ключ – это биты на совпавших базисах (matching_bits).
    #    Алиса может получить те же биты, отфильтровав свои исходные биты по совпавшим позициям.
    alice_key = [alice_bits[i] for i in range(len(alice_bits)) if alice_bases[i] == bob_bases[i]]
    bob_key = matching_bits

    # Проверка, что ключи совпадают и имеют достаточную длину.
    assert alice_key == bob_key, "Ошибка: ключи не совпадают!"
    # Берем первые required_key_len битов общего ключа.
    if len(alice_key) < required_key_len:
        print("Предупреждение: длина ключа меньше необходимой. Повторите с большим initial_key_len.")
        exit(1)
    alice_key = alice_key[:required_key_len]
    bob_key = bob_key[:required_key_len]

    # 4. Алиса шифрует сообщение полученным ключом и отправляет шифротекст.
    encrypted = apply_one_time_pad(alice_message_bits, alice_key)
    print("Зашифрованное сообщение (первые 20 бит):", encrypted[:20])

    # 5. Боб получает шифротекст и расшифровывает своим ключом.
    decrypted_bits = apply_one_time_pad(encrypted, bob_key)
    decrypted_text = bits_to_message(decrypted_bits)

    # 6. Сравнение исходного и расшифрованного сообщений.
    print("Исходное сообщение:    ", alice_message)
    print("Расшифрованное сообщение:", decrypted_text)
    assert alice_message == decrypted_text, "Ошибка: сообщения не совпадают!"
    print("Протокол BB84 успешно завершён. Сообщение передано без ошибок.")

if __name__ == "__main__":
    main()