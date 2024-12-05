import streamlit as st

st.title("Hello this is the newest Website")
st.markdown("Lili stinkt")

answer = st.selectbox("Stinkt Lili?", ("Ja", "Nein"),)
if answer == "Ja":
    st.write("Wääääääh so grusig Lili stinkt wäää")
else:
    st.write("das kann gar nicht sein!")

if st.button("Click Me!"):
    st.write("Haha du stinksch!")

