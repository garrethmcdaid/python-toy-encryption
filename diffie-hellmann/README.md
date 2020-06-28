# Diffie-Hellmann private key exchange

## Introduction

Prior to Diffie-Hellmann, all encryption was symmetric.

That means that if Alice and Bod wanted to encrypt data before they sent it across a network, they first had to share a 
private key, which meant transmitting the key in some way, which meant the key was exposed to corruption.

Diffie-Hellmann solved this problem. It provided a mathematical way for Alice and Bob to use the same key 
without having to transmit it.


## The math

Prime numbers are key to Diffie-Hellmann.

A Prime number is a number than can only be divided by 1 and itself. eg 
```
3, 7, 11 or 29
```
Prime numbers are the building 
blocks of all non-Prime (composite) numbers. They feature regularly in cryptography because they are rigid. 

For instance, the only way to derive the Prime 7 is `1 x 7`, whereas you can derive the non-Prime 16 with 
`1x16, 2x8 or 4x4`

Another mathematical concept that is key to Diffie-Hellman is the *modulo*. 
The modulo of *a* and *b* is equal to the remainder when you divide *a* by *b*, e.g.
 ```
 16(mod 7) = 2
 ``` 

The key exchange is initiated by one of the parties.

Let's say this is Alice, who initiates the key exchange by choosing a Prime number *p*, for which they then find a *Primitive Root*.

What's a Primitive Root?

Lets's say we have the Prime number 7. The Primitive Roots of 7 are:
```markdown
3, 5
```

A Primitive Root of a Prime *p* is a number that when multiplied to the power of every number between 1 and (*p* - 1), 
to which (mod *p*) is then applied, equals a distinct number

Let's test if 3 if a Primitive Root of the Prime 7:

So the numbers between 1 and (p - 1) are `1,2,3,4,5,6` as represented by the series of exponent values applied to 3.


<code>3<sup>1</sup> = 3</code><br>
<code>3<sup>2</sup> = 9</code><br>
<code>3<sup>3</sup> = 27</code><br>
<code>3<sup>4</sup> = 81</code><br>
<code>3<sup>5</sup> = 243</code><br>
<code>3<sup>6</sup> = 729</code><br>

Then, for each value of 3 multiplied by each of these exponents, we apply (mod 7).

```
3(mod 7) = 3
9(mod 7) = 2
27(mod 7) = 6
81(mod 7) = 4
243(mod 7) = 5
729(mod 7) = 1
```

In each case, we get a distinct number, therefore 3 is a Primitive Root of Prime 7. 

In the script, a helper method is defined to find Primitive Roots of given Prime numbers. In cryptographic parlance, 
the Primitive Root is called the *generator*, so let's call it that.

Coming back to Alice, she now has a Prime number and a generator, which she shares with Bob. Either apart of together, 
these numbers cannot be used to decrypt data, so there is no issue in sharing them on a network. 

## The exchange of an encrypted message

Both Alice and Bob now perform another computation to generate a payload.

First, each party chooses a random secret number. They **never** share these numbers.

Alice now generates the following payload:

<code>alice_payload = generator<sup>alice_secret</sup>(mod p)</code>

and sends it to Bob.
 
Bob does the same:
 
<code>bob_payload = generator<sup>bob_secret</sup>(mod p)</code>

and sends it to Alice.


Using each other's payloads, the can now perform a final calculation to reveal the shared component in the payloads, which is their shared key:

Alice

<code>key=bob_payload<sup>alice_secret</sup>(mod p)</code>
 
 
Bob

<code>key=alice_payload<sup>bob_secret</sup>(mod p)</code>

They now both have `key`, which has never been shared across the network, with which they can encrypt and decrypt data.

## The script

Run the script to see this in action. No inputs are required. The script chooses random numbers for you. 
The script also contains comments which provide further information.
 