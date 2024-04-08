from ciphers import caesarCipher
import streamlit as st

st.title('Caesar Cipher')
plaintext = st.text_input(label='a',label_visibility='hidden', placeholder='Input plain text...')
shift = st.number_input(label='a', step=1, label_visibility='hidden')
if plaintext:
    st.info(f'Cipher text: {caesarCipher(plaintext, shift)}')
    st.info(f'Decryption key: {-(shift % 26)} or {26 - shift%26}')
    
st.divider()
st.subheader('What is a Caesar cipher?')
st.write('A Caesar cipher shifts each alphabetic character up (positive) or down (negative) by a certain number of letters (the shift).')
st.warning('**Example plain text:** Hello World!')
st.warning('**Example shift:** 1')
st.warning(f'**Example cipher text:** {caesarCipher("Hello World!", 1)}')

st.divider()
st.subheader('Caesar cipher decryptor')
st.write('Enter your cipher text and decryption key to decrypt it back into plain text.')
ciphertext = st.text_input(label='a',label_visibility='hidden', placeholder='Input cipher text...')
dshift = st.number_input(label='b', step=1, label_visibility='hidden')
if ciphertext:
    st.info(f'**Plain text:** {caesarCipher(ciphertext, dshift)}')
