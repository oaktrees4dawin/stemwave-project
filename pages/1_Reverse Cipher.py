from ciphers import reverseCipher
import streamlit as st

st.title('Reverse Cipher')
plaintext = st.text_input(label='a',label_visibility='hidden', placeholder='Input plain text...')
if plaintext:
    st.info(f'**Cipher text:** {reverseCipher(plaintext)}')

st.divider()
st.subheader('What is a reverse cipher?')
st.write('A reverse cipher simply reverses the plain text.')
st.warning('**Example plain text:** Hello World!')
st.warning(f'**Example cipher text:** {reverseCipher("Hello World!")}')

st.divider()
st.subheader('Reverse cipher decryptor')
st.write('Enter your cipher text to decrypt it back into plain text.')
ciphertext = st.text_input(label='a',label_visibility='hidden', placeholder='Input cipher text...')
if ciphertext:
    st.info(f'**Plain text:** {reverseCipher(ciphertext)}')