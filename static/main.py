from flask import Flask, render_template, request
import mysql.connector
import csv

app = Flask(__name__)

mydb = mysql.connector.connect(host='localhost', user='rohit', passwd='', database='YOGA')

mycursor = mydb.cursor()


@app.route("/")
def root():
    return render_template("./index.html")


@app.route("/index.html")
def home():
    return render_template("./index.html")


@app.route("/about.html")
def about():
    return render_template("./about.html")


@app.route("/service.html")
def service():
    return render_template("./service.html")


@app.route("/price.html")
def price():
    return render_template("./price.html")


@app.route("/class.html")
def clas():
    return render_template("./class.html")


@app.route("/team.html")
def team():
    return render_template("./team.html")


@app.route("/portfolio.html")
def portfolio():
    return render_template("./portfolio.html")


@app.route("/contact.html")
def contact():
    return render_template("./contact.html")


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    try:
        with open('db.csv', mode="a") as database:
            data = request.form.to_dict()
            name = data["Name"]
            email = data["Email"]
            subject = data["Subject"]
            message = data["Message"]
            sv_writer = csv.writer(database, quotechar='"', delimiter=',', quoting=csv.QUOTE_MINIMAL)
            sv_writer.writerow([name, email, subject, message])
    except Exception:
        return "Something went wrong"
    except:
        return "Something went wrong"
    if request.method == "POST":
        data = request.form.to_dict()
        name = data["Name"]
        email = data["Email"]
        subject = data["Subject"]
        message = data["Message"]
        try:
            stmt = "INSERT INTO CONTACT (Name, Email, Subject, Message) VALUES (%s, %s, %s, %s)"
            data = [
                (f'{name}', f'{email}', f'{subject}', f'{message}')
            ]
            mycursor.executemany(stmt, data)
            mydb.commit()
            mycursor.close()
        except AttributeError:
            return "Something went wrong"
    return render_template("./thankyou.html")


if __name__ == '__main__':
    app.run(debug=True)
