import streamlit as st 

st.header("Demo <3 ")



name =st.selectbox("Select Your Name",["Harsh Vardhan","vabhi","Tanishq","Vineet"])


if name !="" :
    st.write(f"Hi {name} !!")
else:
    pass



# hello there this file is from demo branch 2 