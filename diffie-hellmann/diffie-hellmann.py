"""
This script demonstrates the Diffie-Hellmann private key exchange mechanism.
The Diffie-Hellmann key exchange is used to allow contracting parties use the same private key for decryption
without having to actually transfer the key over a network. VPNs are an example use case for Diffie Hellmann.
Definitions
- Prime Number: any number that can only be divided by itself and 1
- modulo: a modulo b is equal to the remainder when a is divided by b
- Primitive Root of a Prime number: a number that when multiplied to the power of
    every number between 1 and the Prime number, modulo P, is equal to a distinct number in that set
- **: Python exponential operator (ie. 2**4 means 2 to the power of 4 = 32)
- %: Python modulo operator (ie. 8%3 means 8 modulo 3 = 2

Experiment:

This is a toy function. Numbers this small would never be used in a real world situation.
To understand how larger numbers make encryption more robust, increase the value of the limit
variable and observe how it takes longer to generate the key.
"""
import random

# We use this limit as the maximum range from which we will obtain a prime number.
# Use of prime numbers is required, but we don't want use very large Primes
# as they consume large amounts of computing power
limit = 1000
print(f'Prime number limit is {limit}\n')


def is_prime(num):
    '''
    This method tests if a chosen number is a Prime number.
    Diffie-Hellman requires the use of Prime numbers.
    :param num:
    :return: True
    '''
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True


def primRoots(theNum):
    """
    The method obtains a list of primitive roots of a given Prime number.
    We require a primitive root to complete a Diffie-Hellmann exchange.
    :param theNum:
    :return: roots[]
    """
    o = 1
    roots = []
    r = 2
    while r < theNum:
        k = pow(r, o, theNum)
        while (k > 1):
            o = o + 1
            k = (k * r) % theNum
        if o == (theNum - 1):
            roots.append(r)
        o = 1
        r = r + 1
    return roots

# Obtain a list of Prime numbers that exist in range from 1 to limit
primes = list(filter(is_prime, range(1,limit)))


# Choose a single random number from the list of Prime numbers.
# This will be the modulo factor in the modulo equation used in Diffie-Hellmann
# This will be generated by one party in the exchange and sent to the other
common_prime=random.choice(primes)
print(f'Prime number selected by Alice as the Common Prime is {common_prime}\n')


# Choose the lowest value of the available primitive roots of the given modulo factor
# This will be generated by one party in the exchange and sent to the other
root=primRoots(common_prime)[0]
print(f'Alice computes {root} as the Primitive Root (generator) of {common_prime}\n')

print(f'The numbers {root} and {common_prime} are now shared over the network from Alice to Bob\n')

# This completes the framework in which we can build the exchange.
# We now introduce the contracting parties, Alice and Bob, who wish to share data over a network
# which can be encrypted and decrypted with the same private key.
#
# They require a way to calculate that private key without having to exchange it over a network
# Bob and Alice share the primitive root and modulo factor over the network.
# Neither of these can be used to decrypt data, so it is safe to do so.

# Alice choses a random secret number
alice_secret=random.choice(range(1,100))
print(f'Alice choses a random secret number of {alice_secret} which she does NOT share\n')

# Bob chooses a random secret number
bob_secret=random.choice(range(1,100))
print(f'Bob choses a random secret number of {bob_secret} which he does NOT share\n')

# Both parties now perform a calculation combining the primitive root, the modulo factor and their secret number
# Each produces a payload that they send to the other party.
alice_payload=(root**alice_secret)%common_prime
print(f'Alice creates a payload of {alice_payload} using her secret number, \
the generator and the Common Prime, and then sends this payload to Bob:\nalice_payload=(root**alice_secret)%common_prime\n')

bob_payload=(root**bob_secret)%common_prime
print(f'Bob creates a payload of {bob_payload} using his secret number, \
the generator and the Common Prime, and then sends this payload to Alice:\nbob_payload=(root**bob_secret)%common_prime\n')

# On receipt of the payload, each party now reverses the computation using their secret number
# This produces the common key
alice_key=(bob_payload**alice_secret)%common_prime
print(f'Alice uses Bob\'s payload to compute their shared private key:\n\
alice_key=(bob_payload**alice_secret)%common_prime = {alice_key}\n')

bob_key=(alice_payload**bob_secret)%common_prime
print(f'Bob uses Alices\'s payload to compute their shared private key:\n\
bob_key=(alice_payload**bob_secret)%common_prime = {bob_key}\n')

if alice_key == bob_key:
    key = alice_key
    print(f'key {key} is verified, and can be used by Alice and Bob to encrypt and decrypt data')
else:
    print(f'Something went wrong...')

