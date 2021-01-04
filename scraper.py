from bs4 import BeautifulSoup
import requests


source=requests.get("https://codeforces.com/problemset").text


soup=BeautifulSoup(source,'lxml')

problems=soup.find('table',class_='problems')

rows=problems.find_all(['tr'])



for i in rows:
    id=i.find_all('a')
    
    code=id[0].text.strip()
    name=id[1].text.strip()
    
    link="www.codeforces.com"
    link+=id[0]['href']
    
    diff=i.find('span',class_='ProblemRating')
    if(diff!=None):
        diff=diff.text
        diff=int(diff)

    

    print(code)
    print(name)
    print(link)
    print(diff)
    print('\n\n')



