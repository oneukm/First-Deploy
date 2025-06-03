import streamlit as st
import google.generativeai as genai
import pandas as pd

data = {
    "Brands": ["FATTY Smoked Meat Sticks", "Slim Jim", "Jack Link’s", "Old Trapper", "Tillamook Country Smoker", "Duke’s", "Old Wisconsin", "Chomps", "Country Archer", "No Man’s Land", "Vermont Smoke and Cure"],
    "Total Answering": [100, 454, 446, 100, 100, 100, 100, 100, 100, 63, 72],
    "Less often than every 3 months": [7.0, 6.167, 8.072, 9, 9, 7.0, 10, 18, 9, 11.111, 6.944],
    "Once every 2-3 months": [9, 14.317, 15.471, 12, 16, 20, 14.0, 22, 21, 22.222, 20.833],
    "Once a month": [25, 20.705, 23.991, 26, 28, 28.0, 31, 25, 23, 17.46, 18.056],
    "Once every 2-3 weeks": [26, 31.718, 31.839, 38, 32, 30, 28.0, 19, 33, 28.571, 33.333],
    "Once a week or more often": [33, 27.093, 20.628, 15, 15, 15, 17, 16, 14.0, 20.635, 20.833],
    "== Once Every 2-3 Weeks + (NET) ==": [59, 58.811, 52.466, 53, 47, 45, 45, 35, 47, 49.206, 54.167],
    "== Once a Month + (NET) ==": [84, 79.515, 76.457, 79, 75, 73, 76, 60, 70, 66.667, 72.222],
    "Just 1": [17, 17.621, 29.596, 30, 33, 26, 26, 22, 27, 23.81, 15.278],
    "2 to 3": [27, 20.705, 28.027, 32, 34, 27, 30, 24, 34, 25.397, 27.778],
    "4 to 5": [17, 16.52, 13.453, 11, 10, 13, 13, 16, 9, 15.873, 18.056],
    "6 to 10": [18, 19.604, 14.798, 14.0, 8, 15, 15, 13, 10, 11.111, 15.278],
    "11 to 15": [13, 8.37, 5.83, 5, 4, 7.0, 6, 8, 9, 11.111, 8.333],
    "16 to 20": [7.0, 4.185, 3.363, 2, 5, 8, 4, 10, 7.0, 3.175, 6.944],
    "More than 20": [1, 12.996, 4.933, 6, 6, 4, 6, 7.0, 4, 9.524, 8.333],
    "== 2 or More (NET) ==": [83, 82.379, 70.404, 70, 67, 74, 74, 78, 73, 76.19, 84.722],
    "== 6 or More (NET) ==": [39, 45.154, 28.924, 27, 23, 34, 31, 38, 30, 34.921, 38.889],
    "== More Than 10 (NET) ==": [21, 25.551, 14.126, 13, 15, 19, 16, 25, 20, 23.81, 23.611]
}

df1 = pd.DataFrame(data)

dataset_text = df1.to_string(index=False)

# Configure Gemini
genai.configure(api_key='AIzaSyCyhUElIKNPyu-9ZColljdlmBDzO8kyIYs')  # Use actual API key
model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit UI
st.title("Tabular Data Chatbot")
st.write("Ask a question based on the dataset.")
 
user_input = st.text_input("Your Question", "")
 
if user_input:
    prompt = f"""
You are an AI assistant. Answer the question based on the given dataset.
 
**Dataset:**
{dataset_text}
 
**Question:** {user_input}
 
**Answer:**
"""
    with st.spinner("Thinking..."):
        response = model.generate_content(prompt)
        st.markdown(f"**Bot:** {response.text.strip()}")
