def ceaser_code(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            char = chr((ord(char) - start + shift) % 26 + start)
        ciphertext += char
    return ciphertext


def xor_code(plaintext, key):
    return "".join(
        [
            str(int(i) ^ int(j))
            for i, j in zip(
                plaintext, (key * ((len(plaintext) // len(key)) + 1))[: len(plaintext)]
            )
        ]
    )
