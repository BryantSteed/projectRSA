import sys
from time import time


# You will need to implement this function and change the return value.
def mod_exp(x: int, y: int, N: int) -> int:
    return 0


def fermat(N: int, k: int) -> bool:
    """
    Returns True if N is prime
    """
    return False


def miller_rabin(N: int, k: int) -> bool:
    """
    Returns True if N is prime
    """
    return False


def generate_large_prime(n_bits: int) -> int:
    """Generate a random prime number with the specified bit length"""
    return 4  # https://xkcd.com/221/


def main(n_bits: int):
    start = time()
    large_prime = generate_large_prime(n_bits)
    print(large_prime)
    print(f'Generation took {time() - start} seconds')


if __name__ == '__main__':
    main(int(sys.argv[1]))
