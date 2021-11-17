import docx
import os
import re
import requests
import sys
from datetime import datetime
from bs4 import BeautifulSoup

# mydoc = docx.Document()

def getInfo(url):

    # url = 'https://medium.com/publishous/a-piece-of-advice-i-desperately-want-every-creative-to-hear-fdb878d87b6e'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    post = soup.find('article')

    data = post.text
    # mydoc.add_paragraph(data)
    print(data)
    # file_path = os.getcwd() + '\\media\\webscraper_result'+f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}" + '.docx'
    # mydoc.save(file_path)

def main():
    try:
        url = sys.argv[1]
        getInfo(url)
    except Exception as e:
        print(f"Got Exception on Page as {e}")
        return

# Driver Code
main()