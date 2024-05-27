import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Set your OpenAI API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyCBpGHIaubNnku2U3I2Fm3PCkQ3ldfHxRA"

# Function to load answer from OpenAI
def load_answer(question):
    try:
        # Initialize OpenAI model
        llm = ChatGoogleGenerativeAI(model="gemini-pro")
        # Make API request to generate answer
        answer = llm.invoke(question)
        return answer
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Function to get user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

# Main function
def main():
    st.set_page_config(page_title="Langchain Demo", page_icon=":robot:")
    st.header("Langchain Demo")

    # Get user input
    user_input = get_text()

    # Display answer on button click
    if st.button("Generate"):
        # Check if user input is empty
        if not user_input:
            st.warning("Please enter a question.")
        else:
            # Load and display answer
            response = load_answer(user_input)
            if response:
                st.subheader("Answer:")
                st.write(response.content)

if __name__ == "__main__":
    main()
