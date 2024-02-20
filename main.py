import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/meankidsatpark.jpg')
with col2:
    st.title("Kyle Hollek")
    content = '''I am a happy father and husband, learning how to program. '''

    st.info(content)

content2= """
Below are some of the apps i have created!
"""

st.write(content2)