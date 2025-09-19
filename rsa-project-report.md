# Project Report - RSA and Primality Tests

## Baseline

### Design Experience

Summary: For the mathematical functions of RSA, my design is to implement ModExp based on the psuedocode found in the textbook. With the fermat primality testing, I will use the Fermat's little theorem psuedocode but only try values of a up to some integer k. This will of course be implemented by calling modexp. For prime number generation, I will simply generate a ranodm number within the specific bit range using pythons built in random library. Then, I will test those random number on the primality test until I find one that is prime.

### Theoretical Analysis - Prime Number Generation

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data

| N    | time (ms) |
|------|-----------|
| 64   |           |
| 128  |           |
| 256  |           |
| 512  |           |
| 1024 |           |
| 2048 |           |

### Comparison of Theoretical and Empirical Results

- Theoretical order of growth: *copy from section above* 
- Measured constant of proportionality for theoretical order: 
- Empirical order of growth (if different from theoretical): 
- Measured constant of proportionality for empirical order: 

![img](img.png)

*Fill me in*

## Core

### Design Experience

Summary: To implement the extended euclids algorithm, I will simply implant the psuedocode into real code. However, I will also make heavy use of my modexp function.

For public and private key generation I will to the following in order:
1. Generate the random prime numbers p and q with my random_prime function.
2. calculate N = p * q
3. calculate phi = (p-1)(q-1). (I've heard this be called Euler's Phi so I use that name)
4. calculate e by iterating through the list of primes and taking extended_euclid(phi, e). If if the GCD part of the return tuple returns a 1, then this e will be the true e, and d, which is the private key, will be set = b from the return tuple. Such that de = 1 (mod phi)
5. return N, e (public), and d (private)

### Theoretical Analysis - Key Pair Generation

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data

| N    | time (ms) |
|------|-----------|
| 64   |           |
| 128  |           |
| 256  |           |
| 512  |           |
| 1024 |           |
| 2048 |           |

### Comparison of Theoretical and Empirical Results

- Theoretical order of growth: *copy from section above* 
- Measured constant of proportionality for theoretical order: 
- Empirical order of growth (if different from theoretical): 
- Measured constant of proportionality for empirical order: 

![img](img.png)

*Fill me in*

## Stretch 1

### Design Experience

Summary: I will use the generate key pair function developed previously to generate the pair.

To encrypt a message, the simple formula of message^e mod N = y encrypted message. And to decrypt a message use y^d mod N.

To do my theoretical analysis. I will simply analyze each function and give my best theoretical calculation of the time complexity.

For the emperical analysis, I will track the time using python's time library. I will use matplotlib to display the data and see if I can predict the order of growth f(x). I may do this for several orders of growth. After that, I will calcualte the constant of proportionality by simply diving the emperical value / function value. I will sum these constants and average them to get a constant of proportionality just as is shown in the instructions.

### Theoretical Analysis - Encrypt and Decrypt

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data

#### Encryption

| N    | time (ms) |
|------|-----------|
| 64   |           |
| 128  |           |
| 256  |           |
| 512  |           |
| 1024 |           |
| 2048 |           |

#### Decryption

| N    | time (ms) |
|------|-----------|
| 64   |           |
| 128  |           |
| 256  |           |
| 512  |           |
| 1024 |           |
| 2048 |           |

### Comparison of Theoretical and Empirical Results

#### Encryption

- Theoretical order of growth: *copy from section above* 
- Measured constant of proportionality for theoretical order: 
- Empirical order of growth (if different from theoretical): 
- Measured constant of proportionality for empirical order: 

![img](img.png)

*Fill me in*

#### Decryption

- Theoretical order of growth: *copy from section above* 
- Measured constant of proportionality for theoretical order: 
- Empirical order of growth (if different from theoretical): 
- Measured constant of proportionality for empirical order: 

![img](img.png)

*Fill me in*

### Encrypting and Decrypting With A Classmate

*Fill me in*

## Stretch 2

### Design Experience

Summary: I will implement the Miller-Rabin test by simply taking the number N in question and performing the test k times for a randomly generated a such that 1 < a < N. If the test fails for any value of a, it will return false, but if it passes for all k values of a, it will return true.

1. The test will take a^N-1 mod N, if it's not 1 or N-1, it returns false
2. The test will do a secuence of square roots on a^N-1, which really is just a^ (N-1) / 2 and perform step 1 again
3. Do the test for k random values of a, if it passed all a values, then return treu

### Discussion: Probabilistic Natures of Fermat and Miller Rabin 

*Fill me in*

## Project Review

*Fill me in*

