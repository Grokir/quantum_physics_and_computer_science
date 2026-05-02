import numpy as np
from simulator  import *
from qrng       import *

def bb84_simulate(original_message):
    alice_bits = original_message
    alice_bases = [np.random.choice(['Z', 'X']) for _ in alice_bits]
    bob_bases = [np.random.choice(['Z', 'X']) for _ in alice_bits]
    bob_bits = []

    for i in range(len(alice_bits)):
        if alice_bases[i] == bob_bases[i]:
            # Совпадение базисов — бит передаётся точно
            bob_bits.append(alice_bits[i])
        else:
            # Разные базисы — 50% шанс ошибки
            bob_bits.append(np.random.choice([0, 1]))

    # Находим совпавшие базисы и соответствующие биты
    matching_bases = []
    matching_bits = []
    for i in range(len(alice_bases)):
        if alice_bases[i] == bob_bases[i]:
            matching_bases.append(alice_bases[i])
            matching_bits.append(alice_bits[i])  # Алиса — источник истины

    return alice_bits, bob_bits, matching_bits, matching_bases, alice_bases, bob_bases
