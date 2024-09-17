import requests
from bs4 import BeautifulSoup
import re
import html2text 
max =100
documents=[]
leaf=[]




def getLinks(url):
    try:
        html_page = requests.get(url)
    except:
        return []
    plain = html_page.text
    soup = BeautifulSoup(plain, "html.parser")
    links = []

    for link in soup.findAll('a',href=True):
        l = link.get('href')
        if l not in documents :
            if len(documents)<max:
                if '#' not in l  :
                    if '?' not in l :
                        if'/wiki' in l:
                            links.append('https://en.wikipedia.org/wiki/'+l)
                            documents.append(l)
                            print("Added 1 Link")
            else:
                return links

    return links

def getAllDocuments(url):
    links =getLinks(url)
    if(len(documents)<max):
        for link in links:
            links+=getAllDocuments(link)
    return links



def Crawl(url):
    i=0
    links = getAllDocuments(url)
    print(links)
    for link in links:
        try:
            source_code = requests.get(link)
            print("Opening: "+ link)
            plain = source_code.text
            soup = BeautifulSoup(plain, "html.parser")
            text = html2text.html2text(soup.prettify())
            title=soup.title.string.replace('/','')
        except:
            print("Cannot Open "+ link)
        with open("./Documents/" + title + ".txt", "w+", encoding='utf-8') as f:
            f.writelines(link + '\n')
            f.write(text)
            f.close()

        i+=1


print(Crawl("https://en.wikipedia.org/wiki/English_language"))
