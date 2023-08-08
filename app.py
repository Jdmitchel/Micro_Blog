import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://maisonjardel:Ah9LLB6MTONFUUSk@webdev.nqkzwyx.mongodb.net/') # connect to mongodb server
app.db = client.MicroBlog


@app.route("/", methods=["GET", "POST"])
def home():
    #print([e for e in app.db.Webdev.find({})])
    if request.method == "POST":
        entry_content = request.form.get("blog-data")
        formatted = datetime.datetime.today().strftime("%Y/%m/%d")
        #entries.append((entry_content, formatted))
        app.db.Webdev.insert_one({"content": entry_content, "date": formatted})

    entries_dates = [
        (entry["content"], 
         entry["date"], 
         datetime.datetime.strptime(entry["date"], "%Y/%m/%d").strftime("%b %d"))
    for entry in app.db.Webdev.find({})
    ]

    return render_template("home.html", entries = entries_dates)



if __name__ == '__main__':
    app.run(debug=True)
