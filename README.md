# AI Travel Planner 🚀

## Overview
The **AI Travel Planner** is a Streamlit-based web application that helps users find the best travel options between two locations. It leverages **LangChain** and **Google Generative AI** to provide recommendations for travel modes (cab, train, bus, flights) along with estimated costs and booking websites.

## Features ✨
- 🏙️ Enter source and destination to get travel options instantly
- 🚆 Provides travel choices like cab, train, bus, and flights
- 💰 Estimates travel costs
- 🌐 Suggests booking websites
- 🎨 Interactive and user-friendly UI with Streamlit

## Technologies Used 🛠️
- **Python**
- **Streamlit** (for UI)
- **LangChain** (for AI-powered responses)
- **Google Generative AI** (Gemini-2.0-pro-exp model)

## Installation & Setup 🏗️
### Prerequisites:
- Python 3.8+
- A Google API key (stored in `apikey.txt`)

### Steps to Run Locally:
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/ai-travel-planner.git
   cd ai-travel-planner
2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt

4. **Add your API key:**
   - Create a file named apikey.txt in the project folder
   - Paste your Google API Key inside it

5. **Run the application:**
   ```sh
   streamlit run app.py
