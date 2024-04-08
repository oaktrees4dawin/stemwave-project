from string import ascii_uppercase as alphabet

def reverseCipher(plaintext):
    return plaintext[::-1]

def atbashCipher(plaintext):
    ciphertext = ''
    for ch in plaintext:
        if not ch.isalpha():
            ciphertext += ch
            continue
        mod = ord('A') + ord('Z') if ch.isupper() else ord('a') + ord('z')
        ciphertext += chr(mod - ord(ch))
    return ciphertext

def caesarCipher(plaintext, shift):
    shift %= 26
    plaintext = [ch for ch in plaintext]
    ciphertext = ''
    while plaintext:
        ch = plaintext.pop(0)
        if not ch.isalpha():
            ciphertext += ch
            continue
        mod = ord('A') if ch.isupper() else ord('a')
        nshift = shift - mod
        ciphertext += chr(mod + (ord(ch) + nshift) % 26)
    return ciphertext

def vigenereCipher(plaintext, key):
    ciphertext = ''
    key = key.upper()
    for i, ch in enumerate(plaintext):
        if not ch.isalpha():
            ciphertext += ch
            continue
        ciphertext += caesarCipher(plaintext=ch, shift=alphabet.index(key[i%len(key)]))
    return  ciphertext
