import streamlit as st
import os


col1, col2 = st.columns([1,3])
with col1:
    st.image("pp.jpg",None,150)
    
with col2:
    st.subheader("Jandel Macabecha")
    st.write("Age: 24")
    st.image("ph.jpg",None,30)
    

st.divider()
st.markdown("**<span style='color:navy'>Hello World!</span>** I am **Jandel Macabecha** hailing from the Queen City of the South, Cebu. I am a Bachelor of Science, major in Information Technology student. I am currently in my 4th year and hopefully, be able to graduate this semester.<br>",unsafe_allow_html=True)
st.markdown("I am an avid programmer and a big fan of video games. Although I spent most of my teenage years doing gaming and zero aspects in IT related stuff, I compensate it by giving my best shot in all my courses here in college.")
st.markdown("In my college journey, I have taken quite an interest in web development's backend aspect where I had quite a blast creating REST APIs in both **<span style='color:green'>Springboot</span>** and **<span style='color:green'>Django</span>**. <br><br>",unsafe_allow_html=True)

mcol1, mcol2 = st.columns([1,13])
mcol1.image("github.png",None,30)
mcol2.caption("https://github.com/LeFruitCake")

ncol1, ncol2 = st.columns([1,13])
ncol1.image("linkedin.png",None,30)
ncol2.caption("https://www.linkedin.com/in/jandel-macabecha-76a557234/")