from ciphers import vigenereCipher
from string import ascii_uppercase
import streamlit as st

st.title('Vigenere Cipher')
plaintext = st.text_input(label='a',label_visibility='hidden', placeholder='Input plain text...')
key = st.text_input(label='a',label_visibility='hidden', placeholder='Input encryption key...').upper()
if plaintext:
    if key.isalpha():
        st.info(f'**Cipher text:** {vigenereCipher(plaintext, key)}')
        st.info(f'**Decryption key:** {"".join([ascii_uppercase[(-ascii_uppercase.index(x))] for x in key] )}')
    elif key:
        st.error('Please enter an alphabetic encryption key.')

st.divider()
st.subheader('What is a Vigenere cipher?')
st.write('A Vigenere cipher is a more complex Caesar cipher where each alphabetic character gets its own shift determined by the key. The shift is determined by the corresponding character in the key\'s position in the alphabet. A has a shift of 0, B has a shift of 1, etc. Note that the key is repeated until it is the same length as the plain text.')
st.warning('**Example plain text:** Hello World!')
st.warning('**Example key:** KEY')
st.warning(f'**Example cipher text:** {vigenereCipher("Hello World!", "KEY")}')

st.divider()
st.subheader('Vigenere cipher decryptor')
st.write('Enter your cipher text and decryption key to decrypt it back into plain text.')
ciphertext = st.text_input(label='a',label_visibility='hidden', placeholder='Input cipher text...')
dkey = st.text_input(label='a', label_visibility='hidden', placeholder='Input decryption key...')
if ciphertext:
    if dkey.isalpha():
        st.info(f'**Plain text:** {vigenereCipher(ciphertext, dkey)}')
    elif dkey:
        st.error('Please enter an alphabetic decryption key.')