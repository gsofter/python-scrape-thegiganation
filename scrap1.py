#Beatiful Soup - To parse the html
from bs4 import BeautifulSoup
#urllib.request - to make http request
from urllib.request import Request, urlopen
#To remove any language special characters
import unicodedata
# EMAIL library
import smtplib
# URL parser
from email_scraper import scrape_emails
from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import urljoin
import re

# from email_scraper import scrape_emails
def findMails(soup):
    mails = []
    for name in soup.find_all('a'):
        if(name is not None):
            emailText=name.text
            match=bool(re.match('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',emailText))
            if('@' in emailText and match==True):
                emailText=emailText.replace(" ",'').replace('\r','')
                emailText=emailText.replace('\n','').replace('\t','')
                if(len(mails)==0)or(emailText not in mails):
                    print(emailText)
                mails.append(emailText)
    return mails

def do_email_scrape_from_url(endpoint):
    mails = []
    req = Request(endpoint, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    webpage = urlopen(req).read()
    
    soup = BeautifulSoup(webpage, 'lxml')
    pageLinks = soup.select('li.menu-item > a')
    for page_link in pageLinks:
        subLink = urljoin(endpoint, page_link.attrs['href'])

        subReq = Request(subLink, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
        subPage = urlopen(subReq)
        # subPageMails = scrape_emails(subPage)
        subSoup = BeautifulSoup(subPage, 'lxml')
        subPageMails = findMails(subSoup)
        mails = mails + subPageMails
    return mails
    
if __name__ == '__main__':
    endpoint = "http://thegiganation.com/"
    mails = do_email_scrape_from_url(endpoint)
    print(mails)