# Toy Encryption in Python

This project presents a series of Python scripts that demonstrate common encryption techniques at a *very* basic level.

Their purpose is not for use in actual encryption, but to explain how encryption works.

Each directory contains a self-contained script, derived from relatively simple math, to demonstrate a specific encryption method.

## The Diffie-Hellmann Key Exchange

Diffie-Hellmann was the first modern breakthrough in encryption. It allows contracting parties to use the same key to encrypt 
messages without the need for the key to be transmitted.

Example: the creation of a VPN between 2 computers

[Click here for more](./diffie-hellmann)

## RSA Public Private Key Encryption

RSA expands on Diffie-Hellman by allowing anyone send an encrypted message to another person if they have a *lock* ( or Public Key )
that has been made available publicly by that person.

Example: sending an encrypted email to someone, or accessing a web server over SSL/TLS

[Click here for more](./rsa)

## Eliptic Curve Encryption

*Coming soon*
