from prime_number_generation import miller_rabin, fermat

def fermat_rabin_failure_rates():
    """Compare the failure rates of Fermat and Miller-Rabin tests on Carmichael numbers."""
    carmichael_num = 561
    k = 20  # Number of iterations for the tests
    fermat_successes = 0
    while True:
        if not fermat(carmichael_num, k):
            fermat_successes += 1
        else:
            break

    print(f'Fermat successes: {fermat_successes}/{fermat_successes + 1}')

    miller_rabin_successes = 0
    while True:
        if not miller_rabin(carmichael_num, k):
            miller_rabin_successes += 1
        else:
            break
    print(f'Miller-Rabin successes: {miller_rabin_successes}/{miller_rabin_successes + 1}')

if __name__ == '__main__':
    fermat_rabin_failure_rates()