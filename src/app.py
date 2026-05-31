import streamlit as st

from agente import PyMentor

mentor = PyMentor()

st.title("PyMentor AI")

pergunta = st.text_area(
    "Digite sua dúvida"
)

if st.button("Enviar"):

    resposta = mentor.responder(pergunta)

    st.write(resposta)