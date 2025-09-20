import sys
import random
from time import time


# You will need to implement this function and change the return value.
def mod_exp(x: int, y: int, N: int) -> int:
    if y == 0:
        return 1
    z = mod_exp(x, y // 2, N)
    y_is_even = y % 2 == 0
    if y_is_even:
        return (z * z) % N
    return (x * z * z) % N



def fermat(N: int, k: int) -> bool:
    """
    Returns True if N is prime
    """
    assert N > 2
    for i in range(k):
        a = random.randint(2, N-1)
        result = mod_exp(a, N-1, N)
        if result != 1:
            return False
    return True


def miller_rabin(N: int, k: int) -> bool:
    """
    Returns True if N is prime
    """
    return False


def generate_large_prime(n_bits: int) -> int:
    """Generate a random prime number with the specified bit length"""
    # https://xkcd.com/221/
    while True:
        prospect = random.getrandbits(n_bits)
        if fermat(prospect, 20):
            return prospect


def main(n_bits: int):
    start = time()
    large_prime = generate_large_prime(n_bits)
    print(large_prime)
    print(f'Generation took {time() - start} seconds')


if __name__ == '__main__':
    main(int(sys.argv[1]))
