import streamlit as st
import os

# get the current working directory
current_working_directory = os.getcwd()

# print output to the console
print(current_working_directory)

st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.image("kids.png")
#st.audio("Audio.mp3")
#st.video("video.mp4")