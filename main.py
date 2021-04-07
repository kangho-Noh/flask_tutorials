from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")

# templates 폴더 안에 있는 html 문서 불러오기.
# templates 폴더 안에 있으면 굳이 경로를 설정하지 않아도 flask가 알아서 찾는다.
db = {}


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/report")
def report():
    word = request.args.get('word')  # url에서 word라는 query argument 가져옴
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs

    else:
        return redirect("/")
    return render_template("report.html",
                           searchingBy=word,
                           resultsNumber=len(jobs),
                           jobs=jobs)


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect('/')


app.run(host="127.0.0.1")
