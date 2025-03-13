import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# Read API Key
with open('apikey.txt', 'r') as file:
    API_KEY = file.read().strip()

# Initialize Google Generative AI Model
chat_model = GoogleGenerativeAI(api_key=API_KEY, model="models/gemini-2.0-pro-exp")

# Define Chat Prompt Template
chat_template = ChatPromptTemplate(messages=[
    ('system', '''
    You are an AI-powered travel planning assistant.
    Provide users with the best travel options (cab, train, bus, flights) along with estimated costs.
    Also, suggest websites for booking tickets.
    Format your response neatly using bullet points and headings. Don't ask any questions to the user.
    '''),
    ('human', 'I want to travel from {source} to {destination}')
])

# Output Parser
output_parser = StrOutputParser()

# Define Chain
chain = chat_template | chat_model | output_parser

# Streamlit App Layout
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="centered")
st.title("🌍 AI Travel Planner")
st.markdown("### Find the best travel options for your journey!")

# Input Form
with st.form(key='travel_form'):
    col1, col2 = st.columns(2)
    with col1:
        place1 = st.text_input('From', placeholder='Enter starting location')
    with col2:
        place2 = st.text_input('To', placeholder='Enter destination')
    
    submit_button = st.form_submit_button(label='🚀 Plan My Trip')

# Process Input on Submit
if submit_button:
    if not place1 or not place2:
        st.error("⚠️ Please enter both source and destination!")
    else:
        with st.spinner("Fetching travel options... 🧳"):
            response = ""  # Placeholder for response text
            for info in chain.stream({'source': place1, 'destination': place2}):
                response += info + "\n"
        
        # Display Results in a Card
        st.markdown("""
        <div style="background-color: #f9f9f9; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <h4>🚆 Recommended Travel Options:</h4>
            <p>""" + response + """</p>
        </div>
        """, unsafe_allow_html=True)