from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/test')
def test():

    age = []
    num = []
    con = sqlite3.connect("localhost.db")
    cur = con.cursor()
    sql = "select Age, count(Age) from aw group by Age"
    data1 = cur.execute(sql)
    for item in data1:
        age.append(item[0])
        num.append(item[1])

    datalist = []
    con = sqlite3.connect("localhost.db")
    cur = con.cursor()
    sql = "select Age, Weight from aw"
    data2 = cur.execute(sql)
    for item in data2:
        datalist.append([item[0], item[1]])

    cur.close()
    con.close()
    return render_template("test.html", age=age, num=num, datalist=datalist)


if __name__ == "__main__":
    app.run(debug=True)
