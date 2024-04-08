from ciphers import atbashCipher
import streamlit as st

st.title('Atbash Cipher')
plaintext = st.text_input(label='a',label_visibility='hidden', placeholder='Input plain text...')
if plaintext:
    st.info(f'**Cipher text:** {atbashCipher(plaintext)}')

st.divider()
st.subheader('What is an atbash cipher?')
st.write('An atbash cipher replaces each alphabetic character with its mirror opposite. A\'s turn into Z\'s, B\'s into Y\'s, etc.')
st.warning('**Example plain text:** Hello World!')
st.warning(f'**Example cipher text:** {atbashCipher("Hello World!")}')

st.divider()
st.subheader('Atbash cipher decryptor')
st.write('Enter your cipher text to decrypt it back into plain text.')
ciphertext = st.text_input(label='a',label_visibility='hidden', placeholder='Input cipher text...')
if ciphertext:
    st.info(f'**Plain text:** {atbashCipher(ciphertext)}')