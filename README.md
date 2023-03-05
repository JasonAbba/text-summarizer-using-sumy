# Text Summarizer using Python :page_with_curl: :computer:

This is a Python program for text summarization using NLP Tokenizers. It uses Streamlit for creating a user interface and Sumy for summarization. The program summarizes a given text by using the LexRank algorithm.
## Dependencies :toolbox:

The program requires the following dependencies to be installed:

- :heavy_check_mark: nltk
- :heavy_check_mark: sumy
- :heavy_check_mark: streamlit

You can install them by running the following command:

`pip install nltk sumy streamlit`

## How to use :man_teacher:

1. Run the program using the following command:
`streamlit run app.py`
2. Once the program is running, you will see an interface where you can paste the text you want to summarize.
3. Click the 'Submit' button to generate the summary.
4. The summary will be displayed in the output section.
5. If you want to clear the input text, click the 'Clear' button.

## Note :memo:

The program downloads the required NLTK package for tokenization. If it's the first time you're running the program, it may take some time to download the package. Also, the program has a CSS file for styling the interface, so make sure to keep the file in the same directory as the Python file.

## Credits :star:
This program was created by **Jason Abba**. Feel free to use and modify it according to your needs.
**To access the webapp, click [here](https://text-summarizer-using-sumy.streamlit.app/)**
