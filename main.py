import streamlit as st
from scrape import scrape_website
st.title("AI Chatbot / Web Scraper")
url = st.text_input("Enter the URL of the website to scrape:")

if st.button("Scrape Site"):
    st.write("Scrapping the website...")
    result = scrape_website(url)
    print(result)
