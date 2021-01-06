from flask import Flask,render_template,url_for,request,redirect
from bs4 import BeautifulSoup
import requests


def process(link,a,b):
    source=requests.get(link).text
    soup=BeautifulSoup(source,'lxml')

    problems=soup.find('table',class_='problems')
    rows=problems.find_all(['tr'])

    lst=[]

    for i in rows:
        prob={}
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
            prob['code']=code
            prob['name']=name
            prob['rating']=diff
            prob['link']=link            
        else:
            continue
        lst.append(prob)
    return lst

app = Flask(__name__)






@app.route("/query",methods=["GET","POST"])
def inp():
    if request.method == "POST":
        link=request.form["lnk"]
        a=int(request.form["ll"])
        b=int(request.form["ul"])
        all_posts=process(link,a,b)
        return redirect(url_for("res"))
    else:
        return render_template('query.html')

link='https://codeforces.com/problemset'
a=1500
b=2100
all_posts=process(link,a,b)

@app.route("/results",methods=['GET'])
def res():
    return render_template('results.html',results=all_posts)



if __name__=="__main__":
    app.run(debug=True)
1