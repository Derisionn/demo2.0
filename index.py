import streamlit as st 

st.header("Demo <3 ")



name =st.selectbox("Select Your Name",["Harsh Vardhan","vabhi","Tanishq","Vineet"])


if name !="" :
    st.write(f"Hi {name} !!")
else:
    pass


st.write("from branch master commit 3")


# this the comiit 2 in the branch master