import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content,
)

from parse import parse_with_ollama

st.title("AI Chatbot / Web Scraper")
url = st.text_input("Enter the URL of the website to scrape:")

if st.button("Scrape Site"):
    st.write("Scrapping the website...")

    result = scrape_website(url)

    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    # Display the cleaned content in a text area
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=400)


if "dom_content" in st.session_state:
    parse_description = st.text_input("Enter the description of the content you want to parse:")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            dom_chunks = split_dom_content(st.session_state.dom_content, parse_description)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)

