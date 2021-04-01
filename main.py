from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

# templates 폴더 안에 있는 html 문서 불러오기.
# templates 폴더 안에 있으면 굳이 경로를 설정하지 않아도 flask가 알아서 찾는다.


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        jobs = get_jobs(word)
        print(jobs)
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word)


app.run(host="127.0.0.1")
