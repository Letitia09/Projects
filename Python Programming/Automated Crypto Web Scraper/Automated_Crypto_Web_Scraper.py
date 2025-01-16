# Project 4 : Automated Crypto Web Scraper
# Name : Anshu Pulipati
# Major : Computer Science


from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import os
import time

def automated_crypto_pull(crypto_url):

    page = requests.get(crypto_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Extract Crypto Name and Price
    crypto_name = soup.find('span', class_='sc-65e7f566-0 lsTl').text
    crypto_price = soup.find('span', class_='sc-65e7f566-0 esyGGG base-text').text
    final_price = crypto_price.replace('$', '')

    # Add timestamp for when the data was pulled
    date_time = datetime.now()

    # Create a dictionary with the data
    dict1 = {'Crypto Name': crypto_name, 'Crypto Price': final_price, 'Timestamp': date_time}

    # Create a DataFrame
    df = pd.DataFrame([dict1])

    # Create directory if it doesn't exist
    path = r'C:\Users\anshu\Downloads\Python Tutorial\Crypto Web Puller'
    if not os.path.exists(path):
        os.mkdir(path)

    # File path with dynamic name (to prevent overwriting)
    file_path = r'C:\Users\anshu\Downloads\Python Tutorial\Crypto Web Puller\Crypto_Automated_Puller.csv'

    # Append to CSV or create if doesn't exist
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, index=False)

    print(f"Data pulled for {crypto_name} at {date_time} is {crypto_price}")


while True:
    try:
        automated_crypto_pull('https://coinmarketcap.com/currencies/bitcoin/')
        time.sleep(3600)  # Pause for 1 hour before running again
    except Exception as e:
        print(f"Error occurred: {e}")
        break

