import requests
from bs4 import BeautifulSoup
headers = {'User-agent' : 'Mozilla/5.0'}
request = requests.get('https://www.bbc.com/news', headers=headers)
html = request.content
sup = BeautifulSoup(html, 'html.parser')

Linetoken = "gNe9xqn89LG3xCMJtAiPPy7Nqvf1H6ImDRS2P7vO0y9"

def LineNotifyMessage(message):
    payload = {'message':message}
    return LineNotify(payload)
def LineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = Linetoken
    headers = {'Authorization':'Bearer ' + token}
    return requests.post(url, headers=headers , data = payload, files=file)

def monkeypoxcheck(keyword):
    news_List = []
    h3 = sup.findAll('h3',{'class':'gs-c-promo-heading__title'})
    for h in h3:
        news_title = h.contents[0].lower()
        if news_title not in news_List:
            if 'bbc' not in news_title:
                news_List.append(news_title)
    no_of_news = 0
    keyword_list = []
    for i, title in enumerate(news_List):
        text = ''
        if keyword.lower() in title:
            text = '<-------keyword'
            no_of_news += 1
            keyword_list.append(title)
        print(i+1, ':', title, text)
    print(f'\n---------- total mention of "{keyword}" = {no_of_news} -----------')
    for i, title in enumerate(keyword_list):
        print(i + 1, ':', title)
        
monkeypoxcheck("monkeypox")
