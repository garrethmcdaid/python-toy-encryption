'''
This script demonstrates RSA Public Private Key Encryption
RSA is an improvement on Diffie-Hellmann in that contracting parties do not need to be known
to each other. For instance, RSA is used when a web browser communicates with a web server.
Definitions
- Prime Number: any number that can only be divided by itself and 1
- modulo: a modulo b is equal to the remainder when a is divided by b
- Primitive Root of a Prime number: a number that when multiplied to the power of
    every number between 1 and the Prime number, modulo P, is equal to a distinct number in that set
- **: Python exponential operator (ie. 2**4 means 2 to the power of 4 = 32)
- %: Python modulo operator (ie. 8%3 means 8 modulo 3 = 2
'''

import random
# GCD means Greatest Common Denominator
from math import gcd


# Utility functions#
####################

# https://stackoverflow.com/questions/48733714/smallest-coprime
def check_co_prime(num, M):
    '''
    Check if 2 numbers are coprime
    - ie they have no common factor that is greater than one
    - eg 14 and 15 are coprime, even though 14 is not a Prime number
    '''
    return gcd(num, M) == 1

# https://stackoverflow.com/questions/48733714/smallest-coprime
def get_smallest_co_prime(M):
    '''
    Find the smallest coprime number for another number
    - You have to start at 2 because -1 and 1 are coprime to every other number
    '''
    for i in range(2, M): # for every number *i* starting from 2 up to M
        if check_co_prime(i, M): # check if *i* is coprime with M
            return i # if it is, return i as the result


def is_prime(num):
    '''
    This method tests if a chosen number is a Prime number.
    RSA requires the use of Prime numbers.
    '''
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True


# https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    '''
    Python implementation of extended Euclidean algorithm
    - required to calculate modular inverse
    '''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


# https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def modinv(a, m):
    '''
    Wrapper for egdc() to calculate modular inverse and find where it does not exist
    '''
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# Place a limit on the number of Primes we will consider
# in calculation to ensure we do not overburden the CPU
limit = 100

# Obtain a list of Prime numbers that exist in range from 7 to limit
# We chose 7 because RSA does not work with Primes below 7
primes = list(filter(is_prime, range(7,limit)))

# Step 1
# RSA starts with the selection of 2 Prime numbers
p1 = random.choice(primes)
p2 = random.choice(primes)

# We ensure that the 2 Prime numbers are not the same
while p2 == p1:
    p2 = random.choice(primes)

# Use this if you want to test with specific Primes
# Uncomment the lines above
# p1 = 7
# p2 = 11

print(f'prime1: {p1} prime2: {p2}')

# Step 2
# Multiply the 2 Prime numbers
factorOfPrimes = p1*p2

print(f'factorOfPrimes: {factorOfPrimes}')


# Step 3
# Find the PHI of the factor of the Primes
# This is the essential part of RSA. Only one party knows this value
phiOfFactorOfPrimes = (p1 - 1)*(p2 - 1)

print(f'phiOfFactorOfPrimes: {phiOfFactorOfPrimes}')

# Step 4
# Get a small exponent (to the power of) of the PHI value of the factor of Primes
# This value needs to be coprime with the PHI value of the factor of Primes
pubExp = get_smallest_co_prime(phiOfFactorOfPrimes)

print(f'pubExp: {pubExp}')

# We know have our Public Key, which is the exponent and the factor of Primes
# Note that the PHI value of the factor of Primes is NOT exposed
print(f'Public Key: ({pubExp}, {factorOfPrimes})')

# Step 5
# The Private Key is the modular inverse of the exponent and the PHI value of the factor of Primes
# See the README for a more detailed explanation
priKey = modinv(pubExp, phiOfFactorOfPrimes)

print(f'Private Key: {priKey}')

# We now have what we need for the parties to exchange secure information

# Bob want to encrypt a message (we use a number for the message) and send it to Alice
# Alice sends Bob her Public Key (pubExp and factorOfPrimes)
# Bob performs calculation 75**pubExp%phiOfFactorOfPrimes
# This is the encrypted payload he sends to Alice

message = random.choice(range(1,10))
print(f'message: {message}')

# This is the encrypted message Bob sends to Alice
encrypted_message = message**pubExp%factorOfPrimes

print(f'encrypted_message: {encrypted_message}')

# Alice can now decrypt the message with her Private Key
decrypted_message = encrypted_message**priKey%factorOfPrimes

print(f'decrypted_message: {decrypted_message}')



