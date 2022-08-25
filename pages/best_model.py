import streamlit as st
from pythainlp.tokenize import word_tokenize
from pythaitts import TTS
st.title("PyThaiTTS Demo - Best model")
tts = TTS(pretrained="khanomtan", mode="best_mode")
st.markdown("""
# PyThaiTTS Demo (Best model) 🎈
Welcome to PyThaiTTS Demo. This website will give you a example text-to-speech from PyThaiTTS.
See more at [https://github.com/PyThaiNLP/PyThaiTTS](https://github.com/PyThaiNLP/PyThaiTTS) and KhanomTan TTS at [https://github.com/wannaphong/KhanomTan-TTS-v1.0](https://github.com/wannaphong/KhanomTan-TTS-v1.0).
"""
)

form = st.form(key="annotation")

with form:
    cols = st.columns((1, 1))
    language = cols[0].selectbox(
        "Language:", ["th-th", "en", "fr-fr", "pt-br", "x-de", "x-lb"], index=0
    )
    speaker_idx = cols[1].selectbox(
        "Speaker:", ["Tsynctwo", "Tsyncone", "Linda", "p259", "p274", "p286", "Bunny", "Judith", "Bernard", "Ed", "Judith", "Kerstin", "Thorsten", "Caroline", "Nathalie", "Sara", "Charel", "Guy", "Jemp", "Luc", "Marco"], index=0
    )
    text = st.text_area("Text:")
    submitted = st.form_submit_button(label="Submit")

if submitted:
    audio_file = tts.tts(text=' '.join(word_tokenize(str(text))).replace('  ',' '), speaker_idx=str(speaker_idx), language_idx=str(language))
    audio_bytes =  open(audio_file,"rb").read()
    st.audio(audio_bytes, format='audio/wav')
