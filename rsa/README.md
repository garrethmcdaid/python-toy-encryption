# RSA Public Private Key Encryption

## Introduction

The Diffie-Hellmann key exchange was a major breakthrough in cryptography. Where previously Alice and Bob would have had
exchange a private key to encrypt the data sent between them, now they had a mechanism to establish a private key without
have to transmit any secure information.

However, Diffie-Hellmann was still limited in that communication between Alice and Bob had to be planned. They would have 
to decide in advance that they were going to communicate securely. If Bob was unknown to Alice, or they had no way of preparing
communication between them, Diffie-Hellmann was of limited use to them.

This is the problem that RSA Public Private Key encryption solves. It allows Bob, or Charlie, or Dave, or Eve, or anyone
to communicate with Alice even if they've never communicated with Alice before, and in a way that doesn't require Alice to
complete a key exchange with any or all of them.

Practical examples are as follows: 

Alice and Bob want to set up a VPN. For this, Diffie-Hellmann is fine, as setting up a 
VPN is generally a deliberate planned project between two parties who know each other, and only those two parties will use
the VPN.

Alice wants to set up a web server, and let Bob, or anyone else login to it with a username and password. For this, Alice needs 
to publish a mechanism that allows people to send her their private data securely. For this, she will use RSA Public Private Key Encryption.

## The math

### Multiplication versus Prime Factorization

Multiplication as a concept shouldn't require explanation. In terms of cryptography, the important thing to note about multiplication
is that computers can multiple large numbers very quickly, because the formula for multiplication is known and predictable. 

Prime Factorization is a less familiar concept. This is where a number is broken down into the Prime numbers that create it.

For instance the Prime Factorisation of 21 is:

<code>2<sup>4</sup> + 5</code>


Computers struggle with Prime Factorisation, because there is no formula to extract it. It involves trial and error. It therefore
takes a computer a lot longer to obtain the Prime Factorization of a number than to multiply two numbers

We will understand the significance of this later.

### The factor of Primes

The math involved in RSA Public Private Key encryption (hereafter referred to as RSA) is more complex than for the Diffie-Hellmann Private Key exchange, 
but both have common features, primarily Prime numbers and the modulo function.

A Prime number is a number than can only be divided by 1 and itself. eg `3, 7, 11 or 29`. Prime numbers are the building blocks 
of all non-Prime (composite) numbers. They feature regularly in cryptography because they are rigid. For instance, the only 
way to derive the Prime 7 is `1x7`, whereas you can derive the non-Prime 16 with `1x16, 2x8 or 4x4`.

The modulo function is as follows. The modulo of *a* and *b* is equal to the remainder when you divide *a* by *b*, e.g.
```markdown
16(mod 7) = 2
```


The objective of RSA is for Alice to develop a *lock* for which only she holds the *key*. She can then publish copies of that 
lock ( minus the key ) and allow others, ie Bob, to lock their data with that lock and send to her. She can then unlock it, as 
she has a key ( and the only key ) that fits any copy of the lock.

Alice starts by creating her lock. For this she choses 2 Prime numbers (we'll use small ones here, but in the real world they would be very large).

```markdown
p1=7
p2=11
```

She nows multiplies them, and obtains value referred to as the factor of Primes (*F*):
```bash
p1 x p2 = F

7 x 11 = 77
```
The factor of Primes (*F*) is 77.

### PHI

At this point, we introduce a new mathematical formula which you probably won't have heard of before, which is known as *PHI*.

For any given number, the PHI value of that number is the number of numbers between 1 and that number where 1 is the largest 
common factor shared between both numbers.

Huh?

Here's an example. Let's get the PHI value of 9. The numbers between 1 and 9 are:
```markdown
1 2 3 4 5 6 7 8
```

Let's check how many have a common factor with 9:
```bash
1 has no common factor with 9 other than 1, so count that
2 has no common factor with 9 other than 1, so count that
3 has a common factor with 9 which is 3, so don't count that
4 has no common factor with 9 other than 1, so count that
5 has no common factor with 9 other than 1, so count that
6 has a common factor with 9 which is 3, so don't count that
7 has no common factor with 9 other than 1, so count that
8 has no common factor with 9 other than 1, so count that
```

So PHI(9) = 6

Now, let's do the same thing for a Prime number, 5:
```bash
1 has no common factor with 5 other than 1, so count that
2 has no common factor with 5 other than 1, so count that
3 has no common factor with 5 other than 1, so count that
4 has no common factor with 5 other than 1, so count that
```

So PHI(5) = 4

If you try this again with any other *Prime* number, no matter how large, you'll notice a similar pattern. 
The PHI value of any Prime number is:
```markdown
p - 1
```

So, if we have two Prime numbers, *p1* and *p2*, we can obtain the PHI value of their factorization as follows:
```markdown
if F = p1 x p2, then PHI(F) = (p1 - 1)(p2 - 1)
```

Now, recall earlier when we explained that computers can multiply numbers very easily but struggle when they have to find 
the Prime Factorization of a number.

Alice has derived the value of F by multiplying p1 x p2. She can also easily derive the value of PHI(F), because she knows 
the component Primes of F.

```markdown
PHI(F) = (p1 - 1)(p2 - 1)
```

However, for anyone else, finding the value of PHI(F) would be very difficult, because they don't know
the component Primes of F. In a real world situation, where very large numbers would be used, someone who wanted to obtain the 
Prime Factorization of F would have to expand enormous computing resources, to the point where doing do would make no sense. 

Alice now has a value, PHI(F) that only she can compute easily, but no one else can. She can now leverage this to complete the RSA framework.

### The Public Exponent

Alice's lock is now partially complete, but it needs another part, the Public Exponent.

In RSA, the Public Exponent (let's call it *e*) is the smallest number that is coprime with the PHI value of the factor of Primes (*PHI(F)*).

What does coprime mean?

One number is coprime with another if their only common factor is 1.

So, `4` is coprime with `9` because the only factor they share is `1` (even though `4` isn't a Prime number).

`9` is **not** coprime with `27`, because they share a common factor, `3`.

For small numbers, we can mentally figure out the smallest coprime, but for large numbers, we use a helper method in the script. 
That's all we need to know. The Public Exponent (*e*) is the smallest coprime of the PHI value of the factor of Primes (*PHI(F()*).

### The Public Key

Alice's lock is now complete. It is composed of the Public Exponent (*e*) and the factor of Primes (*F*), **not** PHI(F)). 
Remember, only Alice should know the value of PHI(F).

In RSA, Alice's lock is called her Public Key. It's a little bit counter-intuitive when we also refer to a Private Key. Perhaps 
a 'Public Lock' is more intuitive, but let's stick with convention, and refer to the "Public Lock" as the Public Key from this point on.

### The Private Key

Alice now needs to make a key to fit her lock. Cryptographically, she needs to create a Private Key from her Public Key.

This is the most complex bit of math in RSA, so hold tight.

Let's recall again: only Alice knows the value of PHI(F), so if she can obtain a value that depends on knowing PHI(F) she has her Private Key.

In RSA, the value used for this is the *modular inverse* of PHI(F). Trying to de-construct the modular inverse into plain speak is not
easy, and probably not necessary. It's somewhat similar to the *multiplicative inverse*, also called the *reciprocal*, which is easier to understand.

Consider:
```markdown
a x b = 1
```
b is the multiplicative inverse of a, and vice versa, because when factored together they make 1. If you have the value of a, 
can easily find the value of b.

The *modular inverse* is where:
```markdown
a x b = 1(mod c)
```
There are three parts to this equation instead of 2, but if you have 2 of the values, you can (maybe not easily for a human, 
but easily for computer) find the third.

In RSA, the multiplicative inverse is expressed as:
```markdown
e x d = 1(mod PHI(F))
```

We know *e* and we know *PHI(F)*, so we can find *d*, which (hey presto!) is Alice's Private Key.

Why? Because we can only find *d* if we know *PHI(F)*, which as you'll recall is the essential rule for creating a Private Key.

To find *d*, even for relatively small numbers, we need to use what's called the **extended Euclidean Algorithm**. The math 
involved in this is too cumbersome to include here, but it isn't computationally complicated, and a simple helper method is 
provided in the script to obtain it.

Remember, what's important is that *d*, the Private Key, can only be derived when PHI(F) is known. How *d* is derived is not so 
important, provided it is derived in some way using PHI(F).

### The exchange of an encrypted message

Alice now has both her lock (her Public Key) and her key (her Private Key). This is all she needs. 

She now publishes her Public Key on the Internet, and sits back and waits to receive encrypted messages from unknown persons 
that she can unlock with her Private Key.

Bob decides he wants to send Alice a secret message that only she can read. He converts the plaintext message to a series of numbers (using ASCII). He know encrypts each 
number (*m*) into an encrypted number (*c* ) as follows:

<code>c = m<sup>e</sup> (mod F)</code>

Where *e* and *F* are obtained from Alice's Public Key.

He then sends *c* to Alice, and Alice decrypts it as follows, using her Private Key, *d*:

<code>m = c<sup>d</sup> (mod F)</code>


Alice, and only Alice, now has Bob's plaintext message *m*, because only Alice knows the value of *d*.

The RSA exchange is now complete and secure.
