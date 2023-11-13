import streamlit as st
from transformers import pipeline

   # Create a title and description
st.title("Text Classification App")
st.write("Enter text for classification:")

   # Create a text input field
user_input = st.text_area("Input Text")

   # Create a button for classification
if st.button("Classify"):
       # Load the text classification pipeline
       classifier = pipeline("sentiment-analysis")

       # Perform text classification on user input
       classification_result = classifier(user_input)

       # Display the classification result
       st.write("Classification Result:")
       for result in classification_result:
           st.write(f"Label: {result['label']}, Score: {result['score']}")