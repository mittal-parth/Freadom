import docx
import re
import requests
import sys
from bs4 import BeautifulSoup

mydoc = docx.Document()

def getInfo(url):

    # url = 'https://medium.com/publishous/a-piece-of-advice-i-desperately-want-every-creative-to-hear-fdb878d87b6e'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    post = soup.find('article')

    data = post.text
    print(data)
    mydoc.add_paragraph(data)

    # Change file name and path here
    mydoc.save("D:\\PARTH DATA\\WEB DEVELOPMENT\\WEC Recruitment Tasks\\web_scraper\\media\\web_scraper_result.docx")

def main():
    try:
        url = sys.argv[1]
        # print(f"Getting Page from {url}")
        getInfo(url)
    except Exception as e:
        print(f"Got Exception on Page as {e}")
        return

    # print('Done')

# Driver Code
main()