import os
import re
import requests
import sys
from datetime import datetime
from bs4 import BeautifulSoup

def getInfo(url):

    #setting headers
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    #finding all article tags
    post = soup.find('article')

    #finding text inside them
    data = post.text
    print(data)

def main():
    try:
        url = sys.argv[1]
        getInfo(url)
    except Exception as e:
        print(f"Got Exception on Page as {e}")
        return

# Driver Code
main()