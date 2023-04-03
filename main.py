import streamlit as st
from PIL import Image
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objects as go



#configurando pagina streamlit-------------------------------------------------
st.set_page_config(
    page_title="trendspy",
    page_icon="🕵️",
)

#acessando matriz da logo------------------------------------------------------
imageLogo = Image.open('logo_trendspy.png')
imageGitLink = Image.open('linkGit.png')
#recebendo imput---------------------------------------------------------------

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.write("")

with col2:
    st.image(imageLogo, width= 250)
    
with col3:
    st.write("")


st.subheader(" View and apply data indicators on Social Media data. ")
st.markdown("---")
st.markdown("1) Choose a search term")
searchTerm = st.text_input('', 'Calculator')

st.write('The current search term to analyze is', searchTerm)
st.markdown("---")
#PYTRENDS CODE------------------------------


#-------------------------------------------
st.markdown("---")
col1Bottom, col2Bottom, col3Bottom = st.columns([1,1,1])
with col1Bottom:
    st.write("")

with col2Bottom:
    st.image(imageGitLink, width= 255)
    
with col3Bottom:
    st.write("")


