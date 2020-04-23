# GigaNation Email Scrapping

### Prerequisites

```
python > 3.7
```

### Setup Enviroment

```
pip install -r requirements.txt
```

### First method

run

```
python scrap1.py
```

Output

```
JEFF@JEFFJBUTLER.COM
JEFF@JEFFJBUTLER.COM
JEFF@JEFFJBUTLER.COM
JEFF@JEFFJBUTLER.COM
```

code

```python
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
```

### Second method

run

```
python scrap2.py
```

Output

```
[
    'jeff@jeffjbutler.com',
    'jeff@jeffjbutler.com',
    'jeff@jeffjbutler.com',
    'jeff@jeffjbutler.com']
```

Code (Using library: email-scraper)

```Python
from email_scraper import scrape_emails

...
subReq = Request(subLink, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
subPageMails = scrape_emails(urlopen(subReq).read().decode('utf-8'))
mails = mails + list(subPageMails)
...
```
