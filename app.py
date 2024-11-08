import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.title('Geração dos mapas interpolados dos pluviómetros')

st.sidebar.image('data/logo.png')

m = leafmap.Map(center=(-22.6,-48.5), zoom=7)

m.to_streamlit(height = 600)


