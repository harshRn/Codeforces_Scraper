from bs4 import BeautifulSoup
import requests


source=requests.get("https://codeforces.com/problemset").text


soup=BeautifulSoup(source,'lxml')

problems=soup.find('table',class_='problems')

rows=problems.find_all(['tr'])


a=int(input())
b=int(input())

lst=[]

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
    else:
        continue

    if(diff>=a and diff<=b):
        lst.append(code)
        lst.append(name)
        lst.append(diff)
        lst.append(link)
print(len(lst))

   



