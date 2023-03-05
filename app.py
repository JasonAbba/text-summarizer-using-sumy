# TEXT SUMMARIZER

#! NEED TO RUN ONLY ONCE
import nltk
nltk.download('punkt')

# Streamlit
import streamlit as st

# Summary Engine
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# JUST TO RELOAD ENTIRE PAGE
# import pyautogui

# Load Local CSS
def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

def sumy_summarizer(input_text):
    parser = PlaintextParser.from_string(input_text,Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document,3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

def runapp():
    # Header Section
    with st.container():
        st.header('Text Summarizer using Python')
        st.write('*using NLP Tokenizers*')
        st.write('---')
    
    # Input Section
    with st.container():
        st.subheader('Article to be summarized:')
        raw_text = st.text_area(key = 'input_text_area', label='text_area', label_visibility='hidden', height=400, placeholder='Paste the text here...')
        st.write('##')
        
        col_left, col_right = st.columns([0.1, 1])
        # Output Section
        with col_left:
            submit = st.button(label='Submit ✅')
        if submit:
                summary_result = sumy_summarizer(raw_text)
                st.write('##')
                st.subheader('Summary:')
                st.write(summary_result)
                st.write('---')
        with col_right:
            clear = st.button(label='Clear 🗑️')
        if clear:
             # Stimulate F5 key press
             # pyautogui.hotkey('F5')
             st.empty()

    # Footer Section
    with st.container():
        html_code = """
            <p style='text-align: center;'>Made with ❤ by <b>Jason Abba</b> </p>
        """
        st.markdown(html_code, unsafe_allow_html=True)

# ----> Execution starts from here    
if __name__ == '__main__':
    st.set_page_config(page_title = 'Text Summarizer V2', page_icon = ':zap:', layout = 'wide')
    local_css("css/style.css")
    runapp() 
