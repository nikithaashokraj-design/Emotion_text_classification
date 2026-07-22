import streamlit as st
import pickle

with open("emotion.pkl","rb+")as file:
    model=pickle.load(file)

with open("vector.pkl","rb+")as file:
    vector=pickle.load(file)
encoder = {0: 'anger',
           1: 'disgust',
           2: 'fear',
           3: 'joy',
           4: 'love',
           5: 'neutral',
           6: 'sadness',
           7: 'surprise'}
st.header("Emotion Text Classification")
text=st.text_input("Enter the text")
bn=st.button("Click here")
if bn and text:
    result=model.predict(vector.transform([text]))
    st.text(encoder[result[0]])
else:
    st.warning("Provide Text")