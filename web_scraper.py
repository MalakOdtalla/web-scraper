import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    ''' method to scrape how many citation in the article, it takes website url as input, and return the count for citations  '''

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations  = soup.findAll('a', title='Wikipedia:Citation needed')
    return len(citations)

def get_citations_needed_report(url):
    """
    method to return the paragraph and the line that contain th citation
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations = soup.findAll('p')
    result = []
    for i in citations:
        paragraph = i.findAll('a', title='Wikipedia:Citation needed')
        if paragraph:
            para = i.text
            # find_sentence = paragraph.split("[citation needed]")
            print(para)
            result.append(para)

    return result






if __name__ == "__main__":

  URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
  print(get_citations_needed_count(URL))
  print(get_citations_needed_report(URL))