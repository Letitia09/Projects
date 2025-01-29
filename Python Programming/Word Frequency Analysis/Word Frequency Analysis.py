# Project 5 : Word Frequency Analysis
# Technologies Used : BeautifulSoup, Pandas, Regular Expression

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# URL of the webpage containing the speech
speech_url = 'http://analytictech.com/mb021/mlk.htm'
response = requests.get(speech_url)

# Parse the HTML content of the page
html_soup = BeautifulSoup(response.text,'html')

# Extract all the paragraphs from the page
speech_paragraphs = html_soup.find_all('p')

# Combine all the paragraph texts into a single string
combined_speech = [p.text for p in speech_paragraphs]
speech_text = " ".join(combined_speech)

# Clean the string by replacing newline characters
cleaned_speech_text = speech_text.replace('\r\n',' ')

# Remove punctuation (non-alphabetic characters) from the text
cleaned_speech_no_punctuation = re.sub(r'[\^w\s]',' ', cleaned_speech_text)

# Convert all text to lowercase
speech_in_lowercase = cleaned_speech_no_punctuation.lower()

# Break the speech into individual words
words_list = re.split(r'\s+', speech_in_lowercase)

# Count the frequency of each word and create a DataFrame
word_count_df = pd.DataFrame(words_list).value_counts()

# Save the word count DataFrame to a CSV file
word_count_df.to_csv(r'C:\Users\anshu\Downloads\Python Tutorial\MLKJ_Speech_Count.csv', header=['Counts'], index_label='Word')
