# import os
#
# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as gen_ai
#
#
# # Load environment variables
# load_dotenv()
#
# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="Chat with Gemini-Pro!",
#     page_icon=":brain:",  # Favicon emoji
#     layout="centered",  # Page layout option
# )
#
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
#
# # Set up Google Gemini-Pro AI model
# gen_ai.configure(api_key=GOOGLE_API_KEY)
# model = gen_ai.GenerativeModel('gemini-pro')
#
#
# # Function to translate roles between Gemini-Pro and Streamlit terminology
# def translate_role_for_streamlit(user_role):
#     if user_role == "model":
#         return "assistant"
#     else:
#         return user_role
#
#
# # Initialize chat session in Streamlit if not already present
# if "chat_session" not in st.session_state:
#     st.session_state.chat_session = model.start_chat(history=[])
#
#
# # Display the chatbot's title on the page
# st.title("🤖 Gemini Pro - ChatBot")
#
# # Display the chat history
# for message in st.session_state.chat_session.history:
#     with st.chat_message(translate_role_for_streamlit(message.role)):
#         st.markdown(message.parts[0].text)
#
# # Input field for user's message
# user_prompt = st.chat_input("Ask Gemini-Pro...")
# if user_prompt:
#     # Add user's message to chat and display it
#     st.chat_message("user").markdown(user_prompt)
#
#     # Send user's message to Gemini-Pro and get the response
#     gemini_response = st.session_state.chat_session.send_message(user_prompt)
#
#     # Display Gemini-Pro's response
#     with st.chat_message("assistant"):
#         st.markdown(gemini_response.text)
import os
import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Input field for Google API key
api_key_input = st.text_input("Enter your Google API Key:")

# Only configure the API and initialize the chat session if the API key is provided
if api_key_input:
    # Save the API key in the session state
    st.session_state.GOOGLE_API_KEY = api_key_input

    # Configure the Google Gemini-Pro AI model
    gen_ai.configure(api_key=st.session_state.GOOGLE_API_KEY)
    model = gen_ai.GenerativeModel('gemini-pro')

    # Initialize the chat session if not already present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])


    # Function to translate roles between Gemini-Pro and Streamlit terminology
    def translate_role_for_streamlit(user_role):
        return "assistant" if user_role == "model" else user_role


    # Display the chatbot's title on the page
    st.title("🤖 Gemini Pro - ChatBot")

    # Display the chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # Input field for user's message
    user_prompt = st.chat_input("Ask Gemini-Pro...")
    if user_prompt:
        # Add user's message to chat and display it
        st.chat_message("user").markdown(user_prompt)

        # Send user's message to Gemini-Pro and get the response
        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # Display Gemini-Pro's response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)
else:
    st.warning("Please enter your Google API Key to start the chat.")
