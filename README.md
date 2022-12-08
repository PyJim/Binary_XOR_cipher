# XOR Cipher
XOR cipher encryption algorithm with python

# Binary XOR Cipher Algorithm

This is a simple implementation of the binary XOR cipher, a type of symmetric-key encryption algorithm that operates on binary data. It can be used to encrypt and decrypt messages using a shared key.

## Usage

To use the binary XOR cipher, run the main.py file and enter the value to be encrypted or decrypted as input followed by the key to be used.

For an XOR operation, encryption and decryption use the same function, and hence no need to worry about either encrypting or decrypting as the results will be the same.

The process is smooth when the key and value have the same number of bits. However, necessary adjustments are made to ensure proper encryption if otherwise. 

## Security

The security of the XOR cipher depends on the strength of the key. A strong key that is difficult to guess or brute-force will make it more difficult for an attacker to decrypt the message. 
It is important to choose a key that is long and random and to keep the key secret.

Additionally, the XOR cipher is vulnerable to known-plaintext attacks, where an attacker has access to both the encrypted and unencrypted versions of the same message. 
In this case, the attacker can easily determine the key by performing the XOR operation on the known plaintext and the corresponding ciphertext. 
Therefore, it is important to use the XOR cipher only for short messages or in situations where known-plaintext attacks are not a concern.







