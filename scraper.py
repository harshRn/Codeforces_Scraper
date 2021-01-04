from bs4 import BeautifulSoup
import requests


#the engine
def process(link,a,b):
    source=requests.get(link).text
    soup=BeautifulSoup(source,'lxml')

    problems=soup.find('table',class_='problems')
    rows=problems.find_all(['tr'])

    lst=[]

    for i in rows:
        lst2=[]
        id=i.find_all('a')
    
        code=id[0].text.strip()
        name=id[1].text.strip()
    
        link="www.codeforces.com"
        link+=id[0]['href']
    
        diff=i.find('span',class_='ProblemRating')
        if(diff!=None):
            diff=diff.text
            diff=int(diff)
        else:
            continue

        if(diff>=a and diff<=b):
            lst2.append(code)
            lst2.append(name)
            lst2.append(diff)
            lst2.append(link)
        else:
            continue
        lst.append(lst2)
    return lst;
